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
- 定义
```
optional_function_scope function function_name( argument1, argument2, argument3..., argumentn)
	function_body
	return result_params_comma_separated
end
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
