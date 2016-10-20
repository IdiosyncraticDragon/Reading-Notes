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
