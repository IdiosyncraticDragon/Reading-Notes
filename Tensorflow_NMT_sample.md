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

### 模型保存与载入
>http://cv-tricks.com/tensorflow-tutorial/save-restore-tensorflow-models-quick-complete-tutorial/

tensorflow保存文件的结构：  
__.meta文件__：保存了整个计算流图的结构信息。  
__.index + .data-xxx-of-xxxx__：0.11版本之前只有一个文件，之后是分成两个文件。二进制格式，保存了all the values of the weights, biases, gradients and all the other variables saved.  
__checkpoint__：simply keeps a record of latest checkpoint files saved.



### Debug
- graph 和 session的模式使得调试不是很方便，所以tf有专门的工具进行代码调试：
```
from tensorflow.python import debug as tf_debug

sess = tf_debug.LocalCLIDebugWrapperSession(sess)
```
这样在运行时，就是在senssion开始前进入debug界面，并可以通过命令检测每次senssion中的一些信息。

### Lib usage
- tf.train.latest_checkpoint( checkpoint_dir, latest_filename=None): return the full path to the latest checkpoint or None if no checkpoint was found.

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

### （for word embedding) 如何提取Transformer的word embedding向量并用其他向量替换？
首先，OpenNMT-tf不带这项功能，所以我们需要对代码进行自定义修改。

`
opennmt/inputters/text_inputter.py
`

中的第364行定义了word embedding向量。
通过，`embeddings = tf.get_variable( "w_embs", shape=shape, dtype=self.dtype, initializer=initializer, trainable=self.trainable)`生成的变量。获得word embedding变量的方法为`outputs = embedding_lookup(embeddings, inputs)`，这个方法实际调用`tf.nn.embedding_lookup`来完成embedding向量查找。

`
tf.get_variable
Gets an existing variable with these parameters or create a new one.
`

#### python函数修饰符@
类似于扩展方法和闭包
`
@method
def kkk():
`
这里method接受kkk函数作为输入，实际调用method(kkk),可以看成是对kkk做包装。
当method是类名是，相当于将kkk作为类的扩展方法。

#### 为什么要对embedding_lookup做包装？
>https://github.com/OpenNMT/OpenNMT-tf/blob/master/opennmt/layers/common.py

让不支持sparse grediant的optimizer能用上。
代码中使用的
`tensorflow.python.framework.function.Defun`是一个tf定义的函数修饰器，作用是“Use this decorator to make a Python function usable directly as a TensorFlow function.”。更深入的就不用了解了。

#### 为什么tf.get_variable这么一个通用方法可以生成word embedding这种特殊向量？
>https://www.tensorflow.org/programmers_guide/embedding

确切说，生成embedding变量的是embedding_lookup函数。那既然已经用tf.variables生成tensor了，那为什么还要用embedding_lookup呢？  参见[API doc](https://www.tensorflow.org/api_docs/python/tf/nn/embedding_lookup)中的内容，可知，这是为了从tensor中按照给定的整数索引对应embedding vector 而做的封装。这样做比直接从embedding matrix中抽取向量的好处在暂时未知，猜测是虽然逻辑上一样，但是这样封装可以提高效率（python,c++,gpu交互之类）。

#### 如何从tensorflow保存的模型中提取word embedding向量？
直接在session.run的时候，evaluate那个word embedding 的矩阵。
直接参考tensorflow提供的[inspect_checkpoint.py](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/tools/inspect_checkpoint.py)，从保存好的模型中提取参数。

#### 如何通过python脚本的方式运行OpenNMT-tf的WMT模型性？
1. onmt-main这个可执行文件是个python代码，直接封装的是 opennmtf/bin/main.py.
2. onmt-main infer 会执行opennmt.runner里面Runner类的一个对象的成员函数infer()

#### 将compositional code learning的方法组合到OpenNMT-tf的Transformer实现之中，需要做那些事情？
1. Transformer中embedding向量的提取，并转成官方compositional code learning项目能接受的模式；测试32x16和64x16两种方式
2. 修改官方代码导出结果的方式（需要细化）
3. 重写embedding_lookup，实现compositional encoding，不训练
4. 重训练模型，查看32x16和64x16能达到的效果如何

#### 如果将简化好的embedding向量放入Transformer？
1. 如何将保存模型中的word embedding向量值替换？
2. 如何设计新的embedding lookup, input数据是什么格式，如何读取进来的。
3. 如何将原始模型的其他值原样复制到新模型
第一个问题需要知道的是，Transformer的最高层结构定义在哪里，即包含各个部分构成的地方，怎么构建模型，怎么载入模型的？

  在opennmt.config.load_model(config["model_dir"], model_name='Transformer')后，会[返回](https://github.com/IdiosyncraticDragon/OpenNMT-tf/blob/master/opennmt/models/catalog.py#L138)一个全新的Transformer:opennmt.models.model.Model模型,并在config["model_dir"]的位置生成一个"model_description.pkl"描述文件。  
  Runner的初始化，主要是讲配置文件里面的参数信息拷贝到Runner对象中去。  
  在Runner中，需要初始化[tf.estimator.Estimator](https://www.tensorflow.org/api_docs/python/tf/estimator/Estimator)，并且infer的时候使用这个对象做inference。  
  Estimator需要一个mode_fn参数，openNMT里面所有的这个参数都是定义在opennmt.models.Model里面。
  具体构建计算流图的过程是这样的（自定向下）：首先在[Model](https://github.com/IdiosyncraticDragon/OpenNMT-tf/blob/master/opennmt/models/model.py)大类中定义抽象函数[_build](https://github.com/IdiosyncraticDragon/OpenNMT-tf/blob/master/opennmt/models/model.py#L144)，这个函数是在各个层面上对模型进行构建的函数。要注意，构建embedding的功能对象是最为[初始化参数](https://github.com/IdiosyncraticDragon/OpenNMT-tf/blob/master/opennmt/models/model.py#L21)传入Model对象的，在_build中构建流图的时候，embedding部分就是通过embedding功能对象 产生的。在Model大类中的model_fn函数里面，通过[_model_fn](https://github.com/IdiosyncraticDragon/OpenNMT-tf/blob/master/opennmt/models/model.py#L78)函数构建整个模型的图，其中会调用具体的对象的_build函数做构图。目前支持的模型，其_build函数实现都在[SequenceToSequence](https://github.com/IdiosyncraticDragon/OpenNMT-tf/blob/master/opennmt/models/sequence_to_sequence.py#L106)类中定义的。将checkpoint中的参数填入模型的过程，应该是在Estimator对象中[完成的](https://github.com/IdiosyncraticDragon/OpenNMT-tf/blob/master/opennmt/runner.py#L185)，也就是说，这是tf完成的事情。

  目前来看，如果要将compositional encoding嵌入进去，就必须新建个模型，然后分别将composisonal encoding的内容和其他部分的内容拷进去。首先构建模型，在不加入太多内容的情况下，需要将compostional encoding得到的tensor打散成M个小tensor，然后利用他们的code来访问各个小tensor内的eoncoding，最后要加入一个求和的过程，即可。  
  但是改结构是很难的，既然encoding部分不需要重训练，那么我们直接将compositional encoding转成完整的encoding然后直接赋值给模型，进行测试，这样就简单很多了。

### 如何使用[contrib.model_pruning](https://github.com/tensorflow/tensorflow/tree/r1.8/tensorflow/contrib/model_pruning)

#### 项目如何作用于已经训练好的模型
有两种方式，一是定义一个新的图结构，在新结构的每个tensor外面包裹一层mask layer；二是定义一个新的图结构，图结构与原始图一一映射，但是每个层换成新设计的层（自带mask）。
**即，是新定义一个图结构，然后将已训练好的参数导入到这个图结构中**

#### 图结构的mask层是怎么实现的？入股要改成L-OBS如何做？

#### 已训练好的模型参数如何导入图结构中？
contrib.model_pruning是在session的初始化时，指定checkpoint的位置来完成这件事情的。

#### 怎么将Transformer展开？怎么在Transfoer中加入mask？
