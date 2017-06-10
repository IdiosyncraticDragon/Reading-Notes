# Caffe
> author: Guiying Li

## MNIST data

在转换mnist的数据的代码 convert_mnist_data.cpp中，有个转换大小段存储的代码，很有意思。这是因为原始数据是用大端存储的，而C／C++是小端存储的。大端存储是高位字节在低位地址（先从高位地址开始编址），小段存储则是高位字节在高位地址（先从低位开始编址）。
```
uinit32_t swap_endian(uinit32_t val){
  val = ((val << 8) & 0xFF00FF00) | ((val >> 8) & 0xFF00FF);
  return (val << 16) | (val >> 16);
}
```
一个字节可以表示0x0~0xFF的值，上面的代码，以字节为单位，先在一字节位单位进行换位，接着以两字节为单位进行换位。分治法的思想。

## Data prefetch

data prefetch是以c++代码的形式在caffe-master/src/caffe/layers/data_layer.cpp中的。无法在python代码中对prefetch进行改动。

## GPU 和 CPU 数据
> http://blog.csdn.net/u012767526/article/details/51459921
```
// Assuming that data are on the CPU initially, and we have a blob.
const Dtype* foo;
Dtype* bar;
foo = blob.gpu_data(); // data copied cpu->gpu.
foo = blob.cpu_data(); // no data copied since both have up-to-date contents.
bar = blob.mutable_gpu_data(); // no data copied.
// ... some operations ...
bar = blob.mutable_gpu_data(); // no data copied when we are still on GPU.
foo = blob.cpu_data(); // data copied gpu->cpu, since the gpu side has modified the data
foo = blob.gpu_data(); // no data copied since both have up-to-date contents
bar = blob.mutable_cpu_data(); // still no data copied.
bar = blob.mutable_gpu_data(); // data copied cpu->gpu.
bar = blob.mutable_cpu_data(); // data copied gpu->cpu.
```

## 代码结构

1. 类的声明存储在 caffe/include/caffe下面

## python 借口

可以直接用的接口在python/caffe/pycaffe.py中能找到

- 指定范围的前向传递：net.forward(start='conv1',end='pool1')．当start为数据层的名字时，会自动做数据prefetch．
