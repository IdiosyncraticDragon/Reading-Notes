# TVM学习与理解



## 散点

![](C:\Users\liguiying\Documents\gitProject\Reading-Notes\pics\20200917_tvm1.png)

![](C:\Users\liguiying\Documents\gitProject\Reading-Notes\pics\20200917_tvm2.png)



## 树莓派搭建TVM运行时环境

因为我们是在PC端利用TVM编译神经网络的，所以在树莓派端我们只需要编译TVM的运行时环境即可(TVM可以分为两个部分，一部分为编译时，另一个为运行时，两者可以拆开)。

**注意树莓派端也需要安装llvm，树莓派端的llvm可以在llvm官方找到已经编译好的压缩包，解压后添加环境变量即可**

1. 安装LLVM

进入官网：https://releases.llvm.org/

找到最新的链接：

![](C:\Users\liguiying\Documents\gitProject\Reading-Notes\pics\20200917_tvm3.png)

下载arm版

![image-20200917131007556](C:\Users\liguiying\Documents\gitProject\Reading-Notes\pics\20200917_tvm4.png)

2. 树莓派编译LLVM

如果下载实在太慢，可以考虑自己编译，这里有电脑上交叉编译和在树莓派自己编译的两个选择。

```bash
wget https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.1/llvm-10.0.1.src.tar.xz
tar -xf llvm-10.0.1.src.tar.xz

(下面对于以前的老版本有用，现在不行了)
cd llvm-10.0.1.src/
./configure --build=armv6-unknown-linux-gnueabi \
--host=armv6-unknown-linux-gnueabi \
--target=armv6-unknown-linux-gnueabi --with-cpu=arm1176jzf-s \
--with-float=hard --with-abi=aapcs-vfp --with-fpu=neon \
--enable-targets=arm --enable-optimized --enable-assertions
make REQUIRES_RTTI=1
sudo make install

（树莓派4B，LLVM10.0.1）
sudo apt-get install -y cmake
mkdir llvm_build #编译不可以在解压后的文件夹内部编译，需要在外部新建一个文件夹，否则编译会失败！
cd llvm_build
cmake ../llvm-10.0.1.src/
cmake --build .  # 等很长时间

```

将llvm保存环境变量：



2. 安装TVM运行时

```bash
git clone --recursive https://github.com/dmlc/tvm
cd tvm
mkdir build
cp cmake/config.cmake build   # 这里修改config.cmake使其支持llvm
cd build
cmake ..
make runtime
```

config.cmake的修改如下：

![image-20200917131513045](C:\Users\liguiying\Documents\gitProject\Reading-Notes\pics\20200917_tvm5.png)



## 参考资料

- https://oldpan.me/archives/the-first-step-towards-tvm-1
- 