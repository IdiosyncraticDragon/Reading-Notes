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

### 

## OpenNMT

### 安装环境
1. 只需要安装lua就行了。
2. 其次lua环境要先安装tds模块（预处理数据时发现），安装方法，使用lua自带的安装器：
   ```
     luarocks install tds
   ```
  这样运行快速入门里的例子就没问题了。
3. 注意，-gpuid 这个参数是从1开始的，如果设成0的话，会自动切换成多核cpu运行。
