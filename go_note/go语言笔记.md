# `Golang标准库文档：

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

```
func Fscanf(r io.Reader, format string, a ...interface{}) (n int, err error)
```

`Fscanf`从`r`扫描文本，根据`format `参数指定的格式将成功读取的空白分隔的值保存进成功传递给本函数的参数。返回成功扫描的条目个数和遇到的任何错误。

## `func Sscanf`

```
func Sscanf(str string, format string, a ...interface{}) (n int, err error)
```

`Sscanf`从字符串`str`扫描文本，根据`format `参数指定的格式将成功读取的空白分隔的值保存进成功传递给本函数的参数。返回成功扫描的条目个数和遇到的任何错误。

## `func Scan`

```
func Scan(a ...interface{}) (n int, err error)
```

`Scan`从标准输入扫描文本，将成功读取的空白分隔的值保存进成功传递给本函数的参数。换行视为空白。返回成功扫描的条目个数和遇到的任何错误。如果读取的条目比提供的参数少，会返回一个错误报告原因。

## `func Fscan`

```
func Fscan(r io.Reader, a ...interface{}) (n int, err error)
```

`Fscan`从r扫描文本，将成功读取的空白分隔的值保存进成功传递给本函数的参数。换行视为空白。返回成功扫描的条目个数和遇到的任何错误。如果读取的条目比提供的参数少，会返回一个错误报告原因。

## `func Sscan`

```
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

```
func Sscanln(str string, a ...interface{}) (n int, err error)
```

`Sscanln`类似`Sscan`，但会在换行时才停止扫描。最后一个条目后必须有换行或者到达结束位置。



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

**`switch`穿透：`fallthrough`（只能穿透一层`case`）：**

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



# 函数

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

### `time`的`Unix`和`UnixNano`方法：

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



### 计算耗时

使用`Unix`和`UnixNano`计算耗时：

```go
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

/*输出：
执行100000次字符串拼接耗费时间为 2 秒
执行100000次字符串拼接耗费时间为 2637625700 纳
*/
```



# 内置函数

## len

用来求`string`、`array`、`slice`、`map`、`channel`等的长度。

```go
n := len("hello")	// n = 5
```

## new

用来分配内存，主要用来分配值内存，比如`int`、`float64`、`struct`等，其第一个实参为类型，而非值。其返回值为指向该类型的新分配的零值的指针：`func new(Type) *Type`

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

内建函数make分配并初始化一个类型为切片、映射、或通道的对象。其第一个实参为类型，而非值。make的返回类型与其参数相同，而非指向它的指针。`func make(Type, size ...IntegerType) Type`

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

- Go中引入的处理方式为：`defer`、`panic`、`recover`

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

## 数组

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



## 切片

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
// 在使用map前，需要先make分配内存
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



## 接口（interface）



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

