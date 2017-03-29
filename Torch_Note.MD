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

## OpenNMT

### 安装环境
1. 只需要安装lua就行了。
2. 其次lua环境要先安装tds模块（预处理数据时发现），安装方法，使用lua自带的安装器：
   ```
     luarocks install tds
   ```
  这样运行快速入门里的例子就没问题了。
3. 注意，-gpuid 这个参数是从1开始的，如果设成0的话，会自动切换成多核cpu运行。
