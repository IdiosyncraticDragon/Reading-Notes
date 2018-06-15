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
