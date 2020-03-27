# ChatterBot
>Github项目：https://github.com/gunthercox/ChatterBot
>
原作者：gunthercox

>代码：Python2/3

>文档：http://chatterbot.readthedocs.io/en/stable/index.html

>参考：http://blog.just4fun.site/create-a-smart-chat-bot.html

## Installation
1. 官方推荐的是用pip安装
```
pip install chatterbot
```
然而我想修改源码，所以势必不能用这种方式安装。
2. 第二种方法，直接从项目中来安装：
```
git clone https://github.com/gunthercox/ChatterBot
# 需要使用python3，否则会有unicode问题，暂时没空做python2的兼容
pip3 install./ChatterBot
```
实测发现，直接用pip也是可以的，所以这个项目应该兼容python2/3。

## Create a Bot
```
bot = ChatBot(
  "Norman",
  storage_adapter="chatterbot.adapters.storage.JsonFileStorageAdapter",
  input_adapter="chatterbot.adapters.input.TerminalAdapter",
  output_adapter="chatterbot.adapters.output.TerminalAdapter",
  logic_adapters=[
      "chatterbot.adapters.logic.MathematicalEvaluation",
      "chatterbot.adapters.logic.TimeLogicAdapter"
  ],
  database="./database.json"
)
```
上面代码中👆，**“Norman”** 是机器人名字。
这里ChatterBot的设计采用了设计模式中的 **Adaptor模式**（适配器模式）， 就是通过一个适配器，来为两个不兼容的借口进行桥接。这种方式有利于ChatterBot去接受各种个样的实际算法／实现／数据。

上面代码中给出的是用来接受json格式数据的 **storage adapter** 和相应的数据路径。

**input_adapter** 和 **output_adapter** 给的都是Terminal adapter就是说，从终端接受输入，也是输出到终端。

**logic_adapters** 是用来对输入内容进行逻辑处理的模块，功能就是针对不同的输入给出不同的输出； 例子重的 __TimeLogicAdapter__ 会在输入询问时间时返回现在的时间，__MathematicalEvaluation__ 则会在输入中有基础数学计算时予以解决。这两个模块需要用到nltk包的一些数据，需要用
```
python -m textblob.download_corpora
```
来下载。应该是需要理解输入中有没有相应的 **“现在时间”** 询问和 **“基本数学计算”** 的话，就需要足量的类似数据吧。

### 示例代码运行：
```
while True:
    try:
     bot_input = bot.get_response(None)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
```
上面这段代码可以让刚刚新建的聊天机器人跑起来。效果是在终端输入话，机器人会相应的在终端回复你。基本上出了数学运算和时间询问，其他时候它就单纯重复你的话而已。如果你没有database.json文件，也没关系，它会从头开始新建一个，因为你没有在新建机器人是设定 **read_only=True**, 所以它会将你说过的话都记入到这个json里去。
