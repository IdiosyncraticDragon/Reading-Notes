# Notes of SWIFT
> author:  Guiying Li

## Basic

### enviroment
1. 如果你想创建 OS x 程序，需要导入 Cocoa 包 import Cocoa
```
import Cocoa
var str = "Hello, playground"
```
2. 如果我们想创建 iOS playground 则需要引入 UIKit
```
import UIKit
var myString = "Hello, World!"
print(myString
```
3. Import

 我们可以使用 import 语句来引入任何的 Objective-C 框架（或 C 库）到 Swift 程序中。例如 import cocoa 语句导入了使用了 Cocoa 库和API，我们可以在 Swift 程序中使用他们。

Cocoa 本身由 Objective-C 语言写成，Objective-C 又是 C 语言的严格超集，所以在 Swift 应用中我们可以很简单的混入 C 语言代码，甚至是 C++ 代码。

### language basic

1. 注释：

```
单行注释：//
多行注释：/**/
多行注释嵌套：
/* 这是第一个多行注释的开头

   /* 这是嵌套的第二个多行注释 */

这是第一个多行注释的结尾 */
```

2. Swift不要求在每行语句的结尾使用分号(;)，但当你在同一行书写多条语句时，必须用分号隔开

3. 空格：
运算符不能直接跟在变量或常量的后面。

4. 数据类型：[Swift是一个类型安全（type safe）的语言。由于 Swift 是类型安全的，所以它会在编译你的代码时进行类型检查（type checks），并把不匹配的类型标记为错误。]

Int: 字长与平台字长一致，64位平台就是Int64一样长．

UInt: 无符号类型Int

Float: 32位浮点数

Double: 64位浮点数

Bool: true和false

字符串："Hello"

字符："c"

optionals: 可选类型来处理值可能缺失的情况。可选类型表示有值或没有值。

5. 类型别名：

类型别名对当前的类型定义了另一个名字，类型别名通过使用 typealias 关键字来定义。语法格式如下：
```
typealias newname = type

e.g.:
typealias Feet = Int

var distance: Feet = 100
```

6. 类型推断:

如果你没有显式指定类型，Swift 会使用类型推断（type inference）来选择合适的类型。

```
let meaningOfLife = 42
// meaningOfLife 会被推测为 Int 类型

let pi = 3.14159
// pi 会被推测为 Double 类型

let anotherPi = 3 + 0.14159
// anotherPi 会被推测为 Double 类型

var varA = 42
// varA 会被推测为 Int 类型 
```

7. 变量

变量声明意思是告诉编译器在内存中的哪个位置上为变量创建多大的存储空间。在使用变量前，你需要使用 var 关键字声明它，如下所示：
```
var variableName = <initial value>

//==========example==========

import Cocoa

var varA = 42

var varB:Float

varB = 3.14159
```
变量名也可以使用简单的 Unicode 字符(包括各种文字甚至还有表情)

8. 变量输出：

在字符串中可以使用括号与反斜线来插入变量．
```
import Cocoa

var name = "菜鸟教程"

var site = "http://www.runoob.com"

print("\(name)的官网地址为：\(site)")
```

9. 可选类型

wfit语言定义后缀？作为命名类型Optional的简写，换句话说，以下两种声明是相等的：
```
var optionalInteger: Int?

var optionalInteger: Optional<Int>
```
Swift 的可选（Optional）类型，用于处理值缺失的情况。可选表示"那儿有一个值，并且它等于 x "或者"那儿没有值"。

Optional 是一个含有两种情况的枚举，None和Some(T)，用来表示可能有或可能没有值。任何类型都可以明确声明为（或者隐式转换）可选类型。当声明一个可选类型的时候，要确保用括号给？操作符一个合适的范围。例如，声明可选整数数组，应该写成(Int[])?；写成Int[]?会报错。 

当你声明一个可选变量或者可选属性的时候没有提供初始值，它的值会默认为nil。

可选项遵照LogicValue协议，因此可以出现在布尔环境中。在这种情况下，如果可选类型T?包含类型为T的任何值（也就是说它的值是Optional.Some(T)），这个可选类型等于true，反之为false。

如果一个可选类型的实例包含一个值，你可以用后缀操作符 ！来访问这个值(这也被称为___可选值的强制解析___)，如下所示：
```
optionalInteger = 42

optionalInteger! // 42
```

- 强制解析
```
var myString:String?

myString = "Hello, Swift!"

print( myString! )
```
- 自动解析

你可以在声明可选变量时使用感叹号（!）替换问号（?）。这样可选变量在使用时就不需要再加一个感叹号（!）来获取值，它会自动解析。

```
var myString:String!

myString = "Hello, Swift!"

print(myString)
```

- 可选绑定

使用可选绑定（optional binding）来判断可选类型是否包含值，如果包含就把值赋给一个临时常量或者变量。可选绑定可以用在if和while语句中来对可选类型的值进行判断并把值赋给一个常量或者变量。
```
if let constantName = someOptional {

    statements

}

//============example==============
var myString:String?

myString = "Hello, Swift!"

if let yourString = myString {

   print("你的字符串值为 - \(yourString)")

}else{

   print("你的字符串没有值")

}
```

10. 常量

常量使用关键字 let 来声明，语法如下：
```
let constantName = <initial value>
```
常量一旦设定，在程序运行时就无法改变其值。

常量可以是任何的数据类型如：整型常量，浮点型常量，字符常量或字符串常量。同样也有枚举类型的常量：

常量类似于变量，区别在于常量的值一旦设定就不能改变，而变量的值可以随意更改。

11. 类型标注

当你声明常量或者变量的时候可以加上类型标注（type annotation），说明常量或者变量中要存储的值的类型。如果要添加类型标注，需要在常量或者变量名后面加上一个冒号和空格，然后加上类型名称。
```
var constantName:<data type> = <optional initial value>
```
加了类型标注后，可以在声明时不给常量赋值，在之后再赋值．

12. 字面量

- 整型字面量
```
let decimalInteger = 17           // 17 - 十进制表示

let binaryInteger = 0b10001       // 17 - 二进制表示

let octalInteger = 0o21           // 17 - 八进制表示

let hexadecimalInteger = 0x11     // 17 - 十六进制表示
```

- 浮点型字面量

除非特别指定，浮点型字面量的默认推导类型为 Swift 标准库类型中的 Double，表示64位浮点数。

浮点型字面量默认用十进制表示（无前缀），也可以用十六进制表示（加前缀 0x）。

十进制浮点型字面量由十进制数字串后跟小数部分或指数部分（或两者皆有）组成。十进制小数部分由小数点 . 后跟十进制数字串组成。指数部分由大写或小写字母 e 为前缀后跟十进制数字串组成，这串数字表示 e 之前的数量乘以 10 的几次方。例如：1.25e2 表示 1.25 ⨉ 10^2，也就是 125.0；同样，1.25e2 表示 1.25 ⨉ 10^2，也就是 0.0125。

- 字符串型字面量

字符串型字面量中不能包含未转义的双引号 （"）、未转义的反斜线（\）、回车符或换行符。
```
转移字符：

\0 : 空字符

\\ : 反斜杠

\b : 退格，将当前位置移到前一列

\f : 换页，将当前位置移到下页开头

\n : 换行符

\r : 回车符

\t : 水平制表符

\v : 垂直制表符

\' : 单引号

\" : 双引号

\000 : 1到3位八进制所代表的任意字符

\xhh... : 1到2为十六进制代表的任意字符
```

- 布尔型字面量

布尔型字面量的默认类型是 Bool。

布尔值字面量有三个值，它们是 Swift 的保留关键字：

```
true 表示真。

false 表示假。

nil 表示没有值
```

13. 运算符

```
    算术运算符

    比较运算符

    逻辑运算符

    位运算符

    赋值运算符

    区间运算符

    其他运算符
```

- 算术运算符：
```
+ 	加号 	A + B 结果为 30

− 	减号 	A − B 结果为 -10

* 	乘号 	A * B 结果为 200

/ 	除号 	B / A 结果为 2

% 	求余 	B % A 结果为 0

++ 	自增 	A++ 结果为 11

-- 	自减 	A-- 结果为 9

```

- 比较运算符：
```

== 	等于 	(A == B) 为 false。

!= 	不等于 	(A != B) 为 true。

\> 	大于 	(A > B) 为 false。

< 	小于 	(A < B) 为 true。

>= 	大于等于 	(A >= B) 为 false。

<= 	小于等于 	(A <= B) 为 true。
```

- 逻辑运算符：
```
&& 	逻辑与。如果运算符两侧都为 TRUE 则为 TRUE。 	(A && B) 为 false。

|| 	逻辑或。 如果运算符两侧至少有一个为 TRUE 则为 TRUE。 	(A || B) 为 true。

! 	逻辑非。布尔值取反，使得true变false，false变true。 	!(A && B) 为 true。
```

- 位运算符：
```
& 	按位与。按位与运算符对两个数进行操作，然后返回一个新的数，这个数的每个位都需要两个输入数的同一位都为1时才为1。

| 	按位或。按位或运算符|比较两个数，然后返回一个新的数，这个数的每一位设置1的条件是两个输入数的同一位都不为0(即任意一个为1，或都为1)。

^ 	按位异或. 按位异或运算符^比较两个数，然后返回一个数，这个数的每个位设为1的条件是两个输入数的同一位不同，如果相同就设为0。

~ 	按位取反运算符~对一个操作数的每一位都取反。

<< 	按位左移。左移操作符（<<）将操作数的所有位向左移动指定的位数。

>> 	按位右移。右移操作符（<<）将操作数的所有位向又移动指定的位数。
```

- 赋值运算符：
```
= 	简单的赋值运算，指定右边操作数赋值给左边的操作数。 	C = A + B 将 A + B 的运算结果赋值给 C

+= 	相加后再赋值，将左右两边的操作数相加后再赋值给左边的操作数。 	C += A 相当于 C = C + A

-= 	相减后再赋值，将左右两边的操作数相减后再赋值给左边的操作数。 	C -= A 相当于 C = C - A

*= 	相乘后再赋值，将左右两边的操作数相乘后再赋值给左边的操作数。 	C *= A 相当于 C = C * A

/= 	相除后再赋值，将左右两边的操作数相除后再赋值给左边的操作数。 	C /= A 相当于 C = C / A

%= 	求余后再赋值，将左右两边的操作数求余后再赋值给左边的操作数。 	C %= A is equivalent to C = C % A


<<= 	按位左移后再赋值 	C <<= 2 相当于 C = C << 2

>>= 	按位右移后再赋值 	C >>= 2 相当于 C = C >> 2

&= 	按位与运算后赋值 	C &= 2 相当于 C = C & 2

^= 	按位异或运算符后再赋值 	C ^= 2 相当于 C = C ^ 2

|= 	按位或运算后再赋值 	C |= 2 相当于 C = C | 2
```

- 区间运算符：
```
闭区间运算符 	闭区间运算符（a...b）定义一个包含从a到b(包括a和b)的所有值的区间，b必须大于等于a.闭区间运算符在迭代一个区间的所有值时是非常有用的，如在for-in循环中 	1...5 区间值为 1, 2, 3, 4 和 5

半开区间运算符 	半开区间 	1.. < 5 区间值为 1, 2, 3, 和 4

//===========example=======

print("闭区间运算符:")

for index in 1...5 {

    print("\(index) * 5 = \(index * 5)")

}

print("半开区间运算符:")

for index in 1..<5 {

    print("\(index) * 5 = \(index * 5)")

}
```

- 其他运算符:
```
    一元运算符对单一操作对象操作（如-a）。一元运算符分前置运算符和后置运算符，前置运算符需紧跟在操作对象之前（如!b），后置运算符需紧跟在操作对象之后（如i++）。

    二元运算符操作两个操作对象（如2 + 3），是中置的，因为它们出现在两个操作对象之间。

    三元运算符操作三个操作对象，和 C 语言一样，Swift 只有一个三元运算符，就是三目运算符（a ? b : c）。
```

- 运算符优先级

逗号操作符具有最低的优先级。

相同优先级中，按结合顺序计算。大多数运算是从左至右计算，只有三个优先级是从右至左结合的，它们是单目运算符、条件运算符、赋值运算符。
```

     指针最优，单目运算优于双目运算。如正负号。

    先乘除（模），后加减。

    先算术运算，后移位运算，最后位运算。请特别注意：1 << 3 + 2 & 7 等价于 (1 << (3 + 2))&7

    逻辑运算最后计算
```

14. 条件语句:
```
if 语句
	if 语句 由一个布尔表达式和一个或多个执行语句组成。

//==============example=================

if boolean\_expression {

   /* 如果布尔表达式为真将执行的语句 */

}

//==============end example=============

if...else 语句
	if 语句 后可以有可选的 else 语句, else 语句在布尔表达式为 false 时执行。

if...else if...else 语句
	if 后可以有可选的 else if...else 语句, else if...else 语句常用于多个条件判断。

内嵌 if 语句
	你可以在 if 或 else if 中内嵌 if 或 else if 语句。

switch 语句
	switch 语句允许测试一个变量等于多个值时的情况。
//==============example=================

switch expression {

   case expression1  :

      statement(s)

      fallthrough /* 可选 */

   case expression2, expression3  :

      statement(s)

      fallthrough /* 可选 */

  
   default : /* 可选 */

      statement(s);

}

注意： case 语句中如果没有使用 fallthrough 语句，则在执行当前的 case 语句后，switch 会终止，控制流将跳转到 switch 语句后的下一行。

如果使用了fallthrough 语句，则会继续执行之后的 case 或 default 语句，不论条件是否满足都会执行。

//==============end example=============
```

15. 循环
- 种类
```
for-in
	遍历一个集合里面的所有元素，例如由数字表示的区间、数组中的元素、字符串中的字符。

for 循环
	用来重复执行一系列语句直到达成特定条件达成，一般通过在每次循环完成后增加计数器的值来实现。

while 循环
	运行一系列语句，如果条件为true，会重复运行，直到条件变为false。

repeat...while 循环
	类似 while 语句区别在于判断循环条件之前，先执行一次循环的代码块。
```

- 循环控制语句
```
continue 语句
	告诉一个循环体立刻停止本次循环迭代，重新开始下次循环迭代。

break 语句
	中断当前循环。

fallthrough 语句
	如果在一个case执行完后，继续执行下面的case，需要使用fallthrough(贯穿)关键字。
```

- 代码实例
for-in
```
for index in var {

   循环体

}

//=====================

var someInts:[Int] = [10, 20, 30]


for index in someInts {

   print( "index 的值为 \(index)")

}
```

for 循环
```
for init; condition; increment{

   循环体

}

//=====================

var someInts:[Int] = [10, 20, 30]


for var index = 0; index < 3; ++index {

   print( "索引 [\(index)] 对应的值为 \(someInts[index])")

}
```

while 循环
```
while condition

{

   statement(s)

}

//===================

var index = 10


while index < 20 

{

   print( "index 的值为 \(index)")

   index = index + 1

}
```

repeat...while 循环
```
repeat

{

   statement(s);

}while( condition );
//===================

var index = 15


repeat{

    print( "index 的值为 \(index)")

    index = index + 1

}while index < 20

```
 16. 字符串
```
isEmpty 	判断字符串是否为空，返回布尔值

hasPrefix(prefix: String) 	检查字符串是否拥有特定前缀

hasSuffix(suffix: String) 	检查字符串是否拥有特定后缀。

Int(String) 	转换字符串数字为整型。

String.characters.count 	计算字符串的长度

utf8 	可以通过遍历 String 的 utf8 属性来访问它的 UTF-8 编码

utf16 	可以通过遍历 String 的 utf8 属性来访问它的 UTF-16 编码

unicodeScalars 	可以通过遍历String值的unicodeScalars属性来访问它的 Unicode 标量编码.

+ 	连接两个字符串，并返回一个新的字符串

+= 	连接操作符两边的字符串并将新字符串赋值给左边的操作符变量

== 	判断两个字符串是否相等

< 	比较两个字符串，对两个字符串的字母逐一比较。

!= 	比较两个字符是否不相等。
```
