# [Python Parallel Programming Cookbook](https://www.packtpub.com/programming/python-parallel-programming-cookbook?/utm_source=python.org&utm_medium=referral&utm_Outreach)

> author: [Giancarlo Zaccone](http://www.allitebooks.org/author/giancarlo-zaccone/)
>
> 中文书名：《python并行编程手册》
>
> reader: Guiying Li

[TOC]

## chapter 1 并行模式

4种并行模式：

![pic1](C:\Users\ThinkPad\Documents\gitRepo\Reading-Notes\pics\20191017_1.png)

既是SISD，SIMD，MISD和MIMD。

共享内存中的缓存一致性（cache coherency），因为processor先从缓存读取数据，如果它需要修改共享内存的数据，那就涉及到其他使用这个共享内存的processor中缓存数据的更新。

SISD就是所有单CPU机器，它只能串行；MISD应用较窄，没有大规模铺开；SIMD要求问题的结构要规则才可以（GPU就是），是很适合分治法的运行结构；MIMD是最通用的结构。

## chapter 2 线程

<img src="C:\Users\ThinkPad\Documents\gitRepo\Reading-Notes\Python Parallel Programming Cookbook_Code\pic1.jpg" alt="pic1" style="zoom:50%;" />

因为GIL的存在，所有基于计算的多线程都不如单线程快（因为线程不并行执行，且有创建开销）；**而在I/O过程中，GIL会被释放，所以进行读写的操作时使用多线程是有用的。**注意，GIL是CPython特有的，Jpthon和IronPython并没有。在访问解释器中的任何东西作为栈和python对象实例钱，解释器都会强制执行中的线程获取GIL，这也是GIL的目的所在——防止不同的而线程访问python对象。我们可以猜出，python解释器会对I/O对象作出特殊判断，若是当前是个I/O对象，不获取GIL。



## Chapter 3 进程

使用的库是`multiprocessing`。在python中多进程并行是真并行，但是进程的创建开销与切换开销远大于线程，不适用于频繁创建的场景。

### 后台运行

`multiprocessing`可以通过`daemon`选项进行后台运行。

```PYTHON
bk_process = multiprocessing.Process(name='111',target=xxx_fun)
bk_process.daemon = True
bk_process.start()
```

该进程的输出不会出现在控制台，同时主程序结束后，后台进程会自动结束，不会一直运行；*且后台进程无法创建子进程*（防止后台进程终止后，会有子进程游离，不结束）。

### 交换对象

进程间交换对象的方法是队列和管道，分别对应于`multiprocessing.Queue`类和`multiprocessing.Pipe`类。

### 进程同步

通过同步原语实现。

`multiprocessing.Lock`：设置是否上锁，关键方法`acquire()`和`release（）`;

`multiprocessing.Event`：设置发送/等待时间，关键方法`set()`和`clear（）`;

`multiprocessing.Barrier`：用于设置同步，关键方法`wait()`;

`multiprocessing.RLock`：设置递归的Lock对象;

`multiprocessing.Semaphore`：信号量，关键方法`acquire()`和`release（）`;

`multiprocessing.Condition`：条件，用于同步线程；关键方法`acquire()`、`wait（）`、`notify（）`和`release（）`;

### 包装好的对象

`multiprocessing.Manager()`提供了一系列包装好的进程工具，它们可以保障共享资源的更新以及进程的管理。



### 如何使用MPI

使用`mpi4py`模块来进行mpi编程。需要在所有参与机器上安装配置。



## Chapter 协程与异步

### 协程与yield

在概念上，协程是功能上与线程一致，但是由程序员调度的子过程，且多个协程是在单线程上切片运行。

在python实现上，协程主要通过**yield**关键词来实现。

使用了**yield**的函数都是生成器，可以有**next**和**send**调用

#### next
yield item 这行代码会产出一个值，提供给 next(...) 的调用方；此外，还会作出让步，暂停执行生成器，让调用方继续工作，直到需要使用另一个值时再调用next()。调用方会从生成器中拉取值。

#### send
生成器的调用方可以使用 .send(...) 方法发送数据，发送的数据会成为生成器函数中 yield 表达式的值。
也就是说忽略yield右侧的值，直接用send值作为yield表达式的输出

yield 关键字甚至还可以不接收或传出数据。不管数据如何流动，yield 都是一种流程控制工具，使用它可以实现协作式多任务：协程可以把控制器让步给中心调度程序，从而激活其他的协程。

从根本上把 yield 视作控制流程的方式，这样就好理解协程了。

特别的，用next就是生成器。用send就是协程。

对采用yield的生成器第一次调用next让它运行到yield处暂停这个操作是预激活。
如果不预激，那么协程没什么用。调用 my_coro.send(x) 之前，记住一定要调用 next(my_coro)。为了简化协程的用法，有时会使用一个预激装饰器，**可以通过` asyncio `模块来载入装饰器**。

### 异步

协程的运行范式其实就是异步模式。

 **异步IO的asyncio库**使用事件循环驱动的协程实现并发。  用户可主动控制程序，在认为耗时IO处添加await（yield from）。在asyncio库中，协程使用@asyncio.coroutine装饰，使用yield from来驱动 。

其中在python3.5版本中，调用方式发生更改：

```python
@asyncio.coroutine -> async

yield from -> await
```

#### asyncio中几个重要概念

**1.事件循环**

管理所有的事件，在整个程序运行过程中不断循环执行并追踪事件发生的顺序将它们放在队列中，空闲时调用相应的事件处理者来处理这些事件。

**2.Future**

Future对象表示尚未完成的计算，还未完成的结果

**3.Task**

是Future的子类，作用是在运行某个任务的同时可以并发的运行多个任务。

asyncio.Task用于实现协作式多任务的库，且Task对象不能用户手动实例化，通过下面2个函数创建：

*asyncio.async()*

*loop.create_task() 或 asyncio.ensure_future()*



## Chapter 5 分布式

### 面向对象中间件

中间件：低耦合度的服务，可以视作没有容器化的微服务。

**Celery**是一个管理分布式任务的python框架，采用面向对象中间件方式实现，其主要特性包括处理大量小型任务，并将其分发给大量计算节点，并将结果组合。（典型的master-slave模型）

使用Celery需要：

- 安装Celery模块
- 消息中介，用于在分布式节点中传输消息的中间件。必须是**面向消息式的中间件**而非是*点对点式*的。支持最完整的是**RabbitMQ**和**Redis**。

### 使用SCOOP进行科学计算

SCOOP需要在各个节点上配置，好处是它包装了进程交互和消息调度，并提供了很多可以用于科学计算的库函数。

### 远程对象调用

**Pyro4**模块提供远程对象调用（ROC)，这使得在代码里可以像调用本地对象一样调用远端服务中的对象。与之相对的是远程方法调用（RPC）。

它和Celery类似，需要先运行一个进行消息交互的中间件（Pyro4的名字服务器），但是它的消息传递是自己实现的，并非通过消息中间件（因为要适配python语言特性，生成python的远程对象调用）。

### 远程过程调用

`rpyc`模块可用于远程过程调用（RPC），

### 基于通信的顺序进程

基于通信的顺序进程（communicating sequential processes, CSP），通过消息传递的方法构建并发，**可以使用`PyCSP`模块实现**，其特点：

- 进程间的消息交换
- 通过线程使用共享内存
- 通过通道完成消息交换（进程间交换值，进程同步）

该模块没有用于消息传递的中间件设置或者名字服务器，所以要跨机器访问时需要知道不同通道绑定的ip和端口。

### 大规模分布式数据管理Disco

包装较好的分布式mapreduce库。



## Chapter 6 GPU编程

### PyCUDA模块

使用该模块`pycuda`时，需要通过字符串把c代码作为字符串传入。通过及时编译的方式部署到GPU设备上去。

### GPUArray

pyCUDA也提供纯的python接口进行GPU调用，这些是通过`pycuda.gpuarray`子模块提供的。

### NumbaPro模块

这是一个python编译器，提供了CUDA的API编程接口，是anacoda开发的，可以在安装好anacoda后通过cond安装。

它一方面支持通过装饰器，对一些函数进行gpu加速；另一方面提供了包装好的cuBLAS、cuFFT、cuRAND和cuSPArse的调用。

### PyOpenCL模块

OpenCL（open computing language)，可以用户不同厂商生成的CPU或者GPU的通用计算框架，由Apple提出，后交由非盈利组织开发维护。该模块包装了OpenCL的功能，提供了python接口。

## 本机代码测试总结



## 本机代码测试总结

### conda搭建python环境

```bash
$> conda create -n python_parallel_programmingv1 flask python=3.3
```

进入python虚拟环境

```bash
$> conda activate python_parallel_programmingv1
```

退出python虚拟环境

```bash
$> conda deactivate
```

书上的测试代码见同级文件夹。

## 命令行弹出另一个线程

```python
import os
os.execvp("python", ("python",) + tuple(["xxx.py", "arg2"]))
print("hi")
```

上述命令可以在命令行shell中再弹出一个进程控制的界面，这个界面运行的是xxx.py文件。注意，这是用一个新的进程替换命运上述命令的进程，在终端上面不会再打印出“hi”了。