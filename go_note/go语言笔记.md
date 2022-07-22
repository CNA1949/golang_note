# Golang标准库文档：

```
https://studygolang.com/pkgdoc
```



# 获取用户终端输入：

## `func Scanf`

```go
func Scanf(format string, a ...interface{}) (n int, err error)
```

`Scanf`从标准输入扫描文本，根据`format`参数指定的格式将成功读取的空白分隔的值保存进成功传递给本函数的参数。返回成功扫描的条目个数和遇到的任何错误。

```go
func main() {
	var name string
	var age byte
	var gender string
	fmt.Print("请输入姓名，年龄，性别，使用空格隔开：")
	fmt.Scanf("%s %d %s", &name, &age, &gender)
	fmt.Println("姓名：", name, "年龄：", age, "性别：", gender)
}
```



## `func Fscanf`

```go
func Fscanf(r io.Reader, format string, a ...interface{}) (n int, err error)
```

`Fscanf`从`r`扫描文本，根据`format `参数指定的格式将成功读取的空白分隔的值保存进成功传递给本函数的参数。返回成功扫描的条目个数和遇到的任何错误。

## `func Sscanf`

```go
func Sscanf(str string, format string, a ...interface{}) (n int, err error)
```

`Sscanf`从字符串`str`扫描文本，根据`format `参数指定的格式将成功读取的空白分隔的值保存进成功传递给本函数的参数。返回成功扫描的条目个数和遇到的任何错误。

## `func Scan`

```go
func Scan(a ...interface{}) (n int, err error)
```

`Scan`从标准输入扫描文本，将成功读取的空白分隔的值保存进成功传递给本函数的参数。换行视为空白。返回成功扫描的条目个数和遇到的任何错误。如果读取的条目比提供的参数少，会返回一个错误报告原因。

## `func Fscan`

```go
func Fscan(r io.Reader, a ...interface{}) (n int, err error)
```

`Fscan`从r扫描文本，将成功读取的空白分隔的值保存进成功传递给本函数的参数。换行视为空白。返回成功扫描的条目个数和遇到的任何错误。如果读取的条目比提供的参数少，会返回一个错误报告原因。

## `func Sscan`

```go
func Sscan(str string, a ...interface{}) (n int, err error)
```

`Sscan`从字符串`str`扫描文本，将成功读取的空白分隔的值保存进成功传递给本函数的参数。换行视为空白。返回成功扫描的条目个数和遇到的任何错误。如果读取的条目比提供的参数少，会返回一个错误报告原因。

## `func Scanln`

```go
func Scanln(a ...interface{}) (n int, err error)
```

`Scanln`类似`Scan`，但会在换行时才停止扫描。最后一个条目后必须有换行或者到达结束位置。

```go
func main() {
	var name string
	var age byte
	var gender string
	fmt.Print("请输入姓名：")
	fmt.Scanln(&name)
	fmt.Print("\n请输入年龄：")
	fmt.Scanln(&age)
	fmt.Print("\n请输入性别：")
	fmt.Scanln(&gender)
	fmt.Println("姓名：", name, "年龄：", age, "性别：", gender)
}
```



## `func Fscanln`

```
func Fscanln(r io.Reader, a ...interface{}) (n int, err error)
```

`Fscanln`类似`Fscan`，但会在换行时才停止扫描。最后一个条目后必须有换行或者到达结束位置。

## `func Sscanln`

```go
func Sscanln(str string, a ...interface{}) (n int, err error)
```

`Sscanln`类似`Sscan`，但会在换行时才停止扫描。最后一个条目后必须有换行或者到达结束位置。



# 值类型与引用类型

golang中的值类型：整型、浮点型、布尔型、`string`、数组、结构体。

golang中的引用类型：`map(映射)`、指针、切片、`channel(管道)`、`interface(接口)`、`function(函数)`

# 变量与常量

[Go语言基础之变量和常量 | 李文周的博客 (liwenzhou.com)](https://www.liwenzhou.com/posts/Go/01_var_and_const/)



# 基本数据类型

[Go语言基础之基本数据类型 | 李文周的博客 (liwenzhou.com)](https://www.liwenzhou.com/posts/Go/02_datatype/)

# 运算符

[Go语言基础之运算符 | 李文周的博客 (liwenzhou.com)](https://www.liwenzhou.com/posts/Go/03_operators/)

# 流程控制

[Go语言基础之流程控制 | 李文周的博客 (liwenzhou.com)](https://www.liwenzhou.com/posts/Go/04_basic/)



# 分支

## switch用法

**golang中`switch`语句`case`后面不需要再加`break`**

```go
switch 表达式 {
case 表达式1,表达式2,...:
    语句块1
case 表达式3, 表达式4:
    语句块2
default:
    语句块
}
```

- `case`后面是一个**表达式**（即：常量值、变量、一个有返回值的函数等）。
- `case`后的各个表达式的值的数据类型，必须和`switch`表达式数据类型一致。
- `case`后面可以带多个表达式，使用个**逗号**间隔。
- `case`后面的表达式如果是常量值（字面量），则要求不能重复。
- `case`后面不需要带`break`，程序匹配到一个`case`后就会执行对应的代码块，然后退出`switch`，如果一个都匹配不到，则执行`default`或者退出`switch`语句。
- `default`语句不是必须的。

**`switch`后面不带表达式，可以当做`if-else if-else`来使用：**

```go
var age int = 18
switch{
    case age == 18:
    	fmt.Println("age == 18")
    case age == 20:
    	fmt.Println("age == 20")
    default:
    	fmt.Println("没有匹配到")
}
var score int = 80
switch{
    case score >= 60:
    	fmt.Println("成绩及格")
    case score >=70 && score < 90:
    	fmt.Println("成绩良好")
    case score >= 90:
    	fmt.Println("成绩优异")
    default:
    	fmt.Println("成绩不及格")
}
```

**`switch`后面可以直接声明/定义一个变量，分号结束，不推荐：**

```go
switch score := 80; {
	case score >= 60:
		fmt.Println("成绩及格")
	case score >= 70 && score < 90:
		fmt.Println("成绩良好")
	case score >= 90:
		fmt.Println("成绩优异")
	default:
		fmt.Println("成绩不及格")
}
```

**`switch`穿透：`fallthrough`（只能穿透一层`case`，并且跳过下一层的判断）：**

```go
var num int = 80
switch{
    case num >= 60:
    	fmt.Println("num >= 60")
    	fallthrough
    case num >=70:
    	fmt.Println("num >= 70")
    case score >= 90:
    	fmt.Println("num >= 90")
    default:
    	fmt.Println("num = ?")
}
/*
输出：
	num >= 60
	num >= 70
*/
```

**Type Switch：`switch`语句还可以被用于`type-switch`来判断某个`interface`变量中实际指向的变量类型：**

```go
var x interface{}
var y = 10.2
x = y
switch x.(type) {
    case int:
    	fmt.Println("x 是 int 型")
    case float64:
    	fmt.Println("x 是 float64 型")
    case bool, string:
    	fmt.Println("x 是 bool 或 string 型")
    default:
    	fmt.Println("x 类型未知")
}
/*
输出：
	x 是 float64 型
*/
```



**`switch`和`if`的比较：**

- 如果判断的具体数值不多，而且符合**整数**、**浮点数**、**字符**、**字符串**这几种类型。使用`switch`语句，简洁高效。
- 其他情况，对区间判断和结果为`bool`类型的判断，使用`if`。



# 循环与跳转

## for循环

### **基本语法：**

```go
// 方式一
for 循环变量初始化;循环条件;循环变量迭代 {
	//循环操作（语句块）/ 循环体
}
// 方式二：将 变量初始化 和 变量迭代 写到其他位置
for 循环判断条件 {
	// 循环执行语句
}
// 方式三：等价于 for;;{}，通常需要配合 break语句 使用
for {
    // 循环执行语句
}
// 方式四：for-range 多用于字符串和数组的遍历，可以包含中文
for index, value :range str{
    // 循环执行语句
}
```

### **`for-range`用法**

**传统方法遍历含有中文的字符串时，按照字节来遍历，中文会出现乱码，但可以将字符串转换为`[]rune`后再来遍历**

```go
// 遍历字符串
func main(){
    str := "love中国"
    // 传统方式，不能遍历含有中文的字符串
    for i := 0; i < len(str); i++ {
        fmt.Printf("index=%d, value=%c\n", i, str[i])
    }
}
    
/*
输出：
index=0, value=l
iindex=1, value=o
index=2, value=v
index=3, value=e
index=4, value=ä
index=5, value=¸
index=6, value=­
index=7, value=å
index=8, value= 
ndex=9, value=½ 
*/

```

```go
// 将字符串转换为 []rune
func main() {
	str := "love中国"
	str2 := []rune(str)
	for i := 0; i < len(str); i++ {
		fmt.Printf("index=%d, value=%c\n", i, str2[i])
	}
}
/*
输出：
index=0, value=l
index=1, value=o
index=2, value=v
index=3, value=e
index=4, value=中
index=5, value=国
*/
```

**`for-range`遍历含有中文的字符串时，是按照字符方式来遍历，不会出现乱码：**

```go
// 遍历字符串
func main() {
	// 遍历字符串
	str := "love中国"
	// for-range，能遍历含有中文的字符串
	for index, value := range str {
		fmt.Printf("index=%d, value=%c\n", index, value)
	}
}
/*
输出：
index=0, value=l
index=1, value=o 
index=2, value=v 
index=3, value=e 
index=4, value=中
index=7, value=国
*/
```



### `for`实现`while`和`do-while`效果

go语言中没有`while`语句和`do-while`语句，但可以使用`for`来实现。

**实现`while`：先判断再执行**

```go
循环变量初始化
for {
    if 循环条件表达式 {
		break	//跳出for循环
    }
    循环操作（语句块）
    循环变量迭代
}
```

```go
func main() {
	// for实现while效果
	var i int = 1 // 循环变量初始化
	for {
		if i > 10 { // 循环条件
			break // 跳出for循环，结束for循环
		}
		fmt.Println("count: ", i)
		i++ // 循环变量的迭代
	}
}
```

**实现`do-while`：先执行，再判断，因此至少执行一次**

```go
循环变量初始化
for {
	循环操作（语句块）
	循环变量迭代
    if 循环条件表达式 {
		break	//跳出for循环
    }
}
```

```go
func main() {
	// for实现do-while效果
	var i int = 1 // 循环变量初始化
	for {
		fmt.Println("count: ", i)
		i++         // 循环变量的迭代
		if i > 10 { // 循环条件
			break // 跳出for循环，结束for循环
		}
	}
}
```

## `break`与标签

- `break`默认会跳出最近的`for`循环。
- `break`后面可以指定标签，跳出标签对应的`for`循环。

```go
func main() {
label2:
	for i := 0; i < 3; i++ {
		// label1
		for j := 0; j < 3; j++ {
			fmt.Println("label2-index:", i, "label1-index:", j)
			break label2
		}
	}
}
/*输出：
label2-index: 0 label1-index: 0
*/
```



## `continue`与标签

- `continue`语句用于结束本次循环，继续执行下一次循环。
- `continue`语句出现在多层嵌套的循环语句体中时，可以通过标签指明要跳过的是哪一层循环。与`break`标签的使用的规则一样。

```go
func main() {
label2:
	for i := 0; i < 3; i++ {
		// label1
		for j := 0; j < 3; j++ {
			fmt.Println("label2-index:", i, "label1-index:", j)
			continue label2
		}
	}
}
/*输出：
label2-index: 0 label1-index: 0
label2-index: 1 label1-index: 0
label2-index: 1 label1-index: 0
*/
```

## `goto`语句

- Go语言的`goto`语句可以无条件地转移到程序中指定的行。
- `goto`语句通常与条件语句配合使用，可用来实现条件转移，跳出循环体等功能。
- 在Go程序设计中一般不主张使用`goto`语句，以免造成程序流程的混乱，使理解和调试程序都产困难。

```go
func main() {
	fmt.Println("goto1")
	goto label1
	fmt.Println("goto2")
	fmt.Println("goto3")
label1:
	fmt.Println("goto4")
	fmt.Println("goto5")
}
/*输出：
goto1
goto4
goto5
*/
```

# 包

- 包的本质实际上就是创建不同的文件夹，来存放程序文件。
- Go语言的每一个文件都是属于一个包的，也就是说Go语言是以包的形式来管理文件和项目目录结构的。
- 包的三大作用：
	- 区分相同名字的函数、变量等标识符。
	- 当程序文件很多时，可以很好的管理项目。
	- 控制函数、变量等访问范围，即作用域。

**打包基本语法：**

```go
package 包名
```

**引入包的基本语法：**

```go
import "包的路径"
```

**包的注意事项：**

- 在给一个文件打包时，该包对应一个文件夹。文件的包名通常和文件所在的文件夹名一致，一般为小写字母。
- 当一个文件要使用其他包函数或变量时，需要先引入对应的包。
- `package`指令在文件第一行，然后是`import`指令。
- 为了让其他包的文件可以访问到本包的函数，则该**函数名的首字母需要大写**，类似其它语言的`public`，这样才能跨包访问。
- 在访问其它包函数、变量时，其语法是 **包名.函数名**。
- 如果包名较长，Go语言支持给包取别名。取别名后，原来的包名即不能使用了，需要使用别名来访问该包的函数和变量。
- 在同一包下，不能有相同的函数名（也不能有相同的全局变量名），否则报重复定义错误。
- 如果要编译成一个可执行程序文件，就需要将这个包声明为`main`，即`package main`。



# 函数（引用类型）

**函数使用的注意事项：**

1. 函数的形参列表可以是多个，返回值列表也可以是多个。

2. 形参列表和返回值列表的数据类型可以是值类型和引用类型。

3. 函数的命名遵循标识符命名规范，首字母不能是数字，首字母大写的函数可以被本包文件和其他包文件使用，类似`public`，首字母小写的函数只能被本包文件使用，其他包文件不能使用，类似`private`。

4. 函数中的变量是局部的，函数外不生效。

5. 基本数据类型和数组默认都是值传递的，即进行**值拷贝**。在函数内修改，不会影响到原来的值。

6. 如果希望函数内的变量能够修改函数外部的变量，可以传入变量的地址，函数内以**指针**的方式操作变量。

7. **Go语言不支持重载**。

8. 在Go中，函数也是一种数据类型，可以赋值给一个变量，则该变量就是一个函数类型的变量了，通过该变量可以对函数进行调用：

	```go
	func getSum(n1 int, n2 int) int {
		return n1 + n2
	}
	func main() {
		s := getSum
		fmt.Printf("s的类型%T, getSum的类型%T\n", s, getSum)
		res := s(10, 20)
		fmt.Println("result=", res)
	}
	/*输出：
	s的类型func(int, int) int, getSum的类型func(int, int) int
	result= 30
	*/
	```

9. 在Go中，函数还可以作为形参，并且可以调用。

	```go
	func getSum(n1 int, n2 int) int {
		return n1 + n2
	}
	
	func calculate(getSum func(int, int) int, num1 int, num2 int) int {
		return getSum(num1, num2)
	}
	
	func main() {
		res := calculate(getSum, 10, 20)
		fmt.Println("result=", res)
	}
	/*输出：
	result= 30
	*/
	```

10. Go支持自定义数据类型：

	```go
	type 自定义数据类型名 数据类型	// 相当于一个别名
	
	//demo
	type myInt int	// myInt等价于int，但go认为 myInt和int是两个类型
	type mySun func(int, int) int	//这里mySun就等价于一个函数类型 func(int, int) int
	```

11. 支持对函数返回值命名：

	```go
	func getSumAndSub(n1 int, n2 int) (sum int, sub int) {
		sum = n1 + n2
		sub = n1 - n2
		return
	}
	
	func main() {
		sum, sub := getSumAndSub(10, 20)
		fmt.Println("sum=", sum, "sub=", sub)
	}
	/*输出：
	sum= 30 sub= -10
	*/
	```

12. 使用 _ 标识符，忽略返回值：

	```go
	func getSumAndSub(n1 int, n2 int) (sum int, sub int) {
		sum = n1 + n2
		sub = n1 - n2
		return
	}
	
	func main() {
		sum, _ := getSumAndSub(10, 20)
		fmt.Println("sum=", sum)
	}
	```

13. Go支持可变参数：

	```go
	// 支持0到多个参数
	func sum1(args ...int) int {
		var sum int
		for i := 0; i < len(args); i++ {
			sum += args[i]
		}
		return sum
	}
	// args是slice切片，通过args[index]可以访问到各个值
	
	// 支持1到多个参数
	func sum2(n1 int, args ...int) int {
		sum := n1
		for i := 0; i < len(args); i++ {
			sum += args[i]
		}
		return sum
	}
	```

	

	

## init函数

- 每一个源文件都可以包含一个`init`函数，该函数会在`main`函数执行前，被Go运行框架调用。**通常可以在`init`函数中完成初始化工作**。
- 如果一个文件同时包含**全局变量定义**，**`init`函数**和**`main`函数**，则执行的流程是 `全局变量定义->init函数->main函数`

```go
//定义全局变量
var age = test()

func test() int {
	fmt.Println("test()...")
	return 20
}

// init函数，通常可以在init函数中完成初始化工作
func init() {
	fmt.Println("init()...")
}

func main() {
	fmt.Println("main()...")
}
/*输出
test()...
init()...       
main()...age= 20
*/
```



## 匿名函数

**匿名函数使用方式：**

**方式一：**在定义匿名函数时就直接调用，这种方式匿名函数只能调用一次。

```go
func main() {
	// 在定义匿名函数时就直接调用，这种方式匿名函数只能调用一次。
	// 案例演示，求两个数的和，使用匿名函数的方式完成
	res := func(n1 int, n2 int) int {
		return n1 + n2
	}(10, 20)	// 传入参数值
	fmt.Println("res=", res)
}
```

**方式二：**将匿名函数赋给一个变量（函数变量），再通过该变量来调用匿名函数。

```go
func main() {
	// 在定义匿名函数时就直接调用，这种方式匿名函数只能调用一次。
	// 案例演示，求两个数的和，使用匿名函数的方式完成
	sum := func(n1 int, n2 int) int {
		return n1 + n2
	}
	res := sum(10, 20)
	fmt.Println("res=", res)
}
```

**全局方式三：匿名函数：**

如果将匿名函数赋给一个全局变量，那么这个匿名函数就成为一个全局匿名函数，可以在程序有效。

```go
var (
	// sum 就是一个全局匿名
	sum = func(n1 int, n2 int) int {
		return n1 + n2
	}
)

func main() {
	// 在定义匿名函数时就直接调用，这种方式匿名函数只能调用一次。
	// 案例演示，求两个数的和，使用匿名函数的方式完成
	res := sum(10, 20)
	fmt.Println("res=", res)
}
```



## 闭包

闭包就是一个函数和与其相关的引用环境组合的一个整体，也就是能够读取其他函数内部变量的函数。在本质上，闭包是将函数内部和函数外部连接起来的桥梁。

```go
func AddUpper() func(int) int {
	var n int = 10
	return func(x int) int {
		n = n + x
		return n
	}
}

func main() {
	f := AddUpper()
	fmt.Println("n=", f(1))
	fmt.Println("n=", f(2))
	fmt.Println("n=", f(3))
}
/*输出：
n= 11
n= 13
n= 16
*/
```

- `AddUpper`返回的是一个匿名函数，但是这个匿名函数引用到函数外的`n`，因此这个匿名函数就和`n`形成一个整体，构成闭包。
- 当反复的调用`f`函数时，因为`n`只初始化一次，所以每调用一次就进行累计。
- 闭包的关键，就是要分析出返回的函数使用（引用）到哪些变量，因为函数和它引用到的变量共同构成闭包。

**demo：**

```go
编写一个程序，具体要求如下：
1）编写一个函数 makeSuffix(suffix string) 可以接受一个文件后缀名（比如 .jpg），并返回一个闭包；
2）调用闭包，可以传入一个文件名，如果该文件名没有指定的后缀（例如 jpg），则返回 文件名.jpg，如果已经有 .jpg 后缀，则返回原文件名。
3）要求使用闭包的方式完成。
4）string HasSuffix，该函数是Go语言内置strings包下的函数，用于判断某个字符串是否有指定的后缀。
```

```go
func makeSuffix(suffix string) func(string) string {
	return func(name string) string {
		// 如果name没有指定后缀，则加上后缀，否则就返回原来的名字
		if !strings.HasSuffix(name, suffix) {
			return name + suffix
		}
		return name
	}
}

func main() {
	f := makeSuffix(".jpg")
	fmt.Println("文件名winter处理后=", f("winter"))
	fmt.Println("文件名bird.jpg处理后=", f("bird.jpg"))
}
/*输出：
文件名winter处理后= winter.jpg
文件名bird.jpg处理后= bird.jpg
*/
```

如果使用传统方法判断，每次都需要传入后缀名，而闭包因为可以保留上次引用的某个值，所以我们传入一次就可以反复使用。



## defer

在函数中，经常需要创建资源（比如数据库连接、文件句柄、锁等），为了在函数执行完毕后，及时的释放资源，Go语言提供了`defer`（延时机制）。

- 当`go`执行到一个`defer`时，不会立即执行`defer`后的语句，而是将`defer`后的语句压入到一个栈中，然后继续执行函数的下一个语句。
- 当函数执行完毕后，再从存`defer`语句的栈中，遵循先入后出的机制，依次从栈顶取出语句执行。在`defer`将语句放入到栈中时，也会将相关的值拷贝并同时入栈。

```go
func deferDemo(n1 int, n2 int) int {
	defer fmt.Println("ok1 defer1...n1=", n1)
	defer fmt.Println("ok2 defer2...n2=", n2)
	n1++
	n2++
	res := n1 + n2
	fmt.Println("ok3 res=", res)
	defer fmt.Println("ok4 defer3...n1++ =", n1)
	defer fmt.Println("ok5 defer4...n2++ =", n2)
	return res
}

func main() {
	result := deferDemo(10, 20)
	fmt.Println("ok6 result=", result)
}
/*输出：
ok3 res= 32
ok5 defer4...n2++ = 21
ok4 defer3...n1++ = 11
ok2 defer2...n2= 20   
ok1 defer1...n1= 10   
ok6 result= 32 
*/
```

**`defer`最主要的价值是在，当函数执行完毕后，可以及时的释放函数创建的资源。**

```go
func test1() {
	// 关闭文件资源
	file := openfile(文件名)
	defer file.Close()
	// 其它代码
}

func test2() {
	// 释放数据库资源
	connect := openDatabase()
	defer connect.Close()
	// 其它代码
}
```



## 函数参数传递方式

**两种传递方式：**

1. **值传递**：基本数据类型、数组和结构体。
2. **引用类型**：指针、slice切片、map、管道chan、interface等。



## 变量作用域

- 函数内部声明/定义的变量叫**局部变量**，作用域仅限于函数内部。

- 函数外部声明/定义的边拉拢叫**全局变量**，作用域在整个包都有效，如果其**首字母为大写**，则作用域在整个程序有效。

- 如果一个变量是在一个代码块中，比如`for`/`if`中，那么这个变量的作用域就在该代码块内。

- **赋值语句不能在函数体外，定义全局变量不能用`name:=值`**

	```go
	name := "tom"
	// 等价于
	var name string 
	name = "tom"
	```



# 字符串

## 字符串常用系统函数

1. 按字节统计字符串的长度函数`len(str)`：

	```go
	str := "hello"
	length := len(str)
	```

2. 字符串遍历，同时处理有中文的字符串，按字符处理`r:=[]rune(str)`：

	```go
	str := "hello,中国"
	r := []rune(str)
	for i := 0;i < len(str); i++ {
		fmt.Printf("index=%d, 字符=%c\n", i, r[i])
	}
	```

3. 字符串转整数函数 `strconv.Atoi(str)`：

	```go
	n, err := strconv.Atoi("hello")
	if err != nil{
	    fmt.Println("转换错误：",err)
	}else {
	    fmt.Println("转换结果：", n)
	}
	```

4. 整数转字符串函数 `strconv.Itoa(12345)`：

	```go
	str := strconv.Itoa(12345)
	fmt.Printf("str=%v, strType=%T", str, str)
	```

5. 字符串转`[]byte`：

	```go
	var bytes = []byte("Hello China")
	```

6. `[]byte`转字符串：

	```go
	str := string([]byte{91,92,93})
	//等价于 str := string([]byte{'a', 'b', 'c'})
	fmt.Printf("str =%v ", str)
	/*
	输出：str = abc
	*/
	```

7. 10进制转2、6、16进制函数 `strconv.FormatInt(十进制数, 进制类型)`：

	```go
	str := strconv.FormatInt(123, 2)
	fmt.Printf("十进制数 123 对应的二进制数为：%v", str)
	```

8. 查找子串是否在指定的字符串中，`strings.Contains(字符串,子串)`：

	```go
	b := strings.Contains("string", "str") // 返回bool值
	```

9. 统计一个字符串有几个指定的子串，`strings.Count(字符串,子串)`：

	```go
	num := strings.Count("abcadcesad", "a")
	```

10. 不区分大小写的字符串比较（`==`是区分字母大小写的），`strings.EqualFold(str1, str2)`

	```go
	b1 := strings.EqualFold("AbC", "aBc") // b1 = true
	b2 := "AbC"=="aBc"	// b2 = false
	```

11. 返回子串在字符串第一次出现的`index`值，如果没有返回`-1`：`strings.Index(字符串, 子串)`

	```go
	index := strings.Index("acdabcaed", "abc")	// index = 3
	```

12. 返回子串在字符串最后一次出现的`index`值，如果返回`-1`：`strings.LastIndex(字符串, 子串)`

	```go
	index := strings.LastIndex("abcdeabdes", "ab")	//index = 5
	```

13. 将指定的子串替换成另外一个子串：`strings.Replace(字符串, 原子串, 新子串, n)`，n可以指定期望替换多少个，如果`n = -1`表示全部替换。

	```go
	newStr := strings.Replace("abcdeabdes", "ab", "##", -1)	// newStr = "##cde##des"
	```

14. 按照指定的某个字符，为分割标识，将一个字符串拆分成**字符串数组**：`strings.Split(字符串, 分割标识)`

	```go
	strArr := strings.Split("hello,China,love", ",")	// strArr = [hell, China, love]
	```

15. 将字符串的字母进行大小写的转换：`strings.ToLower(字符串)`/`strings.ToUpper(字符串)`

	```go
	str := "HELLO, go"
	str1 := strings.ToLower(str)
	str2 := strings.ToUpper(str)
	fmt.Println("str1=", str1)
	fmt.Println("str2=", str2)
	/*输出：
	str1= hello, go
	str2= HELLO, GO
	*/
	```

16. 去除字符串左右字符：

	- 将字符串左右两边的空格去掉：`strings.TrimSpace(字符串)`

		```go
		newStr := strings.TrimSpace(" hello#  ") // newStr = "hello#"
		```

	- 将字符串左右两边指定的字符去掉：`strings.Trim(字符串, cutset)`，`cutset`为指定左右需要去掉的字符组合，顺序任意。

		```go
		newStr1 := strings.Trim("#!hello!#", "#!")	// 可去除字符 # 和 !
		newStr2 := strings.Trim("#!hello!#", "!#")	// 可去除字符 # 和 !
		newStr3 := strings.Trim("#!hello!#", "#")	// 无法去除字符 #
		newStr4 := strings.Trim("#!hello!#", "!")	// 无法去除字符 !
		```

	- 将字符串左边指定的字符去掉：`strings.TrimLeft(字符串, cutset)`，`cutset`为指定左侧需要去掉的字符组合，顺序任意。

		```go
		newStr1 := strings.TrimLeft("$@hello", "$@") // newStr1 = "hello"
		newStr2 := strings.TrimLeft("$@hello", "$")	//newStr2 = "@hello"
		newStr3 := strings.TrimLeft("$@hello", "@")
		//newStr2 = "$@hello" 去除字符失效
		```

	- 将字符串右边指定的字符去掉：`strings.TrimRight(字符串, cutset)`，`cutset`为指定右侧需要去掉的字符组合，顺序任意。

		```go
		newStr1 := strings.TrimRight("hello#!", "!#")	//newStr1 = "hello"
		newStr2 := strings.TrimRight("hello#!", "!")	//newStr2 = "hello#"
		newStr3 := strings.TrimRight("hello#!", "#")
		//newStr2 = "hello#!" 去除字符失效
		```

17. 判断字符串是否以指定的字符串开头：`strings.HasPrefix(字符串, 子串)`

	```go
	b := strings.HasPrefix("https://baidu.com", "https") //b=true
	```

18. 判断字符串是狗以指定的字符串结束：`strings.HasSuffix(字符串, 子串)`

	```go
	b := strings.HasSuffix("picture.jpg", "jpg") //b=true
	```



# 时间和日期

**`time.Time`用于表示时间类型**

## 获取当前时间：

```go
now := time.Now()
fmt.Printf("nowTime=%v , type=%T", now, now)
/*输出：
nowTime=2022-07-10 21:04:26.5471671 +0800 CST m=+0.003307801 , type=time.Time
*/
```

## 获取具体时间信息：

```go
// 通过now可以获取到年月日，时分秒
func main() {
	// 获取当前时间
	now := time.Now()
	fmt.Printf("nowTime=%v , type=%T\n", now, now)
	// 通过now可以获取到年月日，时分秒
	fmt.Printf("年=%v\n", now.Year())
	fmt.Printf("月=%v\n", now.Month())
	fmt.Printf("日=%v\n", now.Day())
	fmt.Printf("时=%v\n", now.Hour())
	fmt.Printf("分=%v\n", now.Minute())
	fmt.Printf("秒=%v\n", now.Second())
}
/*输出：
nowTime=2022-07-10 21:09:09.090123 +0800 CST m=+0.005980901 , type=time.Time
年=2022
月=July
日=10  
时=21  
分=9   
秒=9  
*/
```

## 格式化日期和时间：

**方式一：**

使用`Printf`或者`SPrintf`：

```go
func main() {
	// 获取当前时间
	now := time.Now()
	// 使用fmt.Printf()格式化日期和时间
	fmt.Printf("fmt.Printf() -当前年月日：%d-%02d-%02d %02d:%02d:%02d\n",
		now.Year(), now.Month(), now.Day(), now.Hour(), now.Minute(), now.Second())
    
	// 使用fmt.Sprintf()格式化日期和时间
	dateStr := fmt.Sprintf("fmt.Sprintf() -当前年月日：%d-%02d-%d %d:%d:%d\n",
		now.Year(), now.Month(), now.Day(), now.Hour(), now.Minute(), now.Second())
	fmt.Println(dateStr)
}
/*输出：
fmt.Printf() -当前年月日：2022-07-10 21:21:22
fmt.Sprintf() -当前年月日：2022-07-10 21:21:22
*/
```

**方式二：**

使用`time.Format(str)`方法：

`str`的参考时间已经定义好了，样式可以更改，但必须使用定义好的时间。

```go
Mon Jan 2 15:04:05 -0700 MST 2006
即：
2006-01-02 15:04:05
```



```go
func main() {
	// 获取当前时间
	now := time.Now()
	// 使用now.Format()格式化日期和时间
	fmt.Println(now.Format("2006-01-02 15:04:05"))
	fmt.Println(now.Format("2006/01/02"))
	fmt.Println(now.Format("15:04:05"))
    fmt.Println(now.Format("2006"))	//只取年
    fmt.Println(now.Format("01"))	//只取月
    fmt.Println(now.Format("02"))	//只取日
    fmt.Println(now.Format("15"))	//只取时
    fmt.Println(now.Format("04"))	//只取分
    fmt.Println(now.Format("05"))	//只取秒
}
/*输出：
2022-07-10 22:05:13
2022/07/10
22:05:13  
2022      
07        
10        
22        
05        
13 
*/
```



## 时间常量与休眠

### **时间常量：**

```go
const (
    Nanosecond  Duration = 1	//纳秒
    Microsecond          = 1000 * Nanosecond	//微妙
    Millisecond          = 1000 * Microsecond	//毫秒
    Second               = 1000 * Millisecond	//秒
    Minute               = 60 * Second	//分钟
    Hour                 = 60 * Minute	//小时
)
```

### **时间常量的作用：**

在程序中可用于获取指定时间单位的时间，例如想得到100毫秒：

```go
t := 100 * time.Millisecond
```

### **休眠`time.Sleep(t)`**

```go
// 每个1秒打印一个数字，打印到10就退出
i := 0
for {
	i++
	if i > 10 {
		break
	}
	fmt.Println(i)
	time.Sleep(1 * time.Second)
}

// 每隔0.1秒打印一个数字，打印到10就退出
i := 0
for {
	i++
	if i > 10 {
		break
	}
	fmt.Println(i)
	time.Sleep(100 * time.Millisecond)
}
```

### `time`的`Unix`和`UnixNano`方法

```go
func (t Time) Unix() int64
```

`Unix`将t表示为`Unix`时间，即从时间点`January 1, 1970 UTC`到时间点t所经过的时间（**单位秒**）。

```go
func (t Time) UnixNano() int64
```

`UnixNano`将`t`表示为Unix时间，即从时间点`January 1, 1970 UTC`到时间点t所经过的时间（**单位纳秒**）。如果纳秒为单位的`unix`时间超出了`int64`能表示的范围，结果是未定义的。注意这就意味着`Time`零值调用`UnixNano`方法的话，结果是未定义的。

```go
nowTime := time.Now()
// Unix时间（单位：秒）
fmt.Printf("Unix时间戳=%v\n", nowTime.Unix())
// UnixNano时间（单位：纳秒）
fmt.Printf("UnixNano时间戳=%v\n", nowTime.UnixNano())
/*输出：
Unix时间戳=1657463960
UnixNano时间戳=1657463960970240800
*/
```



## 计算耗时

使用`Unix`和`UnixNano`计算耗时：

```go
func main() {
	startUnix := time.Now().Unix()
	startUnixNano := time.Now().UnixNano()
	str := ""
	for i := 0; i < 100000; i++ {
		str += strconv.Itoa(i)
	}
	endUnix := time.Now().Unix()
	endUnixNano := time.Now().UnixNano()
	fmt.Printf("执行100000次字符串拼接耗费时间为 %v 秒\n", endUnix-startUnix)
	fmt.Printf("执行100000次字符串拼接耗费时间为 %v 纳秒\n", endUnixNano-startUnixNano)
}

/*输出：
执行100000次字符串拼接耗费时间为 2 秒
执行100000次字符串拼接耗费时间为 2637625700 纳秒
*/
```

使用`time.Now()`和`time.Since()`：

```go
func Since(t Time) Duration
//Since返回从t到现在经过的时间，等价于time.Now().Sub(t)。
```

```go
func main() {
	start := time.Now()

	str := ""
	for i := 0; i < 100000; i++ {
		str += strconv.Itoa(i)
	}
	cost := time.Since(start)
	end := time.Now()
	fmt.Printf("time.Since()：执行100000次字符串拼接耗费时间为 %v \n", cost)
	fmt.Printf("time.Now().Sub()：执行100000次字符串拼接耗费时间为 %v \n", end.Sub(start))
}
/*输出：
time.Since()：执行100000次字符串拼接耗费时间为 2.7780809s 
time.Now().Sub()：执行100000次字符串拼接耗费时间为 2.7780809s 
*/
```



# 内存分配（new和make）

## len

用来求`string`、`array`、`slice`、`map`、`channel`等的长度。

```go
n := len("hello")	// n = 5
```

## new

用来分配内存，主要用来分配值内存，比如`int`、`float64`、`struct`等，其第一个实参为类型，而非值。其**返回值为指向该类型的新分配的零值的指针**：`func new(Type) *Type`

```go
a := new(int)
fmt.Printf("a的类型%T\na的地址:%v\na所指向的值：%v\na所指向的值的地址：%v", a, &a, *a, &(*a))
/*输出：
a的类型*int
a的地址:0xc0000ce018
a所指向的值：0
a所指向的值的地址：0xc0000aa058
*/
```

## make

内建函数make分配并初始化一个类型为**切片、映射、通道**的对象。其第一个实参为类型，而非值。**make的返回类型与其参数相同，而非指向它的指针**。`func make(Type, size ...IntegerType) Type`

```
切片：size指定了其长度。该切片的容量等于其长度。切片支持第二个整数实参可用来指定不同的容量；
     它必须不小于其长度，因此 make([]int, 0, 10) 会分配一个长度为0，容量为10的切片。
映射：初始分配的创建取决于size，但产生的映射长度为0。size可以省略，这种情况下就会分配一个
     小的起始大小。
通道：通道的缓存根据指定的缓存容量初始化。若 size为零或被省略，该信道即为无缓存的。
```

**以切片为例：**

```go
var 切片名 []type = make([]type, len, cap)k
// type是数据类型，len是大小，cap是指定切片的容量，cap > len
```

```go
var slice []int = make([]int, 3, 5)
slice[0] = 1
slice[1] = 2
slice[2] = 3
fmt.Println("slice =", slice)
fmt.Println("slice len (切片长度/元素个数)=", len(slice))
fmt.Println("slice cap(切片容量) = ", cap(slice))
/*输出：
slice = [1 2 3]
slice len (切片长度/元素个数)= 3
slice cap(切片容量) =  5 
*/
```



# 错误处理

- Go语言不支持传统的`try...catch...fianlly`

- Go中引入的处理方式为：**`defer`、`panic`、`recover`**

- Go语言中可以抛出一个`panic`异常，然后再`defer`中通过`recover`捕获这个异常：

	```go
	func test() {
		// 使用defer + recover 来捕获和处理异常
		defer func() {
			err := recover() //recover()内置函数，可以捕获到异常
			if err != nil {  // 说明捕获到错误
				fmt.Println("err=", err)
			}
		}()
		num1 := 10
		num2 := 0
		res := num1 / num2
		fmt.Println("res=", res)
	}
	
	func main() {
		test()
		fmt.Println("test之后下面的代码...")
	}
	/*输出：
	err= runtime error: integer divide by zero
	test之后下面的代码...
	*/
	```



## 自定义错误

**Go语言中，使用`errors.New`和`panic`内置函数来自定义错误。**

- `errors.New("错误说明")`会返回一个`error`类型的值，表示一个错误。
- `panic`内置函数，接受一个`interface{}`类型的值（也就是任何值）作为参数，可以接受`error`类型的变量，输出错误信息，并退出程序。

```go
// 函数去读取配置文件init.conf的信息
// 如果文件名传入不正确，就返回一个自定义的错误
func readConf(fileName string) (err error) {
	if fileName == "config.ini" {
		//读取...
		return nil
	} else {
		// 返回一个自定义错误
		return errors.New("读取文件错误")
	}
}

func test() {
	err := readConf("config2.ini")
	if err != nil {
		// 如果读取文件发送给错误，就输出这个错误，并终止程序
		panic(err)
	}
	fmt.Println("test()继续执行...")
}

func main() {
	test()
	fmt.Println("test之后下面的代码...")
}
/*输出：
panic: 读取文件错误

goroutine 1 [running]:
main.test()
        D:/DevelopmentSoftWare/GoLand/GoLand_Workspace/demo/algorithm/hexadecima
lConversion.go:222 +0x49
main.main()
        D:/DevelopmentSoftWare/GoLand/GoLand_Workspace/demo/algorithm/hexadecima
lConversion.go:228 +0x19

Process finished with the exit code 2
*/
```



# 数组和切片

## 数组（值类型）

数组可以存放多个同一类型的数据。数组也是一种数据类型，在Go中，数组是**值类型**。

### **数组的定义：**

```go
var 数组名 [数组大小]数据类型

var a [3]int
// 赋值
a[0] = 1
a[1] = 2
a[2] = 3
```



- 数组的地址可以通过数组名类获取`&intArr`

	```go
	var a [3]int
	fmt.Printf("%p", &a)
	/*输出
	0xc00000e168
	*/
	```

- 数组的第一个元素的地址，就是数组的首地址：

	```go
	var a [3]int
		a[0] = 1
		a[1] = 2
		a[2] = 3
		fmt.Printf("数组地址（通过数组名获取）：%p\n", &a)
		fmt.Printf("数组的首地址(第一个元素的地址)：%p", &a[0])
	/*输出：
	数组地址（通过数组名获取）：0xc00000e168
	数组的首地址(第一个元素的地址)：0xc00000e168
	*/
	```

- 数组的各个元素的地址间隔大小是依据数组的类型决定的。比如`int64 -> 8` 、`int32 -> 4`



### 数组的初始化：

```go
// 方式一
var a1 [3]int = [3]int{1, 2, 3}
// 方式二
var a2 = [3]int{1, 2, 3}
// 方式三
var a3 = [...]int{1, 2, 3}
// 方式四
a4 := [...]string{1: "tom", 0: "jack", 2: "mary"}

fmt.Println("a1=", a1, "\na2=", a2, "\na3=", a3, "\na4=", a4)
/*输出:
a1= [1 2 3]
a2= [1 2 3]
a3= [1 2 3]
a4= [jack tom mary]
*/
```



### 数组的遍历

**传统方式：**

```go
var a1 [3]int = [3]int{1, 2, 3}
for i := 0; i < len(a1); i++ {
	fmt.Println(a1[i])
}
```

**for - range结构遍历：**

```go
var a1 [3]int = [3]int{1, 2, 3}
for index, value := range a1 {
    fmt.Println("index:", index, "value:", value)
}
```

- 第一个返回值`index`是数组的下标
- 第二个返回值`value`是在`index`下标位置的值
- `index`、`value`都是仅在`for`循环内部可见的局部变量
- 遍历数组元素的时候，如果不想使用下标`index`，可以直接把`index`改为下划线`_`
- `index`和`value`的名称不是固定的，可以自行设置名称



### 数组使用注意

1. 数组是多个相同类型数据的集合，一个数组一旦声明/定义了，其长度是固定的，不能动态变化。
2. `var arr []int`，这时候`arr`就是一个`slice`切片。
3. 数组中的元素可以是任何数据类型，包括值类型和引用该类型，但是不能混用。
4. 数组创建后，如果没有赋值，有默认值（零值）：
	- 数值类型数组：默认值为`0`
	- 字符串数组：默认值为 `""`
	- bool数组：默认值为 `false`
5. 使用数组的步骤：
	- 声明数组并开辟空间
	- 给数组各个元素赋值（默认零值）
	- 使用数组
6. 数组的下标是从`0`开始的。
7. 数组下标必须在指定范围内使用，否则报`panic：数组越界`。
8. Go的数组属于值类型，在默认情况下是值传递，因此传递会进行拷贝，数组间不会相互影响。
9. 如想在其它函数中去修改原来的数组，可以使用引用传递（指针方式）。
10. 长度是数组类型的一部分，在传递函数参数时，需要考虑数组的长度。



## 切片（引用类型）

- 切片的英文是`slice`。

- 切片是数组的一个引用，因此切片是引用类型，在进行传递时，遵守引用传递的机制。

- 切片的使用和数组类似，遍历切片、访问切片的元素和求切片的长度都一样。

- 切片的长度是可以变化的，因此切片是一个可以动态变化的数组。

- `slice`从底层来说，其实就是一个数据结构（`struct`结构体）

	```go
	type slice struct {
		ptr *[切片元素个数]int
		len int
		cap int
	}
	```

	

### 切片的定义与使用

**方式一：**

定义一个切片，然后让切片去引用一个已将创建好的数组：

```go
var arr [5]int = [5]int{1, 2, 3, 4, 5}
var slice = arr[1:4] // 取不到4，实际元素范围为1 - 3
fmt.Println("arr =", arr)
fmt.Println("slice =", slice)
fmt.Println("slice len (切片长度/元素个数)=", len(slice))
fmt.Println("slice cap(切片容量) = ", cap(slice))

/*输出：
arr = [1 2 3 4 5]
slice = [2 3 4]                 
slice len (切片长度/元素个数)= 3
slice cap(切片容量) =  4
*/
```

**方式二：**

通过`make`来创建切片

```go
var slice []int = make([]int, 3, 5)
slice[0] = 1
slice[1] = 2
slice[2] = 3
fmt.Println("slice =", slice)
fmt.Println("slice len (切片长度/元素个数)=", len(slice))
fmt.Println("slice cap(切片容量) = ", cap(slice))

/*输出：
slice = [1 2 3]
slice len (切片长度/元素个数)= 3
slice cap(切片容量) =  5 
*/

```

**方式三：**

定义一个切片，直接就指定具体数组

```go
var strSlice []string = []string{"tom", "jack","mary"}
fmt.Println("slice len (切片长度/元素个数)=", len(strSlice))
fmt.Println("slice cap(切片容量) = ", cap(strSlice))
/*输出：
strSlice len (切片长度/元素个数)= 3
strSlice cap(切片容量) =  3
*/
```



### 切片的遍历

与数组一样，有两种方式：

```go
var slice []string = []string{"tom", "jack", "mary"}
// 使用常规的forU型循环遍历切片
for i := 0; i < len(slice); i++ {
	fmt.Printf("index=%d, value=%v\n", i, slice[i])
}
// 使用for-range方式遍历切片
for index, value := range slice {
	fmt.Printf("index=%d, value=%v\n", index, value)
}
```



### 切片的使用注意

1. 切片初始化时`var slice = arr[startIndex : endIndex]`，从`arr`数组下标为`startIndex`起，取到下标为`endIndex - 1`。

2. 切片初始化时，仍然不能越界。范围在`0 : len(arr)`之间，但是可以动态增长：

	- `var slice = arr[0 : end]` 等价于 `var slice = arr[ : end]`
	- `var slice = arr[start : len(arr)]` 等价于 `var slice = arr[start : ]`
	- `var slice = arr[0 : len(arr)]` 等价于 `var slice = arr[ : ]`

3. `cap`是一个内置函数，用于统计切片的容量，即最大可以存放多少个元素。

4. 切片定义完后，还不能使用个，因为本身是一个空的，需要让其引用到一个数组，或者`make`一个空间供切片使用。

5. 切片可以继续切片：

	```go
	var slice1 []int = []int{1, 2, 3, 4, 5}
	slice2 := slice1[1:3]
	```

6. 用`append`内置函数，可以对切片进行动态追加：

	```go
	var slice []int = []int{1, 2, 3}
	slice = append(slice, 4, 5, 6)	// slice = [1, 2, 3, 4, 5, 6]
	```

	`append`底层原理：

	```
	切片append操作的本质就是对数组扩容
	go底层会创建一个新的数组newArr
	将slice原来包含的元素拷贝到新的数组newArr
	slice重新引用到newArr
	注意nnewArr是在底层来维护的，程序员不可见
	```

7. 切片的拷贝：`copy`

	```go
	var slice []int = []int{1, 2, 3}
	var newSlice = make([]int, 5)
	copy(newSlice, slice)
	fmt.Println("slice=", slice)
	fmt.Println("newSlice=", newSlice)
	
	/*输出
	slice= [1 2 3]
	newSlice= [1 2 3 0 0]
	*/
	```

8. 关于拷贝的注意：以下代码仍然可以运行

	```go
	var slice []int = []int{1, 2, 3}
	var newSlice = make([]int, 1)	//len(newSlice) = 1
	copy(newSlice, slice)
	fmt.Println("slice=", slice)
	fmt.Println("newSlice=", newSlice)
	/*输出
	slice= [1 2 3]
	newSlice= [1]
	*/
	```

9. 切片是引用类型，在传递时，遵守引用传递机制。



## 	string和切片

- `string`底层是一个`byte`数组，因此`string`也可以进行切片处理：

	```go
	str := "hello@chongqing.com"
	slice := str[0:5]
	fmt.Println("slice=", slice) // slice = "hello"
	```

- `string`是不可变的，也就是说不能通过`str[0] = value`方式来修改字符串

- 如果需要修改字符串，可以先将`string`转换为`[]byte`或`[]rune`，之后再修改，重新转成`string`

	```GO
	str := "hello@chongqing.com"
	arr1 := []byte(str)
	arr1[0] = 'z'
	str = string(arr1)
	fmt.Println("STR=", str)
	```

	转成`[]byte`后，可以处理英文和字母，但不能处理中文。原因是`[]type`按字节处理，而一个汉字是3个字节，因此就会出现乱码。

	```go
	str := "hello@chongqing.com"
	// arr := []byte(str) // 会报错
	arr1 := []rune(str)
	arr1[0] = '北'
	str = string(arr1)
	```

	

## 二维数组

### 二维数组的定义与使用

**方式一：先声明/定义，再赋值**

```go
var arr2 [2][2]int	// 声明/定义一个2 x 2的二维数组
// 给二维数组赋值
arr2[0][0] = 1
arr2[0][1] = 2
arr2[1][0] = 3
arr2[1][1] = 4
```

**方式二：直接初始化**

```go
// 方式一
var arr2 [2][2]int = [2][2]int{{1, 2}, {3, 4}}
// 方式二
var arr2 [2][2]int = [...][2]int{{1, 2}, {3, 4}}
// 方式三
var arr2 = [2][2]int{{1, 2}, {3, 4}}
// 方式四
var arr2 = [...][2]int{{1, 2}, {3, 4}}
```



### 二维数组的遍历

- 双层`for`循环遍历

	```go
	var arr2 [2][2]int = [2][2]int{{1, 2}, {3, 4}}
	for i := 0; i < len(arr2); i++ {
	    for j := 0; j < len(arr2[i]); j++ {
	        fmt.Printf("%v\t", arr2[i][j])
	    }
	    fmt.Println()
	}
	/*输出：
	1       2
	3       4
	*/
	```

- 双层`for-range`遍历

	```go
	var arr2 = [...][2]int{{1, 2}, {3, 4}}
	for _, value1 := range arr2 {
		for _, value2 := range value1 {
			fmt.Printf("%v\t", value2)
		}
		fmt.Println()
	}
	/*输出：
	1       2
	3       4
	*/
	```

	



# map（引用类型）



## map的声明

`map`是`key-value`数据结构，又称字段或者关联数组。

**基本语法**

```go
var 变量名 map[keyType]valueType
```

**key和value的类型**

- `golang`中的`map`的`key`和`value`可以是很多种类型，比如`bool`、数字、`string`、指针、`channel`，还可以是只包含前面几个类型的接口、结构体、数组。

- `key`通常为`int`、`string`，但**不能为`slice`、`map`、`function`，因为这几个无法用`==`来判断。**

- **`value`的类型没有`key`的类型的限制**

```go
// map的声明举例
var m map[string]string
var m map[string]int
var m map[int]string
var m map[string]map[string]string
```

**注意：声明是不会分配内存的，初始化需要`make`，分配内存后才能赋值和使用。**

```go
// 声明map
var m map[string]string
// 在使用map前，需要先make分配内存
m = make(map[string]string, 5)
m["m1"] = "孙悟空"
m["m2"] = "猪八戒"
m["m1"] = "齐天大圣"
m["m3"] = "沙僧"
fmt.Println(m)
/*输出：
map[m1:齐天大圣 m2:猪八戒 m3:沙僧]
*/
```

- `map`在使用前一定要`make`
- `map`的`key`是不能重复的，如果重复了，前面的就会被最后这个`key-value`覆盖
- `map`和`value`是可以相同的
- `map`的`key-value`是无序的



## map的使用

**方式一：**

```go
var m map[string]string
// 这种方式在使用map前，需要先make分配内存，之后可自动增长
m = make(map[string]string, 3)	// 初始分配的容量为 3，可自动增长
m["m1"] = "孙悟空"
m["m2"] = "猪八戒"
m["m1"] = "齐天大圣"
m["m3"] = "沙僧"
fmt.Println(m)
/*输出：
map[m1:齐天大圣 m2:猪八戒 m3:沙僧]
*/
```

**方式二：**

```go
cities := make(map[string]string)
cities["c1"] = "北京"
cities["c2"] = "重庆"
cities["c3"] = "四川"
fmt.Println(cities)
/*输出：
map[c1:北京 c2:重庆 c3:四川]
*/
```

**方式三：**

```go
colors := map[string]string{
    "color1": "red",
    "color2": "blue",
    "color3": "green",
}
colors["color4"] = "black"
fmt.Println(colors)
/*输出：
map[color1:red color2:blue color3:green color4:black]
*/
```



## map的增删改查

### map的增加和更新：

```go
mapName[key] = value	//如果key还没有，就新增，如果key已存在，就覆盖
```

### map删除：

```go
delete(mapName, key)	// delete是一个内置函数，如果key存在，就删除该key-value，如果key不存在就不操作，也不会报错
```

如果要删除`map`的所有`key-value`，可以遍历逐个删除，或者`mapName = make(...)`，`make`一个新的，让原来的称为垃圾，被`gc`回收。

### map查找：

```go
colors := map[string]string{
    "color1": "red",
    "color2": "blue",
    "color3": "green",
}
value, ok := colors["color3"]
if ok {
    fmt.Println("有color3 key，其value = ", value)
} else {
    fmt.Println("没有color3 key")
}
```



## map遍历

`map`的遍历使用`for-range`遍历：

```go
colors := map[string]string{
    "color1": "red",
    "color2": "blue",
    "color3": "green",
}
for key, value := range colors {
    fmt.Printf("key=%v, value=%v\n", key, value)
}
/*输出：
key=color1, value=red
key=color2, value=blue 
key=color3, value=green
*/
```

## map排序

`golang`中`map`的排序，是先将`key`进行排序，然后根据`key`值遍历输出：

```go
func main() {
	m := map[int]int{
		1:10,
		4:5,
		3:9,
		2:0,
	}
	fmt.Println(m)

	var keys []int
	for k, _ :=range m{
		keys = append(keys,k)
	}
	//排序
	sort.Ints(keys)
	fmt.Println(keys)

	for _,k :=range keys{
		fmt.Printf("key=%v,value=%v\n",k,m[k])
	}
}
/*输出：
map[1:10 2:0 3:9 4:5]
[1 2 3 4]
key=1,value=10
key=2,value=0
key=3,value=9
key=4,value=5
*/
```



## map使用细节

1. `map`是引用该类型，在一个函数接受`map`并修改后，会直接修改原来的`map`。
2. `map`的容量达到后，再增加`map`元素，会自动扩容，并不会发生`panic`，即`map`能够动态的增长。
3. `map`的`value`也经常使用`struct`类型，更适和管理复杂的数据（比`value`是一个`map`更好）。



# 面向对象编程

- Golang也支持面向对象编程（OOP），但是和传统的面向对象编程有区别，并不是纯粹的面向对象语言。而说Golang支持面向对象编程特性是比较准确的。
- Golang没有类（class），Go语言的结构体（struct）和其它编程语言的类（class）有同等地位，可以理解Golang是基于结构体来实现OOP特性的。
- Golang面向对象编程去掉了传统OOP语言的继承、方法重载、构造函数和析构函数、隐藏的`this`指针。
- Golang仍然有面向对象编程的继承、封装和多态的特性，只是实现的方法和其他OOP语言不一样，比如继承：Golang没有`extends`关键字，go的继承是通过匿名字段来实现的。

## 结构体（值类型）

### 结构体的声明

```go
type 结构体名称 struct {
	变量1 类型1
	变量2	类型2
	...
}
```

举例：

```go
type Student struct {
	Name string
	Age int
	Score float32
}
```

**结构体和结构体变量（实例）的区别和联系：**

- 结构体是自定义的数据类型，代表一类事物
- 结构体变量（实例）是具体的，实际的，代表一个具体变量



### **创建结构体变量**

```go
// 方式一
var person Person
// 方式二
var person Person = Person{}
// 方式三
var person *Person = new Person
// 方式四
var person *Person = &Person{}
```

- 方式三和方式四返回的是**结构体指针**。
- 结构体指针访问字段的标准方式应该是：`(*结构体指针).字段名`，比如`(*person).Name`。
- 但go也支持 `结构体指针.字段名`，比如 `person.Name`。go编译器底层将`person.Name`转化为`(*person).Name`。

### **给结构体中的变量赋值**

**普通类型结构体变量**

```go
type Student struct {
	Name string
	Age int
}
// 方式一
var stu1 Student
stu1.Name = "tom"
stu1.Age = 20
//方式二
var stu2 = Student{"tom", 20}
// 方式三
stu3 := Student{"tom",20}
// 方式四
var stu4 = Student{
	Name:"tom",
	Age:20,
}
// 方式五
stu5 := Student{
	Name:"tom",
	Age:20
}
```

**指针类型结构体变量**

```go
type Student struct {
	Name string
	Age int
}
// 方式一
var stu1 *Student
(*stu1).Name = "tom" //或 stu1.Name
(*stu1).Age = 20	//或 sut1.Age
//方式二
var stu2 = &Student{"tom", 20}
// 方式三
stu3 := &Student{"tom",20}
// 方式四
var stu4 = &Student{
	Name:"tom",
	Age:20,
}
// 方式五
stu5 := &Student{
	Name:"tom",
	Age:20
}
```



### 结构体使用注意

1. 字段声明语法同变量，示例：`字段名 字段类型`。

2. 字段的类型可以为：基本类型、数组、引用类型。

3. 在创建一个结构体变量后，如果没有给字段赋值，都对应一个零值（默认值）：`bool`类型是`false`、数值是`0`，字符串是`""`，数组类型的默认值与其元素类型相关，比如`score [3]int`的默认值为`[0, 0, 0]`，指针、切片和`map`的零值都是`nil`，即还没分配空间。

4. 不同结构体变量的字段是独立的，互不影响，一个结构体变量字段的更改，不影响另外一个，结构体是**值类型**。

5. 结构体的所有字段在内存中是**连续的**。

6. 结构体是用户单独定义的类型，和其它类型进行转换时需要有完全相同的字段（名字、个数和类型）：

	```go
	type A struct {
		Num int
	}
	type B struct {
		Num int
	}
	type C struct {
		num int
	}
	
	func main() {
		var a A
		var b B
		var c C
		a = A(b)	// 可以转换
		b = B(a)	// 可以转换
		c = C(a)	// 不能转换
	}
	```

7. 结构体进行`type`重新定义（相当于取别名），而Golang认为是新的数据类型，但可以进行强转：

	```go
	type integer int
	
	func main() {
		var i int = 20
		var j integer = 30
		j = i	// 不可以
		j = integer(i)	// 可以
		i = int(j)	//可以
	}
	```

8. `struct`的每一个字段上，都可以写上一个`tag`，该`tag`可以通过反射机制获取，常见的使用场景就是**序列化**和**反序列化**：

	```go
	type Student struct {
		Name string `json:"name"`	// `json:"name"` 就是struct tag
		Age int `json:"age"`
		height float32 `json:"height"`
	}
	
	func main() {
		// 创建一个 Student 变量
		stu := Student{"孙悟空", 500, 170.0}
	
		// 将stu变量序列化为json格式字串
		// json.Marshal 函数中使用反射
		jsonStu, err := json.Marshal(stu)
		if err!=nil{
			fmt.Println("json 处理错误：",err)
		}
		fmt.Println("jsonStu：",string(jsonStu))
	}
	/*输出：
	jsonStu： {"name":"孙悟空","age":500}
	*/
	```

	



## 方法

golang中的方法是**作用在指定的数据类型上的**（即：和指定的数据类型绑定），因此**自定义类型都可以有方法**，而不仅仅是`struct`。

### 方法的声明和调用

```go
func (recevier type) methodName (参数列表) (返回值列表) {
	方法体
	return 返回值
}
// 或者
func (recevier *type) methodName (参数列表) (返回值列表) {
	方法体
	return 返回值
}
```

- 参数列表：表示方法输入。
- `recevier type`：表示这个方法和`type`这个类型进行绑定，或者说该方法作用于`type`类型。
- `recevier type`：`type`可以是结构体，也可以是其它的自定义类型。
- `recevier`：就是`type`类型的一个变量（实例）。
- 返回值列表：表示返回的值，可以返回多个值。
- 方法主体：表示为了实现某一功能代码块。
- `return`语句不是必须的。

```go
func (s Student)learning(){
	fmt.Printf("name=%v, age=%v, learning()...\n",s.Name,s.Age)
}

func (s *Student)totalScore(chinese float64, math float64,english float64)string{
	return fmt.Sprintf("name=%v, age=%v, totalScore=%v",(*s).Name,(*s).Age, chinese+math+english)
	//return fmt.Sprintf("name=%v, age=%v, totalScore=%v",s.Name,s.Age, chinese+math+english)
}

func main() {
	var s = Student{"孙悟空",500}
	s.learning() //调用方法
	fmt.Println(s.totalScore(90,92,90))
	var ptr_s *Student= &Student{"猪八戒", 600}
	(*ptr_s).learning()
	(ptr_s).learning()
	fmt.Println(ptr_s.totalScore(90,80,85))
	fmt.Println((*ptr_s).totalScore(90,80,85))
}
/*输出：
name=孙悟空, age=500, learning()...
name=孙悟空, age=500, totalScore=272
name=猪八戒, age=600, learning()...
name=猪八戒, age=600, learning()...
name=猪八戒, age=600, totalScore=255
name=猪八戒, age=600, totalScore=255
*/
```

- `func (s Student) learning(){}`表示`Studetn`结构体有一方法，方法名为`learning`，`s`表示哪个`Student`变量调用，这个`p`就是它的副本。
- `(s Student)`体现`learning`方法是和`Student`类型绑定的。
- `learning`方法只能通过`Student`类型的变量来调用，而不能直接调用，也不能使用其它类型变量来调用。

### 方法使用注意

1. 结构体类型是值类型，在方法调用中，遵守值类型的传递机制，是值拷贝传递方式。

2. 如果想在方法中修改结构体变量的值，可以通过结构体指针的方式来处理：

	```go
	type Student struct {
		Name string
		Age int
	}
	
	func (s Student)changeValue(){
		s.Name = "猪八戒"
		s.Age = 600
	}
	
	func (s *Student)changeValueByPointer(){
		s.Name = "吴承恩"
		s.Age = 40
	}
	
	func main() {
		var s = Student{"孙悟空",500}
		fmt.Println("s :",s)
		s.changeValue()
		fmt.Println("(s Student)changeValue:",s)
		s.changeValueByPointer()
		fmt.Println("(s *Student)changeValueByPointer:",s)
	}
	/*输出：
	s : {孙悟空 500}
	(s Student)changeValue: {孙悟空 500}
	(s *Student)changeValueByPointer: {吴承恩 40}
	*/
	```

3. Golang中的方法作用在指定的数据类型上的（即：和指定的数据类型绑定），因此自定义类型都可以有方法，而不仅仅是`struct`：

	```go
	type integer int
	
	func (i integer)test(){
		fmt.Println(i)
	}
	
	func main() {
		var i integer = 20
		i.test()
	}
	```

4. 方法的访问范围空值的规则和函数一样。方法名首字母小写，只能在本包访问，方法首字母大写，可以在本包和其它包访问。

5. 如果一个类型实现了`String()`这个方法，那么`fmt.Println`默认会调用这个变量的`String()`进行输出：

	```go
	type Student struct {
		Name string
		Age int
	}
	
	func (s Student)String()string{
		str := fmt.Sprintf("姓名=%v，年龄=%v",s.Name,s.Age)
		return str
	}
	
	func main() {
		var s = Student{"孙悟空",500}
		fmt.Println(s)
	}
	/*输出:
	姓名=孙悟空，年龄=500
	*/
	```

	

### 方法和函数的区别

1. 调用方式不同：
	- 函数：`函数名(实参列表)`
	- 方法：`变量.方法名(实参列表)`
2. 对于普通函数，接受者为值类型时，不能将指针类型的数据直接传递；而对于方法，接受者为值类型时，可以直接用指针类型的变量调用方法，接受者为引用类型时，同样可以直接用值类型的变量调用方法。



## 面向对象编程特性-封装

封装（encapsulation）就是把抽象出来的字段和对字段的操作封装在一起，数据被保护在内容部，程序的其他包只有通过被授权的操作（方法）才能对字段进行操作。封装的好处：

- 隐藏实现细节
- 可以对数据进行验证，保证安全合理

### **go语言封装的实现步骤**

1. 将结构体、字段（属性）的首字母小写（不能导出了，其它包不能使用，类似`private`）

2. 给结构体所在包提供一个工厂模式的函数，首字母大写，类似一个构造函数。

3. 提供一个首字母大写的`Set`方法（类似于其它语言的`public`），用于对属性判断并赋值：

	```go
	func  (e 接头体类型名)SetXxx(参数列表)(返回值列表){
		//加入数据验证的业务逻辑
		e.字段 = 参数
	}
	```

4. 提供一个首字母大写的`Get`方法（类似于其它语言的`public`，用于获取属性的值：

	```go
	func (e 结构体类型名)GetXxx(){
		rerturn e.字段
	}
	```

注意：在Golang开发中并没有特别强调封装，不用总是用面向对象编程语言的语法特向来看待Golang，Golang本身对面向对象的特性做了简化。



### 应用例子

```
写一个程序（person.go），不能随便查看人的年龄、工资等隐私，并对输入的年龄进行合理的验证。
设计：model包 - person.go
	main包 - main.go （调用Person结构体）
```

```go
// ./model/person.go
package model

import "fmt"

type person struct {
	Name string
	age int	//其它包不能直接访问
	salary float64 //其它包不能直接访问
}

// NewPerson 写一个工厂模式的函数，相当于构造函数
func NewPerson(name string) *person {
	return &person{
		Name:name,
	}
}

// 为了访问 age 和 salary ，编写一对 SetXxx方法和 GetXxx 方法
func (p *person) SetAge(age int){
	if age > 0 && age < 150{
		p.age = age
	}else{
		fmt.Println("年龄范围不正确...")
		p.age = 30	//提供默认值
	}
}

func (p *person)GetAge()int{
	return p.age
}

func (p *person)SetSalary(salary float64){
	if salary >= 3000 && salary <=30000{
		p.salary = salary
	}else {
		fmt.Printf("薪水范围不正确...")
		p.salary = 8000	//提供默认值
	}
}

func(p *person)GetSalary()float64{
	return p.salary
}
```

```go
// ./main.go
package main

import (
	"demo/model"
	"fmt"
)

func main() {
	p := model.NewPerson("zhongxi")
	p.SetAge(18)
	p.SetSalary(5000)
	fmt.Println(p)
	fmt.Printf("Name:%v,age=%v,salary=%v",p.Name,p.GetAge(),p.GetSalary())
}

/*输出：
&{zhongxi 18 5000}
Name:zhongxi,age=18,salary=5000
*/
```



## 面向对象编程特性-继承

在Golang中，如果一个`struct`嵌套了另一个**匿名结构体**，那么这个结构体可以直接访问匿名结构体的字段和方法，从而实现了继承特性。

### 嵌套匿名结构体的基本语法

```go
type Goods struct {
    Name string
    Price int
}

type Book struct {
    Goods //嵌套匿名结构体 Goods
    Writer string
}
```

### 应用例子

```go
package main

import (
	"fmt"
)

type Student struct {
	Name string
	Age int
	Score int
}

// 将 Pupil 和 Graduate 共有的方法也绑定到 *Student
func (stu *Student)ShowInfo(){
	fmt.Printf("学生名字：%v， 年龄：%v， 成绩：%v",stu.Name,stu.Age,stu.Score)
}

func (stu *Student)SetScore(score int){
	stu.Score = score
}

// 小学生
type Pupil struct {
	Student // 嵌入了 Student 匿名结构体
}

 func (p *Pupil)testing(){
	 // Pupil 结构体特有的方法
	 fmt.Println("小学生正在考试中...")
 }

func main() {
	pupil := &Pupil{}
	pupil.Student.Name = "tom"
	pupil.Student.Age = 10
	pupil.Student.SetScore(90)
	pupil.testing()
	pupil.Student.ShowInfo()
}
/*输出：
小学生正在考试中...
学生名字：tom， 年龄：10， 成绩：90
*/
```

- 继承提高了代码的复用性
- 继承提高了代码的扩展性和维护性

### 其他特点

1. 结构体可以使用嵌套匿名结构体所有的字段和方法，即：无论首字母大写或者小写的字段、方法都可以使用。

2. 匿名结构体字段访问可以简化。

	```
	type A struct {
		Name string
		age int
	}
	
	func (a *A) f1() {
	    fmt.Println("A f1")
	}
	
	func (a *A) F1() {
	    fmt.Println("A F1")
	}
	
	type B struct {
	    A
	}
	
	func main(){
		var b1,b2 B
		b1.A.Name = "tom"
		b1.A.age = 19
		b2.Name = "jack"
		b2.age = 20
		b1.A.f1()
		b1.A.F1()
		b2.f1()
		b2.F1()
	}
	```

	当直接通过`b1、b2`访问字段或方法时，编译器会先看`b1、b2`对应的类型有没有`Name`，如果有，则直接调用`B`类型的`Name`字段；如果没有就去看`B`中嵌入的匿名结构体`A`有没有声明`Name`字段，如果有就调用，如果没有就继续查找，找不到就报错。

3. 当**结构体**和**匿名结构体**有相同的字段或者方法时，编译器采用就近访问原则访问，如果希望访问匿名结构体的字段和方法，可以通过匿名结构体名来区分。

4. 结构体嵌入两个（或多个）匿名结构体，如两个匿名结构体有相同的字段和方法（同时结构体本身没有同名的字段和方法），在访问时，就必须明确指定匿名结构体名字，否则编译报错。

	```GO
	type A struct {
		Name string
		age int
	}
	
	type B struct {
		Name string
		Score float64
	}
	
	type C struct {
		A
		B
	}
	
	func main(){
		var c C
		c.A.Name = "tom"
		c.B.Name = "JACK"
		fmt.Println("c:",c)
	}
	/*输出：
	c: {{tom 0} {JACK 0}}
	*/
	```

5. 如果一个`struct`嵌套了一个有名结构体，这种模式就是**组合**，此时在访问组合的机构体的字段或方法时，必须带上结构体的名字。

	```go
	type A struct {
		Name string
		age int
	}
	
	type B struct {
		Name string
		Score float64
	}
	
	type C struct {
	    // 组合的结构体
		a A
		b B
	}
	
	func main(){
		var c C
	    // 访问组合的结构体的字段或方法必须带上结构体的名字
		c.a.Name = "tom"
		c.b.Name = "JACK"
		fmt.Println("c:",c)
	}
	```

6. 嵌套匿名结构体后，也可以在创建结构体变量（实例）时，直接指定各个匿名结构体字段的值：

	```go
	type A struct {
		Name string
		age int
	}
	
	type B struct {
		Name string
		Score float64
	}
	
	type C1 struct {
		A
		B
	}
	
	type C2 struct {
		*A
		*B
	}
	
	func main(){
		c1 := C1{
			A{"Tom", 90},
			B{"Jack", 85},
		}
		c2 := C2{
			&A{"Michael",95},
			&B{"Elizabeth",100},
		}
		fmt.Println("c1-A: ",c1.A,"c1-B: ",c1.B)
		fmt.Println("c2-*A",*(c2.A),"c2-*B",*(c2.B))
	}
	/*输出：
	c1-A:  {Tom 90} c1-B:  {Jack 85}
	c2-*A {Michael 95} c2-*B {Elizabeth 100}
	*/
	```

7. 如果一个结构体有多个同类型的匿名字段，必须给定名字：

	```GO
	type A struct {
		int
		int	
	}	// 错误，多个同类型的匿名字段必须给定名字
	
	type C1 struct {
		A int
		B int	
	}
	```



## 面向对象编程特性-多重继承

如果一个`struct`嵌套了多个匿名结构体，那么该结构体可以直接访问嵌套的匿名结构体的字段和方法，从而实现**多重继承**。

**应用例子**

```GO
type A struct {
	Name string
	age int
}

type B struct {
	Name string
	Score float64
}

type C1 struct {
	A
	B
}
```

**使用细节说明**

- 如果嵌入的匿名结构体有相同的字段名或者方法名，则在访问时需要通过匿名结构体类型名来区分。

	```go
	// c1 := C1{...}
	fmt.Println(c1.A.Name)
	fmt.Println(c1.B.name)
	```

- 为了保证代码的简洁性，尽量不使用多重继承。



## 接口（引用类型）



- 在Golang中，**多态**的特性主要是通过**接口**来体现的。
- **实现接口 <==>实现接口声明的所有方法**。
- `interface`类型可以定义一组方法，但是这些方法不需要实现，**并且`interface`不能包含任何变量**。到某个自定义类型（比如结构体）要使用的时候，再根据具体情况把这些方法的进行实现。
- **接口里的所有方法都没有方法体**，即接口的方法都是没有实现的方法。接口体现了程序设计的**多态**和**高内聚低耦合**的思想。
- Golang中的接口，不需要显式地实现。只要一个变量（实例）含有接口类型中的所有方法，那么这个变量就实现了这个接口，因此Golang中没有`implement`这样的关键字。
- 如果有两个不同名字（`A`和`B`）的接口，`A`中**只含有**方法`f1`和`f2`，`B`中**也含有**方法`f1`和`f2`，那么实现了接口`B`，也就同样实现了接口`A`。



### 基本语法

```go
type 接口名 interface {
    方法名1(参数列表)返回值列表
    方法名2(参数列表)返回值列表
}

// 实现接口中的所有方法
func (v 自定义类型)方法名1(参数列表)返回值列表 {
    // 方法实现
}
func (v 自定义类型)方法名2(参数列表)返回值列表 {
    // 方法实现
}
```

### 接口使用注意

- 接口本身不能创建实例，但是可以**指向一个实现了改接口的自定义类型的变量（实例）**

	```go
	type A interface {
		SayHello()
	}
	
	type Stu struct {
		Name string
	}
	
	func (stu Stu)SayHello(){
		fmt.Println("hello,",stu.Name)
	}
	
	func main(){
		var stu = Stu{"Tom"}	// 结构体变量，实现了 SayHello() ，实现了 接口 A
		var a A = stu
		a.SayHello()
	}
	```

- 接口中所有的方法都没有方法体，即都是没有实现的方法。

- 在Golang中，一个自定义类型需要将某个接口的所有方法都实现，即可以是这个自定义类型实现了接口。

- 一个自定义类型只有实现了某个接口，才能将该自定义类型的实例（变量）赋给接口类型。

- 只要是自定义数据类型，就可以实现接口，不仅仅是结构体类型。

- **一个自定义类型可以实现多个接口：**

	```go
	type A interface {
		SayHello()
	}
	
	type B interface {
		SayGoodbye()
	}
	
	type Stu struct {
		Name string
	}
	
	func (stu Stu)SayHello(){
		fmt.Println("hello,",stu.Name)
	}
	
	func (stu Stu)SayGoodbye() {
		fmt.Println("goodbye", stu.Name)
	}
	
	func main(){
		var stu = Stu{"Tom"}	// 结构体变量，实现了 SayHello() ，实现了 接口 A
		var a A = stu
		var b B = stu
		a.SayHello()
		b.SayGoodbye()
		stu.SayHello()
		stu.SayGoodbye()
	}
	```

- **Golang接口中不能有任何变量。**

- 一个接口（比如A接口）可以继承多个别的接口（比如B，C接口），这时候如果要实现A接口，也必须将B，C接口的方法也全部实现。

	```GO
	type A interface {
		SayHello()
	}
	
	type B interface {
		SayGoodbye()
	}
	
	type C interface {
		A
		B
		SayNice()
	}
	
	type Stu struct {
		Name string
	}
	
	func (stu Stu)SayHello(){
		fmt.Println("hello,",stu.Name)
	}
	
	func (stu Stu)SayGoodbye() {
		fmt.Println("goodbye", stu.Name)
	}
	
	func (stu Stu)SayNice(){
		fmt.Println("nice,",stu.Name)
	}
	
	func main(){
		var stu = Stu{"Tom"}	// 结构体变量，实现了 SayHello() ，实现了 接口 A
		var c C = stu
		c.SayHello()
		c.SayGoodbye()
		c.SayNice()
	}
	```

- `interface`类型默认是一个指针（引用类型），如果没有对`interface`初始化就使用，那么就会输出`nil`。

- 空接口`interface{}`没有任何方法，所以所有类型都实现了空接口，即我们**可以把任何一个变量赋给空接口**。

	```go
	type T interface {
		// 空接口
	}
	
	// 使用
	var t T = stu
	var t2 interface{} = stu
	var num1 int = 5
	t = num1
	t2 = num1
	```



### 接口和继承的区别

1. 继承的价值主要在于解决代码的**复用性**和**可维护性**；接口的价值主要在于**设计好各种规范（方法）**，让其它自定义类型去实现这些方法。
2. 接口比继承更加灵活。继承是满足`is - a`的关系，而接口只需满足`like - a`的关系。
3. 接口在一定程度上实现代码的解耦。



## 面向对象编程-多态

在Golang中，**多态特征是通过接口实现的**。按照统一的接口来调用不同的实现，这时接口变量就呈现不同的形态。

**接口体现多态的两种形式：**

- **多态参数：**

	```go
	type Usb interface {
		Start()
		Stop()
	}
	
	type Phone struct {
		Name string
	}
	
	type Camera struct {
		Name string
	}
	
	type Computer struct {
		Name string
	}
	
	func (p Phone)Start(){
		fmt.Printf("phone-%v start...\n", p.Name)
	}
	
	func (p Phone)Stop() {
		fmt.Printf("phone-%v stop...\n",p.Name)
	}
	
	func (c Camera)Start(){
		fmt.Printf("camera-%v start...\n", c.Name)
	}
	
	func (c Camera)Stop() {
		fmt.Printf("camera-%v stop...\n",c.Name)
	}
	
	func (cp Computer)Working(usb Usb){
		fmt.Printf("computer-%v is working...\n",cp.Name)
		usb.Start()
		usb.Stop()
	}
	
	func main(){
		var u1 Usb = Phone{"p1"}
		var u2 Usb = Camera{"c1"}
		var cp = Computer{"cp1"}
		cp.Working(u1)
		cp.Working(u2)
	}
	/*输出：
	computer-cp1 is working...
	phone-p1 start...
	phone-p1 start...
	computer-cp1 is working...
	camera-c1 start...
	camera-c1 start...
	*/
	```

- **多态数组：**

	```go
	// 接着前面的例子...
	
	func main() {
		// 定义一个 Usb 接口数组，可以存放 Phone 和 Camera 的结构体变量
		// 这里体现 多态数组
		var usbArr [3]Usb
		usbArr[0] = Phone{"三星"}
		usbArr[1] = Phone{"苹果"}
		usbArr[2] = Camera{"尼康"}
		usbArr[0].Start()
	}
	/*输出：
	phone-三星 start...
	camera-尼康 stop...
	*/
	```

	

# 类型断言

## 基本用法

由于接口是一般类型，不知道具体类型，如果要转成具体类型，就需要使用类型断言。

```go
type Point struct{
	x int
	y int
}

func main() {
	var a interface{}	// 空接口
	var point Point = Point{1,2}
	a = point	// ok
	var b Point
	//b = a	//error: cannot use a (variable of type interface{}) as type Point in assignment: need type assertion
	b = a.(Point)	// 类型断言
	fmt.Println(b)
}
```

`b = a.(Point)`就是类型断言，表示判断`a`是否指向`Point`类型的变量，如果是就转成`Point`类型并赋值给`b`变量，否则报错。

在进行类型断言时，如果类型不匹配，就会报`panic`，因此进行类型断言时，要确保原来的空接口指向的就是断言类型。可以带上检测机制，跳过报`panic`。

```go
// ....
if b, ok := a.(Point); ok {
    fmt.Println("convert success")
    fmt.Printf("b 的类型是 %T ，值是 %v", b, b)
}else {
    fmt.Println("convert fail")
}
```

## 实例1

给`Phone`结构体增加一个特有的方法`call()`，当`Usb`接收的是`Phone`变量时，还需要调用`call()`：

```go
package main

import "fmt"

type Usb interface {
	Start()
	Stop()
}

type Phone struct {
	Name string
}

type Camera struct {
	Name string
}

type Computer struct {
	Name string
}

func (p Phone)Start(){
	fmt.Printf("phone-%v start...\n", p.Name)
}

func (p Phone)Stop() {
	fmt.Printf("phone-%v stop...\n",p.Name)
}

func (p Phone)Call() {
	fmt.Printf("phone-%v is calling...\n",p.Name)
}
func (c Camera)Start(){
	fmt.Printf("camera-%v start...\n", c.Name)
}

func (c Camera)Stop() {
	fmt.Printf("camera-%v stop...\n",c.Name)
}

func (cp Computer)Working(usb Usb){
	fmt.Printf("computer-%v is working...\n",cp.Name)
	usb.Start()
	// 如果 usb 指向Phone 结构体变量，则还需要调用 Call 方法
	// 类型断言
	if phone, ok := usb.(Phone); ok{
		phone.Call()
	}
	usb.Stop()
}

func main(){
	var u1 Usb = Phone{"p1"}
	var u2 Usb = Camera{"c1"}
	var cp = Computer{"cp1"}
	cp.Working(u1)
	cp.Working(u2)
}
/*输出：
computer-cp1 is working...
phone-p1 start...
phone-p1 is calling...
phone-p1 stop...
computer-cp1 is working...
camera-c1 start...
camera-c1 stop...
*/
```



## 实例2

编写一个函数，可以判断输入的参数是什么类型：

```go
type A struct {
	Name string
}

func TypeJudge(items... interface{}){
	for index , item := range items{
		switch item.(type) {
		case bool:
			fmt.Printf("第%v个参数是 bool 类型，值是%v\n",index,item)
		case float32:
			fmt.Printf("第%v个参数是 float32 类型，值是%v\n",index,item)
		case float64:
			fmt.Printf("第%v个参数是 float64 类型，值是%v\n",index,item)
		case int,int8,int16,int32,int64:
			fmt.Printf("第%v个参数是 整数 类型，值是%v\n",index,item)
		case string:
			fmt.Printf("第%v个参数是 string 类型，值是%v\n",index,item)
		case A:
			fmt.Printf("第%v个参数是 A结构体 类型，值是%v\n",index,item)
		case *A:
			fmt.Printf("第%v个参数是 *A结构体指针 类型，值是%v\n",index,item)
		default:
			fmt.Printf("第%v个类型不确定，值是%v\n",index,item)
		}
	}
}

func main(){
	var a0 interface{} = true
	var a1 interface{} = 5
	var a2 interface{} = 5.5
	var a3 interface{} = "str"
	var a4 interface{} = A{"tom"}
	var a5 interface{} = &A{"jack"}
	TypeJudge(a0, a1, a2,a3,a4,a5)
}
/*输出：
第0个参数是 bool 类型，值是true
第1个参数是 整数 类型，值是5
第2个参数是 float64 类型，值是5.5
第3个参数是 string 类型，值是str
第4个参数是 A结构体 类型，值是{tom}
第5个参数是 *A结构体指针 类型，值是&{jack}
*/
```



# 文件操作

## 文件的基本介绍

1. **文件的概念：**文件是数据源（保存数据的地方）的一种，比如word文档、txt文件、excel文件等。文件最主要的作用就是保存数据，既可以保存文本、图片，也可以保存视频、声音等。
2. **输入流和输出流：**
	- **流：**数据在数据源（文件）和程序（内存）之间经历的路径。
	- **输入流：**数据从数据源（文件）到程序（内存）的路径。
	- **输出流：**数据从程序（内存）到数据源（文件）的路径。
3. `os.File`封装所有文件相关操作，`File`是一个结构体。[Go语言标准库文档中文版 | Go语言中文网 | Golang中文社区 | Golang中国 (studygolang.com)](https://studygolang.com/pkgdoc)



## 打开和关闭文件

```go
func Open(name string) (file *File, err error)
Open打开一个文件用于读取。如果操作成功，返回的文件对象的方法可用于读取数据；对应的文件描述符具有O_RDONLY模式。如果出错，错误底层类型是*PathError。

func (f *File) Close() error
Close关闭文件f，使文件不能用于读写。它返回可能出现的错误
```



```go
import (
	"fmt"
	"os"
)

func main() {
	// 打开文件
    // file的叫法：file对象、file指针、file文件句柄
	file, err := os.Open("C:\\Users\\16688\\Desktop\\file.txt")
	if err != nil {
		fmt.Println("open file err=", err)
	}
	// 输出file 就是一个指针 *File
	fmt.Printf("file=%v", file)	// file=&{0xc0000d0780}
	// 关闭文件
	err = file.Close()
	if err != nil {
		fmt.Println("close file err=", err)
	}
}
```



## 读取文件

1. 读取文件的内容并显示在终端（带缓冲区的方式），使用`os.Open, file.Close, bufio.NewReader()`。

	```go
	func NewReader(rd io.Reader) *Reader
	NewReader创建一个具有默认大小(4096)缓冲、从r读取的*Reader。
	```

	```
	// C:\\Users\\16688\\Desktop\\file.txt
	
	第一行：I love 中国
	第二行：I love 重庆
	第三行：I love 开州
	
	```

	```go
	import (
		"fmt"
		"os"
	)
	
	func main() {
		// 打开文件
		file, err1 := os.Open("C:\\Users\\16688\\Desktop\\file.txt")
		if err1 != nil {
			fmt.Println("open file err=", err1)
		}
		// 当函数退出时，要及时的关闭 file
		defer file.Close() // 及时关闭 file 句柄，否则会有内存泄露
	
		// 创建一个 *Reader ，带缓冲的，默认缓冲区为4096
		reader := bufio.NewReader(file)
	
		// 循环读取文件的内容
		for {
			str, err2 := reader.ReadString('\n') //读到一个换行就结束
			if err2 == io.EOF {                  // io.EOF 表示文件的末尾
				break
			}
			fmt.Print(str) //输出内容
		}
		fmt.Println("文件读取结束...")
	}
	/*输出：
	第一行：I love 中国
	第二行：I love 重庆
	第三行：I love 开州
	文件读取结束...
	*/
	```

	1. 读取文件的内容并显示在终端（使用`ioutil`一次将整个文件读入到内存中），这种方式**适用于文件不大的情况**。**使用`ioutil.ReadFile()`不需要显示地关闭文件，因为文件的`Open`和`Close`已经被封装到`ReadFile`函数内部。**

	```go
	func ReadFile(filename string) ([]byte, error)
	ReadFile 从filename指定的文件中读取数据并返回文件的内容。成功的调用返回的err为nil而非EOF。因为本函数定义为读取整个文件，它不会将读取返回的EOF视为应报告的错误。
	```

	```
	// C:\\Users\\16688\\Desktop\\file.txt
	
	第一行：I love 中国
	第二行：I love 重庆
	第三行：I love 开州
	
	```

	```go
	import (
		"fmt"
		"io/ioutil"
	)
	
	func main() {
		// 使用 ioutil.ReadFile 一次性将文件内容读取到位
		fileName := "C:\\Users\\16688\\Desktop\\file.txt"
		content, err := ioutil.ReadFile(fileName)
		if err != nil {
			fmt.Printf("read file err=%v", err)
		}
		fmt.Println(string(content)) // []byte需要转换为 string 才能正常显示原文件内容
		fmt.Println("文件读取结束...")
	}
	```



## 写入文件

### os.OpenFile函数

```go
func OpenFile(name string, flag int, perm FileMode) (file *File, err error)
/* 
OpenFile是一个更一般性的文件打开函数，大多数调用者都应用Open或Create代替本函数。它会使用指定的选项（如O_RDONLY等）、指定的模式（如0666等）打开指定名称的文件。如果操作成功，返回的文件对象可用于I/O。如果出错，错误底层类型是*PathError。
*/

// flat 参数：文件打开模式（可以组合）
const (
    O_RDONLY int = syscall.O_RDONLY // 只读模式打开文件
    O_WRONLY int = syscall.O_WRONLY // 只写模式打开文件
    O_RDWR   int = syscall.O_RDWR   // 读写模式打开文件
    O_APPEND int = syscall.O_APPEND // 写操作时将数据附加到文件尾部
    O_CREATE int = syscall.O_CREAT  // 如果不存在将创建一个新文件
    O_EXCL   int = syscall.O_EXCL   // 和O_CREATE配合使用，文件必须不存在
    O_SYNC   int = syscall.O_SYNC   // 打开文件用于同步I/O
    O_TRUNC  int = syscall.O_TRUNC  // 如果可能，打开时清空文件
)

// perm 参数：权限控制
0777: 创建了一个普通文件，所有人拥有所有的读、写、执行权限
0666：创建了一个普通文件，所有人拥有对该文件的读、写，但都不可执行
0644：创建了一个普通该文件，文件所有者对该文件有读写权限，用户组合其他人只有读权限。都没有执行权限

// demo
file, err := os.OpenFile(filePath, os.O_WRONLY|os.O_CREATE, 0666)
if err != nil {
    fmt.Printf("open file err=%v", err)
}
defer file.Close()
```

**方式一：**

```go
func NewWriter(w io.Writer) *Writer
// NewWriter创建一个具有默认大小缓冲、写入w的*Writer。

writer := bufio.NewWriter(file)
writer.WriteString(str)
writer.Flush()
```

**方式二：**

```go
func WriteFile(filename string, data []byte, perm os.FileMode) error
//函数向filename指定的文件中写入数据。如果文件不存在将按给出的权限创建文件，否则在写入数据之前清空文件。
err = ioutil.WriterFile(file,)
```



### 应用1（bufio.NewWriter）

创建一个新文件`file/txt`，写入内容：5句 "hello World"

```go
import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	fileName := "C:\\Users\\16688\\Desktop\\file.txt"
	file, err := os.OpenFile(fileName, os.O_WRONLY, 0666)
	if err != nil {
		fmt.Printf("open file err=%v", err)
	}
	defer file.Close()

	// 准备写入 "I love 中国"
	str := "I love 中国\n"
	// 准备写入的代缓存的 *writer
	writer := bufio.NewWriter(file)
	for i := 0; i < 5; i++ {
		writer.WriteString(str)
	}
	/*
		因为 writer 是带缓存，因此在调用 writerString 方法时，
		其实内容是先写入到缓存的，所以需要调用 Flush()方法，
		将缓冲的数据真正写入到文件中，否则文件中会没有数据！
	*/
	writer.Flush()
}
```



### 应用2（ioutil.WriterFile）

将一个文件（file1.txt）的内容，写入到另外一个文件（file2.txt）。注：这两个文件已经存在。

```go
import (
	"fmt"
	"io/ioutil"
)

func main() {
	file1Name := "C:\\Users\\16688\\Desktop\\file1.txt"
	file2Name := "C:\\Users\\16688\\Desktop\\file2.txt"
	// 使用 ioutil.ReadFile 一次性将 file1.txt 文件内容读取到位
	data, err1 := ioutil.ReadFile(file1Name)
	if err1 != nil {
		fmt.Printf("read file err=%v", err1)
	}
	// 将 data 一次性写入到 file2.txt
	err2 := ioutil.WriteFile(file2Name, data, 0666)
	if err2 != nil {
		fmt.Println("write file error :", err2)
	}
}
```



## 判断文件是否存在

Golang判断文件或文件夹是否存在使用`os.Stat()`函数返回的错误值进行判断：

```go
//Stat返回描述文件f的FileInfo类型值。如果出错，错误底层类型是*PathError。
func (f *File) Stat() (fi FileInfo, err error)
```

- 如果返回的错误值为`nil`，说明文件或文件夹存在。
- 如果返回的错误类型使用`os.IsNotExist(err)`判断为`true`，说明文件或文件夹不存在。
- 如果返回的错误为其它类型，则不确定是否存在。

```go
func PathExists(path string) (bool, error) {
	_, err := os.Stat(path)
	if err == nil {
		return true, nil
	}
	if os.IsNotExist(err) {
		return false, nil
	}
	return false, err
}

func main() {
	file1Name := "C:\\Users\\16688\\Desktop\\file1.txt"
	file2Name := "C:\\Users\\16688\\Desktop\\file2.txt"
	isExist1, err1 := PathExists(file1Name)
	if err1 != nil {
		fmt.Println("error1:", err1)
	}
	isExist2, err2 := PathExists(file2Name)
	if err2 != nil {
		fmt.Println("error2:", err2)
	}
	fmt.Printf("%v exists? :%v\n", file1Name, isExist1)
	fmt.Printf("%v exists? :%v\n", file1Name, isExist2)
}
```



## 拷贝文件

```go
func Copy(dst Writer, src Reader) (written int64, err error)
/*
将src的数据拷贝到dst，直到在src上到达EOF或发生错误。返回拷贝的字节数和遇到的第一个错误。
对成功的调用，返回值err为nil而非EOF，因为Copy定义为从src读取直到EOF，它不会将读取到EOF视为应报告的错误。如果src实现了WriterTo接口，本函数会调用src.WriteTo(dst)进行拷贝；否则如果dst实现了ReaderFrom接口，本函数会调用dst.ReadFrom(src)进行拷贝。
*/
```

将一张图片`C:\Users\16688\Desktop\fileFolder1\p.jpg`拷贝到另一个文件夹`C:\Users\16688\Desktop\fileFolder2\`下

```go
func CopyFile(dstFileName string, srcFileName string) (written int64, err error) {
	// 打开 scrFileName
	srcFile, err1 := os.Open(srcFileName)
	if err1 != nil {
		fmt.Println("open file err1:", err1)
	}
	defer srcFile.Close()
	// 通过 srcFile 获取到 Reader
	reader := bufio.NewReader(srcFile)
	// 打开 dstFileName
	dstFile, err2 := os.OpenFile(dstFileName, os.O_WRONLY|os.O_CREATE, 0666)
	if err2 != nil {
		fmt.Println("open file err2:", err2)
		return
	}
	// 通过 dstFile 获取到 Writer
	writer := bufio.NewWriter(dstFile)
	defer dstFile.Close()

	return io.Copy(writer, reader)

}
func main() {
	dstFileName := "C:\\Users\\16688\\Desktop\\fileFolder2\\p.jpg"
	srcFileName := "C:\\Users\\16688\\Desktop\\fileFolder1\\p.jpg"
	_, err := CopyFile(dstFileName, srcFileName)
	if err == nil {
		fmt.Println("拷贝成功!")
	} else {
		fmt.Println("拷贝失败!")
	}
}
```





## 统计英文、数字、空格和其它字符数量

打开一个文件，创建一个`Reader`，每读取一行，就去统计该行有多少个 英文、数字、空格和其他字符，然后将结果保存到一个结构体中。

```go
package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

// 定义一个结构体，用于保存统计结果
type CharCount struct {
	ChCount    int // 记录英文个数
	NumCount   int // 记录数字的个数
	SpaceCount int // 记录空格的个数
	OtherCount int // 记录其他字符的个数
}

func main() {
	fileName := "D:\\DevelopmentSoftWare\\GoLand\\GoLand_Workspace\\demo\\test1.txt"
	file, err := os.Open(fileName)
	if err != nil {
		fmt.Printf("open file err=%v\n", err)
		return
	}
	defer file.Close()
	// 定义一个CharCount实例
	var count CharCount
	// 创建一个Reader
	reader := bufio.NewReader(file)
	//开始循环的读取 fileName 的内容
	for {
		str, err := reader.ReadString('\n')
		if err == io.EOF { // 读到文件末尾就退出
			break
		}
		// 为了兼容中文字符，可以将str转成[]rune
		strRune := []rune(str)
		// 遍历 strRune，进行统计
		for _, v := range strRune {
			switch {
			case v >= 'a' && v <= 'z':
				fallthrough
			case v >= 'A' && v <= 'Z':
				count.ChCount++
			case v == ' ' || v == '\t':
				count.SpaceCount++
			case v >= '0' && v <= '9':
				count.NumCount++
			default:
				count.OtherCount++
			}
		}
	}
	fmt.Printf("字符的个数：%v\n数字的个数：%v\n空格的个数：%v\n其它字符个数：%v",
		count.ChCount, count.NumCount, count.SpaceCount, count.OtherCount)
}
```



# 获取命令行参数

`os.Args`是一个`string`的切片，用来存储所有的命令行参数。

```go
// main.go
package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Println("命令行的参数个数：", len(os.Args))
	// 遍历os.Args切片，就可以得到所有的命令行输入参数值
	for i, v := range os.Args {
		fmt.Printf("args[%v]=%v\n", i, v)
	}
}
```

```shell
# 终端命令行
D:\DevelopmentSoftWare\GoLand\GoLand_Workspace\demo> go build -o test.exe main.go	# 生成一个 test.exe 文件
D:\DevelopmentSoftWare\GoLand\GoLand_Workspace\demo> .\test.exe tom 123 D:\file\file.txt 2.5

# 终端输出：
命令行的参数个数： 5
args[0]=D:\DevelopmentSoftWare\GoLand\GoLand_Workspace\demo\test.exe
args[1]=tom
args[2]=123
args[3]=D:\file\file.txt
args[4]=2.5

```



**`flag`包用来解析命令行参数**

前面的方式是比较原生的方式，对解析参数不是特别方便，特别是带有指定参数形式的命令行。比如`.\test.exe -a 123 -b abc -c 2.5`这样形式的命令行，go提供了`flag`包，可以方便的解析命令行参数，而且参数顺序可以随意。

该包中有一个`Parse()`方法，对于解析命令行参数非常重要：

```go
func (f *FlagSet) Parse(arguments []string) error
/*
从arguments中解析注册的flag。必须在所有flag都注册好而未访问其值时执行。未注册却使用flag -help时，会返回ErrHelp。
*/
```

```go
// main.go
package main

import (
	"flag"
	"fmt"
)

func main() {
	var name string
	var age int
	var height float64

	flag.StringVar(&name, "name", "", "姓名，默认为空")
	flag.IntVar(&age, "age", 20, "年龄，默认为20")
	flag.Float64Var(&height, "height", 1.70, "身高，默认1.70")

	// 这里有一个非常重要的操作，转换,必须调用该方法从arguments中解析注册的flag
	flag.Parse()

	fmt.Printf("name:%v, age:%v, height:%v", name, age, height)
}

```

```shell
# 终端命令行
D:\DevelopmentSoftWare\GoLand\GoLand_Workspace\demo> go build -o test.exe main.go	# 生成一个 test.exe 文件
D:\DevelopmentSoftWare\GoLand\GoLand_Workspace\demo> .\test.exe .\test.exe -name tom -age 22 -height 1.75


# 终端输出：
name:tom, age:22, height:1.75
```



# Json

## JSON基本介绍

JSON（JavaScript Object Notation）是一种轻量级的数据交换格式。

JSON易于机器解析和生成，并有效地提升网络传输效率，通常程序在网络传输时会先将数据（结构体、map等）**序列化**成json字符串，当接收方的得到json字符串时，再**反序列化**恢复成原来的数据类型（结构体、map等）。这种方式已然成为各个语言的标准。

在JS语言中，一切都是对象。因此，任何的数据类型都可以通过JSON来表示，即任何数据类型都可以转换成json格式，如字符串、数字、对象、数组、map、结构体等。

**JSON键值对**时用来保存数据的一种方式。

```go
键值对中的键名下载前面并用双引号 "" 包裹，使用冒号 : 分割，然后紧接着值
{"name":"zhongxi", "age":22, "HeightAndWeight":[1.70,57], "color":{"clothes":"white", "pants":"blue"}}

{
    "name":"zhongxi",
    "age":22,
    "HeightAndWeight":[
        1.7,
        57
    ],
    "color":{
        "clothes":"white",
        "pants":"blue"
    }
}
```



https://www.json.cn/ 网站可以验证一个json格式的数据是否正确。尤其是编写比较复杂的json格式数据的时候。



## 序列化

json序列化是指，将有`key-value`结构的数据类型（比如结构体、map、切片）序列化成json字符串的操作。

```go
func Marshal(v interface{}) ([]byte, error)
Marshal函数返回v的json编码。
```

```go
package main

import (
	"encoding/json"
	"fmt"
)

type Student struct {
	Name     string
	Age      int
	Birthday string
	Height   float64
}

func testStruct() {
	// 对结构体序列化
	stu := Student{
		Name:     "张三",
		Age:      3,
		Birthday: "2019-1-1",
		Height:   0.5,
	}
	// 将 stu 序列化
	data, err := json.Marshal(&stu)
	if err != nil {
		fmt.Println("序列化错误：", err)
	}
	// 输出序列化后的结果
	fmt.Printf("student序列化后=%v\n", string(data))
}

func testMap() {
	// 将 map 进行序列化
	// 定义一个map
	var a map[string]interface{}
	a = make(map[string]interface{})
	a["name"] = "tom"
	a["age"] = 20
	a["gender"] = "男"
	// 将 a 进行序列化
	data, err := json.Marshal(a)
	if err != nil {
		fmt.Println("序列化错误：", err)
	}
	// 输出序列化后的结果
	fmt.Printf("a 序列化后=%v\n", string(data))
}

func testSlice() {
    // 对切片进行序列化
	var slice []map[string]interface{}
	var m1 = map[string]interface{}{
		"name":   "jack",
		"age":    22,
		"gender": "男",
	}
	var m2 = map[string]interface{}{
		"name":   "mary",
		"age":    23,
		"gender": "女",
	}
	slice = append(slice, m1, m2)
	// 将 slice 进行序列化
	data, err := json.Marshal(slice)
	if err != nil {
		fmt.Println("序列化错误：", err)
	}
	// 输出序列化后的结果
	fmt.Printf("slice 序列化后=%v\n", string(data))
}

func testFloat64() {
	// 对基本数据类型进行序列化
	var num float64 = 23.45
	// 将 num 进行序列化
	data, err := json.Marshal(num)
	if err != nil {
		fmt.Println("序列化错误：", err)
	}
	// 输出序列化后的结果
	fmt.Printf("num 序列化后=%v\n", string(data))
}

func main() {
	testStruct()	// 对结构体进行序列化
	testMap()	// 对 map 进行序列化
	testSlice()	// 对切片进行序列化
	testFloat64()	// 对基本数据类型进行序列化
}
/*输出：
student序列化后={"Name":"张三","Age":3,"Birthday":"2019-1-1","Height":0.5}
a 序列化后={"age":20,"gender":"男","name":"tom"}
slice 序列化后=[{"age":22,"gender":"男","name":"jack"},{"age":23,"gender":"女","name":"mary"}]
num 序列化后=23.45
*/
```



对于结构体的序列化，如果我们希望序列化后的`key`的名字，可以给`struct`指定一个`tag`标签。

```go
type Student struct {
	Name     string  `json:"stu_name"` // 反射机制
	Age      int     `json:"stu_age"`
	Birthday string  `json:"stu_birthday"`
	Height   float64 `json:"stu_height"`
}

// 序列化后
student序列化后={"stu_name":"张三","stu_age":3,"stu_birthday":"2019-1-1","stu_height":0.5}
```



## 反序列化

json反序列化是指，将`json`字符串饭序列化成对应的数据类型（比如结构体、map、切片等）的操作。

```go
func Unmarshal(data []byte, v interface{}) error
Unmarshal函数解析json编码的数据并将结果存入v指向的值。
```

```go
package main

import (
	"encoding/json"
	"fmt"
)

type Student struct {
	Name     string
	Age      int
	Birthday string
	Height   float64
}

func unmarshalStruct() {
	// 对结构体反序列化
	str := "{\"Name\":\"张三\",\"Age\":3,\"Birthday\":\"2019-1-1\",\"Height\":0.5}"
	var stu Student // 定义一个Student实例
	// 将 str 反序列化
	err := json.Unmarshal([]byte(str), &stu)
	if err != nil {
		fmt.Println("反序列化错误：", err)
	}
	// 输出序列化后的结果
	fmt.Println("str序列化后:", stu)
}

func unmarshalMap() {
	// 将 map 进行反序列化
	str := "{\"age\":20,\"gender\":\"男\",\"name\":\"tom\"}"
	// 定义一个map
	var a map[string]interface{}
	// 反序列化不需要make对a进行初始化，因为make操作已经被封装到 Unmarshal 函数中
	// 将 a 进行反序列化
	err := json.Unmarshal([]byte(str), &a)
	if err != nil {
		fmt.Println("反序列化错误：", err)
	}
	// 输出序列化后的结果
	fmt.Println("a序列化后:", a)
}

func unmarshalSlice() {
	// 对切片进行反序列化
	str := "[{\"age\":22,\"gender\":\"男\",\"name\":\"jack\"},{\"age\":23,\"gender\":\"女\",\"name\":\"mary\"}]"
	// 定义一个slice
	// 反序列化不需要make对slice进行初始化，因为make操作已经被封装到 Unmarshal 函数中
	var slice []map[string]interface{}
	// 将 slice 进行反序列化
	err := json.Unmarshal([]byte(str), &slice)
	if err != nil {
		fmt.Println("反序列化错误：", err)
	}
	// 输出序列化后的结果
	fmt.Println("slice序列化后:", slice)
}

func main() {
	unmarshalStruct() //对结构体进行反序列化
	unmarshalMap()    //对map进行反序列化
	unmarshalSlice()  //对切片进行反序列化
}
/*输出：
str序列化后: {张三 3 2019-1-1 0.5}
a序列化后: map[age:20 gender:男 name:tom]
slice序列化后: [map[age:22 gender:男 name:jack] map[age:23 gender:女 name:mary]]
*/
```

- 在反序列化一个json字符串时，要确保反序列化后的数据类型和原来序列化前的数据类型一致。

- 如果json字符串是通过程序获取到的，则不需要再对`"`进行转义处理。

	```go
	func unmarshalMap() {
		// 将 map 进行反序列化
		//str := "{\"age\":20,\"gender\":\"男\",\"name\":\"tom\"}"
		str := testMap()	//通过程序获取的，不需要对 " 进行转义
		//......
	}
	```



# 单元测试

[Go语言标准库文档中文版 | Go语言中文网 | Golang中文社区 | Golang中国 (studygolang.com)](https://studygolang.com/pkgdoc) - testing

go语言中自带一个轻量级的测试框架`testing`和自带的`go test`命令来实现单元测试和性能测试。`testing`框架和其他语言中的测试框架类似，可以基于这个框架写针对相应函数的测试用例，也可以基于该框架写相应的压力测试用例。

```go
import "testing"

testing 提供对 Go 包的自动化测试的支持。通过 'go test'命令，能够自动执行如下形式的任何函数：
func TestXxx(t *testing.T)
其中 Xxx 可以是任何字母数字字符串（但第一个字母不能是 [a-z]），用于识别测试例程。
在这些函数中，使用 Error, Fail 或相关方法来发出失败信号。

要编写一个新的测试套件，需要创建一个名称以 _test.go 结尾的文件，该文件包含 `TestXxx` 函数，如上所述。 将该文件放在与被测试的包相同的包中。该文件将被排除在正常的程序包之外，但在运行 “go test” 命令时将被包含。 
```

通过单元测试，可以解决如下问题：

1. 确保每个函数时可运行，并且运行结果是正确的。
2. 确保写出来的代码性能是好的。
3. 单元测试能及时的发现程序设计或实现的逻辑错误，使问题及早暴露，便于问题的定位解决，而性能测试的重点在于发现程序设计上的一些问题，让程序能够在高并发的情况下还能保持稳定。

## 基本用法

使用go的单元测试，对`numSquare`进行测试：

```go
// square.go
func NumSquare(n int) int {
	square := n * n
	return square
}
```

创建一个名称以 `_test.go` 结尾的文件`square_test.go`，该文件包含 `TestNumSquare` 函数， 将该文件放在与被测试文件的包相同的包中。

```go
// square_test.go
package main

import (
	"testing"
)

// 编写一个测试用例，去测试NumSquare是否正确
func TestNumSquare(t *testing.T) {
	//调用NumSquare
	square := NumSquare(10)
	if square != 10 {
		t.Fatalf("NumSquare(10)执行错误，期望值=%v，实际值=%v", 100, square)
	}
	// 如果正确，输出日志
	t.Logf("NumSquare(10)执行正确...")
}
```

直接运行`square_test.go`

```
=== RUN   TestNumSquare
    square_test.go:15: NumSquare(10)执行正确...
--- PASS: TestNumSquare (0.00s)
PASS
```



## 使用注意

1. 测试用例文件名必须以`_test.go`结尾。
2. 测试用例函数必须以`Test`开头，一般来说就是`Test+被测试的函数名`，比如`TestNumSquare`。
3. `TestXxx(t *testing.T)`的形参类型必须是`*testing.T`。
4. 一个测试用例文件中，可以有多个测试用例函数。
5. 终端测试用例指令：
	- `go test`，如果运行正确，无日志；运行错误，会输出日志。
	- `go test -v`，无论运行正确还是错误，都输出日志。
6. 当出现错误时，可以使用`t.Fatalf`来格式化输出错误信息，并退出程序。
7. `t.Logf`方法可以输出相应的日志。
8. **测试用例函数，并没有放在`main`函数中，但仍然能执行。**
9. `PASS`表示测试用例运行成功，`FAIL`表示测试用例运行失败。
10. 终端测试单个文件，一定要带上被测试的原文件:`go test -v square_test.go square.go`。
11. 测试单个方法：`go test -v -test.run TestNumSquare`



# goroutine和channel

## goroutine

### 进程和线程

1. 进程就是程序在操作系统中的一次执行过程，是系统进行资源分配和调度的基本单位。
2. 线程是进程的一个执行实例，是程序执行的最小单元，它是比进程更小的能独立运行的基本单位。
3. 一个进程可以创建和销毁多个线程，同一个进程中的多个线程可以并发执行。
4. 一个程序至少有一个进程，一个进程至少有一个线程。

### 并发和并行

**并发：**多线程程序在单核上运行（同一时间段内执行多个任务）。

- 多个任务作用在一个CPU。
- 从微观角度看，在一个时间点上，其实只有一个任务在执行。

**并行：**多线程程序在多核上运行（同一时刻执行多个任务）。

- 多个任务作用在多个CPU。
- 从微观的角度看，在一个时间点上，就是多个任务在同时执行。



### Go协程和Go主线程

**go主线程**：是一个物理线程，直接作用在CPU上，是重量级的，非常耗费CPU资源。

**协程**：从主线程开启的，是轻量级的线程，是逻辑态。对资源消耗相对较小。一个Go线程上，可以起多个协程，可以理解为协程是轻量级的线程（编译器做优化）。Go协程的特点：

1. 有独立的栈空间。
2. 共享程序堆空间。
3. 调度由用户控制。
4. 协程是轻量级的线程。

协程机制是Golang的重要特点，可以轻松的开启上万个协程。而其它编程语言的并发一般基于线程的，开启过多的线程，资源耗费大。

**Go语言中的操作系统线程和`goroutine`的关系：**

- 一个操作系统线程对应用户态多个`goroutine`。
- go程序可以同时使用多个操作系统线程。
- `goroutine`和OS线程是多对多的关系，即`m:n`。





**主线程和协程的运行机制：**

- 如果主线程退出了，则协程即使还没有执行完毕，也会退出。
- 协程也可以在主线程退出之前结束，比如完成了自己的任务。

```
案例：编写一个程序，完成如下功能：
1）在主线程（可以理解成进程）中，开启一个goroutine，该协程每个一秒输出 "hello,world..."
2）在主线程中也每个一秒输出"hello,golang..."，输出10次后，退出程序
3）要求主线程和goroutine同时执行。
```

```go
package main

import (
	"fmt"
	"strconv"
	"time"
)

func test() {
	for i := 1; i <= 10; i++ {
		fmt.Println("test() hello,world " + strconv.Itoa(i))
		time.Sleep(time.Second)
	}
}

func main() {
	go test() // 开启了一个协程
	for i := 1; i <= 10; i++ {
		fmt.Println("main() hello,golang " + strconv.Itoa(i))
		time.Sleep(time.Second)
	}
}

/*输出：
main() hello,golang 1
test() hello,world 1
test() hello,world 2
main() hello,golang 2
main() hello,golang 3
test() hello,world 3
test() hello,world 4
main() hello,golang 4
main() hello,golang 5
test() hello,world 5
test() hello,world 6
main() hello,golang 6
main() hello,golang 7
test() hello,world 7
test() hello,world 8
main() hello,golang 8
main() hello,golang 9
test() hello,world 9
test() hello,world 10
main() hello,golang 10
*/
```



### sync.WaitGroup

如果上面的`test()`中循环打印10次，而`main()`中只循环打印5次，会出现这样的结果：

```go
main() hello,golang 1
test() hello,world 1
test() hello,world 2
main() hello,golang 2
main() hello,golang 3
test() hello,world 3
test() hello,world 4
main() hello,golang 4
test() hello,world 5
main() hello,golang 5
```

很明显，主线程结束后，协程并没有完成所有打印。

**如何保证在所有的协程完成之后，主线程才结束？**

```go
package main

import (
	"fmt"
	"strconv"
	"sync"
	"time"
)

var wg sync.WaitGroup

func test() {
	defer wg.Done() //test()结束时，通知计数器-1
	for i := 1; i <= 10; i++ {
		fmt.Println("test() hello,world " + strconv.Itoa(i))
		time.Sleep(time.Second)
	}
}

func main() {
	wg.Add(1) //需要开启一个协程，则设置计数器为1
	go test() // 开启了一个协程
	for i := 1; i <= 5; i++ {
		fmt.Println("main() hello,golang " + strconv.Itoa(i))
		time.Sleep(time.Second)
	}
	wg.Wait() //阻塞，等所有协程结束后main才结束
}
/*输出：
main() hello,golang 1
test() hello,world 1
main() hello,golang 2
test() hello,world 2
main() hello,golang 3
test() hello,world 3
test() hello,world 4
main() hello,golang 4
main() hello,golang 5
test() hello,world 5
test() hello,world 6
test() hello,world 7
test() hello,world 8
test() hello,world 9
test() hello,world 10
*/
```



### MPG模式

- **M**：操作系统的主线程（是物理线程）。
- **P**：协程执行需要的上下文。
- **G**：协程



### 获取和设置Golang运行的CPU数

```go
/* NumCPU返回本地机器的逻辑CPU个数。*/
func NumCPU() int

/* GOMAXPROCS设置可同时执行的最大CPU数，并返回先前的设置。
若 n < 1，它就不会更改当前设置。本地机器的逻辑CPU数可通过 NumCPU 查询。本函数在调度程序优化后会去掉。*/
func GOMAXPROCS(n int) int

/*
go1.8后，默认让程序运行在多个核上，可以不用设置了
go1.8前，仍需要设置一下，可以更高效的利用CPU
*/
```

```go
package main

import (
	"fmt"
	"runtime"
)

func main() {
	// 获取当前系统CPU的数量
	num := runtime.NumCPU()
	// 设置num-1个CPU运行Go程序
	oldNum := runtime.GOMAXPROCS(num - 1)
	fmt.Println("num=", num)	// num=12
	fmt.Println("oldNum=", oldNum)	// oldNum=12
}
```



### 捕获panic

如果开启了一个协程，但是这个协程出现了`panic`，如果不捕获这个`panic`，就会造成整个程序崩溃。可以在`goroutine`中使用`recover`来捕获`panic`，这样即使这个协程发生问题，但主线程仍然不受影响，可以继续执行：

```go
func sayHello() {
	time.Sleep(time.Second)
	fmt.Println("hello,world!")
}

func test() {
	// 这里可以使用defer + recover
	defer func() {
		// 捕获test抛出的panic
		if err := recover(); err != nil {
			fmt.Println("test()发生错误", err)
		}
	}()

	//定义了一个map，发生 nil map error
	var myMap map[int]string
	myMap[0] = "golang" // error
}

func main() {
	go sayHello()
	go test()
	for i := 1; i <= 10; i++ {
		fmt.Println("main() ok=", i)
		time.Sleep(time.Second)
	}
}
```



## channel（引用类型）

### channel的基本介绍

- `channel`本质就是一个数据结构-队列。
- 数据是先进先出（FIFO: first in first out）。
- `channel`本身就是线程安全的，多`goroutine`访问时，也不会发生资源竞争问题，不需要加锁。
- `channel`有类型的，一个`string`的`channel`只能存放`string`类型数据。

### 定义/声明channel

```go
var 变量名 chan 数据类型

//demo：
var intChan chan int	// intChan用于存放int数据
var mapChan chan map[int]string //mapChan用于存放map[int]string类型数据
var perChan chan Person
var perChan2 chan *Person
```

- `channel`是引用类型。
- `channel`必须初始化才能写入数据，即`make`后才能使用。
- `channel`是由类型，只能写入相应类型的数据。



### channel的初始化、写入、读取

初始化：

```go
var intChan chan int
intChan = make(chan int, 3)
```

将数据写入管道中和从管道中读取数据：

```go
intChan <- 10	// 写入

var num int
num = <-intChan	// 读取
```

案例：

```go
func main() {
	// 创建一个可以存放 3 个int类型的管道
	var intChan chan int
	intChan = make(chan int, 3)
	// 看看intChan 是什么
	fmt.Printf("intChan的值=%v，intChan本身的地址=%p\n", intChan, &intChan)

	// 向管道中写入数据，需要注意，写入数据时，不能超过其容量
	intChan <- 10
	num := 200
	intChan <- num
	intChan <- -50

	// 管道的长度和cap（容量）
	fmt.Printf("intChan len=%v, cap=%v\n", len(intChan), cap(intChan))
	// 从管道中读取数据
	// 在没有使用协程的情况下，如果管道中的数据已经全部取出，再取就会报告deadlock
	var num2 int
	num2 = <-intChan
	fmt.Println("num2=", num2)
	fmt.Printf("intChan len=%v, cap=%v\n", len(intChan), cap(intChan))
}
/*输出：
intChan的值=0xc00010e000，intChan本身的地址=0xc000006028
intChan len=3, cap=3
num2= 10
intChan len=2, cap=3
*/
```



### 通道类型（有无缓冲区）

**无缓冲区（又称同步通道）：**

```go
var ch chan int
ch = make(chan int)
ch <- 10  //向通道里放入数据
fmt.Println(x)
close(ch)
```

上面的程序会发生`deadlock`错误，由于使用`ch := make(chan int)`创建的是无缓冲的通道，无缓冲的通道只有在有接收方能够接收值的时候才能发送成功，否则会一直处于等待发送的阶段。同理，如果对一个无缓冲通道执行接收操作时，没有任何向通道中发送值的操作那么也会导致接收操作阻塞。

其中一种解决无缓冲通道的死锁问题就是在将数据放入通道之前创建一个`goroutine`去接受值：

```go
func main() {
	var ch chan int
	ch = make(chan int)
	var x int
	go func(int) {
		x = <-ch
	}(x) //从通道里取出数据，由于没有缓冲区，如果没有接受者，则通道会发生阻塞
	ch <- 10 //向通道里放入数据
	fmt.Println(x)
	close(ch)
}
```

另一种解决上面死锁问题的方法就是使用有缓冲区的通道。



**有缓冲区（又称异步通道）：**

只要通道的容量大于零，那么该通道就属于有缓冲的通道，通道的容量表示通道中最大能存放的元素数量。当通道内已有元素数达到最大容量后，再向通道执行发送操作就会阻塞，除非有从通道执行接收操作。

```go
var ch chan int
ch = make(chan int, 1)
ch <- 10 //向通道里放入数据
x := <-ch	// 从通道里取出数据
fmt.Println(x)
close(ch)
```







### channel使用注意

1. `channel`中只能存放指定的数据类型。
2. `channel`的数据放满后，就不能再放入了，再存放会报告`deadlock`。
3. 如果从`channel`中取出数据后，可以继续放入。
4. 在没有使用协程的情况下，如果`channel`数据取完了，再取就会报`deadlock`。

### 案例演示

#### `int`型`channel`：

```go
func main() {
	// 创建一个可以存放 2 个int类型的管道
	var intChan chan int
	intChan = make(chan int, 2)

	// 向管道中写入数据
	intChan <- 10
	intChan <- 20
	//intChan <- 30 //因为intChan的容量为2，再存放会报告deadlock

	// 从管道中取数据
	num1 := <-intChan
	num2 := <-intChan
	//num3 := <-intChan //因为这时候intChan中已经没有数据了，再取就会报告deadlock

	fmt.Printf("num1=%v  num2=%v", num1, num2)
}
/*输出：
num1=10  num2=20
*/
```

#### `map`型`channel`：

```go
func main() {
	// 创建一个可以存放 2 个map[string]string类型的管道
	var mapChan chan map[string]string
	mapChan = make(chan map[string]string, 2)

	m1 := map[string]string{
		"city1": "北京",
		"city2": "重庆",
	}
	m2 := map[string]string{
		"country1": "中国",
		"country2": "俄罗斯",
	}
	// 向管道中写入数据
	mapChan <- m1
	mapChan <- m2
	//mapChan <- m2 //因为mapChan的容量为2，再存放会报告deadlock

	// 从管道中取数据
	m11 := <-mapChan
	m22 := <-mapChan
	//m33 := <-mapChan //因为这时候mapChan中已经没有数据了，再取就会报告deadlock

	fmt.Printf("m11=%v  m22=%v", m11, m22)
}
/*输出：
m11=map[city1:北京 city2:重庆]  m22=map[country1:中国 country2:俄罗斯]
*/
```

#### 结构体型`channel`：

```go
type Student struct {
	Name string
	Age  int
}

func main() {
	// 创建一个可以存放 2 个Student类型的管道
	var stuChan chan Student
	stuChan = make(chan Student, 2)

	stu1 := Student{
		Name: "tom",
		Age:  22,
	}
	stu2 := Student{
		Name: "jack",
		Age:  25,
	}
	// 向管道中写入数据
	stuChan <- stu1
	stuChan <- stu2
	//stuChan <- stu2 //因为stuChan的容量为2，再存放会报告deadlock

	// 从管道中取数据
	stu11 := <-stuChan
	stu22 := <-stuChan
	//stu33 := <-stuChan //因为这时候stuChan中已经没有数据了，再取就会报告deadlock

	fmt.Printf("stu11=%v  stu22=%v", stu11, stu22)
}
/*输出：
stu11={tom 22}  stu22={jack 25}
*/
```

#### 结构体指针型`channel`：

```go
type Student struct {
	Name string
	Age  int
}

func main() {
	// 创建一个可以存放 2 个 *Student 类型的管道
	var stuPChan chan *Student
	stuPChan = make(chan *Student, 2)

	stuP1 := &Student{
		Name: "tom",
		Age:  22,
	}
	stuP2 := &Student{
		Name: "jack",
		Age:  25,
	}
	// 向管道中写入数据
	stuPChan <- stuP1
	stuPChan <- stuP2
	//stuPChan <- stuP2 //因为stuPChan的容量为2，再存放会报告deadlock

	// 从管道中取数据
	stuP11 := <-stuPChan
	stuP22 := <-stuPChan
	//stuP33 := <-stuPChan //因为这时候stuPChan中已经没有数据了，再取就会报告deadlock

	fmt.Printf("stuP11=%v  stuP22=%v", stuP11, stuP22)
}
/*输出：
stuP11=&{tom 22}  stuP22=&{jack 25}
*/
```



#### 任意数据类型`channel`：

```go
func main() {
	// 创建一个可以存放 4 个任意类型的管道
	var allChan chan interface{}
	allChan = make(chan interface{}, 4)

	var num1 int = 20
	m1 := map[string]string{"city1": "北京", "city2": "重庆"}
	stu1 := Student{
		Name: "tom",
		Age:  22,
	}
	stuP1 := &Student{
		Name: "jack",
		Age:  25,
	}
	// 向管道中写入数据
	allChan <- num1
	allChan <- m1
	allChan <- stu1
	allChan <- stuP1
	// 从管道中取数据
	num2 := <-allChan
	m2 := <-allChan
	stu2 := <-allChan
	stuP2 := <-allChan

	fmt.Printf("num2=%v  m2=%v  stu2=%v  stuP2=%v", num2, m2, stu2, stuP2)
}
/*输出：
num2=20  m2=map[city1:北京 city2:重庆]  stu2={tom 22}  stuP2=&{jack 25}
*/
```



#### 任意数据类型`channel`与类型断言：

```go
type Student struct {
	Name string
	Age  int
}

func main() {
	// 创建一个可以存放 1 个任意类型的管道
	var allChan chan interface{}
	allChan = make(chan interface{}, 1)

	stu1 := Student{
		Name: "tom",
		Age:  22,
	}
	// 向管道中写入数据
	allChan <- stu1
	// 从管道中取数据
	stu2 := <-allChan
	fmt.Printf("stu2=%T, stu2=%v\n", stu2, stu2)
	// stu2.Name //不能直接用，编译不通过
	// 需要使用类型断言
	s := stu2.(Student)
	fmt.Printf("stu2.Name=%v", s.Name)
}
/*输出：
stu2=main.Student, stu2={tom 22}
stu2.Name=tom
*/
```



### `channel`的关闭和遍历

#### `channel`的关闭

使用内置函数`close`可以关闭`channel`，当`channel`关闭后，就不能再向`channel`写数据了，但是仍然可以从该`channel`读取数据。

```go
func close(c chan<- Type)
/*
内建函数close关闭信道，该通道必须为双向的或只发送的。它应当只由发送者执行，而不应由接收者执行，其效果是在最后发送的值被接收后停止该通道。在最后的值从已关闭的信道中被接收后，任何对其的接收操作都会无阻塞的成功。对于已关闭的信道，语句：
*/
x, ok := <-c	//还会将ok置为false。
```



```go
func main() {
	intChan := make(chan int, 3)
	intChan <- 100
	intChan <- 200
	close(intChan) //close
	//intChan <- 300 // 关闭通道之后不能够再写入
	// 但关闭通道后，读取数据是可以的
	n1 := <-intChan
	fmt.Println("n1=", n1)
}
```



#### `channel`的遍历

`channel`支持`for-range`的方式进行遍历，注意两个细节：

- 在遍历时，如果`channel`没有关闭，则会出现`deadlock`的错误。
- 在遍历时，如果`channel`已经关闭，则会正常遍历数据，遍历完后，就会退出遍历。

**注意：**遍历`channel`如果要用`for`循环遍历，需要先确定`channel`的大小，如果动态地用`channel`大小做判断条件，最终只能取出一半的数据：

```go
func main() {
	intChan1 := make(chan int, 10)
	intChan2 := make(chan int, 10)
	for i := 0; i < 10; i++ {
		intChan1 <- i //存放5个数据到intChan1
		intChan2 <- i //存放5个数据到intChan2
	}
	// 不能动态使用channel大小作为普通的for循环判断条件，否则只能取出一半的数据
	fmt.Printf("方式一： ")
	for i := 0; i < len(intChan1); i++ {
		num := <-intChan1
		fmt.Printf("%v  ", num)
	}
	// 可以先确定channel大小，再进行普通的for循环遍历
	fmt.Printf("\n方式二： ")
	chanLen := len(intChan2)
	for j := 0; j < chanLen; j++ {
		num := <-intChan2
		fmt.Printf("%v  ", num)
	}
}
/*输出：
方式一： 0  1  2  3  4  
方式二： 0  1  2  3  4  5  6  7  8  9
*/
```



**使用`for-range`遍历`channel`：**

```go
func main() {
	intChan := make(chan int, 10)
	for i := 0; i < 10; i++ {
		intChan <- i //存放5个数据到intChan
	}
	// 使用for-range遍历channel
	// 在遍历时，如果channel没有关闭，则会出现deadlock的错误
	// 在遍历时，如果channel已经关闭，则会正常遍历数据，遍历完后，就会退出遍历
	close(intChan) // 关闭channel
	fmt.Println("\n遍历前channel大小：", len(intChan))
	for v := range intChan {
		fmt.Printf("%v  ", v)
	}
	fmt.Println("\n遍历后channel大小：", len(intChan))
}
/*输出：
遍历前channel大小： 10
0  1  2  3  4  5  6  7  8  9  
遍历后channel大小： 0
*/
```



### 



### goroutine和channel结合实例

**注意：在读入的数据数量大于通道的容量时，可以读写频率不一样，但不能只写不读，否则会发生阻塞。**

#### 实例1：

编写`goroutine`和`channel`协同工作的程序，要求如下：

1. 开启一个`writeData协程`，向管道`intChan`中写入50个整数。
2. 开启一个`readData`协程，从管道`intChan`中读取`writeData`写入的数据。
3. 注意：`writeData`和`readData`操作的是同一个管道。
4. 主线程需要等待`writeData`和`readData`协程都完成工作了才能推出。

```go
package main

import (
	"fmt"
	"time"
)

func writeData(intChan chan int) {
	for i := 1; i <= 20; i++ {
		// 放入数据
		intChan <- i
		fmt.Println("writeData: ", i)
		time.Sleep(time.Second )
	}
	close(intChan) // 写入完了就关闭
}

func readData(intChan chan int, exitChan chan bool) {
	for {
		v, ok := <-intChan
		if !ok {
			break
		}
		time.Sleep(time.Second )
		fmt.Println("readData: ", v)
	}
	exitChan <- true //读完数据后，向exitChan写入true
	close(exitChan)  //写入后关闭exitChan
}

func main() {
	intChan := make(chan int, 20)
	exitChan := make(chan bool, 1)
	go writeData(intChan)
	go readData(intChan, exitChan)
	for {
		_, ok := <-exitChan
		fmt.Println("exit-ok:", ok)
		if !ok {
			break
		}
	}
}

```



#### 实例2：

统计1-200000的数字中，哪些是素数？

**传统方法：**

```go
func main() {
	var count int
	start := time.Now().UnixMicro() // 单位：微秒
label:
	for num := 2; num <= 200000; num++ {
		for i := 2; i < num; i++ {
			if num%i == 0 { //说明该num不是素数
				continue label
			}
		}
		//fmt.Printf("%v是素数！\n", num)
		count++
	}
	end := time.Now().UnixMicro() // 单位：微秒
	fmt.Printf("素数个数：%v\n", count)
	fmt.Printf("传统方法耗时= %v 微秒", end-start)
}
/*输出：
素数个数：17984
传统方法耗时= 11725486 微秒
*/
```



**使用`goroutine`和`channel`：**

```go
package main

import (
	"fmt"
	"time"
)

func putNum(intChan chan int, n int) {
	// 向intChan中放入n个数据
	for i := 2; i <= n; i++ {
		intChan <- i
	}
	close(intChan) //关闭
}

func primeNumber(intChan chan int, primeChan chan int, exitChan chan bool) {
label:
	for {
		num, ok := <-intChan
		if !ok { // intChan 取不到
			break
		}
		// 判断是不是素数
		for i := 2; i < num; i++ {
			if num%i == 0 { // 说明该num不是素数
				continue label
			}
		}
		primeChan <- num //如果该num是素数，就放入primeChan中
	}
	fmt.Println("有一个primeNum 协程因取不到数据而退出！")
	// 由于创建的多个协程共用primeChan管道，这里还不能关闭primeChan，防止其他协程不能向通道中写入数据
	exitChan <- true //向exitChan 写入true,标识该协程结束，退出管道
}

func closePrimeChan(exitChan chan bool, primeChan chan int) {
	for i := 0; i < 4; i++ {
		<-exitChan
	}
	end = time.Now().UnixMicro() // 单位：微秒
	close(primeChan)
}

func main() {

	intChan := make(chan int, 10000)
	primeChan := make(chan int, 200000)
	// 标识退出的管道协程
	exitChan := make(chan bool, 4)

	start = time.Now().UnixMicro() // 单位：微秒

	// 开启一个putNum协程，向intChan中放入1-200000个数
	go putNum(intChan, 200000)
	// 开启4个primeNumber协程，从intChan中取出数据，并判断是否为素数
	// 如果是素数，就放入到primeChan
	for i := 0; i < 4; i++ {
		go primeNumber(intChan, primeChan, exitChan)
	}

	//当从exitChan中取出4个数据，就可以放心关闭primeChan
	go closePrimeChan(exitChan, primeChan)

	// 遍历primeChan，把结果取出来
	for {
		//res, ok := <-primeChan
		_, ok := <-primeChan
		if !ok {
			fmt.Printf("素数个数：%v\n", count)
			fmt.Printf("main线程退出，耗时：%v 微秒", end-start)
			break
		}
		count++ // 统计素数个数
		//fmt.Printf("素数=%d\n", res)
	}
}
/*输出：
有一个primeNum 协程因取不到数据而退出！
有一个primeNum 协程因取不到数据而退出！
有一个primeNum 协程因取不到数据而退出！
有一个primeNum 协程因取不到数据而退出！
素数个数：17984
main线程退出，耗时：3147292 微秒
*/
```

传统方法耗时：11725486 微秒

使用`goroutine`和`channel`耗时：3147292 微秒

可以看出传统方法耗时是使用`goroutine`和`channel`耗时的**大约4倍**。



### `channel`使用细节

#### 单向通道

`channel`可以声明为只读或者只写（**即单向通道**）.在函数传参及任何赋值操作中全向通道（正常通道）可以转换为单向通道，但是无法反向转换。

```go
func main() {
	// 1.在默认情况下，管道是双向的
	var ch1 chan int
	ch1 = make(chan int, 3)
	ch1 <- 10
	num1 := <-ch1
	fmt.Println(num1)

	// 2.声明为只写
	var ch2 chan<- int
	ch2 = ch1 // ch1转换为单向只写通道
	ch2 <- 20
	//num2 := <-ch2 // 错误，只能写，不能读
	fmt.Println("ch2", ch2)

	// 3.声明为只读
	var ch3 <-chan int
	ch3 = ch1 // ch1转换为单向只读通道
	num3 := <-ch3
	//ch3 <- 30	//错误，只能读，不能写
	fmt.Println("num3=", num3)
}
```



#### select语句

Select 的使用方式类似于之前学到的 switch 语句，它也有一系列 case 分支和一个默认的分支。每个 case 分支会对应一个通道的通信（接收或发送）过程。select 会一直等待，直到其中的某个 case 的通信操作完成时，就会执行该 case 分支对应的语句。具体格式如下：

```go
select {
case <-ch1:
	//...
case data := <-ch2:
	//...
case ch3 <- 10:
	//...
default:
	//默认操作
}
```

**select语句具有以下特点：**

- 可以处理一个或多个channel的发送/接受操作。
- 如果多个case同时满足，select会随机选择一个执行。
- 对于没有case的select会一直阻塞，可用于阻塞main函数，防止退出。

```go
func main() {
	// 使用select可以解决从管道取数据的阻塞问题
	// 1.定义一个含有10个int数据的管道
	intChan := make(chan int, 10)
	for i := 1; i <= 10; i++ {
		intChan <- i
	}
	// 2.定义一个含有5个string数据的管道
	stringChan := make(chan string, 5)
	for i := 1; i <= 5; i++ {
		stringChan <- "hello," + fmt.Sprintf("%d", i)
	}

	//close(intChan)
	//close(stringChan)
	//for i := 0; i < 15; i++ {
	//	fmt.Println("intChan:", <-intChan)
	//	fmt.Println("stringChan:", <-stringChan)
	//} // 如果没有关闭intChan、stringChan，就会阻塞而导致deadlock

	// 在实际开发中，不好确定什么时候关闭通道
	// 可以使用select方式解决
	for {
		// 注意：这里intChan、stringChan一直没有关闭，并不会一直阻塞而导致deadlock
		// 会自动匹配case
		select {
		case v := <-intChan:
			fmt.Println("intChan:", v)
			time.Sleep(time.Second)
		case v := <-stringChan:
			fmt.Println("intChan:", v)
			time.Sleep(time.Second)
		default:
			fmt.Println("都取不到了，不取了，退出程序！")
			return
		}
	}
}
```



# 反射

## 基本介绍

- 反射可以在运行时**动态获取变量的各种信息**，比如变量的类型（type）、类别（kind）。
- 如果是结构体变量，还可以获取到结构体本身的信息（包括结构体的字段、方法）。
- 通过反射，可以修改变量的值，可以调用关联的方法。



## reflect包

在Go语言的反射机制中，任何接口值都由是`一个具体类型`和`具体类型的值`两部分组成的。 在Go语言中反射的相关功能由内置的reflect包提供，任意接口值在反射中都可以理解为由`reflect.Type`和`reflect.Value`两部分组成，并且reflect包提供了`reflect.TypeOf`和`reflect.ValueOf`两个函数来获取任意对象的Value和Type。

### reflect.Type

#### Type接口

```go
type Type interface {
    // Kind返回该接口的具体分类
    Kind() Kind
    // Name返回该类型在自身包内的类型名，如果是未命名类型会返回""
    Name() string
    // PkgPath返回类型的包路径，即明确指定包的import路径，如"encoding/base64"
    // 如果类型为内建类型(string, error)或未命名类型(*T, struct{}, []int)，会返回""
    PkgPath() string
    // 返回类型的字符串表示。该字符串可能会使用短包名（如用base64代替"encoding/base64"）
    // 也不保证每个类型的字符串表示不同。如果要比较两个类型是否相等，请直接用Type类型比较。
    String() string
    // 返回要保存一个该类型的值需要多少字节；类似unsafe.Sizeof
    Size() uintptr
    // 返回当从内存中申请一个该类型值时，会对齐的字节数
    Align() int
    // 返回当该类型作为结构体的字段时，会对齐的字节数
    FieldAlign() int
    // 如果该类型实现了u代表的接口，会返回真
    Implements(u Type) bool
    // 如果该类型的值可以直接赋值给u代表的类型，返回真
    AssignableTo(u Type) bool
    // 如该类型的值可以转换为u代表的类型，返回真
    ConvertibleTo(u Type) bool
    // 返回该类型的字位数。如果该类型的Kind不是Int、Uint、Float或Complex，会panic
    Bits() int
    // 返回array类型的长度，如非数组类型将panic
    Len() int
    // 返回该类型的元素类型，如果该类型的Kind不是Array、Chan、Map、Ptr或Slice，会panic
    Elem() Type
    // 返回map类型的键的类型。如非映射类型将panic
    Key() Type
    // 返回一个channel类型的方向，如非通道类型将会panic
    ChanDir() ChanDir
    // 返回struct类型的字段数（匿名字段算作一个字段），如非结构体类型将panic
    NumField() int
    // 返回struct类型的第i个字段的类型，如非结构体或者i不在[0, NumField())内将会panic
    Field(i int) StructField
    // 返回索引序列指定的嵌套字段的类型，
    // 等价于用索引中每个值链式调用本方法，如非结构体将会panic
    FieldByIndex(index []int) StructField
    // 返回该类型名为name的字段（会查找匿名字段及其子字段），
    // 布尔值说明是否找到，如非结构体将panic
    FieldByName(name string) (StructField, bool)
    // 返回该类型第一个字段名满足函数match的字段，布尔值说明是否找到，如非结构体将会panic
    FieldByNameFunc(match func(string) bool) (StructField, bool)
    // 如果函数类型的最后一个输入参数是"..."形式的参数，IsVariadic返回真
    // 如果这样，t.In(t.NumIn() - 1)返回参数的隐式的实际类型（声明类型的切片）
    // 如非函数类型将panic
    IsVariadic() bool
    // 返回func类型的参数个数，如果不是函数，将会panic
    NumIn() int
    // 返回func类型的第i个参数的类型，如非函数或者i不在[0, NumIn())内将会panic
    In(i int) Type
    // 返回func类型的返回值个数，如果不是函数，将会panic
    NumOut() int
    // 返回func类型的第i个返回值的类型，如非函数或者i不在[0, NumOut())内将会panic
    Out(i int) Type
    // 返回该类型的方法集中方法的数目
    // 匿名字段的方法会被计算；主体类型的方法会屏蔽匿名字段的同名方法；
    // 匿名字段导致的歧义方法会滤除
    NumMethod() int
    // 返回该类型方法集中的第i个方法，i不在[0, NumMethod())范围内时，将导致panic
    // 对非接口类型T或*T，返回值的Type字段和Func字段描述方法的未绑定函数状态
    // 对接口类型，返回值的Type字段描述方法的签名，Func字段为nil
    Method(int) Method
    // 根据方法名返回该类型方法集中的方法，使用一个布尔值说明是否发现该方法
    // 对非接口类型T或*T，返回值的Type字段和Func字段描述方法的未绑定函数状态
    // 对接口类型，返回值的Type字段描述方法的签名，Func字段为nil
    MethodByName(string) (Method, bool)
    // 内含隐藏或非导出方法
}
```





#### TypeOf

在Go语言中，使用`reflect.TypeOf()`函数可以获得任意值的类型对象（`reflect.Type`），程序通过类型对象可以访问任意值的类型信息。

```go
func reflectType(x interface{}) {
	t := reflect.TypeOf(x)
	fmt.Printf("type:%v\n", t)
}

func main() {
	var a float32 = 3.14
	reflectType(a) //type:float32
	var b int64 = 100
	reflectType(b) //type:int64
}
```

#### Name()与Kind()

在反射中关于类型还划分为两种：`类型（Type）`和`种类（Kind）`。因为在Go语言中我们可以使用type关键字构造很多自定义类型，而`种类（Kind）`就是指底层的类型，但在反射中，当需要区分指针、结构体等大品种的类型时，就会用到`种类（Kind）`。 举个例子，我们定义了两个指针类型和两个结构体类型，通过反射查看它们的类型和种类：

```go
type myInt int64

func reflectType(x interface{}) {
	t := reflect.TypeOf(x)
	fmt.Printf("typeName:%v  kind:%v\n", t.Name(), t.Kind())
}

func main() {
	var a *float32 // 指针
	var b myInt    // 自定义类型
	var c rune     // 类型别名(int32)
	reflectType(a) //typeName:  kind:ptr
	reflectType(b) //typeName:myInt kind:int64
	reflectType(c) //typeName:int32 kind:int32

	type person struct {
		name string
		age  int
	}
	var d = person{"孙悟空", 500}

	type book struct{ title string }
	var e = book{"《西游记》"}

	reflectType(d) // typeName:person kind:struct
	reflectType(e) // typeName:book kind:struct
}
```

Go语言的反射中像数组、切片、Map、指针等类型的变量，它们的`.Name()`都是返回`空`/`""`

在`reflect`包中定义的Kind类型如下，Kind代表Type类型值表示的具体分类。零值表示非法分类：

```go
type Kind uint
const (
    Invalid Kind = iota  // 非法类型
    Bool                 // 布尔型
    Int                  // 有符号整型
    Int8                 // 有符号8位整型
    Int16                // 有符号16位整型
    Int32                // 有符号32位整型
    Int64                // 有符号64位整型
    Uint                 // 无符号整型
    Uint8                // 无符号8位整型
    Uint16               // 无符号16位整型
    Uint32               // 无符号32位整型
    Uint64               // 无符号64位整型
    Uintptr              // 指针
    Float32              // 单精度浮点数
    Float64              // 双精度浮点数
    Complex64            // 64位复数类型
    Complex128           // 128位复数类型
    Array                // 数组
    Chan                 // 通道
    Func                 // 函数
    Interface            // 接口
    Map                  // 映射
    Ptr                  // 指针
    Slice                // 切片
    String               // 字符串
    Struct               // 结构体
    UnsafePointer        // 底层指针
)
```



### reflect.Value

#### ValueOf

`reflect.ValueOf()`返回的是`reflect.Value`类型，其中包含了原始值的值信息。`reflect.Value`与原始值之间可以互相转换。

```go
func ValueOf(i interface{}) Value
//ValueOf返回一个初始化为i接口保管的具体值的Value，ValueOf(nil)返回Value零值。
```

`reflect.Value`类型提供的**获取原始值**的方法如下：

|            方法            |                             说明                             |
| :------------------------: | :----------------------------------------------------------: |
| `Interface() interface {}` | 将值以`interface{}`类型返回，可以通过类型断言转换为指定类型  |
|       `Int() int64`        |     将值以`int`类型返回，所有有符号整型均可以此方式返回      |
|      `Uint() uint64`       |     将值以`uint`类型返回，所有无符号整型均可以此方式返回     |
|     `Float() float64`      | 将值以双精度(`float64`类型返回)，所有浮点数（`float32`、`float64`）均可以此方式返回 |
|       `Bool() bool`        |                     将值以`bool`类型返回                     |
|     `Bytes() []bytes`      |               将值以字节数组`[]bytes`类型返回                |
|     `String() string`      |                     将值以字符串类型返回                     |

```go
func main() {
	// 将int类型的原始值转换为reflect.Value类型
	a := reflect.ValueOf(10)
	// 将float32 类型的原始值转换为reflect.Value类型
	var v float32 = 3.14
	b := reflect.ValueOf(v)

	fmt.Printf("type a : %T\n", a) //type a : reflect.Value
	fmt.Printf("type b : %T\n", b) //type b : flect.Value
}
```



#### 通过反射获取值

```go
func reflectValue(x interface{}) {
	v := reflect.ValueOf(x)
	k := v.Kind()
	switch k {
	case reflect.Int32:
		//v.Int()从反射中获取整型的原始值(int64)，然后通过int32()强制类型转换
		fmt.Printf("type is int32, value is %d\n", int32(v.Int()))
	case reflect.Float32:
		//v.Int()从反射中获取浮点型的原始值(float64)，然后通过float32()强制类型转换
		fmt.Printf("type is float32, value is %f\n", float32(v.Float()))
	}
}

func main() {
	var a float32 = 3.14
	var b int32 = 100
	reflectValue(a) // type is float32, value is 3.140000
	reflectValue(b) // type is int32, value is 100
}
```



#### 通过反射设置变量的值

想要在函数中通过反射修改变量的值，需要注意函数参数传递的是值拷贝，必须传递变量地址才能修改变量值。而反射中使用专有的`Elem()`方法来获取指针对应的值。

```go
func reflectSetValue(x interface{}) {
	v := reflect.ValueOf(x)
	//if v.Kind() == reflect.Int64{
	//	v.SetInt(200)	//修改的是副本，reflect包会引发panic
	//}
	if v.Elem().Kind() == reflect.Int64 {
		v.Elem().SetInt(200)
	}
}

func main() {
	var a int64 = 100
	reflectValue(&a)
	fmt.Println("修改值后的a：", a) // 修改值后的a：100
}
```



#### isNil()和isValid()

```go
func (v Value) IsNil() bool
/*
IsNil报告v持有的值是否为nil。v持有的值的分类必须是通道、函数、接口、映射、指针、切片之一；否则IsNil函数会导致panic。注意IsNil并不总是等价于go语言中值与nil的常规比较。例如：如果v是通过使用某个值为nil的接口调用ValueOf函数创建的，v.IsNil()返回真，但是如果v是Value零值，会panic。
*/

func (v Value) IsValid() bool
/*
IsValid返回v是否持有一个值。如果v是Value零值会返回假，此时v除了IsValid、String、Kind之外的方法都会导致panic。绝大多数函数和方法都永远不返回Value零值。如果某个函数/方法返回了非法的Value，它的文档必须显式的说明具体情况。
*/
```

- `IsNil()`常被用于判断**指针是否为空**。
- `IsValid()`常被用于判定**返回值是否有效**。

```go
func main() {
	// int类型空指针
	var a *int
	fmt.Println("var a *int isNil: ", reflect.ValueOf(a).IsNil())
	// nil值
	fmt.Println("nil isValid: ", reflect.ValueOf(nil).IsValid())
}
/*输出：
var a *int isNil:  true
nil isValid:  false
*/
```



#### 其他方法：

```go
func (v Value) FieldByName(name string) Value
/*
返回该类型名为name的字段（的Value封装）（会查找匿名字段及其子字段），如果v的Kind不是Struct会panic；如果未找到会返回Value零值。
*/

func (v Value) MethodByName(name string) Value
/*
返回v的名为name的方法的已绑定（到v的持有值的）状态的函数形式的Value封装。返回值调用Call方法时不应包含接收者；返回值持有的函数总是使用v的持有者作为接收者（即第一个参数）。如果未找到该方法，会返回一个Value零值。
*/

func (v Value) MapIndex(key Value) Value
/*
返回v持有值里key持有值为键对应的值的Value封装。如果v的Kind不是Map会panic。如果未找到对应值或者v持有值是nil映射，会返回Value零值。key的持有值必须可以直接赋值给v持有值类型的键类型。
*/

func (v Value) Type() Type
// 返回v持有的值的类型的Type表示。

func (v Value) Kind() Kind
// Kind返回v持有的值的分类，如果v是Value零值，返回值为Invalid

func (v Value) Elem() Value
/*
Elem返回v持有的接口保管的值的Value封装，或者v持有的指针指向的值的Value封装。如果v的Kind不是Interface或Ptr会panic；如果v持有的值为nil，会返回Value零值。
*/

func (v Value) Field(i int) Value
// 返回结构体的第i个字段（的Value封装）。如果v的Kind不是Struct或i出界会panic


```

```go
func main() {
	// 实例化一个匿名结构体
	a := struct {
		Name string
	}{"tom"}
	// 尝试从结构体中查找"abc"字段
	v := reflect.ValueOf(a).FieldByName("Name")
	fmt.Println("是否存在结构体成员Name:", v.IsValid(), ",其值为：", v)
	// 尝试从结构体中查找"abc"方法
	fmt.Println("是否存在结构体方法GetName:", reflect.ValueOf(a).MethodByName("GetName").IsValid())
	// map
	b := map[string]int{}
	// 尝试从map中查找一个不存在的键
	fmt.Println("map中是否存在键city：", reflect.ValueOf(b).MapIndex(reflect.ValueOf("city")).IsValid())
}
/*输出：
是否存在结构体成员Name: true ,其值为： tom
是否存在结构体方法GetName: false
map中是否存在键city： false
*/
```



## 结构体反射

### 基本方法

任意值通过`reflect.TypeOf()`获得反射对象信息后，如果它的类型是结构体，可以通过反射值对象（`reflect.Type`）的`NumField()`和`Field()`方法获得结构体成员的详细信息。

**`reflect.Type`中与获取结构体成员相关的的方法如下表所示：**

|                             方法                             |                             说明                             |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
|                  `Field(i int) StructField`                  |          根据索引，返回索引对应的结构体字段的信息。          |
|                       `NumField() int`                       |                   返回结构体成员字段数量。                   |
|        `FieldByName(name string) (StructField, bool)`        |       根据给定字符串返回字符串对应的结构体字段的信息。       |
|           `FieldByIndex(index []int) StructField`            | 多层成员访问时，根据 []int 提供的每个结构体的字段索引，返回字段的信息。 |
| `FieldByNameFunc(match func(string) bool) (StructField,bool)` |              根据传入的匹配函数匹配需要的字段。              |
|                      `NumMethod() int`                       |               返回该类型的方法集中方法的数目。               |
|                     `Method(int) Method`                     |               返回该类型方法集中的第i个方法。                |
|             `MethodByName(string)(Method, bool)`             |             根据方法名返回该类型方法集中的方法。             |



**`reflect.Value`中与获取结构体成员相关的的方法如下表所示：**

|                       方法                       |                             说明                             |
| :----------------------------------------------: | :----------------------------------------------------------: |
|         `func (v Value) NumMethod() int`         |               返回v持有值的方法集的方法数目。                |
|       `func (v Value) Method(i int) Value`       | 返回v持有值类型的第i个方法的已绑定（到v的持有值的）状态的函数形式的Value封装 |
| `func (v Value) MethodByName(name string) Value` | 返回v的名为name的方法的已绑定（到v的持有值的）状态的函数形式的Value封装。 |
|                       ...                        |                             ...                              |



### StructField类型

`StructField`类型用来描述结构体中的一个字段的信息。

```go
type StructField struct {
    // Name是字段的名字。PkgPath是非导出字段的包路径，对导出字段该字段为""。
    // 参见http://golang.org/ref/spec#Uniqueness_of_identifiers
    Name    string
    PkgPath string
    Type      Type      // 字段的类型
    Tag       StructTag // 字段的标签
    Offset    uintptr   // 字段在结构体中的字节偏移量
    Index     []int     // 用于Type.FieldByIndex时的索引切片
    Anonymous bool      // 是否匿名字段
}
```



### 结构体反射实例

当我们使用反射得到一个结构体数据之后可以通过索引依次获取其字段信息，也可以通过字段名去获取指定的字段信息。

```go
package main

import (
	"fmt"
	"reflect"
)

type student struct {
	Name  string `json:"stu_name"`
	Score int    `json:"stu_score"`
}

// 给 student 添加两个方法 Study 和 Sleep

func (s student) Study() string {
	msg := "学习使我快乐！"
	fmt.Printf(msg)
	return msg
}

func (s student) Sleep() string {
	msg := "早睡觉，身体好！"
	fmt.Println(msg)
	return msg
}

func printMethod(x interface{}) {
	// 遍历打印x包含的方法
	t := reflect.TypeOf(x)
	v := reflect.ValueOf(x)
	fmt.Println("x 含有的方法数量：", t.NumMethod())
	//因为下面需要拿到具体的方法去调用，所以使用的是指信息
	for i := 0; i < v.NumMethod(); i++ {
		methodType := v.Method(i).Type()
		fmt.Printf("method name: %s, method: %s\n", t.Method(i).Name, methodType)
		// 通过反射调用方法传递的参数必须是 []reflect.Value 类型
		var args = []reflect.Value{}
		v.Method(i).Call(args)
	}
}

func main() {
	stu1 := student{"孙悟空", 90}
	t := reflect.TypeOf(stu1)
	fmt.Printf("stu1 type: %v, kind: %v\n", t.Name(), t.Kind())
	// 通过for循环遍历结构体的所以字段信息
	fmt.Println("通过for循环遍历结构体的所以字段信息：")
	for i := 0; i < t.NumField(); i++ {
		field := t.Field(i) // 通过索引，返回索引对应的结构体字段的信息
		fmt.Printf("index:%v, name:%v, type:%v, json tag:%v\n", field.Index, field.Name, field.Type, field.Tag)
	}

	//通过字段名获取指定结构体字段信息
	fmt.Println("通过字段名获取指定结构体字段信息：")
	if nameField, ok := t.FieldByName("Name"); ok {
		fmt.Printf("index:%v, name:%v, type:%v, json tag:%v\n", nameField.Index, nameField.Name, nameField.Type, nameField.Tag)
	}
	if scoreField, ok := t.FieldByName("Score"); ok {
		fmt.Printf("index:%v, name:%v, type:%v, json tag:%v\n", scoreField.Index, scoreField.Name, scoreField.Type, scoreField.Tag)
	}

	// 遍历打印s包含的方法
	printMethod(stu1)
}
```



## 反射案例

1. 对基本数据类型、interface{}、reflect.Value进行相互转换

	```go
	func reflectTest1(x interface{}) {
		// 通过反射获取传入的变量的type，kind以及值
		xType := reflect.TypeOf(x) // 获取到 reflect.Type
		fmt.Println("xType= ", xType)
		xValue := reflect.ValueOf(x) //获取到 reflect.Value
		newXValue := 2 + xValue.Int()
		fmt.Printf("xValue= %v , newXValue= %v\n", xValue, newXValue)
		// 将 xValue 转换成 interface{}
		interValue := xValue.Interface()
		// 将interface{}通过断言转成需要的类型
		num := interValue.(int)
		fmt.Println("num=", num)
	}
	
	func main() {
		var x int = 100
		reflectTest1(x)
	}
	/*输出：
	xType=  int
	xValue= 100 , newXValue= 102
	num= 100
	*/
	```

2. 使用反射来遍历结构体的字段，调用结构体的方法，并获取结构体标签的值：

	```go
	package main
	
	import (
		"fmt"
		"reflect"
	)
	
	type Student struct {
		Name  string  `json:"stu_name"`
		Age   int     `json:"stu_age"`
		Score float32 `json:"成绩"`
		Sex   string
	}
	
	func (s Student) GetSum(n1 int, n2 int) int {
		// 方法一：返回两个数的和
		return n1 + n2
	}
	
	func (s *Student) SetStudent(name string, age int, score float32, sex string) {
		// 方法二：接收四个值，给s赋值
		s.Name = name
		s.Age = age
		s.Score = score
		s.Sex = sex
	}
	
	func (s Student) ShowInfo() {
		// 显示s的值
		fmt.Println("-----start-----")
		fmt.Println(s)
		fmt.Println("-----end-----")
	}
	
	func TestStruct(a interface{}) {
		// 获取reflect.Type类型
		aType := reflect.TypeOf(a)
		// 获取reflect.Value类型
		aValue := reflect.ValueOf(a)
		// 获取a对应的类别kind
		aKind := aValue.Kind()
		// 如果传入的不是struct就退出
		if aKind != reflect.Struct {
			fmt.Println("expect struct")
			return
		}
		// 如果传入的是struct，就进行如下操作：
		// 获取该结构体有几个字段
		fieldNum := aValue.NumField()
		fmt.Printf("this struct has %d fields\n", fieldNum)
	
		// 遍历结构体的所有字段
		for i := 0; i < fieldNum; i++ {
			fmt.Printf("Field %d, 值= %v\n", i, aValue.Field(i))
			// 获取到struct标签，注意需要通过reflect.Type来获取tag标签的值
			tagValue := aType.Field(i).Tag.Get("json")
			// 如果该字段有tag标签就显示，否则就不显示
			if tagValue != "" {
				fmt.Printf("Field %d, tag= %v\n", i, tagValue)
			}
		}
	
		// 获取到该结构体有多少个方法
		numOfMethod := aValue.NumMethod() // numOfMethod=2，虽然struct有三个方法，但其中一个是绑定的struct指针
		fmt.Printf("\nthis struct has %d methods\n", numOfMethod)
	
		// 注意：方法的排序默认是按照函数名的排序（ASCII码）
		//调用结构体的第一个方法
		var params []reflect.Value
		params = append(params, reflect.ValueOf(10), reflect.ValueOf(20))
		//调动结构体的第一个方法，即GetSum()，参数n1,n2需要使用[]reflect.Value类型来传入，返回的结果也是[]reflect.Value
		res := aValue.Method(0).Call(params)
		fmt.Println("method 1 result: ", res[0].Int())
	
		//调用结构体第三个方法打印结构体信息
		fmt.Println("method 2 result: ")
		aValue.Method(1).Call(make([]reflect.Value, 0))
	
	}
	
	func main() {
		var stu Student = Student{}
		stu.SetStudent("tom", 22, 90.5, "男")
		TestStruct(stu)
	}
	/*输出：
	this struct has 4 fields
	Field 0, 值= tom
	Field 0, tag= stu_name
	Field 1, 值= 22
	Field 1, tag= stu_age
	Field 2, 值= 90.5
	Field 2, tag= 成绩
	Field 3, 值= 男
	
	this struct has 2 methods
	method 1 result:  30
	method 2 result: 
	-----start-----
	{tom 22 90.5 男}
	-----end-----
	*/
	```

	

# 并发安全与锁

## 数据竞争

有时候代码中可能会存在多个 goroutine 同时操作一个资源（临界区）的情况，这种情况下就会发生`竞态问题`（数据竞态）。这就好比现实生活中十字路口被各个方向的汽车竞争，还有火车上的卫生间被车厢里的人竞争。下面演示一个数据竞争的示例：

```go
package main

import (
	"fmt"
	"sync"
)

var (
	x  int64
	wg sync.WaitGroup //等待组
)

// add 对全局变量x执行5000次加1操作
func add() {
	for i := 0; i < 5000; i++ {
		x = x + 1
	}
	wg.Done()
}

func main() {
	wg.Add(2)
	go add()
	go add()
	wg.Wait()
	fmt.Println(x)
}
```

上面代码执行后，每次执行的结果都不同，原因是开启了两个`goroutine`分别执行`add`函数，这两个`goroutine`在访问和修改全局的x变量时就会存在数据竞争，某个`goroutine`中对全局变量x的修改可能会覆盖掉另一个`goroutine`中的操作，所以导致最后的结果与预期不符合。

如何解决这种存在资源竞争的问题呢？

## 互斥锁

互斥锁是一种常用的控制共享资源访问的方法，它能够保证同一时间只有一个 goroutine 可以访问共享资源。Go 语言中使用`sync`包中提供的`Mutex`类型来实现互斥锁。

`sync.Mutex`提供了两个方法供我们使用。

|           方法名           |                             功能                             |
| :------------------------: | :----------------------------------------------------------: |
|  `func (m *Mutex) Lock()`  |       Lock方法锁住m，如果m已经加锁，则阻塞直到m解锁。        |
| `func (m *Mutex) Unlock()` | Unlock方法解锁m，如果m未加锁会导致运行时错误。锁和线程无关，可以由不同的线程加锁和解锁。 |

下面的示例代码中使用互斥锁限制每次只有一个 `goroutine `才能修改全局变量`x`，从而修复上面代码中的问题。

```go
package main

import (
	"fmt"
	"sync"
)

var (
	x  int64
	wg sync.WaitGroup //等待组
	m  sync.Mutex     // 互斥锁
)

// add 对全局变量x执行5000次加1操作
func add() {
	for i := 0; i < 5000; i++ {
		m.Lock() // 修改x前加锁
		x = x + 1
		m.Unlock() // 修改后解锁
	}
	wg.Done()
}

func main() {
	wg.Add(2)
	go add()
	go add()
	wg.Wait()
	fmt.Println(x)
}
```

上面代码多次执行后，每一次都会得到预期的结果：10000

使用互斥锁能够保证同一时间有且只有一个 `goroutine` 进入临界区，其他的 `goroutine` 则在等待锁；当互斥锁释放后，等待的 `goroutine` 才可以获取锁进入临界区，多个 `goroutine` 同时等待一个锁时，唤醒的策略是随机的。



## 读写互斥锁

互斥锁是完全互斥的，但是实际上有很多场景是读多写少的，当我们并发的去读取一个资源而不涉及资源修改的时候是没有必要加互斥锁的，这种场景下使用读写锁是更好的一种选择。读写锁在 Go 语言中使用`sync`包中的`RWMutex`类型。

`sync.RWMutex`提供了以下5个方法：

|                方法名                 |                             功能                             |
| :-----------------------------------: | :----------------------------------------------------------: |
|      `func (rw *RWMutex) Lock()`      |    Lock方法将rw锁定为写入状态，禁止其他线程读取或者写入。    |
|     `func (rw *RWMutex) Unlock()`     | Unlock方法解除rw的写入锁状态，如果m未加写入锁会导致运行时错误。 |
|     `func (rw *RWMutex) RLock()`      | RLock方法将rw锁定为读取状态，禁止其他线程写入，但不禁止读取。 |
|    `func (rw *RWMutex) RUnlock()`     | Runlock方法解除rw的读取锁状态，如果m未加读取锁会导致运行时错误。 |
| `func (rw *RWMutex) RLocker() Locker` | Rlocker方法返回一个互斥锁，通过调用rw.Rlock和rw.Runlock实现了Locker接口。 |

读写锁分为两种：读锁和写锁。当一个 goroutine 获取到读锁之后，其他的 goroutine 如果是获取读锁会继续获得锁，如果是获取写锁就会等待；而当一个 goroutine 获取写锁之后，其他的 goroutine 无论是获取读锁还是写锁都会等待。

下面使用代码构造一个读多写少的场景，然后分别使用互斥锁和读写锁查看它们的性能差异：

```GO
package main

import (
	"fmt"
	"sync"
	"time"
)

var (
	x       int64
	wg      sync.WaitGroup //等待组
	mutex   sync.Mutex     // 互斥锁
	rwMutex sync.RWMutex   // 读写锁
)

func writeWithLock() {
	// 使用互斥锁模拟写操作
	mutex.Lock() // 加互斥锁
	x = x + 1
	time.Sleep(10 * time.Millisecond) // 假设读操作耗时10毫秒
	mutex.Unlock()                    // 释放互斥锁
	wg.Done()
}

func readWithLock() {
	// 使用互斥锁模拟读操作
	mutex.Lock()                // 加互斥锁
	time.Sleep(time.Nanosecond) // 假设读操作耗时1毫秒
	mutex.Unlock()              // 释放互斥锁
	wg.Done()
}

func writeWithRWLock() {
	// 使用读写互斥锁模拟写操作
	rwMutex.Lock() // 加写锁（不可读写）
	x = x + 1
	time.Sleep(10 * time.Millisecond) // 假设读操作耗时10毫秒
	rwMutex.Unlock()                  //释放写锁
	wg.Done()
}

func readWithRWLock() {
	// 使用读写互斥锁模拟读操作
	rwMutex.RLock()             //加读锁（禁止写入，可以读取）
	time.Sleep(time.Nanosecond) // 假设读操作耗时1毫秒
	rwMutex.RUnlock()           // 释放读锁
	wg.Done()
}

func do(wf, rf func(), wc, rc int) {
	start := time.Now()
	// wc 个并发写操作
	for i := 0; i < wc; i++ {
		wg.Add(1)
		go wf()
	}
	// rc个并发读操作
	for i := 0; i < rc; i++ {
		wg.Add(1)
		go rf()
	}
	wg.Wait()
	cost := time.Since(start)
	fmt.Printf("x: %v , cost: %v\n", x, cost)
}
```





```go
func main() {
	// 读操作和写操作数量级差别大的时候
	// 使用互斥锁，10此并发写，1000并发读
	do(writeWithLock, readWithLock, 10, 1000)
	x = 0
	// 使用读写互斥锁，10次并发写，1000次并发读
	do(writeWithRWLock, readWithRWLock, 10, 1000)
	x = 0

	// 读操作和写操作数量级差别不大的时候
	do(writeWithLock, readWithLock, 100, 100)
	x = 0
	// 使用读写互斥锁，10次并发写，1000次并发读
	do(writeWithRWLock, readWithRWLock, 100, 100)
}
/*输出：
x: 10 , cost: 15.6513644s
x: 10 , cost: 170.0309ms
x: 1000 , cost: 31.0239713s
x: 1000 , cost: 15.5804944s
*/
```

从最终的执行结果可以看出，使用读写互斥锁在读多写少的场景下能够极大地提高程序的性能。不过需要注意的是如果一个程序中的读操作和写操作数量级差别不大，那么读写互斥锁的优势就发挥不出来。



## sync.WaitGroup

在代码中生硬的使用`time.Sleep`肯定是不合适的，Go语言中可以使用`sync.WaitGroup`来实现并发任务的同步。 `sync.WaitGroup`有以下几个方法：

|                 方法名                 |                             功能                             |
| :------------------------------------: | :----------------------------------------------------------: |
| `func (wg * WaitGroup) Add(delta int)` | Add方法向内部计数加上delta，delta可以是负数；如果内部计数器变为0，Wait方法阻塞等待的所有线程都会释放，如果计数器小于0，方法panic。注意Add加上正数的调用应在Wait之前，否则Wait可能只会等待很少的线程。一般来说本方法应在创建新的线程或者其他应等待的事件之前调用。 |
|     `func (wg *WaitGroup) Done()`      |    Done方法减少WaitGroup计数器的值，应在线程的最后执行。     |
|     `func (wg *WaitGroup) Wait()`      |            Wait方法阻塞直到WaitGroup计数器减为0。            |

`sync.WaitGroup`内部维护着一个计数器，计数器的值可以增加和减少。例如当我们启动了 N 个并发任务时，就将计数器值增加N。每个任务完成时通过调用 Done 方法将计数器减1。通过调用 Wait 来等待并发任务执行完，当计数器值为 0 时，表示所有并发任务已经完成。

**需要注意`sync.WaitGroup`是一个结构体，进行参数传递的时候要传递指针。**

**不使用`sync.WaitGroup`：**

```go
package main

import (
	"fmt"
)

func hello() {
	defer func() {
		fmt.Println("hello()...结束")
	}()
	for i := 1; i <= 5; i++ {
		fmt.Println("hello Goroutine: ", i)
	}
}

func show() {
	defer func() {
		fmt.Println("show()...结束")
	}()
	for i := 1; i <= 5; i++ {
		fmt.Println("show time: ", i)
	}
}

func main() {
	go hello()
	go show()
	for i := 1; i <= 2; i++ {
		fmt.Println("main()... : ", i)
	}
	defer func() {
		fmt.Println("main()...结束")
	}()
}
/*输出：
hello Goroutine:  1
hello Goroutine:  2
hello Goroutine:  3
hello Goroutine:  4
hello Goroutine:  5
hello()...结束
main()... :  1
main()... :  2
main()...结束
show time:  1
show time:  2
show time:  3
show time:  4
*/
/*输出2：
main()... :  1
hello Goroutine:  1
hello Goroutine:  2
main()... :  2
main()...结束
hello Goroutine:  3
hello Goroutine:  4
*/
```

上述代码运行结果经常会出现`main`程序结束，而协程并没有输出完。为了解决这种情况，可以引入`sync.WaitGroup`：

```go
package main

import (
	"fmt"
	"sync"
)

var wg sync.WaitGroup

func hello() {
	defer func() {
		fmt.Println("hello()...结束")
		wg.Done()
	}()
	for i := 1; i <= 5; i++ {
		fmt.Println("hello Goroutine: ", i)
	}
}

func show() {
	defer func() {
		fmt.Println("show()...结束")
		wg.Done()
	}()
	for i := 1; i <= 5; i++ {
		fmt.Println("show time: ", i)
	}
}

func main() {
	wg.Add(2)
	go hello()
	go show()
	for i := 1; i <= 2; i++ {
		fmt.Println("main()... : ", i)
	}
	wg.Wait()
	defer func() {
		fmt.Println("main()...结束")
	}()
}
/*输出：
hello Goroutine:  1
hello Goroutine:  2
show time:  1
show time:  2
show time:  3
show time:  4
show time:  5
show()...结束
main()... :  1
hello Goroutine:  3
hello Goroutine:  4
hello Goroutine:  5
hello()...结束
main()... :  2
main()...结束
*/
```

引入`sync.WaitGroup`后，`wg.Wait()`会一直阻塞`main()`结束进程，直到`sync.WaitGroup`内部计数器为0，则表示所有`wg.Add()`添加的并发任务已经全部完成。



## sync.Once



在某些场景下我们需要确保某些操作即使在高并发的场景下也只会被执行一次，例如只加载一次配置文件等。

Go语言中的`sync`包中提供了一个针对只执行一次场景的解决方案——`sync.Once`，`sync.Once`只有一个`Do`方法，其签名如下：

```go
func (o *Once) Do(f func())
```

Do方法当且仅当第一次被调用时才执行函数f。换句话说，给定变量：

```go
var once Once
```

如果once.Do(f)被多次调用，只有第一次调用会执行f，即使f每次调用Do 提供的f值不同。需要给每个要执行仅一次的函数都建立一个Once类型的实例。

Do用于必须刚好运行一次的初始化。因为f是没有参数的，因此可能需要**使用闭包**来提供给Do方法调用。



**加载配置文件示例：**

延迟一个开销很大的初始化操作到真正用到它的时候再执行是一个很好的实践。因为预先初始化一个变量（比如在init函数中完成初始化）会增加程序的启动耗时，而且有可能实际执行过程中这个变量没有用上，那么这个初始化操作就不是必须要做的。我们来看一个例子：

```go
var icons map[string]image.Image

func loadIcons() {
	icons = map[string]image.Image{
		"left":  loadIcon("left.png"),
		"up":    loadIcon("up.png"),
		"right": loadIcon("right.png"),
		"down":  loadIcon("down.png"),
	}
}

// Icon 被多个goroutine调用时不是并发安全的
func Icon(name string) image.Image {
	if icons == nil {
		loadIcons()
	}
	return icons[name]
}
```

多个 goroutine 并发调用Icon函数时不是并发安全的，现代的编译器和CPU可能会在保证每个 goroutine 都满足串行一致的基础上自由地重排访问内存的顺序。loadIcons函数可能会被重排为以下结果：

```go
func loadIcons() {
	icons = make(map[string]image.Image)
	icons["left"] = loadIcon("left.png")
	icons["up"] = loadIcon("up.png")
	icons["right"] = loadIcon("right.png")
	icons["down"] = loadIcon("down.png")
}
```

在这种情况下就会出现即使判断了`icons`不是nil也不意味着变量初始化完成了。考虑到这种情况，我们能想到的办法就是添加互斥锁，保证初始化`icons`的时候不会被其他的 goroutine 操作，但是这样做又会引发性能问题。

使用`sync.Once`改造的示例代码如下：

```go
var icons map[string]image.Image

var loadIconsOnce sync.Once

func loadIcons() {
	icons = map[string]image.Image{
		"left":  loadIcon("left.png"),
		"up":    loadIcon("up.png"),
		"right": loadIcon("right.png"),
		"down":  loadIcon("down.png"),
	}
}

// Icon 是并发安全的
func Icon(name string) image.Image {
	loadIconsOnce.Do(loadIcons)
	return icons[name]
}
```



**并发安全的单例模式：**

下面是借助`sync.Once`实现的并发安全的单例模式：

```go
package singleton

import (
    "sync"
)

type singleton struct {}

var instance *singleton
var once sync.Once

func GetInstance() *singleton {
    once.Do(func() {
        instance = &singleton{}
    })
    return instance
}
```

`sync.Once`其实内部包含一个互斥锁和一个布尔值，互斥锁保证布尔值和数据的安全，而布尔值用来记录初始化是否完成。这样设计就能保证初始化操作的时候是并发安全的并且初始化操作也不会被执行多次。



## sync.Map

Go 语言中内置的 map 不是并发安全的，请看下面这段示例代码：

```go
package main

import (
	"fmt"
	"strconv"
	"sync"
)

var m = make(map[string]int)

func get(key string) int {
	return m[key]
}

func set(key string, value int) {
	m[key] = value
}

func main() {
	wg := sync.WaitGroup{}
	for i := 0; i < 10; i++ {
		wg.Add(1)
		go func(n int) {
			key := strconv.Itoa(n)
			set(key, n)
			fmt.Printf("k=:%v,v:=%v\n", key, get(key))
			wg.Done()
		}(i)
	}
	wg.Wait()
}
```

将上面的代码编译后执行，会报出`fatal error: concurrent map writes`错误。**我们不能在多个 `goroutine` 中并发对内置的 `map` 进行读写操作，否则会存在数据竞争问题。**

像这种场景下就需要为 map 加锁来保证并发的安全性了，Go语言的`sync`包中提供了一个开箱即用的并发安全版 map——`sync.Map`。开箱即用表示其不用像内置的 map 一样使用 make 函数初始化就能直接使用。同时`sync.Map`内置了诸如`Store`、`Load`、`LoadOrStore`、`Delete`、`Range`等操作方法。

|                            方法名                            |              功能               |
| :----------------------------------------------------------: | :-----------------------------: |
|        `func (m *Map) Store(key, value interface{})`         |        存储key-value数据        |
| `func (m *Map) Load(key interface{}) (value interface{}, ok bool)` |       查询key对应的value        |
| `func (m *Map) LoadOrStore(key, value interface{}) (actual interface{}, loaded bool)` |    查询或存储key对应的value     |
| `func (m *Map) LoadAndDelete(key interface{}) (value interface{}, loaded bool)` |          查询并删除key          |
|           `func (m *Map) Delete(key interface{})`            |             删除key             |
|  `func (m *Map) Range(f func(key, value interface{}) bool)`  | 对map中的每个key-value依次调用f |

下面的代码示例演示了并发读写`sync.Map`：

```go
package main

import (
	"fmt"
	"strconv"
	"sync"
)

var m = sync.Map{}

func main() {
	wg := sync.WaitGroup{}
	// 对m执行20个并发的读写操作
	for i := 0; i < 20; i++ {
		wg.Add(1)
		go func(n int) {
			key := strconv.Itoa(n)
			m.Store(key, n)         // 存储key-value
			value, _ := m.Load(key) //根据key取值
			fmt.Printf("k=:%v,v:=%v\n", key, value)
			wg.Done()
		}(i)
	}
	wg.Wait()
}
```



## 原子操作

针对整数数据类型（int32、uint32、int64、uint64）我们还可以使用原子操作来保证并发安全，通常直接使用原子操作比使用锁操作效率更高。Go语言中原子操作由内置的标准库`sync/atomic`提供。

### atomic包

#### 读取操作：

|                             方法                             |                说明                |
| :----------------------------------------------------------: | :--------------------------------: |
|          `func LoadInt32(addr *int32) (val int32)`           |  LoadInt32原子性的获取*addr的值。  |
|          `func LoadInt64(addr *int64) (val int64)`           |  LoadInt64原子性的获取*addr的值。  |
|         `func LoadUint32(addr *uint32) (val uint32)`         | LoadUint32原子性的获取*addr的值。  |
|         `func LoadUint64(addr *uint64) (val uint64)`         | LoadUint64原子性的获取*addr的值。  |
|       `func LoadUintptr(addr *uintptr) (val uintptr)`        | LoadUintptr原子性的获取*addr的值。 |
| `func LoadPointer(addr *unsafe.Pointer) (val unsafe.Pointer)` | LoadPointer原子性的获取*addr的值。 |



#### 写入操作：

|                             方法                             |                    说明                    |
| :----------------------------------------------------------: | :----------------------------------------: |
|          `func StoreInt32(addr *int32, val int32)`           |  StoreInt32原子性的将val的值保存到*addr。  |
|          `func StoreInt64(addr *int64, val int64)`           |  StoreInt64原子性的将val的值保存到*addr。  |
|         `func StoreUint32(addr *uint32, val uint32)`         | StoreUint32原子性的将val的值保存到*addr。  |
|         `func StoreUint64(addr *uint64, val uint64)`         | StoreUint64原子性的将val的值保存到*addr。  |
|       `func StoreUintptr(addr *uintptr, val uintptr)`        | StoreUintptr原子性的将val的值保存到*addr。 |
| `func StorePointer(addr *unsafe.Pointer, val unsafe.Pointer)` | StorePointer原子性的将val的值保存到*addr。 |



#### 修改操作：

|                             方法                             |                             说明                             |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
|    `func AddInt32(addr *int32, delta int32) (new int32)`     |      AddInt32原子性的将delta的值添加到*addr并返回新值。      |
|    `func AddInt64(addr *int64, delta int64) (new int64)`     |      AddInt64原子性的将delta的值添加到*addr并返回新值。      |
|  `func AddUint32(addr *uint32, delta uint32) (new uint32)`   | AddUint32原子性的将delta的值添加到*addr并返回新值。如要减去一个值c，调用AddUint32(&x, ^uint32(c-1))；特别的，让x减1，调用AddUint32(&x, ^uint32(0))。 |
|  `func AddUint64(addr *uint64, delta uint64) (new uint64)`   |     AddUint64原子性的将delta的值添加到*addr并返回新值。      |
| `func AddUintptr(addr *uintptr, delta uintptr) (new uintptr)` |     AddUintptr原子性的将delta的值添加到*addr并返回新值。     |



#### 交换操作：

|                             方法                             |                       说明                       |
| :----------------------------------------------------------: | :----------------------------------------------: |
|     `func SwapInt32(addr *int32, new int32) (old int32)`     |  SwapInt32原子性的将新值保存到*addr并返回旧值。  |
|     `func SwapInt64(addr *int64, new int64) (old int64)`     |  SwapInt64原子性的将新值保存到*addr并返回旧值。  |
|   `func SwapUint32(addr *uint32, new uint32) (old uint32)`   | SwapUint32原子性的将新值保存到*addr并返回旧值。  |
|   `func SwapUint64(addr *uint64, new uint64) (old uint64)`   | SwapUint64原子性的将新值保存到*addr并返回旧值。  |
| `func SwapUintptr(addr *uintptr, new uintptr) (old uintptr)` | SwapUintptr原子性的将新值保存到*addr并返回旧值。 |
| `func SwapPointer(addr *unsafe.Pointer, new unsafe.Pointer) (old unsafe.Pointer)` | SwapPointer原子性的将新值保存到*addr并返回旧值。 |



#### 比较并交换操作：

|                             方法                             |                             说明                             |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| `func CompareAndSwapInt32(addr *int32, old, new int32) (swapped bool)` | CompareAndSwapInt32原子性的比较\*addr和old，如果相同则将new赋值给\*addr并返回真。 |
| `func CompareAndSwapInt64(addr *int64, old, new int64) (swapped bool)` | CompareAndSwapInt64原子性的比较\*addr和old，如果相同则将new赋值给\*addr并返回真。 |
| `func CompareAndSwapUint32(addr *uint32, old, new uint32) (swapped bool)` | CompareAndSwapUint32原子性的比较\*addr和old，如果相同则将new赋值给\*addr并返回真。 |
| `func CompareAndSwapUint64(addr *uint64, old, new uint64) (swapped bool)` | CompareAndSwapUint64原子性的比较\*addr和old，如果相同则将new赋值给\*addr并返回真。 |
| `func CompareAndSwapUintptr(addr *uintptr, old, new uintptr) (swapped bool)` | CompareAndSwapUintptr原子性的比较\*addr和old，如果相同则将new赋值给\*addr并返回真。 |
| `func CompareAndSwapPointer(addr *unsafe.Pointer, old, new unsafe.Pointer) (swapped bool)` | CompareAndSwapPointer原子性的比较\*addr和old，如果相同则将new赋值给\*addr并返回真。 |



### 示例

编写一个示例来比较下互斥锁和原子操作的性能：

```go
package main

import (
	"fmt"
	"sync"
	"sync/atomic"
	"time"
)

type Counter interface {
	Inc()
	Load() int64
}

// 普通版
type CommonCounter struct {
	counter int64
}

func (c *CommonCounter) Inc() {
	c.counter++
}

func (c *CommonCounter) Load() int64 {
	return c.counter
}

// 互斥锁版
type MutexCounter struct {
	counter int64
	lock    sync.Mutex
}

func (m *MutexCounter) Inc() {
	m.lock.Lock()
	defer m.lock.Unlock()
	m.counter++
}

func (m *MutexCounter) Load() int64 {
	m.lock.Lock()
	defer m.lock.Unlock()
	return m.counter
}

// 原子操作版
type AtomicCounter struct {
	counter int64
}

func (a *AtomicCounter) Inc() {
	atomic.AddInt64(&a.counter, 1)
}

func (a *AtomicCounter) Load() int64 {
	return atomic.LoadInt64(&a.counter)
}

func test(c Counter) {
	var wg sync.WaitGroup
	start := time.Now()
	for i := 0; i < 1000; i++ {
		wg.Add(1)
		go func() {
			c.Inc()
			wg.Done()
		}()
	}
	wg.Wait()
	cost := time.Since(start)
	fmt.Println(c.Load(), cost)
}

func main() {
	c1 := CommonCounter{} // 非并发安全
	test(&c1)
	c2 := MutexCounter{} // 使用互斥锁实现并发安全
	test(&c2)
	c3 := AtomicCounter{} // 并发安全且比互斥锁效率更高
	test(&c3)
}
/*输出：
普通版：counter:  984 , costTime:  1.1491ms
互斥锁版：counter:  1000 , costTime:  546.1µs
原子操作版：counter:  1000 , costTime:  516.2µs
*/
```

`atomic`包提供了底层的原子级内存操作，对于同步算法的实现很有用。这些函数必须谨慎地保证正确使用。除了某些特殊的底层应用，使用通道或者 sync 包的函数/类型实现同步更好。