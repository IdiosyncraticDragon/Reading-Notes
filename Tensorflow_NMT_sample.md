# NMT sample of TF
> https://github.com/tensorflow/nmt/
> authors of tutorials: Thang Luong, Eugene Brevdo, Rui Zhao
> author of this post: Guiying Li

## hints from prelimiaries
- operation '...' in python: 类似于声明操作。打印出来是说省略
```
$> a=...
$> a
Out[2]: Ellipsis
```

### what is computational graph
-  A computational graph is a series of TensorFlow operations arranged into a graph of nodes.
- tensors are the flowing stream.
- A graph can be parameterized to accept external inputs, known as placeholders. A placeholder is a promise to provide a value later.
- Variables allow us to add trainable parameters to a graph.
- Constants are initialized when you call tf.constant, and their value can never change. By contrast, variables are not initialized when you call tf.Variable. To initialize all the variables in a TensorFlow program, you must explicitly call a special operation as follows:
```
init = tf.global_variables_initializer()
sess.run(init)
```
- Before Variables can be used within a session, they must be initialized using that session.
- InteractiveSession for ipython
- 如此看来，计算图就是对于操作流程的叙述，这个图中，每个节点是操作，每条有向边上传输的都是tensor。但是这个东西只是个描述，本身不承担实际的计算，实际计算应该是有C++ backend完成的。所以每个计算图需要在一个session中才能计算，这个session的功能就是根据这个图，使用c++ backend去初始化一个根据图定义好的环境（可能包含编译的过程）。

### session and graph

- 默认状态下tf会有个global的默认大图，所有的operation和tensor都是这个大图的子结构。每个session都只是执行需要执行的那部分子图。如下的代码可以指定大图：
```
with tf.Graph().as_default():
```
- default session: tf.Session.as_default(), 它返回了一个context manager（姑且称为上下文管理器）来将这个Session变为default session。 这样的好处是，当有default session的时候，直接运行operation.run()或tensor.eval()两个命令可以直接在default session中执行，不需要使用session run
- InterativeSession就是初始化自己是default session，这是它与一般的session的区别。

### 计算图的依赖控制
有的时候，计算图上有些附加操作，但是本身去看计算图时，没有这些附加操作，图也能得到结果。那么默认的，tf会忽略这些操作。比如：
```
a=tf.Variable(0, dtype=tf.int32)
b=tf.Variable(0, dtype=tf.int32)
depop=tf.assign(a,a+1)
c=a+b
```


### Debug
- graph 和 session的模式使得调试不是很方便，所以tf有专门的工具进行代码调试：
```
from tensorflow.python import debug as tf_debug

sess = tf_debug.LocalCLIDebugWrapperSession(sess)
```
这样在运行时，就是在senssion开始前进入debug界面，并可以通过命令检测每次senssion中的一些信息。

## 调用结构解析

### Inference过程的调用结构
起点都是nmt.py， train是调用train.py中的train函数，inference是调用inference.py中的inference函数。

inference函数中
1. 要根据具体使用的模型，生成graph，这些graph都是model.py中Model类的子类；
2. 然后根据情况要返回single/multi_worker_inference, 在这个返回的函数中开启session，运行计算。


## 单元测试
```
import tensorflow as tf

    class SquareTest(tf.test.TestCase):

      def testSquare(self):
        with self.test_session():
          x = tf.square([2, 3])
          self.assertAllEqual(x.eval(), [4, 9])

    if __name__ == '__main__':
      tf.test.main()
```

## OpenNMT-tf 使用与Transformer模型的训练

### sentencepiece与BPE
> url: https://github.com/google/sentencepiece/tree/master/python

要用sentencepiece来处理数据，目的是使用BPE方法，通过unsupervise的方法训练一个模型，来对原始数据进行编码解码。

训练的语句为：

`
spm_train --input=data/train.txt --model_prefix=wmtende --vocab_size=32000 --character_coverage=1 --model_type=bpe
`

上面选项中：

--input：是原始输入数据的路径，每行一条语句，源语言和目标语言都放入一个文件或者用逗号隔开的两个文件，不需要做预处理。

--model_type: 训练什么样的编码模型，有unigram(默认),bpe,char和word。

--input_sentence_size:指定用来训练的语句数的上限，默认是1千万句。

#### 问题1，修改容器系统的编码
> 在docker容器中，系统ubuntu 16.04

在处理数据时，编码问题可能会导致结果不对。
在ubuntu下通过如下方法设置支持中文的系统编码：

`
apt-get -y install language-pack-zh-hans
export LANG="zh_CN.UTF-8"
export LANGUAGE="zh_CN:zh"
export LC_ALL="zh_CN.UTF-8"
`

#### 问题 IWSLT数据的结构
以（英文，中文）对为例，英文翻译成中文和中文翻译成英文是两个数据集。每个数据集中tran.tags.x-y.x/y这两个文件是训练的数据对，其他是test和validation，这些数据里面的内容都是一样的。只有一个train.x/y这个数据的内容是不一样的，它似乎只是用来提供目标种的形态信息。

train.tags.x-y.x/y文件中是以xml的格式存储信息，
