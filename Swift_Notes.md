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
