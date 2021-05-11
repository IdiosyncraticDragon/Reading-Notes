# Python Keypoints

[TOC]

## Special Characters

### python函数修饰符@
类似于扩展方法和闭包  
`
@method
`

`def kkk():`

这里method接受kkk函数作为输入，实际调用method(kkk),可以看成是对kkk做包装。
当method是类名是，相当于将kkk作为类的扩展方法。


## Build-in Functions

### Dictionary

- dicObj.get(key, default = None): return a value for the given key. If key is not available, then returns default value.

### 时间

主要是datetime和calendar两个模块可以提供



## Python 2.7 Modules

### import abc
> Abstract Base Classes  

This module provides the infrastructure for defining abstract base classes (ABCs) in Python.

### import six
Six provides simple utilities for wrapping over differences between Python 2 and Python 3.

### import pickle
The *pickle* module has an optimized cousin called the *cPickle* module. As its name implies, *cPickle* is written in *C*, so it can be up to 1000 times faster than *pickle*. However it does not support subclassing of the *Pickler()* and *Unpickler()* classes.

### getattr 函数
`
getattr(object, name[, default]):
`  
Return the value of the named attribute of object. name must be a string. If the string is the name of one of the object’s attributes, the result is the value of that attribute. For example, getattr(x, 'foobar') is equivalent to x.foobar. If the named attribute does not exist, default is returned if provided, otherwise AttributeError is raised.

## Numpy



## Pandas

> https://pandas.pydata.org/docs/user_guide/index.html#user-guide
>
> 《利用python进行数据分析 第二版》



### 时序、日期功能

pandas中的基础时间序列数据，是由时间戳索引的Series，而在pandas外部，时间数据结构一般表示为python字符串或datetime对象。

和其他series一样，不同索引的时间序列series之间的算术运算在日期上自动对齐。



#### 数据结构

pandas captures 4 general time related concepts 

Timestamp： pd.to_datetime or pd.date_range

Timedelta: pd.to_timedelta or pd.timedelta_range

Period: pd.Period or pd.period_range

DateOffset: pd.Dataoffset

pd.NaT (not a time)表示时间的null值

pd里面认为，时间的数据结构常用于pd.Series和pd.DataFrame中作为索引使用。因此，很多设计考虑都是倾向这方面。

```python
# Series
longer_ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
# DataFrame
dates = pd.date_range('1/1/2000',periods=100, freq='W-WED')
long_df = pd.DataFrame(np.random.randn(100,4), index=dates, columns=['A',"B","C","D"])
```



Timestamp是表示最小时间点的数据结构，Period是表示时间段（time spans）的时间结构。

在存储的时候，Timestamp中的数值是以nano seconds单位进行存储的。

Timestamp和Period都可以用到pd.Series数据结构中用作索引的元素。此时，

如果是一个list的Timestamp或Period，他们作为索引的实际数据结构会自动转化为

DatetimeIndex

PeriodIndex



#### 对比、检索、筛选、排序、转换操作

- 时间格式转换

可以将一系列时间数据结构（strings, epochs, or a mixture）通过pd转化为pd自定的时间数据结构。这个转换通过pd.to_datetime函数实现。

1. 可以将pd.Series中的时间值进行转换

   此时时间值不是作为索引，经过转换后，返回的是拥有同样索引结构的pd.Series对象。只是对值进行了转换。

2. 可以将一个list中的时间值进行转换

   此时返回的是一个DatetimeIndex对象。以便用于作为索引。但如果是单个时间对象（不是list），则只返回Timestamp对象。

```python
In [52]: pd.to_datetime("12-11-2010 00:00", format="%d-%m-%Y %H:%M")
Out[52]: Timestamp('2010-11-12 00:00:00')
```

pd.to_datetime函数可以i通过format来识别时间对象的格式。

3. 可以将pd.DataFrame中一列时间值进行转换

   转换结果是一个pd.Series，时间是series中的值（不是索引），故而是Timestamp对象的集合

   ```python
   In [53]: df = pd.DataFrame(
      ....:     {"year": [2015, 2016], "month": [2, 3], "day": [4, 5], "hour": [2, 3]}
      ....: )
      ....: 
   
   In [54]: pd.to_datetime(df)
   Out[54]: 
   0   2015-02-04 02:00:00
   1   2016-03-05 03:00:00
   dtype: datetime64[ns]
   ```

   这里默认识别一些给定的column名称，

   必填的：year, month, day

   可选的：hour`, `minute`, `second`, `millisecond`, `microsecond`, `nanosecond

4. 可以将整数值转换为时间结构

   整数值默认为Epoch time计时方法，epoch是一个固定的通用的时间，也就是世界标准时间1970年1月1日0时0分，以这个时间为起点，每过去一秒，数值加1。对应的就可以算出公历时间日期（不算闰秒）。因为Time stamp的最小单位是nano seconds，所以epoch time会四舍五入为最接近的nano seconds数值。

- 切片索引

可以用时间字符串、datetime对象或pandas的时间戳对象进行切片索引，这样获得的结果是原数据的视图，即不会有数据拷贝发生。

### 频率

pd.date_range是用于根据特定频率生成指定长度的DatetimeIndex

Series和Dataframe都有一个shift方法用于进行简单的前向或者后向一位，而不改变索引（只移动值）。

####  HDFStore

参考：https://www.cnpython.com/qa/414138

这是对hdf5文件读取的一个高阶封装接口。 