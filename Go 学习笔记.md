# Go 学习笔记

> 链接1：https://www.cnblogs.com/qcrao-2018/p/11124360.html

[TOC]

## 安装

### windows安装



### linux 安装

```BASH
wget https://dl.google.com/go/go1.12.7.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.12.7.linux-amd64.tar.gz
```

配置

```BAsh
vim ~/.zshrc
#-----.zshrc
export PATH=$PATH:/usr/local/go/bin
export GOPATH=$HOME/gitProject/go_practice_project
```

### 树莓派4Blinux安装

### 

```BASH
wget https://dl.google.com/go/go1.15.7.linux-arm64.tar.gz
sudo tar -C /usr/local -xzf go1.15.7.linux-arm64.tar.gz
```

配置

```BAsh
vim ~/.zshrc
#-----.zshrc
export PATH=$PATH:/usr/local/go/bin
export GOPATH=$HOME/gitProject/go_practice_project
```

### 

## 使用学习

### go 代理

参考[^1]

对于go1.13以上：

```bash
$ go env -w GO111MODULE=on
$ go env -w GOPROXY=https://goproxy.cn,direct
```

对于其下的版本：

```BASH
$ export GO111MODULE=on
$ export GOPROXY=https://goproxy.cn
```

使用自建的代理程序：

```GO
package main

import (
	"net/http"
	"os"

	"github.com/goproxy/goproxy"
)

func main() {
	g := goproxy.New()
	g.GoBinEnv = append(
		os.Environ(),
		"GOPROXY=https://goproxy.cn,direct", // Use goproxy.cn as the upstream proxy
		"GOPRIVATE=git.example.com",         // Solve the problem of pulling private modules
	)
	g.ProxiedSUMDBs = []string{"sum.golang.org https://goproxy.cn/sumdb/sum.golang.org"} // Proxy the default checksum database
	http.ListenAndServe("localhost:8080", g)
}
```

然后运行：

```BASH
$ go run goproxy.go
```

然后设置：

```BASH
$ go env -w GO111MODULE=on
$ go env -w GOPROXY= http://localhost:8080
```



### GOPATH和GOROOT

使用

```BASH
go env
```

可以查看go重要的设置参数，其中GOROOT是go的安装目录，里面包含了go编译器和标准库。

GOPATH是第三方库和用户项目的位置。

利用GOPATH来指定第三方库的方式，是go最原始的自带方式，现在主流方式是go module。



### GO Module



### 注释

```GO
/*多行注释*/
//单行注释
```

 **{** 不能单独放在一行

```GO
package main

import "fmt"

func main()  
{  // 错误，{ 不能在单独的行上
    fmt.Println("Hello, World!")
}
```



### 行分割

在 Go 程序中，一行代表一个语句结束。每个语句不需要像 C 家族中的其它语言一样以分号 ; 结尾，因为这些工作都将由 Go 编译器自动完成。

如果你打算将多个语句写在同一行，它们则必须使用 ; 人为区分，但在实际开发中我们并不鼓励这种做法。

### 运行

直接运行

```BASH
go run hello.GO
```

生成二进制文件，再运行

```BASH
go build
./hello
```

### 变量

声明变量的一般形式是使用 var 关键字

```GO
var identifier type
var identifier1, identifier2 type
```

例子

```GO
package main
import "fmt"
func main() {
    var a string = "Runoob"
    fmt.Println(a)

    var b, c int = 1, 2
    fmt.Println(b, c)
}
```

**变量声明，带类型**

```GO
var v_name v_type
v_name = value
```

例子

```GO
package main
import "fmt"
func main() {

    // 声明一个变量并初始化
    var a = "RUNOOB"
    fmt.Println(a)

    // 没有初始化就为零值
    var b int
    fmt.Println(b)

    // bool 零值为 false
    var c bool
    fmt.Println(c)
}
```

**变量声明，自动判断类型**

```GO
var v_name = value
```

例子

```GO
package main
import "fmt"
func main() {
    var d = true
    fmt.Println(d)
}
```

**:=,省略var**

**注意 \**:=\** 左侧如果没有声明新的变量，就产生编译错误，**

例子

```GO
v_name := value
```

例子

```GO
var intVal int 

intVal :=1 // 这时候会产生编译错误

intVal,intVal1 := 1,2 // 此时不会产生编译错误，因为有声明新的变量，因为 := 是一个声明语句
```



**综合例子**

```GO
//类型相同多个变量, 非全局变量
var vname1, vname2, vname3 type
vname1, vname2, vname3 = v1, v2, v3

var vname1, vname2, vname3 = v1, v2, v3 // 和 python 很像,不需要显示声明类型，自动推断

vname1, vname2, vname3 := v1, v2, v3 // 出现在 := 左侧的变量不应该是已经被声明过的，否则会导致编译错误


// 这种因式分解关键字的写法一般用于声明全局变量
var (
    vname1 v_type1
    vname2 v_type2
)
```



如果你声明了一个局部变量却没有在相同的代码块中使用它，同样会得到编译错误，例如下面这个例子当中的变量 a：

```GO
package main

import "fmt"

func main() {
   var a string = "abc"
   fmt.Println("hello, world")
}
```

 #### 变量作用范围

Go 语言中变量可以在三个地方声明：

- 函数内定义的变量称为局部变量
- 函数外定义的变量称为全局变量
- 函数定义中的变量称为形式参数

### 数组

```go
var variable_name [SIZE] variable_type
```

**数组初始化**

```GO
var balance = [5]float32{1000.0, 2.0, 3.4, 7.0, 50.0}
balance := [5]float32{1000.0, 2.0, 3.4, 7.0, 50.0}
//长度不确定
var balance = [...]float32{1000.0, 2.0, 3.4, 7.0, 50.0}
或
balance := [...]float32{1000.0, 2.0, 3.4, 7.0, 50.0}
//如果设置了数组的长度，我们还可以通过指定下标来初始化元素：
//将索引为 1 和 3 的元素初始化
balance := [5]float32{1:2.0,3:7.0}

```



### 切片

切片是对数组的抽象。长度不可改变，在特定场景中这样的集合就不太适用，Go 中提供了一种灵活，功能强悍的内置类型切片("动态数组")，与数组相比切片的长度是不固定的，可以追加元素，在追加时可能使切片的容量增大。

```go
var identifier []type
```

切片不需要说明长度。

或使用 **make()** 函数来创建切片:

```go
var slice1 []type = make([]type, len)

也可以简写为

slice1 := make([]type, len)
```

也可以指定容量，其中 **capacity** 为可选参数。

```
make([]T, length, capacity)
```

这里 len 是数组的长度并且也是切片的初始长度。

切片是可索引的，并且可以由 len() 方法获取长度。

切片提供了计算容量的方法 cap() 可以测量切片最长可以达到多少。

```go
package main

import "fmt"

func main() {
   var numbers = make([]int,3,5)

   printSlice(numbers)
}

func printSlice(x []int){
   fmt.Printf("len=%d cap=%d slice=%v\n",len(x),cap(x),x)
}

```

一个切片在未初始化之前默认为 nil，长度为 0，实例如下：

```GO
package main

import "fmt"

func main() {
   var numbers []int

   printSlice(numbers)

   if(numbers == nil){
      fmt.Printf("切片是空的")
   }
}

func printSlice(x []int){
   fmt.Printf("len=%d cap=%d slice=%v\n",len(x),cap(x),x)
}
```

可以通过设置下限及上限来设置截取切片 *[lower-bound:upper-bound]*，实例如下

```go
package main

import "fmt"

func main() {
   /* 创建切片 */
   numbers := []int{0,1,2,3,4,5,6,7,8}  
   printSlice(numbers)

   /* 打印原始切片 */
   fmt.Println("numbers ==", numbers)

   /* 打印子切片从索引1(包含) 到索引4(不包含)*/
   fmt.Println("numbers[1:4] ==", numbers[1:4])

   /* 默认下限为 0*/
   fmt.Println("numbers[:3] ==", numbers[:3])

   /* 默认上限为 len(s)*/
   fmt.Println("numbers[4:] ==", numbers[4:])

   numbers1 := make([]int,0,5)
   printSlice(numbers1)

   /* 打印子切片从索引  0(包含) 到索引 2(不包含) */
   number2 := numbers[:2]
   printSlice(number2)

   /* 打印子切片从索引 2(包含) 到索引 5(不包含) */
   number3 := numbers[2:5]
   printSlice(number3)

}

func printSlice(x []int){
   fmt.Printf("len=%d cap=%d slice=%v\n",len(x),cap(x),x)
}
```

如果想增加切片的容量，我们必须创建一个新的更大的切片并把原分片的内容都拷贝过来。

下面的代码描述了从拷贝切片的 copy 方法和向切片追加新元素的 append 方法。

```go
package main

import "fmt"

func main() {
   var numbers []int
   printSlice(numbers)

   /* 允许追加空切片 */
   numbers = append(numbers, 0)
   printSlice(numbers)

   /* 向切片添加一个元素 */
   numbers = append(numbers, 1)
   printSlice(numbers)

   /* 同时添加多个元素 */
   numbers = append(numbers, 2,3,4)
   printSlice(numbers)

   /* 创建切片 numbers1 是之前切片的两倍容量*/
   numbers1 := make([]int, len(numbers), (cap(numbers))*2)

   /* 拷贝 numbers 的内容到 numbers1 */
   copy(numbers1,numbers)
   printSlice(numbers1)  
}

func printSlice(x []int){
   fmt.Printf("len=%d cap=%d slice=%v\n",len(x),cap(x),x)
}
```



#### 初始化

```
s :=[] int {1,2,3 } 
```

直接初始化切片，**[]** 表示是切片类型，**{1,2,3}** 初始化值依次是 **1,2,3**，其 **cap=len=3**。

```
s := arr[:] 
```

初始化切片 **s**，是数组 arr 的引用。

```
s := arr[startIndex:endIndex] 
```

将 arr 中从下标 startIndex 到 endIndex-1 下的元素创建为一个新的切片。

```
s := arr[startIndex:] 
```

默认 endIndex 时将表示一直到arr的最后一个元素。

```
s := arr[:endIndex] 
```

默认 startIndex 时将表示从 arr 的第一个元素开始。

```
s1 := s[startIndex:endIndex] 
```

通过切片 s 初始化切片 s1。

```
s :=make([]int,len,cap) 
```

通过内置函数 **make()** 初始化切片**s**，**[]int** 标识为其元素类型为 int 的切片。

### 值类型和引用类型

 int、float、bool 和 string 这些基本类型都属于值类型，使用这些类型的变量直接指向存在内存中的值，当使用等号 `=` 将一个变量的值赋值给另一个变量时，如：`j = i`，实际上是在内存中将 i 的值进行了拷贝。

可以通过 &i 来获取变量 i 的内存地址，例如：0xf840000040（每次的地址都可能不一样）。值类型的变量的值存储在栈中。

内存地址会根据机器的不同而有所不同，甚至相同的程序在不同的机器上执行后也会有不同的内存地址。因为每台机器可能有不同的存储器布局，并且位置分配也可能不同。

一个引用类型的变量 r1 存储的是 r1 的值所在的内存地址（数字），或内存地址中第一个字所在的位置。

指针变量通过`*`定义。

### range的使用

Go 语言中 range 关键字用于 for 循环中迭代数组(array)、切片(slice)、通道(channel)或集合(map)的元素。在数组和切片中它返回元素的索引和索引对应的值，在集合中返回 key-value 对。

```go
package main
import "fmt"
func main() {
    //这是我们使用range去求一个slice的和。使用数组跟这个很类似
    nums := []int{2, 3, 4}
    sum := 0
    for _, num := range nums {
        sum += num
    }
    fmt.Println("sum:", sum)
    //在数组上使用range将传入index和值两个变量。上面那个例子我们不需要使用该元素的序号，所以我们使用空白符"_"省略了。有时侯我们确实需要知道它的索引。
    for i, num := range nums {
        if num == 3 {
            fmt.Println("index:", i)
        }
    }
    //range也可以用在map的键值对上。
    kvs := map[string]string{"a": "apple", "b": "banana"}
    for k, v := range kvs {
        fmt.Printf("%s -> %s\n", k, v)
    }
    //range也可以用来枚举Unicode字符串。第一个参数是字符的索引，第二个是字符（Unicode的值）本身。
    for i, c := range "go" {
        fmt.Println(i, c)
    }
}
```

### map使用

Map 是一种无序的键值对的集合。Map 最重要的一点是通过 key 来快速检索数据，key 类似于索引，指向数据的值。Map 是一种集合，所以我们可以像迭代数组和切片那样迭代它。不过，Map 是无序的，我们无法决定它的返回顺序，这是因为 Map 是使用 hash 表来实现的。如果不初始化 map，那么就会创建一个 nil map。nil map 不能用来存放键值对

```GO
/* 声明变量，默认 map 是 nil */
var map_variable map[key_data_type]value_data_type

/* 使用 make 函数 */
map_variable := make(map[key_data_type]value_data_type)
```

例子

```GO
package main

import "fmt"

func main() {
    var countryCapitalMap map[string]string /*创建集合 */
    countryCapitalMap = make(map[string]string)

    /* map插入key - value对,各个国家对应的首都 */
    countryCapitalMap [ "France" ] = "巴黎"
    countryCapitalMap [ "Italy" ] = "罗马"
    countryCapitalMap [ "Japan" ] = "东京"
    countryCapitalMap [ "India " ] = "新德里"

    /*使用键输出地图值 */
    for country := range countryCapitalMap {
        fmt.Println(country, "首都是", countryCapitalMap [country])
    }

    /*查看元素在集合中是否存在 */
    capital, ok := countryCapitalMap [ "American" ] /*如果确定是真实的,则存在,否则不存在 */
    /*fmt.Println(capital) */
    /*fmt.Println(ok) */
    if (ok) {
        fmt.Println("American 的首都是", capital)
    } else {
        fmt.Println("American 的首都不存在")
    }
}
```

**delete**

delete() 函数用于删除集合的元素, 参数为 map 和其对应的 key。

```GO
package main

import "fmt"

func main() {
        /* 创建map */
        countryCapitalMap := map[string]string{"France": "Paris", "Italy": "Rome", "Japan": "Tokyo", "India": "New delhi"}

        fmt.Println("原始地图")

        /* 打印地图 */
        for country := range countryCapitalMap {
                fmt.Println(country, "首都是", countryCapitalMap [ country ])
        }

        /*删除元素*/ delete(countryCapitalMap, "France")
        fmt.Println("法国条目被删除")

        fmt.Println("删除元素后地图")

        /*打印地图*/
        for country := range countryCapitalMap {
                fmt.Println(country, "首都是", countryCapitalMap [ country ])
        }
}
```

### 类型转换

类型转换用于将一种数据类型的变量转换为另外一种类型的变量

```GO
type_name(expression)
```

例子

```GO
package main

import "fmt"

func main() {
   var sum int = 17
   var count int = 5
   var mean float32
   
   mean = float32(sum)/float32(count)
   fmt.Printf("mean 的值为: %f\n",mean)
}
```

### 指针

```go
var var_name *var-type
```

在指针类型前面加上 * 号（前缀）来获取指针所指向的内容。

```GO
package main

import "fmt"

func main() {
   var a int= 20   /* 声明实际变量 */
   var ip *int        /* 声明指针变量 */

   ip = &a  /* 指针变量的存储地址 */

   fmt.Printf("a 变量的地址是: %x\n", &a  )

   /* 指针变量的存储地址 */
   fmt.Printf("ip 变量储存的指针地址: %x\n", ip )

   /* 使用指针访问值 */
   fmt.Printf("*ip 变量的值: %d\n", *ip )
}
```

#### 空指针

当一个指针被定义后没有分配到任何变量时，它的值为 nil。



### 常量

```GO
const identifier [type] = value
```

你可以省略类型说明符 [type]，因为编译器可以根据变量的值来推断其类型。

#### iota

特殊常量，可以认为是一个可以被编译器修改的常量。iota 在 const关键字出现时将被重置为 0(const 内部的第一行之前)，const 中每新增一行常量声明将使 iota 计数一次(iota 可理解为 const 语句块中的行索引)。

iota 可以被用作枚举值：

```GO
const (
    a = iota
    b = iota
    c = iota
)
```

例子

```GO
package main

import "fmt"

func main() {
    const (
            a = iota   //0
            b          //1
            c          //2
            d = "ha"   //独立值，iota += 1
            e          //"ha"   iota += 1
            f = 100    //iota +=1
            g          //100  iota +=1
            h = iota   //7,恢复计数
            i          //8
    )
    fmt.Println(a,b,c,d,e,f,g,h,i)
}
```

以上实例运行结果为：

```
0 1 2 ha ha 100 100 7 8
```



### 字符串

字符串可以通过 **+** 实现

```GO
package main
import "fmt"
func main() {
    fmt.Println("Google" + "Runoob")
}
```

### 结构体

```go
type struct_variable_type struct {
   member definition
   member definition
   ...
   member definition
}
```

如果要访问结构体成员，需要使用点号 **.** 操作符，格式为：

```go
结构体.成员名
```

#### 实例化

结构体的定义只是一种内存布局的描述，只有当结构体实例化时，才会真正地分配内存，因此必须在定义结构体并实例化后才能使用结构体的字段。

**实例化形式1**

```GO
//形式
var ins T
//具体
type Point struct {
    X int
    Y int
}
var p Point
p.X = 10
p.Y = 20
```

其中，T 为结构体类型，ins 为结构体的实例。

**实例化形式2**

还可以直接实例化指针型的结构体。以使用 new 关键字对类型（包括结构体、整型、浮点数、字符串等）进行实例化，结构体在实例化后会形成指针类型的结构体。

```go
//形式
ins := new(T)
//具体
type Player struct{
    Name string
    HealthPoint int
    MagicPoint int
}
tank := new(Player)
tank.Name = "Canon"
tank.HealthPoint = 300
```

其中：

- T 为类型，可以是结构体、整型、字符串等。
- ins：T 类型被实例化后保存到 ins 变量中，ins 的类型为 *T，属于指针

经过 new 实例化的结构体实例在成员赋值上与基本实例化的写法一致。在 C/C++ 语言中，使用 new 实例化类型后，访问其成员变量时必须使用`->`操作符。

在Go语言中，访问结构体指针的成员变量时可以继续使用`.`，这是因为Go语言为了方便开发者访问结构体指针的成员变量，使用了语法糖（Syntactic sugar）技术，将 ins.Name 形式转换为 (*ins).Name。

**实例化形式3**

在Go语言中，对结构体进行`&`取地址操作时，视为对该类型进行一次 new 的实例化操作，取地址格式如下：

```go
//形式
ins := &T{}
```

其中：

- T 表示结构体类型。
- ins 为结构体的实例，类型为 *T，是指针类型。

取地址实例化是最广泛的一种结构体实例化方式，如下所示

```go
//结构体定义
type Command struct {
    Name    string    // 指令名称
    Var     *int      // 指令绑定的变量
    Comment string    // 指令的注释
}
//实例化1
cmd := &Command{}
cmd.Name = "version"
cmd.Var = &version
cmd.Comment = "show version"
//实例化2
func newCommand(name string, varref *int, comment string) *Command {
    return &Command{
        Name:    name,
        Var:     varref,
        Comment: comment,
    }
}
cmd = newCommand(
    "version",
    &version,
    "show version",
)
```

#### 初始化

结构体在实例化时可以直接对成员变量进行初始化，初始化有两种形式分别是以字段“键值对”形式和多个值的列表形式，键值对形式的初始化适合选择性填充字段较多的结构体，多个值的列表形式适合填充字段较少的结构体。

**键值对模式**

```go
ins := 结构体类型名{
    字段1: 字段1的值,
    字段2: 字段2的值,
    …
}
```



**多值列表模式**

```GO
ins := 结构体类型名{
    字段1的值,
    字段2的值,
    …
}
```

要注意：

- 必须初始化结构体的所有字段。
- 每一个初始值的填充顺序必须与字段在结构体中的声明顺序一致。
- 键值对与值列表的初始化形式不能混用。

#### 匿名结构体初始化

匿名结构体没有类型名称，无须通过 type 关键字定义就可以直接使用。

```GO
ins := struct {
    // 匿名结构体字段定义
    字段1 字段类型1
    字段2 字段类型2
    …
}{
    // 字段值初始化（可选）
    初始化字段1: 字段1的值,
    初始化字段2: 字段2的值,
    …
}
```



### 函数

```GO
func function_name( [parameter list] ) [return_types] {
   函数体
}
```

### 接口

Go 语言提供了另外一种数据类型即接口，它把所有的具有共性的方法定义在一起，任何其他类型只要实现了这些方法就是实现了这个接口。

```GO
/* 定义接口 */
type interface_name interface {
   method_name1 [return_type]
   method_name2 [return_type]
   method_name3 [return_type]
   ...
   method_namen [return_type]
}

/* 定义结构体 */
type struct_name struct {
   /* variables */
}

/* 实现接口方法 */
func (struct_name_variable struct_name) method_name1() [return_type] {
   /* 方法实现 */
}
...
func (struct_name_variable struct_name) method_namen() [return_type] {
   /* 方法实现*/
}
```

例子

```GO
package main

import (
    "fmt"
)

type Phone interface {
    call()
}

type NokiaPhone struct {
}

func (nokiaPhone NokiaPhone) call() {
    fmt.Println("I am Nokia, I can call you!")
}

type IPhone struct {
}

func (iPhone IPhone) call() {
    fmt.Println("I am iPhone, I can call you!")
}

func main() {
    var phone Phone

    phone = new(NokiaPhone)
    phone.call()

    phone = new(IPhone)
    phone.call()

}
```



### 错误处理

通过内置的错误接口提供了非常简单的错误处理机制。

error类型是一个接口类型，这是它的定义：

```GO
type error interface {
    Error() string
}
```

### 并发

#### goroutine

Go 语言支持并发，我们只需要通过 go 关键字来开启 goroutine 即可。

goroutine 是轻量级线程，goroutine 的调度是由 Golang 运行时进行管理的。

goroutine 语法格式：

```GO
go 函数名( 参数列表 )
```

例如：

```
go f(x, y, z)
```

开启一个新的 goroutine:

```
f(x, y, z)
```

Go 允许使用 go 语句开启一个新的运行期线程， 即 goroutine，以一个不同的、新创建的 goroutine 来执行一个函数。 同一个程序中的所有 goroutine 共享同一个地址空间。

```GO
package main

import (
        "fmt"
        "time"
)

func say(s string) {
        for i := 0; i < 5; i++ {
                time.Sleep(100 * time.Millisecond)
                fmt.Println(s)
        }
}

func main() {
        go say("world")
        say("hello")
}
```

#### channel

通道（channel）是用来传递数据的一个数据结构。

通道可用于两个 goroutine 之间通过传递一个指定类型的值来同步运行和通讯。操作符 `<-` 用于指定通道的方向，发送或接收。如果未指定方向，则为双向通道。

```GO
ch := make(chan int)
ch <- v    // 把 v 发送到通道 ch
v := <-ch  // 从 ch 接收数据
           // 并把值赋给 v
```

默认情况下，通道是不带缓冲区的。发送端发送数据，同时必须有接收端相应的接收数据。

以下实例通过两个 goroutine 来计算数字之和，在 goroutine 完成计算后，它会计算两个结果的和：

```GO
package main

import "fmt"

func sum(s []int, c chan int) {
        sum := 0
        for _, v := range s {
                sum += v
        }
        c <- sum // 把 sum 发送到通道 c
}

func main() {
        s := []int{7, 2, 8, -9, 4, 0}

        c := make(chan int)
        go sum(s[:len(s)/2], c)
        go sum(s[len(s)/2:], c)
        x, y := <-c, <-c // 从通道 c 中接收

        fmt.Println(x, y, x+y)
}
```

通道可以设置缓冲区，通过 make 的第二个参数指定缓冲区大小：

```
ch := make(chan int, 100)
```

带缓冲区的通道允许发送端的数据发送和接收端的数据获取处于异步状态，就是说发送端发送的数据可以放在缓冲区里面，可以等待接收端去获取数据，而不是立刻需要接收端去获取数据。

不过由于缓冲区的大小是有限的，所以还是必须有接收端来接收数据的，否则缓冲区一满，数据发送端就无法再发送数据了。

**注意**：如果通道不带缓冲，发送方会阻塞直到接收方从通道中接收了值。如果通道带缓冲，发送方则会阻塞直到发送的值被拷贝到缓冲区内；如果缓冲区已满，则意味着需要等待直到某个接收方获取到一个值。接收方在有值可以接收之前会一直阻塞。

**遍历通道与关闭通道**

通过 range 关键字来实现遍历读取到的数据，类似于与数组或切片。格式如下：

```
v, ok := range ch
```

如果通道接收不到数据后 ok 就为 false，这时通道就可以使用 **close()** 函数来关闭。

```GO
package main

import (
        "fmt"
)

func fibonacci(n int, c chan int) {
        x, y := 0, 1
        for i := 0; i < n; i++ {
                c <- x
                x, y = y, x+y
        }
        close(c)
}

func main() {
        c := make(chan int, 10)
        go fibonacci(cap(c), c)
        // range 函数遍历每个从通道接收到的数据，因为 c 在发送完 10 个
        // 数据之后就关闭了通道，所以这里我们 range 函数在接收到 10 个数据
        // 之后就结束了。如果上面的 c 通道不关闭，那么 range 函数就不
        // 会结束，从而在接收第 11 个数据的时候就阻塞了。
        for i := range c {
                fmt.Println(i)
        }
}
```



### 包管理

当标识符（包括常量、变量、类型、函数名、结构字段等等）以一个大写字母开头，如：Group1，那么使用这种形式的标识符的对象就可以被外部包的代码所使用（客户端程序需要先导入这个包），这被称为导出（像面向对象语言中的 public）；标识符如果以小写字母开头，则对包外是不可见的，但是他们在整个包的内部是可见并且可用的（像面向对象语言中的 protected ）。



## 原理分析

> https://www.cnblogs.com/qcrao-2018/p/11124360.html



## 引用

[^1]: https://goproxy.cn/