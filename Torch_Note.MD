# Note of Torch
> author: Guiying Li

## Basic

### Loop
- while Loop
```
while(condition)
do
   statements
end
```
- for Loop
```
for var=exp1,exp2,exp3 do  
    <执行体>  
end  
```
var从exp1变化到exp2，每次变化以exp3为步长递增var，并执行一次"执行体"。exp3是可选的，如果不指定，默认为1。
- repeat Loop
```
repeat
   statements
until( condition )
```

### 流程控制
- if 语句
```
if(布尔表达式)
then
   --[ 在布尔表达式为 true 时执行的语句 --]
end
```
- if...else 语句
```
if(布尔表达式)
then
   --[ 布尔表达式为 true 时执行该语句块 --]
else
   --[ 布尔表达式为 false 时执行该语句块 --]
end
```

### 函数
- 基本定义
```
optional_function_scope function function_name( argument1, argument2, argument3..., argumentn)
	function_body
	return result_params_comma_separated
end
```
- 可变参数
Lua函数可以接受可变数目的参数，和C语言类似在函数参数列表中使用三点（...) 表示函数有可变的参数。
Lua将函数的参数放在一个叫arg的表中，#arg 表示传入参数的个数。
```
function average(...)
   result = 0
   local arg={...}
   for i,v in ipairs(arg) do
      result = result + v
   end
   print("总共传入 " .. #arg .. " 个数")
   return result/#arg
end
```

### 运算符

#### 算术运算符
A=10， B=20

操作符 | 描述 | 实例
---|---|---
+	| 加法	| A + B 输出结果 30
- |	减法	| A - B 输出结果 -10
*	| 乘法	| A * B 输出结果 200
/	| 除法	| B / A w输出结果 2
%	| 取余	| B % A 输出结果 0
^	| 乘幂	| A^2 输出结果 100
-	| 负号	| -A 输出结果v -10

#### 关系运算符
A=10,B=20

操作符	| 描述	| 实例
---|---|----
==	| 等于，检测两个值是否相等，相等返回 true，否则返回 false	| (A == B) 为 false。
~=	| 不等于，检测两个值是否相等，相等返回 false，否则返回 true<	| (A ~= B) 为 true。
\>	| 大于，如果左边的值大于右边的值，返回 true，否则返回 false	| (A > B) 为 false。
<	| 小于，如果左边的值大于右边的值，返回 false，否则返回 true	| (A < B) 为 true。
\>=	| 大于等于，如果左边的值大于等于右边的值，返回 true，否则返回 false	| (A >= B) 返回 false。
<=	| 小于等于， 如果左边的值小于等于右边的值，返回 true，否则返回 false	| (A <= B) 返回 true。

#### 逻辑运算符
A=true, B=false

操作符	| 描述	| 实例
---|---|---
and	| 逻辑与操作符。 若 A 为 false，则返回 A，否则返回 B。	| (A and B) 为 false。
or	| 逻辑或操作符。 若 A 为 true，则返回 A，否则返回 B。	| (A or B) 为 true。
not	| 逻辑非操作符。与逻辑运算结果相反，如果条件为 true，逻辑非为 false。	| not(A and B) 为 true。

#### 其它运算符

操作符	| 描述	| 实例
---|---|---
..	| 连接两个字符串	|a..b ，其中 a 为 "Hello " ， b 为 "World", 输出结果为 "Hello World"。
\#	| 一元运算符，返回字符串或表的长度。	| #"Hello" 返回 5

#### 运算符优先级
```
优先级从高到低：
^
not    - (unary)
*      /
+      -
..
<      >      <=     >=     ~=     ==
and
or
```
除了^和..外所有的二元运算符都是左连接的。
```
a+i < b/2+1          <-->       (a+i) < ((b/2)+1)
5+x^2*8              <-->       5+((x^2)*8)
a < y and y <= z     <-->       (a < y) and (y <= z)
-x^2                 <-->       -(x^2)
x^y^z                <-->       x^(y^z)
```

### 字符串
- 单引号间的一串字符。
- 双引号间的一串字符。
- [[和]]间的一串字符。

#### 字符串操作
- string.upper(argument): 字符串全部转为大写字母。
- string.lower(argument): 字符串全部转为小写字母。
- string.gsub(mainString,findString,replaceString,num):在字符串中替换,mainString为要替换的字符串， findString 为被替换的字符，replaceString 要替换的字符，num 替换次数（可以忽略，则全部替换）。
- string.strfind (str, substr, [init, [end]]): 在一个指定的目标字符串中搜索指定的内容(第三个参数为索引),返回其具体位置。不存在则返回 nil。
- string.reverse(arg): 字符串反转。
- string.format(...)： 返回一个类似printf的格式化字符串
```
> string.format("the value is:%d",4)
the value is:4
```
- string.char(arg) 和 string.byte(arg[,int]): char 将整型数字转成字符并连接， byte 转换字符为整数值(可以指定某个字符，默认第一个字符)。
```
> string.char(97,98,99,100)
abcd
> string.byte("ABCD",4)
68
> string.byte("ABCD")
65
```
- string.len(arg): 计算字符串长度。
- string.rep(string, n)): 返回字符串string的n个拷贝
- .. : 链接两个字符串

### 数组

#### 一维数组
一维数组是最简单的数组，其逻辑结构是线性表。
```
array = {"Lua", "Tutorial"}
```
索引默认从1开始，但是因为是线性表，所以键是可以指定的。如果指定索引从0甚至负数开始，也是可以的。
```
array = {}

for i= -2, 2 do
   array[i] = i *2
end

for i = -2,2 do
   print(array[i])
end
```

#### 多维数组
多维数组即数组中包含数组或一维数组的索引键对应一个数组。
```
-- 初始化数组
array = {}
for i=1,3 do
   array[i] = {}
      for j=1,3 do
         array[i][j] = i*j
      end
end

-- 访问数组
for i=1,3 do
   for j=1,3 do
      print(array[i][j])
   end
end
```
以上的实例中，数组设定了指定的索引值，这样可以避免出现 nil 值，有利于节省内存空间。

### 迭代器

#### 泛型 for 迭代器
泛型 for 在自己内部保存迭代函数，实际上它保存三个值：迭代函数、状态常量、控制变量。
泛型 for 迭代器提供了集合的 key/value 对，语法格式如下：
```
for k, v in pairs(t) do
    print(k, v)
end
---------实例---------
array = {"Lua", "Tutorial"}

for key,value in ipairs(array)
do
   print(key, value)
end
```
以上实例中我们使用了 Lua 默认提供的迭代函数 ipairs。
下面我们看看范性for的执行过程：
- 首先，初始化，计算in后面表达式的值，表达式应该返回范性for需要的三个值：迭代函数、状态常量、控制变量；与多值赋值一样，如果表达式返回的结果个数不足三个会自动用nil补足，多出部分会被忽略。
- 第二，将状态常量和控制变量作为参数调用迭代函数（注意：对于for结构来说，状态常量没有用处，仅仅在初始化时获取他的值并传递给迭代函数）。
- 第三，将迭代函数返回的值赋给变量列表。
- 第四，如果返回的第一个值为nil循环结束，否则执行循环体。
- 第五，回到第二步再次调用迭代函数

在Lua中我们常常使用函数来描述迭代器，每次调用该函数就返回集合的下一个元素。Lua 的迭代器包含以下两种类型：
- 无状态的迭代器
- 多状态的迭代器

#### 无状态的迭代器
无状态的迭代器是指不保留任何状态的迭代器，因此在循环中我们可以利用无状态迭代器避免创建闭包花费额外的代价。
每一次迭代，迭代函数都是用两个变量（状态常量和控制变量）的值作为参数被调用，一个无状态的迭代器只利用这两个值可以获取下一个元素。
这种无状态迭代器的典型的简单的例子是ipairs，他遍历数组的每一个元素。
以下实例我们使用了一个简单的函数来实现迭代器，实现 数字 n 的平方：
```
function square(iteratorMaxCount,currentNumber)
   if currentNumber<iteratorMaxCount
   then
      currentNumber = currentNumber+1
   return currentNumber, currentNumber*currentNumber
   end
end

-- i,n = square(3,0),当square返回nil的时候停止循环
for i,n in square,3,0
do
   print(i,n)
end
```
迭代的状态包括被遍历的表（循环过程中不会改变的状态常量）和当前的索引下标（控制变量），ipairs和迭代函数都很简单，我们在Lua中可以这样实现：
```
function iter (a, i)
    i = i + 1
    local v = a[i]
    if v then
       return i, v
    end
end

function ipairs (a)
    return iter, a, 0
end
```
#### 多状态的迭代器
很多情况下，迭代器需要保存多个状态信息而不是简单的状态常量和控制变量，最简单的方法是使用闭包，还有一种方法就是将所有的状态信息封装到table内，将table作为迭代器的状态常量，因为这种情况下可以将所有的信息存放在table内，所以迭代函数通常不需要第二个参数。
```
array = {"Lua", "Tutorial"}

function elementIterator (collection)
   local index = 0
   local count = #collection
   -- 闭包函数
   return function ()
      index = index + 1
      if index <= count
      then
         --  返回迭代器的当前元素
         return collection[index]
      end
   end
end

for element in elementIterator(array)
do
   print(element)
end
```

### 表
构造器是创建和初始化表的表达式。表是Lua特有的功能强大的东西。最简单的构造函数是{}，用来创建一个空表。可以直接初始化数组:
  ```
  -- 初始化表
mytable = {}

-- 指定值
mytable[1]= "Lua"

-- 移除引用
mytable = nil
-- lua 垃圾回收会释放内存
  ```

### 模块与包
模块类似于一个封装库，从 Lua 5.1 开始，Lua 加入了标准的模块管理机制，可以把一些公用的代码放在一个文件里，以 API 接口的形式在其他地方调用，有利于代码的重用和降低代码耦合度。
Lua 的模块是由变量、函数等已知元素组成的 table，因此创建一个模块很简单，就是创建一个 table，然后把需要导出的常量、函数放入其中，最后返回这个 table 就行。以下为创建自定义模块 module.lua，文件代码格式如下：
```
-- 文件名为 module.lua
-- 定义一个名为 module 的模块
module = {}

-- 定义一个常量
module.constant = "这是一个常量"

-- 定义一个函数
function module.func1()
    io.write("这是一个公有函数！\n")
end

local function func2()
    print("这是一个私有函数！")
end

function module.func3()
    func2()
end

return module
```
由上可知，模块的结构就是一个 table 的结构，因此可以像操作调用 table 里的元素那样来操作调用模块里的常量或函数。
上面的 func2 声明为程序块的局部变量，即表示一个私有函数，因此是不能从外部访问模块里的这个私有函数，必须通过模块里的公有函数来调用.

#### require 函数
```
require("<模块名>")
require "<模块名>"
local m = require("module")
```

##### 加载机制
于自定义的模块，模块文件不是放在哪个文件目录都行，函数 require 有它自己的文件路径加载策略，它会尝试从 Lua 文件或 C 程序库中加载模块。
require 用于搜索 Lua 文件的路径是存放在全局变量 package.path 中，当 Lua 启动后，会以环境变量 LUA_PATH 的值来初始这个环境变量。如果没有找到该环境变量，则使用一个编译时定义的默认路径来初始化。
当然，如果没有 LUA_PATH 这个环境变量，也可以自定义设置，在当前用户根目录下打开 .profile 文件（没有则创建，打开 .bashrc 文件也可以），例如把 "~/lua/" 路径加入 LUA_PATH 环境变量里：
```
#LUA_PATH
export LUA_PATH="~/lua/?.lua;;"
```
文件路径以 ";" 号分隔，最后的 2 个 ";;" 表示新加的路径后面加上原来的默认路径。
接着，更新环境变量参数，使之立即生效。
如果找过目标文件，则会调用 package.loadfile 来加载模块。否则，就会去找 C 程序库。
搜索的文件路径是从全局变量 package.cpath 获取，而这个变量则是通过环境变量 LUA_CPATH 来初始。
搜索的策略跟上面的一样，只不过现在换成搜索的是 so 或 dll 类型的文件。如果找得到，那么 require 就会通过 package.loadlib 来加载它。

#### C包
<strong>这一部分，不是很懂</strong>

Lua和C是很容易结合的，使用C为Lua写包。
与Lua中写包不同，C包在使用以前必须首先加载并连接，在大多数系统中最容易的实现方式是通过动态连接库机制。
Lua在一个叫loadlib的函数内提供了所有的动态连接的功能。这个函数有两个参数:库的绝对路径和初始化函数。所以典型的调用的例子如下
```
local path = "/usr/local/lua/lib/libluasocket.so"
local f = loadlib(path, "luaopen_socket")
```
loadlib函数加载指定的库并且连接到Lua，然而它并不打开库（也就是说没有调用初始化函数），反之他返回初始化函数作为Lua的一个函数，这样我们就可以直接在Lua中调用他。

### 元表
在 Lua table 中我们可以访问对应的key来得到value值，但是却无法对两个 table 进行操作。
因此 Lua 提供了元表(Metatable)，允许我们改变table的行为，每个行为关联了对应的元方法。
例如，使用元表我们可以定义Lua如何计算两个table的相加操作a+b。
当Lua试图对两个表进行相加时，先检查两者之一是否有元表，之后检查是否有一个叫"\__add"的字段，若找到，则调用对应的值。"\__add"等即时字段，其对应的值（往往是一个函数或是table）就是"元方法"。
有两个很重要的函数来处理元表：
- setmetatable(table,metatable): 对指定table设置元表(metatable)，如果元表(metatable)中存在__metatable键值，setmetatable会失败 。
- getmetatable(table): 返回对象的元表(metatable)。

设置元表：
```
mytable = {}                          -- 普通表
mymetatable = {}                      -- 元表
setmetatable(mytable,mymetatable)     -- 把 mymetatable 设为 mytable 的元表
```
#### \__index 元方法
这是 metatable 最常用的键。
当你通过键来访问 table 的时候，如果这个键没有值，那么Lua就会寻找该table的metatable（假定有metatable）中的__index 键。如果__index包含一个表格，Lua会在表格中查找相应的键。
<strong>Remar:</strong>这相当与扩展一个表的内容。
```
> other = { foo = 3 }
> t = setmetatable({}, { __index = other })
> t.foo
3
> t.bar
nil
```
如果__index包含一个函数的话，Lua就会调用那个函数，table和键会作为参数传递给函数。
\__index 元方法查看表中元素是否存在，如果不存在，返回结果为 nil；如果存在则由 \__index 返回结果。

#### \__newindex 元方法
\__newindex 元方法用来对表更新，\__index则用来对表访问 。
当你给表的一个缺少的索引赋值，解释器就会查找\__newindex 元方法：如果存在则调用这个函数而不进行赋值操作。

#### 数学操作

模式	| 描述
--- | ---
\__add	|对应的运算符 '+'.
\__sub	|对应的运算符 '-'.
\__mul	|对应的运算符 '* '.
\__div	|对应的运算符 '/'.
\__unm	|对应的运算符 '-'.
\__concat	|对应的运算符 '..'.
\__eq	|对应的运算符 '=='.
\__lt	|对应的运算符 '<'.

#### \__call 元方法
\__call 元方法在 Lua 将表当成函数来用时被调用。

#### \__tostring 元方法
\__tostring 元方法用于修改表的输出行为。

### 协同程序
Lua 协同程序(coroutine)与线程比较类似：拥有独立的堆栈，独立的局部变量，独立的指令指针，同时又与其它协同程序共享全局变量和其它大部分东西。

线程与协同程序的主要区别在于，一个具有多个线程的程序可以同时运行几个线程，而协同程序却需要彼此协作的运行。
在任一指定时刻只有一个协同程序在运行，并且这个正在运行的协同程序只有在明确的被要求挂起的时候才会被挂起。
协同程序有点类似同步的多线程，在等待同一个线程锁的几个线程有点类似协同。

### 文件I/O
Lua I/O 库用于读取和处理文件。分为简单模式（和C一样）、完全模式。
- 简单模式（simple model）拥有一个当前输入文件和一个当前输出文件，并且提供针对这些文件相关的操作。
- 完全模式（complete model） 使用外部的文件句柄来实现。它以一种面对对象的形式，将所有的文件操作定义为文件句柄的方法

#### 基础语法
打开文件操作如下：
```
file = io.open (filename [, mode])
```
模式 |	描述
---|---
r	| 以只读方式打开文件，该文件必须存在。
w	| 打开只写文件，若文件存在则文件长度清为0，即该文件内容会消失。若文件不存在则建立该文件。
a	| 以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。（EOF符保留）
r+ | 以可读写方式打开文件，该文件必须存在。
w+ |打开可读写文件，若文件存在则文件长度清为零，即该文件内容会消失。若文件不存在则建立该文件。
a+ | 与a类似，但此文件可读可写
b | 二进制模式，如果文件是二进制文件，可以加上b
+| 号表示对文件既可以读也可以写

### 错误处理
我们可以使用两个函数：assert 和 error 来处理错误。实例如下：
```
local function add(a,b)
   assert(type(a) == "number", "a 不是一个数字")
   assert(type(b) == "number", "b 不是一个数字")
   return a+b
end
add(10)
```
实例中assert首先检查第一个参数，若没问题，assert不做任何事情；否则，assert以第二个参数作为错误信息抛出。
```
error (message [, level])
```
功能：终止正在执行的函数，并返回message的内容作为错误信息(error函数永远都不会返回)
通常情况下，error会附加一些错误位置的信息到message头部。
Level参数指示获得错误的位置:
- Level=1[默认]：为调用error位置(文件+行号)
- Level=2：指出哪个调用error的函数的函数
- Level=0:不添加错误位置信息

### Debug
Lua 提供了 debug 库用于提供创建我们自定义调速器的功能。Lua 本身并未有内置的调速器，但很多开发者共享了他们的 Lua 调速器代码。

### 垃圾回收
Lua 采用了自动内存管理。 这意味着你不用操心新创建的对象需要的内存如何分配出来， 也不用考虑在对象不再被使用后怎样释放它们所占用的内存。
Lua 运行了一个垃圾收集器来收集所有死对象 （即在 Lua 中不可能再访问到的对象）来完成自动内存管理的工作。 Lua 中所有用到的内存，如：字符串、表、用户数据、函数、线程、 内部结构等，都服从自动管理。
<strong>垃圾收集器间歇率</strong>和<strong>垃圾收集器步进倍率</strong>是其中两个重要的概念。

## seq2seq-attn项目

### Remark
折腾了两三天，总算明白怎么用这个代码复现论文实验了。需要复现的论文有两篇：
1. Luong, M.T., Pham, H, D. Manning, C. Effective Approaches to Attention-based Neural Machine Translation. EMNLP,2015
2. See, A, Luong, M.T., D.Manning, C. Compression of Neural Machine Translation Models via Pruning. CoNLL, 2016.

### 论文1结果复现
首先将项目下载：https://github.com/harvardnlp/seq2seq-attn，并让其可运行，这个简单，直接安装好torch就行了。接着在项目页的最下端下载pre-trained模型。接着最重要的是：数据。
特别注意，直接从openNMT里下载wmt15数据里的newstest2013的数据，并不适合本项目，无法用这个复现出论文1和2中提到的seq2seq-attn网络的效果。要直接用项目里data下面的src-test.txt（英语）和targ-test.txt数据！！
然后，translation脚本：
```
--en to de
th evaluate.lua -model /home/deepModels/torch_models/seq2seq-attn/en-to-de-model.t7 -src_dict /home/deepModels/torch_models/seq2seq-attn/en.dict -targ_dict /home/deepModels/torch_models/seq2seq-attn/de.dict -src_file data/src-test.txt -targ_file data/targ-test.txt -output_file pred.txt -gpuid 1
--  BLEU score
perl multi-bleu.perl data/targ-test.txt < pred.txt
th evaluate.lua -model /home/deepModels/torch_models/seq2seq-attn/de-to-en-model.t7 -src_dict /home/deepModels/torch_models/seq2seq-attn/de.dict -targ_dict /home/deepModels/torch_models/seq2seq-attn/en.dict -src_file data/targ-test.txt -targ_file data/src-test.txt -output_file pred.txt -gpuid 1
--de to en
--  BLEU score
```
perl multi-bleu.perl data/src-test.txt < pred.txt
这里特别注意，multi-bleu.perl脚本要从moses项目（https://github.com/moses-smt/mosesdecoder）下载，脚本位置在scripts/generic下面。
最后可以跑出来，pretrained model中en-to-de的BLEU scroe=19.5；de-to-en的BLEU scroe=20.74。根据项目的issues页面的问题，pretrained models对应于论文1中，表格1和表格3中的“Base + reverse + dropout + global attention (location) + feed input”模型。但是，Ppl.的值依然对应不上。

### 论文2结果复现

#### luajit: not enough memory
这个问题是luajit的运行内存限制是2GB，而torch默认都是根据luajit安装的，如果要解决这个问题，就需要用原生的lua来重装torch。这个项目可以很好的解决问题：https://github.com/torch/distro。
安装好后，切换适应于不同lua的torch很容易，只要在~/.bashrc(bash用户)或是~/.zshrc(zsh用户)中将不用的torch版本注释掉就行了。一般刚安装好时，文件最下面那一行就是指定torch版本的语句。

在切换完lua后，还要安装bit module不然有些程序没法正常运行；因为luajit的bit模块是自带的，但是原生lua并不是。
```
luarocks install luabitop
```

### 论文 Bahdanau et al. 2015复现 （opennmt-py)
pytorch这种还没完全成熟的项目，好多坑啊。。。

#### 数据集WMT14
特别注意，使用的数据是可以从这里下载的：http://www-lium.univ-lemans.fr/~schwenk/cslm_joint_paper/ （里面的bitexts after selection）。我还专门跑WMT14去下载一遍，WMT14里提供的数据中，UN数据的形式非常不好，使用UN数据自带的extraction.py后得到的en/fr文件的行数不一致，无法使用，而bitexts数据处理过后，数据行数是一致的。

#### 数据预处理
- 内存的占用非常巨大，en文件1.7G，fr文件2G，但是在preprocess.py运行时，会占完30+G，然后因为内存不够而进程idle（lua版的opennmt没有这个问题，所以要不是bug要不就是有解决方法的）。在preprocess.py阶段使用-dynamic_dict标签尝试下：有所改善，内存是逐渐增加，而且在占满内存后进程还有以CPU利用20~50%的速度运行，但是占满内存这种事肯定是不正常的；通过查看github的issue，确定这是个bug=》还是用lua版的进行数据预处理吧，但是lua处理后的数据opennmt-py是用不了的，因为它保存的是lua编写的数据结构，而不是单纯的文本信息。 目前发现内存占用大的原因是src/tgt_seq_length太小了，将它设大可以避免内存耗尽问题, 但是依然要使用巨量的内存。
- 特别注意，数据是要做Tokenization的，未做tokennization的数据，现在训练了2个epoch，预测出来的还全是unk。训练3个epoch后还是如此，停止此训练,训练的是lua版的模型。
- 现在改成了2层的模型，用Opennmt-py在在dgx-1上训练，训练了3个epoch已经接近了论文的效果。


### 论文training rnn as fast as CNNs，Lei et al.,2017复现 (opennmt-py)
### 数据集WMT14 en-to-de
数据集从 https://nlp.stanford.edu/projects/nmt/ 下载。**特别注意** 这个数据不是通用的数据，整整两周，我用这个数据没有浮现sru、luong和transfomer，因为这个数据内部是有作者专门为自己的程序而插入的mark的。在数据的下载链接那并没说这个事。

### 数据预处理
- 依然有内存开销极大的情况. 首先这个在building training阶段出现这个错误的时候，通过将onmt/IO.py中196行的filter_pred设为None可以解决这个而问题，filter_pred是用在torchtext.data.Dataset这个函数中的，不在opennmt项目中，它的用途是在提供程序选项opt的情况，根据opt中的语句最大长度，过滤掉数据中长度长于最大长度的语句。目前可以认为是这个过滤过程出了问题，变成了一个大耗内存的操作，但是这个问题并不是比如出现的，根据这个issuse（https://github.com/OpenNMT/OpenNMT-py/pull/291）的看法，是因为默认设置的语句最大长度为50，而训练数据里面全部都比50大，于是会出现这个问题（既出现bug，把内存耗完），这个issuse的做法是在preprocess是通过选项设置将语句的最大长度设置为1000，但即使这样内存开销还是很大，可见IO代码中还是有问题，但是不是会出现一直增长导致内存耗尽的问题。目前正在测试这个做法是否有效：靠谱，能解决这问题！
- vocabulary限制为50K，要做tokenizattion，translation时需要unk replacement，没有明确说需要做句子过滤,但是如果它参考的是luong的话，那么句子长度是不能超过50的。

### 训练
- 禁用input_feed 通过设置-input_feed 0, 这个量是当bool量在代码里用的
- 运行sru需要安装cupy和pynvrt两个python包，后一个pip安装成功，前一个失败。这里安装失败的原因是cupy需要cuda而容器内没有，nvidia-docker的作用是将硬件GPU自动映射如docker，而不需要专门挂在，不会将外界的cuda也加载进来，所以还要安装。下载的容器里是安装了英伟达驱动的，所以再次安装驱动会失败，之所以一般觉得没驱动，是因为驱动的那些应用，如nvidia-smi没有加入path，用find / -name nvidia找一下就能找到路径了。还有nvcc是在cuda里面的，就要去/usr/local/cuda-8.0/bin里去找。特别注意，环境变量很重要，docker容器中已经包含了环境，只是环境变量没设置，nvidia驱动的位置一般在/usr/local/nvidia下面，它的bin要加入环境变量PATH中；cuda的lib64要加入LD_LIBRARY_PATH中。
  - pull pytorch latest docker image
  - 修改~/.bashrc,将/usr/local/nvidia/bin加入path
  - 安装cuda，修改系统变量
  - 安装opennmt-py的requirement
  - 安装pynvrtc
  - 安装cupy时报错，ld找不多-lcuda，这是找不多/usr/lib/libcuda.so这么一个共享链接库，因为ld不会用到LD_LIBRARY_PATH这个环境变量。始终无法解决这个问题，很可能是因为cuda的版本不对要求
  - 在一个cuda已经安装好的环境里，安装pytorch（github主页教程，python setup.py install时需要编译c语言），再安装opennmt-py
### 测试
- 测试出问题，不明所以，原因出在pytorch/text/torchtext上面，要求强制回退到0.1.1版本。回退之后，出现的问题是cupy库的CUDA_ERROR_INVALID_HANDLE问题。坑爹的是找了一天，从sru的原作者的项目issue中发现（https://github.com/taolei87/sru/issues/8），这个可能是代码本身的问题，它只能用一块显卡，既是是不同的进程运行，也只能运行在一块显卡上面。解决方法(我使用解决方法2)
```
可设置环境变量CUDA_VISIBLE_DEVICES，指明可见的cuda设备
方法1： 在/etc/profile或~/.bashrc的配置文件中配置环境变量(/etc/profile影响所有用户，~/.bashrc影响当前用户使用的bash shell)
在/etc/profile文件末尾添加以下行：
export CUDA_VISIBLE_DEVICES=0,1 ##仅显卡设备0,1GPU可见。可用的GPU可通过nvidia-smi -L命令查看
:wq保存并退出
source /etc/profile使配置文件生效
方法2：若上述配置无效，可在执行cuda程序时指明参数，如
CUDA_VISIBLE_DEVICES=0,1 ./cuda_executable
```

## OpenNMT

### 安装环境
1. 只需要安装lua就行了。
2. 其次lua环境要先安装tds模块（预处理数据时发现），安装方法，使用lua自带的安装器：
   ```
     luarocks install tds
   ```
  这样运行快速入门里的例子就没问题了。
3. 注意，-gpuid 这个参数是从1开始的，如果设成0的话，会自动切换成多核cpu运行。

## OpenNMT-py
>2017.11

### API和模块

#### onmt/Translator.py包含已训练好模型的调用
但是OpenNMT-py的调用结构封装的很严实，并不是很好进行修改。

- 层次查找：下面是一个模型load后的树状结构，一般叶子节点是可以访问到存储参数的。
```
NMTModel (
  (encoder): RNNEncoder (
    (embeddings): Embeddings (
      (make_embedding): Sequential (
        (emb_luts): Elementwise (
          (0): Embedding(50002, 1000, padding_idx=1)
        )
      )
    )
    (rnn): LSTM(1000, 1000, num_layers=4, dropout=0.2)
  )
  (decoder): InputFeedRNNDecoder (
    (embeddings): Embeddings (
      (make_embedding): Sequential (
        (emb_luts): Elementwise (
          (0): Embedding(50004, 1000, padding_idx=1)
        )
      )
    )
    (dropout): Dropout (p = 0.2)
    (rnn): StackedLSTM (
      (dropout): Dropout (p = 0.2)
      (layers): ModuleList (
        (0): LSTMCell(2000, 1000)
        (1): LSTMCell(1000, 1000)
        (2): LSTMCell(1000, 1000)
        (3): LSTMCell(1000, 1000)
      )
    )
    (attn): GlobalAttention (
      (linear_in): Linear (1000 -> 1000)
      (linear_out): Linear (2000 -> 1000)
      (sm): Softmax ()
      (tanh): Tanh ()
    )
  )
  (generator): Sequential (
    (0): Linear (1000 -> 50004)
    (1): LogSoftmax ()
  )
)
```

#### 常用的结构单元
- Embedding层：pytorch的Embedding在这里被层层封装
self.model.encoder.embeddings.make_embedding[0][0].weight才能访问到保存的embendding。

- LSTM层：
  - Encoder节点的LSTM是pytorch自带的LSTM所以可以用 **weight_ih_l层数** 这样的方法来访问参数。
  - Decoder节点的LSTM可能是OpenNMT-py自己构建的StackedRNN，但是它的构成单元还是pytorch的RNNCell，所以可以追溯到构建单元的LSTMCell，然后用 **weight_ih**/**wegiht_hh**/**bias_ih**/**bias_hh** 这些属性变量来访问参数。

- Generator:
  这是指从网络output部分到预测结果部分的衔接结构

### 实现细节
>使用的python,pytorch函数，自己定义的函数等

- itertools.count函数：
count(),	参数：start, [step]；	输出：start, start+step, start+2*step, …
示例：count(10) --> 10 11 12 13 14 ...
实现中使用了yield关键字，每次调用才返回一个结果，不是一次产生一个列表。

- collections.defaultdict()：
众所周知，在Python中如果访问字典中不存在的键，会引发KeyError异常。collections.defaultdic本身提供了默认值，所以不会出现keyerror异常。
defaultdict类的初始化函数接受一个类型作为参数，当所访问的键不存在的时候，可以实例化一个值作为默认值；或者可以接受一个无参函数作为初始化参数，以这个函数的返回值作为默认值。
示例：
1.
$ dd = defaultdict(list)
$ dd['foo']
[]
2.
$ counts = defaultdict(lambda: 0)
$ counts['foo']
0

- vocab 和fields的结构关系，极其复杂，我觉得应该忽略不管。

- embedding构建中的，接受的参数feature_dict是什么：暂时不知道，跑出来是空列表
- embedding接受的参数，word_dict.stoi包含的是什么：里面是以单词为键，以一个整型为值的字典。应该是用来生成word embedding的单词序号
word_dict = fields['src'/'tgt'].vocab这格式直接从vocab.pt中load出来的src和tgt的vocab，

- 在构建RNNEncoder中用到的getattr函数：
getattr(object, name[,default])
获取对象object的属性或者方法，如果存在打印出来，如果不存在，打印出默认值，默认值可选。
需要注意的是，如果是返回的对象的方法，返回的是方法的内存地址，如果需要运行这个方法，
可以在后面添加一对括号。

## py-torch

### python

#### 语言特性

- （内置）next函数：函数必须接收一个可迭代对象参数，每次调用的时候，返回可迭代对象的下一个元素。如果所有元素均已经返回过，则抛出StopIteration 异常。

##### Variable变量
- data保存数据，grad保存梯度，都是tensor，不会自动更新data需要手动通过grad来更新data
```
w1=Variable(torch.Tensor([1.0, 2.0, 3.0]), requires_grad=True)
w1.data
w1.grad
```
- 使用backward()函数计算梯度，注意梯度是累加到每个相关Variable的grad张量中的,不对grad清零的话它会一直累加下去
```
x=Variable(torch.Tensor([1,1,1]))
w1=Variable(torch.Tensor([1.0, 2.0, 3.0]), requires_grad=True)
d1=w1.dot(x)
d2=w1.dot(torch.cat((d,d,d)))
d2.backward()

w1.grad
Out[44]:
Variable containing:
 12
 12
 12
[torch.FloatTensor of size 3]
```
注意，这里计算的时候先计算d1->d2时w1的梯度，为6，存到grad中；再极端delta d1到w1的梯度，分别诶(1+2+3)=6.加起来是12.

- 如果要重复计算一个计算流图的梯度的话（就是同一个输入做两次backward），需要在第一次backward是设置retain_graph=True
这个的判断应该不是通过某个计算过程中最后的地方有没有做过backward判断，而是整个图中是否已经有哪个带grad的参数被更新了，有就会报错（需要retain_graph）。
所以计算流程中有一部分做要先做backward，先做的就要用retain_graph.对于给定的x，截止最后一次backward前，都要如此。


#### __future__ 模块
Python提供了__future__模块，把下一个新版本的特性导入到当前版本，于是我们就可以在当前版本中测试一些新版本的特性。

### 常用API
- torch.bmm: torch.bmm(batch1, batch2, out=None) → Tensor; Performs a batch matrix-matrix product of matrices stored in batch1 and batch2.
batch1 and batch2 must be 3D Tensors each containing the same number of matrices.
If batch1 is a b x n x m Tensor, batch2 is a b x m x p Tensor, out will be a b x n x p Tensor.

- class torch.nn.GRU(\*args, \*\*kwargs)
input_size – The number of expected features in the input x
hidden_size – The number of features in the hidden state h
num_layers – Number of recurrent layers.
bias – If False, then the layer does not use bias weights b_ih and b_hh. Default: True
batch_first – If True, then the input and output tensors are provided as (batch, seq, feature)
dropout – If non-zero, introduces a dropout layer on the outputs of each RNN layer except the last layer
bidirectional – If True, becomes a bidirectional RNN. Default: False
获取GRU保存权值的方法是通过下面几个属性变量：
weight_ih_l层数，input-hidden
weight_hh_k层数，hidden-hidden
bias_in_l层数，input-hidde bias
bias_hh_l层数，hidden-hidden bias
```
> encoder.gru.weight_ih_l0.size()
torch.Size([1500, 500])
```

- GRU在bidirection为true情况下的输出隐藏状态维度是(2,batch_size, hidden_size)
- 如果想变量能自动求导的话，在定义时需要将变量包裹进autograd.Variable里，并在能适用cuda的情况下，适用.cuda()数据
- 特别注意GRU单元的维度结构为：输入:input, hidden_0, input=>(seq_len, batch, input_size),  hidden=>(num_layers * num_directions, batch, hidden_size);输出:output, hidden_n, output=>(seq_len, batch, hidden_size * num_directions),hidden_n=>(num_layers * num_directions, batch, hidden_size)

- view function: reshape the tensor. 可以使用-1参数，不过只有一维可以，-1的意思是这一维度的数字不知道，有程序自己推定。

- torch.squeeze(tensor [, dim]):将tensor中1的的维度去掉，如nx1xm,经过squeeze后变成nxm;如果指定了dim，则事当dim维为1时去掉那一维，不然维持不变。

- torch.nn.utils.rnn.pack_padded_sequence(inut, lengths, batch_first=False) => PackedSequence object
Packs a Variable containing padded sequences of variable length. Input can be of size  __TXBX*__ where T is the length of the longest sequence (equal to lengths[0]), B is the batch size, and * is any number of dimensions (including 0). If __batch_first__ is True __BxTx*__ inputs are expected. The sequences should be sorted by length in a decreasing order, i.e. input[:,0] should be the longest sequence, and input[:, B-1] the shortest one.

- torch.nn.utils.rnn.pad_packed_sequence(sequence, batch_first=False, padding_value=0.0) => (Variable containing the padded sequence, [lengths of each sequence in the batch])
Pads a packe batch of variable length sequences. It is an inverse operation to pack_padded_sequence.
The reurened Variable's data will be of size __TXBX*__. If __batch_first__ is True, the data will be transposed into __BXTX*__ format.

- torch.nn.Embedding
A simple lookup table taht stores embeddings of a fixed dictionary and size.
This module is often used to store word embeddings and retrieve them using indices. The input to the module is a list of indices, and the output is the corresponding word embeddings.
想要修改这个对象的权值，需要通过embedding.weight.data来进行修改。

- torch.nn.functional.log_softmax(input, dim=None)
input is Variable, dim is the dimension along which log_softmax will be computed.

- Tensor.contiguous() -> Tensor
Returens a contiguous tensor containing the same data as this tensor. Contiguous tensor is contiguous in memeory in C order. If this tensor is contiguous, this function returns the origianl tensor.

### 实现细节
- 对于长度不定的输入语句，如何实现batch模型的输入？
