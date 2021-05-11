# gRPC与云原生应用开发

> gPRC：Up and Running

[TOC]

## 安装

环境安装与配置。

官网：https://grpc.io/

mac系统：

首先安装protocol compiler

```bash
$ brew install protobuf
$ protoc --version  # Ensure compiler version is 3+
```

然后，准备好客户端和服务器端语言，这里是go和python（书里面是go和java）。

### go

接着，安装go gplugins for grpc和protocol compiler。

```bash
$ export GO111MODULE=on  # Enable module mode
$ go get google.golang.org/protobuf/cmd/protoc-gen-go \
         google.golang.org/grpc/cmd/protoc-gen-go-grpc
```

上面这种方式是需要翻墙的。

protoc-gen-go源码在：https://github.com/protocolbuffers/protobuf-go

protoc-gen-go-grpc源码在：https://github.com/grpc/grpc-go

这个翻墙是比较麻烦的，我使用的翻墙器是shadowsocksR的，基于sock5协议，需要想办法将之转化为http协议，在对接go get。

使用cow进行转换。

**mac上polipo安装使用（可以解决http代理，但是无法访问https）**

参考博客[^1][^2][^3]

```bash
brew install polipo
```

创建`~/.polipo`

```.polipo
socksParentProxy="127.0.0.1:1086"
socksProxyType="socks5"
proxyAddress="127.0.0.1"
proxyPort=8123
```

其中127.0.0.1:1086是shadowsocksR监听的地址和端口。

运行polipo

```bash
polipo
```

**继续配置**

然后安装go的gRPC插件：

```bash
http_proxy=127.0.0.1:8123 https_proxy=127.0.0.1:8123 go get google.golang.org/protobuf/cmd/protoc-gen-go \
         google.golang.org/grpc/cmd/protoc-gen-go-grpc
```

检查是否安装好：

```bash
(base) ➜  service ls -ll $(go env GOPATH)/bin
total 32536
-rwxr-xr-x  1 liguiying  staff  8445104  2  3 10:57 protoc-gen-go
-rwxr-xr-x  1 liguiying  staff  8211552  2  3 10:57 protoc-gen-go-grpc
```

测试功能正常性，

```bash
git clone -b v1.35.0 https://github.com/grpc/grpc-go
cd grpc-go
cd examples/helloworld
```

在一个终端中（server）：

```bash
http_proxy=127.0.0.1:8123 https_proxy=127.0.0.1:8123 go run greeter_server/main.go
```

在另一个中（client）

```bash
http_proxy=127.0.0.1:8123 https_proxy=127.0.0.1:8123 go run  greeter_client/main.go
```

client显示：

```bash
(base) ➜  helloworld git:(577eb696) http_proxy=127.0.0.1:8123 https_proxy=127.0.0.1:8123 go run  greeter_client/main.go
2021/02/03 16:28:43 Greeting: Hello world
```





### python

Mac 安装anaconda

```bash
conda create -n grpc-python python=3.7
conda activate grpc-python
```

安装grpc

```bash
python -m pip install grpcio
```

安装grpc-tools（包括grpc 编译器和python插件）

```bash
python -m pip install grpcio-tools
```



## chapter 2

**go实现服务端**

定义一个productinfo服务，用go实现服务器端，用python实现客户端。

新建文件ProductInfo.proto

```protobuf
syntax = "proto3";
//package ecommerce;
option go_package = ".;ecommerce"; //最后生成的go文件是处在哪个目录哪个包中，.代表在当前目录生成，ecommerce代表了生成的go文件的包名是ecommerce。

service ProductInfo {
    rpc addProduct(Product) returns (ProductID);
    rpc getProduct(ProductID) returns (Product);
}

message Product {
    string id = 1;
    string name = 2;
    string description = 3;
    float price = 4;
}

message ProductID{
    string value = 1;
}
```

构建文件结构

```bash
mkdir productinfo
kdir -p productinfo/service
mkdir -p productinfo/service/ecommerce
cd productinfo/service
go mod init production/service
```

会生成go.mod模块文件和go.sum

go.mod内容（可能需要手动修改）

```go
module production/service

go 1.15

require (
	github.com/gofrs/uuid v3.2.0+incompatible
	github.com/golang/protobuf v1.4.3
	golang.org/x/net v0.0.0-20210119194325-5f4716e94777 // indirect
	golang.org/x/sys v0.0.0-20210124154548-22da62e12c0c // indirect
	golang.org/x/text v0.3.5 // indirect
	google.golang.org/genproto v0.0.0-20210202153253-cf70463f6119 // indirect
	google.golang.org/grpc v1.35.0
	google.golang.org/grpc/cmd/protoc-gen-go-grpc v1.1.0 // indirect
	google.golang.org/protobuf v1.25.0
)
```



注意，新的api和命令和书里有区别，参考[^4]。

文件结构

```bash
productinfo/
--- productinfo/service
--- ProductInfo.proto
--- --- productinfo/service/ecommerce
--- --- go.mod
--- --- go.sum
```

生成服务器端/客户端的接口：

```bash
protoc --go_out=service/ecommerce --go_opt=paths=source_relative --go-grpc_out=service/ecommerce --go-grpc_opt=paths=source_relative ProductInfo.proto
```

生成文件(在productinfo/service/ecommerce下)

```bash
ProductInfo.pb.go      
ProductInfo_grpc.pb.go
```

创建go的服务器端实现service/main.go

```go
package main

import (
	"context"
	"log"
	"net"

	"github.com/gofrs/uuid"
	pb "production/service/ecommerce"
	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

const (
	port = ":50051"
)

// server is used to implement ecommerce/product_info.
type server struct {
	pb.UnimplementedProductInfoServer
	productMap map[string]*pb.Product
}

// AddProduct implements ecommerce.AddProduct
func (s *server) AddProduct(ctx context.Context,
							in *pb.Product) (*pb.ProductID, error) {
	out, err := uuid.NewV4()
	if err != nil {
		return nil, status.Errorf(codes.Internal, "Error while generating Product ID", err)
	}
	in.Id = out.String()
	if s.productMap == nil {
		s.productMap = make(map[string]*pb.Product)
	}
	s.productMap[in.Id] = in
	log.Printf("Product %v : %v - Added.", in.Id, in.Name)
	return &pb.ProductID{Value: in.Id}, status.New(codes.OK, "").Err()
}

// GetProduct implements ecommerce.GetProduct
func (s *server) GetProduct(ctx context.Context, in *pb.ProductID) (*pb.Product, error) {
	product, exists := s.productMap[in.Value]
	if exists && product != nil {
		log.Printf("Product %v : %v - Retrieved.", product.Id, product.Name)
		return product, status.New(codes.OK, "").Err()
	}
	return nil, status.Errorf(codes.NotFound, "Product does not exist.", in.Value)
}

func main() {
	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterProductInfoServer(s, &server{})
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
```

特别注意

```go
pb.UnimplementedProductInfoServer
```

文件结构

```bash
productinfo/
--- ProductInfo.proto
--- productinfo/service
    |
--- --- go.mod
--- --- go.sum
--- --- productinfo/service/ecommerce
        |
--- --- --- ProductInfo.pb.go
--- --- --- ProductInfo_grpc.pb.go
```



然后build生成可执行文件，进入productionInfo/service，执行

```bash
cd service
http_proxy=127.0.0.1:8123 https_proxy=127.0.0.1:8123 go build -i -v -o bin/server
```

注意，需要联网下载没有的依赖。

**go生成客户端**

由proto生成的go 接口pb的两个文件是一样的。

在production下创建go_client和go_client/ecommerce

```bash
protoc --go_out=go_client/ecommerce --go_opt=paths=source_relative --go-grpc_out=go_client/ecommerce --go-grpc_opt=paths=source_relative ProductInfo.proto
```

创建go_client/main.go

```golang
package main

import (
	"context"
	"log"
	"time"

	pb "production/go_client/ecommerce"
	"google.golang.org/grpc"
)

const (
	address = "localhost:50051"
)

func main() {
	// Set up a connection to the server.
	conn, err := grpc.Dial(address, grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := pb.NewProductInfoClient(conn)

	// Contact the server and print out its response.
	name := "Apple iPhone 11"
	description := "Meet Apple iPhone 11. All-new dual-camera system with Ultra Wide and Night mode."
	price := float32(699.00)
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()
	r, err := c.AddProduct(ctx, &pb.Product{Name: name, Description: description, Price: price})
	if err != nil {
		log.Fatalf("Could not add product: %v", err)
	}
	log.Printf("Product ID: %s added successfully", r.Value)

	product, err := c.GetProduct(ctx, &pb.ProductID{Value: r.Value})
	if err != nil {
		log.Fatalf("Could not get product: %v", err)
	}
	log.Printf("Product: %v", product.String())
}

```

在go_client下生成mod（需要手动修改）

```bash
go mod init production/go_client
```

```mod
module production/go_client

go 1.15

require (
	github.com/golang/protobuf v1.4.3
	google.golang.org/grpc v1.35.0
	google.golang.org/protobuf v1.25.0
)
```

可能要修改后再生成一次

编译

```bash
cd go_client
http_proxy=127.0.0.1:8123 https_proxy=127.0.0.1:8123 go build -i -v -o bin/client
```



**go服务端配合go客户端运行**

Terminal1,

```bash
gitProject/gRPC_workspace/chapter2/productinfo/service
./bin/server
```

Terminal2,

```bash
cd gitProject/gRPC_workspace/chapter2/productinfo/go_client
./bin/client
```





## 参考

[^1]: https://www.myfreax.com/convert-shadowsocks-into-an-http-proxy/
[^2]:  https://blog.csdn.net/jiangzhanweiabc/article/details/91977411
[^3]: https://www.jb51.net/article/147524.htm
[^4]: https://www.cnblogs.com/hongjijun/p/13724738.html