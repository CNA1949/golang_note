# 笔记介绍

笔记参考来源：[Gin框架介绍及使用 | 李文周的博客 (liwenzhou.com)](https://www.liwenzhou.com/posts/Go/gin/#autoid-0-4-5)

# 安装gin框架与使用

## 安装gin

```shell
go get -u github.com/gin-gonic/gin
```

## 使用示例

```go
package main

import "github.com/gin-gonic/gin"

func main(){
	// 创建一个默认的路由引擎
	router := gin.Default()
	// GET：请求方式； /hello：请求路径
	// 当客户端以GET方法请求/hello路径时，会执行后面的匿名函数
	router.GET("/hello",func(c *gin.Context){
		// c.JSON：返回JSON格式的数据
		c.JSON(200,gin.H{
			"message":"hello world!",
		})
	})
	// 启动HTTP服务，默认在8080端口启动服务
	router.Run()
}
```

将上面的代码保存并编译执行，然后使用浏览器打开`localhost:8080/hello`就能看到一串JSON字符串。



# RESTful API

REST与技术无关，代表的是一种软件架构风格，REST是Representational State Transfer的简称，中文翻译为“表征状态转移”或“表现层状态转化”。

推荐阅读[阮一峰 理解RESTful架构](http://www.ruanyifeng.com/blog/2011/09/restful.html)

简单来说，REST的含义就是客户端与Web服务器之间进行交互的时候，使用HTTP协议中的4个请求方法代表不同的动作。

- `GET`用来获取资源。
- `POST`用来新建资源。
- `PUT`用来更新资源。
- `DELETE`用来删除资源。

只要API程序遵循了REST风格，那就可以称其为RESTful API。目前在前后端分离的架构中，前后端基本都是通过RESTful API来进行交互。

例如，我们现在要编写一个管理书籍的系统，我们可以查询对一本书进行查询、创建、更新和删除等操作，我们在编写程序的时候就要设计客户端浏览器与我们Web服务端交互的方式和路径。按照经验我们通常会设计成如下模式：

| 请求方法 |     URL      |     含义     |
| :------: | :----------: | :----------: |
|   GET    |    /book     | 查询书籍信息 |
|   POST   | /create_book | 创建书籍记录 |
|   POST   | /update_book | 更新书籍信息 |
|   POST   | /delete_book | 删除书籍信息 |

**同样的需求我们按照RESTful API设计如下：**

| 请求方法 |  URL  |     含义     |
| :------: | :---: | :----------: |
|   GET    | /book | 查询书籍信息 |
|   POST   | /book | 创建书籍记录 |
|   PUT    | /book | 更新书籍信息 |
|  DELETE  | /book | 删除书籍信息 |

Gin框架支持开发RESTful API的开发。

```go
func main() {
	r := gin.Default()
	r.GET("/book", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "GET",
		})
	})

	r.POST("/book", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "POST",
		})
	})

	r.PUT("/book", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "PUT",
		})
	})

	r.DELETE("/book", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "DELETE",
		})
	})
    r.Run(":8080")
}
```

开发RESTful API的时候我们通常使用[Postman](https://www.getpostman.com/)来作为客户端的测试工具。

# 模板与渲染

在一些前后端不分离的Web架构中，我们通常需要在后端将一些数据渲染到HTML文档中，从而实现动态的网页（网页的布局和样式大致一样，但展示的内容并不一样）效果。

我们这里说的模板可以理解为事先定义好的HTML文档文件，模板渲染的作用机制可以简单理解为文本替换操作–使用相应的数据去替换HTML文档中事先准备好的标记。

## Go语言的模板引擎



Go语言内置了文本模板引擎`text/template`和用于HTML文档的`html/template`。它们的作用机制可以简单归纳如下：

1. 模板文件通常定义为`.tmpl`和`.tpl`为后缀（也可以使用其他的后缀），必须使用`UTF8`编码。
2. 模板文件中使用`{{`和`}}`包裹和标识需要传入的数据。
3. 传给模板这样的数据就可以通过点号（`.`）来访问，如果数据是复杂类型的数据，可以通过{ { .FieldName }}来访问它的字段。
4. 除`{{`和`}}`包裹的内容外，其他内容均不做修改原样输出。



## 模板引擎的使用

Go语言模板引擎的使用可以分为三部分：定义模板文件、解析模板文件和模板渲染。

### 定义模板文件

其中，定义模板文件时需要我们按照相关语法规则去编写，后文会详细介绍。

### 解析模板文件

上面定义好了模板文件之后，可以使用下面的常用方法去解析模板文件，得到模板对象：

```go
func (t *Template) Parse(src string) (*Template, error)
func ParseFiles(filenames ...string) (*Template, error)
func ParseGlob(pattern string) (*Template, error)
```

当然，你也可以使用`func New(name string) *Template`函数创建一个名为`name`的模板，然后对其调用上面的方法去解析模板字符串或模板文件。

### 模板渲染

渲染模板简单来说就是使用数据去填充模板：

```go
func (t *Template) Execute(wr io.Writer, data interface{}) error
func (t *Template) ExecuteTemplate(wr io.Writer, name string, data interface{}) error
```



### 基本示例

#### 定义模板文件

我们按照Go模板语法定义一个`hello.tmpl`的模板文件，内容如下：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Hello</title>
</head>
<body>
<p>Hello {{.}}</p>
</body>
</html>
```

#### 解析和渲染模板文件

然后我们创建一个`main.go`文件，在其中写下HTTP server端代码如下：

```go
package main

import (
	"fmt"
	"html/template"
	"net/http"
)

func sayHello(w http.ResponseWriter, r *http.Request){
	// 解析指定文件生成模板对象
	tmpl,err := template.ParseFiles("./demo1/hello.tmpl")
	if err!=nil{
		fmt.Println("create template failed, err:",err)
		return
	}
	// 利用给定数据渲染模板，并将结果写入w
	tmpl.Execute(w,"玛卡巴卡")
}

func main() {
	http.HandleFunc("/",sayHello)
	err := http.ListenAndServe(":8080",nil)
	if err != nil {
		fmt.Println("HTTP server failed,err:", err)
		return
	}
}
```

将上面的`main.go`文件编译执行，然后使用浏览器访问`http://localhost:8080/`就能看到页面上显示了“Hello 玛卡巴卡”。 这就是一个最简单的模板渲染的示例，Go语言模板引擎详细用法请往下阅读。

## 模板语法

### {{.}}

模板语法都包含在`{{`和`}}`中间，其中`{{.}}`中的点表示当前对象。

当我们传入一个结构体对象时，我们可以根据`.`来访问结构体的对应字段。例如：

```go
// main.go
package main

import (
	"fmt"
	"html/template"
	"net/http"
)

type UserInfo struct {
	Name   string
	Gender string
	Age    int
}

func sayHello(w http.ResponseWriter, r *http.Request) {
	// 解析指定文件生成模板对象
	tmpl, err := template.ParseFiles("./demo1/hello.tmpl")
	if err != nil {
		fmt.Println("create template failed, err:", err)
		return
	}
	// 利用给定数据渲染模板，并将结果写入w
	user := UserInfo{
		Name:   "小王子",
		Gender: "男",
		Age:    18,
	}
	tmpl.Execute(w, user)
}
func main() {
	http.HandleFunc("/", sayHello)
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		fmt.Println("HTTP server failed,err:", err)
		return
	}
}

```

模板文件`hello.tmpl`内容如下：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Hello</title>
</head>
<body>
    <p>Hello {{.Name}}</p>
    <p>性别：{{.Gender}}</p>
    <p>年龄：{{.Age}}</p>
</body>
</html>
```

同理，当我们传入的变量是map时，也可以在模板文件中通过`.`根据key来取值。

### 注释

```
{{/* a comment */}}
注释，执行时会忽略。可以多行。注释不能嵌套，并且必须紧贴分界符始止。
```

### pipeline

`pipeline`是指产生数据的操作。比如`{{.}}`、`{{.Name}}`等。Go的模板语法中支持使用管道符号`|`链接多个命令，用法和unix下的管道类似：`|`前面的命令会将运算结果(或返回值)传递给后一个命令的最后一个位置。

**注意：**并不是只有使用了`|`才是pipeline。Go的模板语法中，`pipeline的`概念是传递数据，只要能产生数据的，都是`pipeline`。

### 变量

我们还可以在模板中声明变量，用来保存传入模板的数据或其他语句生成的结果。具体语法如下：

```
$obj := {{.}}
```

其中`$obj`是变量的名字，在后续的代码中就可以使用该变量了。

### 移除空格

有时候我们在使用模板语法的时候会不可避免的引入一下空格或者换行符，这样模板最终渲染出来的内容可能就和我们想的不一样，这个时候可以使用`{{-`语法去除模板内容左侧的所有空白符号， 使用`-}}`去除模板内容右侧的所有空白符号。

例如：

```template
{{- .Name -}}
```

**注意：**`-`要紧挨`{{`和`}}`，同时与模板值之间需要使用空格分隔。

### 条件判断

Go模板语法中的条件判断有以下几种:

```
{{if pipeline}} T1 {{end}}

{{if pipeline}} T1 {{else}} T0 {{end}}

{{if pipeline}} T1 {{else if pipeline}} T0 {{end}}
```

### range

Go的模板语法中使用`range`关键字进行遍历，有以下两种写法，其中`pipeline`的值必须是数组、切片、字典或者通道。

```
{{range pipeline}} T1 {{end}}
如果pipeline的值其长度为0，不会有任何输出

{{range pipeline}} T1 {{else}} T0 {{end}}
如果pipeline的值其长度为0，则会执行T0。
```

### with

```
{{with pipeline}} T1 {{end}}
如果pipeline为empty不产生输出，否则将dot设为pipeline的值并执行T1。不修改外面的dot。

{{with pipeline}} T1 {{else}} T0 {{end}}
如果pipeline为empty，不改变dot并执行T0，否则dot设为pipeline的值并执行T1。
```

### 预定义函数

执行模板时，函数从两个函数字典中查找：首先是模板函数字典，然后是全局函数字典。一般不在模板内定义函数，而是使用Funcs方法添加函数到模板里。

预定义的全局函数如下：

```
and
    函数返回它的第一个empty参数或者最后一个参数；
    就是说"and x y"等价于"if x then y else x"；所有参数都会执行；
or
    返回第一个非empty参数或者最后一个参数；
    亦即"or x y"等价于"if x then x else y"；所有参数都会执行；
not
    返回它的单个参数的布尔值的否定
len
    返回它的参数的整数类型长度
index
    执行结果为第一个参数以剩下的参数为索引/键指向的值；
    如"index x 1 2 3"返回x[1][2][3]的值；每个被索引的主体必须是数组、切片或者字典。
print
    即fmt.Sprint
printf
    即fmt.Sprintf
println
    即fmt.Sprintln
html
    返回与其参数的文本表示形式等效的转义HTML。
    这个函数在html/template中不可用。
urlquery
    以适合嵌入到网址查询中的形式返回其参数的文本表示的转义值。
    这个函数在html/template中不可用。
js
    返回与其参数的文本表示形式等效的转义JavaScript。
call
    执行结果是调用第一个参数的返回值，该参数必须是函数类型，其余参数作为调用该函数的参数；
    如"call .X.Y 1 2"等价于go语言里的dot.X.Y(1, 2)；
    其中Y是函数类型的字段或者字典的值，或者其他类似情况；
    call的第一个参数的执行结果必须是函数类型的值（和预定义函数如print明显不同）；
    该函数类型值必须有1到2个返回值，如果有2个则后一个必须是error接口类型；
    如果有2个返回值的方法返回的error非nil，模板执行会中断并返回给调用模板执行者该错误；
```



### 比较函数

布尔函数会将任何类型的零值视为假，其余视为真。

下面是定义为函数的二元比较运算的集合：

```
eq      如果arg1 == arg2则返回真
ne      如果arg1 != arg2则返回真
lt      如果arg1 < arg2则返回真
le      如果arg1 <= arg2则返回真
gt      如果arg1 > arg2则返回真
ge      如果arg1 >= arg2则返回真
```

为了简化多参数相等检测，eq（只有eq）可以接受2个或更多个参数，它会将第一个参数和其余参数依次比较，返回下式的结果：

```
{{eq arg1 arg2 arg3}}
```

**比较函数只适用于基本类型（或重定义的基本类型，如”type Celsius float32”）。但是，整数和浮点数不能互相比较。**



### 自定义函数

Go的模板支持自定义函数。

```go
package main

import (
	"fmt"
	"html/template"
	"io/ioutil"
	"net/http"
)

type UserInfo struct {
	Name   string
	Gender string
	Age    int
}

func sayHello(w http.ResponseWriter, r *http.Request) {
	htmlByte, err := ioutil.ReadFile("./demo1/hello.tmpl")
	if err != nil {
		fmt.Println("read html failed, err:", err)
		return
	}
	// 自定义一个模板函数
	f := func(arg string) (string, error) {
		return arg + "（自定义函数内容）", nil
	}

	// 采用链式操作在Parse之前调用Funcs添加自定义的f函数
	tmpl, err := template.New("hello").Funcs(template.FuncMap{"f": f}).Parse(string(htmlByte))
	if err != nil {
		fmt.Println("create template failed, err:", err)
		return
	}

	user := UserInfo{
		Name:   "小王子",
		Gender: "男",
		Age:    18,
	}
	// 使用user渲染模板，并将结果写入w
	tmpl.Execute(w, user)
}
func main() {
	http.HandleFunc("/", sayHello)
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		fmt.Println("HTTP server failed,err:", err)
		return
	}
}

```

我们可以在模板文件`hello.tmpl`中按照如下方式使用我们自定义的`f`函数了。

```
{{f .Name}}	/* f是自定义函数的函数名，后面的.Name就是f的形参*/
```



### 嵌套template

我们可以在template中嵌套其他的template。这个template可以是单独的文件，也可以是通过`define`定义的template。

举个例子： `t.tmpl`文件内容如下：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>tmpl test</title>
</head>
<body>

<h1>测试嵌套template语法</h1>
<hr>
{{template "ul.tmpl"}}
<hr>
{{template "ol.tmpl"}}
</body>
</html>

{{ define "ol.tmpl"}}
<ol>
    <li>吃饭</li>
    <li>睡觉</li>
    <li>打游戏</li>
</ol>
{{end}}
```

`ul.tmpl`文件内容如下：

```html
<ul>
    <li>注释</li>
    <li>日志</li>
    <li>测试</li>
</ul>
```

我们注册一个`templDemo`路由处理函数：

```go
http.HandleFunc("/tmpl", tmplDemo)
```

`tmplDemo`函数的具体内容如下：

```go
func tmplDemo(w http.ResponseWriter, r *http.Request) {
	tmpl, err := template.ParseFiles("./t.tmpl", "./ul.tmpl")
	if err != nil {
		fmt.Println("create template failed, err:", err)
		return
	}
	user := UserInfo{
		Name:   "小王子",
		Gender: "男",
		Age:    18,
	}
	tmpl.Execute(w, user)
}
```

**注意**：在解析模板时，被嵌套的模板一定要在后面解析，例如上面的示例中`t.tmpl`模板中嵌套了`ul.tmpl`，所以`ul.tmpl`要在`t.tmpl`后进行解析。



### block

```
{{block "name" pipeline}} T1 {{end}}
```

`block`是定义模板`{{define "name"}} T1 {{end}}`和执行`{{template "name" pipeline}}`缩写，典型的用法是定义一组根模板，然后通过在其中重新定义块模板进行自定义。

定义一个**根模板**`templates/base.tmpl`，内容如下：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <title>Go Templates</title>
</head>
<body>
<div class="container-fluid">
    {{block "content" . }}{{end}}
</div>
</body>
</html>
```

然后定义一个`templates/index.tmpl`，”继承”`base.tmpl`：

```html
{{template "base.tmpl"}}

{{define "content"}}
<div>Hello world!</div>
{{end}}
```

然后使用`template.ParseGlob`按照正则匹配规则解析模板文件，然后通过`ExecuteTemplate`渲染指定的模板：

```go
func index(w http.ResponseWriter, r *http.Request) {
	tmpl, err := template.ParseGlob("templates/*.tmpl")
	if err != nil {
		fmt.Println("create template failed, err:", err)
		return
	}
	err = tmpl.ExecuteTemplate(w, "index.tmpl", nil)
	if err != nil {
		fmt.Println("render template failed, err:", err)
		return
	}
}

func main() {
	http.HandleFunc("/", index)
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		fmt.Println("HTTP server failed,err:", err)
		return
	}
}
```

如果我们的模板名称冲突了，例如不同业务线下都定义了一个`index.tmpl`模板，我们可以通过下面两种方法来解决。

1. 在模板文件开头使用`{{define 模板名}}`语句显式的为模板命名。
2. 可以把模板文件存放在`templates`文件夹下面的不同目录中，然后使用`template.ParseGlob("templates/**/*.tmpl")`解析模板。



### 修改默认的标识符

Go标准库的模板引擎使用的花括号`{{`和`}}`作为标识，而许多前端框架（如`Vue`和 `AngularJS`）也使用`{{`和`}}`作为标识符，所以当我们同时使用Go语言模板引擎和以上前端框架时就会出现冲突，这个时候我们需要修改标识符，修改前端的或者修改Go语言的。这里演示如何修改Go语言模板引擎默认的标识符：

```go
template.New("test").Delims("{[", "]}").ParseFiles("./t.tmpl")
```



## text/template与html/tempalte的区别

`html/template`针对的是需要返回HTML内容的场景，在模板渲染过程中会对一些有风险的内容进行转义，以此来防范跨站脚本攻击。

例如，我定义下面的模板文件`templates/xss.tmpl`：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Hello</title>
</head>
<body>
    {{ . }}
</body>
</html>
```

这个时候传入一段JS代码并使用`html/template`去渲染该文件，会在页面上显示出转义后的JS内容：`<script>alert('嘿嘿嘿')</script> `这就是html/template为我们做的事。

但是在某些场景下，我们如果相信用户输入的内容，不想转义的话，可以自行编写一个safe函数，手动返回一个`template.HTML`类型的内容。示例如下：

```go
func xss(w http.ResponseWriter, r *http.Request){
	tmpl,err := template.New("xss.tmpl").Funcs(template.FuncMap{
		"safe": func(s string)template.HTML {
			return template.HTML(s)
		},
	}).ParseFiles("./templates/xss.tmpl")
	if err != nil {
		fmt.Println("create template failed, err:", err)
		return
	}
	jsStr := `<script>alert('嘿嘿嘿')</script>`
	err = tmpl.Execute(w, jsStr)
	if err != nil {
		fmt.Println(err)
	}
}
```

这样我们只需要在模板文件不需要转义的内容后面使用我们定义好的safe函数就可以了。

```
{{ . | safe }}
```



# Gin渲染

## HTML渲染

首先定义一个存放模板文件的`templates`文件夹，然后在其内部按照业务分别定义一个`posts`文件夹和一个`users`文件夹。 `posts/index.html`文件的内容如下：

```html
{{define "posts/index.html"}}
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>posts/index</title>
</head>
<body>
    {{.title}}
</body>
</html>
{{end}}
```

`users/index.html`文件的内容如下：

```html
{{define "users/index.html"}}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>users/index</title>
</head>
<body>
    {{.title}}
</body>
</html>
{{end}}
```

Gin框架中使用`LoadHTMLGlob()`或者`LoadHTMLFiles()`方法进行HTML模板渲染：

```go
func main() {
	r := gin.Default()
	r.LoadHTMLGlob("templates/**/*")
	//r.LoadHTMLFiles("templates/posts/index.html", "templates/users/index.html")
	r.GET("/posts/index", func(c *gin.Context) {
		c.HTML(http.StatusOK, "posts/index.html", gin.H{
			"title": "posts/index",
		})
	})

	r.GET("users/index", func(c *gin.Context) {
		c.HTML(http.StatusOK, "users/index.html", gin.H{
			"title": "users/index",
		})
	})

	r.Run(":8080")
}
```



## 自定义模板函数

定义一个不转义相应内容的`safe`模板函数如下：

```go
package main

import (
	"github.com/gin-gonic/gin"
	"html/template"
	"net/http"
)

func main() {
	r := gin.Default()
    // gin框架中给模板添加自定义函数
	r.SetFuncMap(template.FuncMap{
		"safe": func(str string) template.HTML {
			return template.HTML(str)
		},
	})
	r.LoadHTMLFiles("./templates/safe.tmpl")
	r.GET("/safe", func(c *gin.Context) {
		c.HTML(http.StatusOK, "safe.tmpl", ""<h1>嘿嘿嘿</h1>"")
	})

	r.Run(":8080")
}

```

在`safe.tmpl`中使用定义好的`safe`模板函数：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <title>定义一个不转义相应内容的safe模板函数</title>
</head>
<body>
<div>{{ . | safe }}</div>
</body>
</html>
```



## 静态文件处理

创建一个`./statics/index.css`文件：

```css
body {
    background-color: cadetblue;
}
```

在`safe.tmpl`文件中添加使用`index.css`：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <title>定义一个不转义相应内容的safe模板函数</title>
    <link rel="stylesheet" href="/xxx/index.css">
</head>
<body>
<div>{{ . | safe }}</div>
</body>
</html>
```

在`./templates/main.go`中添加加载静态文件代码：

```go
func main() {
	r := gin.Default()
	// 加载静态文件
	r.Static("/xxx", "./statics")

	// gin框架中给模板添加自定义函数
	r.SetFuncMap(template.FuncMap{
		"safe": func(str string) template.HTML {
			return template.HTML(str)
		},
	})
	r.LoadHTMLFiles("./templates/safe.tmpl")
	r.GET("/safe", func(c *gin.Context) {
		c.HTML(http.StatusOK, "safe.tmpl", "<h1>嘿嘿嘿</h1>")
	})

	r.Run(":8080")
}
```



## 使用模板继承

Gin框架默认都是使用单模板，如果需要使用`block template`功能，可以通过`"github.com/gin-contrib/multitemplate"`库实现，具体示例如下：

首先，假设我们项目目录下的templates文件夹下有以下模板文件，其中`home.tmpl`和`index.tmpl`继承了`base.tmpl`：

```
templates
├── includes
│   ├── home.tmpl
│   └── index.tmpl
├── layouts
│   └── base.tmpl
└── scripts.tmpl
```

然后我们定义一个`loadTemplates`函数如下：

```go
func loadTemplates(templatesDir string) multitemplate.Renderer {
	r := multitemplate.NewRenderer()
	layouts, err := filepath.Glob(templatesDir + "/layouts/*.tmpl")
	if err != nil {
		panic(err.Error())
	}
	includes, err := filepath.Glob(templatesDir + "/includes/*.tmpl")
	if err != nil {
		panic(err.Error())
	}
	// 为layouts/和includes/目录生成 templates map
	for _, include := range includes {
		layoutCopy := make([]string, len(layouts))
		copy(layoutCopy, layouts)
		files := append(layoutCopy, include)
		r.AddFromFiles(filepath.Base(include), files...)
	}
	return r
}
```

我们在`main`函数中：

```go
func indexFunc(c *gin.Context){
	c.HTML(http.StatusOK, "index.tmpl", nil)
}

func homeFunc(c *gin.Context){
	c.HTML(http.StatusOK, "home.tmpl", nil)
}

func main(){
	r := gin.Default()
	r.HTMLRender = loadTemplates("./templates")
	r.GET("/index", indexFunc)
	r.GET("/home", homeFunc)
	r.Run()
}
```



## 补充文件路径处理

关于模板文件和静态文件的路径，我们需要根据公司/项目的要求进行设置。可以使用下面的函数获取当前执行程序的路径。

```go
func getCurrentPath() string {
	if ex, err := os.Executable(); err == nil {
		return filepath.Dir(ex)
	}
	return "./"
}
```



## JSON渲染

**注意：**gin.H 是map[string]interface{}的缩写

```go
package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func main() {
	r := gin.Default()

	// gin.H 是map[string]interface{}的缩写
	r.GET("/jsonMap", func(c *gin.Context) {
		// 方式一：使用map(或用过gin.H{}进行拼接)
		// gin.H 就是 map[string]interface{} 的缩写

		//data := map[string]interface{}{
		//	"name":    "孙悟空",
		//	"message": "吃俺老孙一棒！",
		//	"age":     500,
		//}
		data := gin.H{"name": "孙悟空", "message": "吃俺老孙一棒！", "age": 500}
		c.JSON(http.StatusOK, data)
	})
	r.GET("/jsonStruct", func(c *gin.Context) {
		// 方法二：使用结构体
		var msg struct {
			// 结构体中的字段名必须首字母大写
			// 如果想要返回前端的字段名显示小写，可以用tag
			Name    string `json:"user"`
			Message string
			Age     int
		}
		msg.Name = "猪八戒"
		msg.Message = "吃俺老猪一耙！"
		msg.Age = 600
		c.JSON(http.StatusOK, msg) // json的序列化
	})
	r.Run(":8080")
}
```

在浏览器中分别输入`http://localhost:8080/jsonMap`和`http://localhost:8080/jsonStruct`查看结果。



## XML渲染

注意需要使用具名的结构体类型。

```go
func main() {
	r := gin.Default()
	// gin.H 是map[string]interface{}的缩写
	r.GET("/someXML", func(c *gin.Context) {
		// 方式一：自己拼接JSON
		c.XML(http.StatusOK, gin.H{"message": "Hello world!"})
	})
	r.GET("/moreXML", func(c *gin.Context) {
		// 方法二：使用结构体
		type MessageRecord struct {
			Name    string
			Message string
			Age     int
		}
		var msg MessageRecord
		msg.Name = "小王子"
		msg.Message = "Hello world!"
		msg.Age = 18
		c.XML(http.StatusOK, msg)
	})
	r.Run(":8080")
}
```

## YMAL渲染

```go
r.GET("/someYAML", func(c *gin.Context) {
	c.YAML(http.StatusOK, gin.H{"message": "ok", "status": http.StatusOK})
})
```



## protobuf渲染

```go
r.GET("/someProtoBuf", func(c *gin.Context) {
	reps := []int64{int64(1), int64(2)}
	label := "test"
	// protobuf 的具体定义写在 testdata/protoexample 文件中。
	data := &protoexample.Test{
		Label: &label,
		Reps:  reps,
	}
	// 请注意，数据在响应中变为二进制数据
	// 将输出被 protoexample.Test protobuf 序列化了的数据
	c.ProtoBuf(http.StatusOK, data)
})
```



# 获取参数

## 获取querystring参数

`querystring`指的是URL中`?`后面携带的参数，用`key=value`形式，多个`key=value`用`&`连接，例如：`http://localhost:8080/web?name=孙悟空&age=500&gender=男`。 获取请求的querystring参数的方法如下：

```go
package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func main(){
    // 获取浏览器那边发请求携带的 query string 参数
	r := gin.Default()
	r.GET("/web", func(c *gin.Context) {
		// 方式一：通过Query获取请求中携带的querystring参数 (常用)
		name := c.Query("name")
		age := c.Query("age")
		gender := c.Query("gender")
		//// 方式二：通过DefaultQuery获取，取不到就用指定的默认值
		//name := c.DefaultQuery("name", "未知")
		//// 方式三：通过GetQuery获取，取不到，第二个参数就返回false
		//name, ok := c.GetQuery("name")
		//if !ok {
		//	// 取不到
		//	name = "未知"
		//}

		c.JSON(http.StatusOK, gin.H{
			"name":   name,
			"age":    age,
			"gender": gender,
		}) //输出结果给调用方
	})

	r.Run(":8080")
}
```



## 获取form参数

当前端请求的数据通过form表单提交时，例如向`/user/search`发送一个POST请求，获取请求数据的方式如下：

`login.html`文件：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>登录</title>
</head>
<body>
<form action="/login" method="post">
    <div>
        <label for="username">username:</label>
        <input type="text" name="username" id="username">
    </div>
    <div>
        <label for="password">password:</label>
        <input type="text" name="password" id="password">
    </div>
    <div>
        <input type="submit" value="登录">
    </div>

</form>

</body>
</html>
```

`main.go`文件：

```go
package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func main(){
    // 获取form
	r := gin.Default()
	r.LoadHTMLFiles("./getParameter/login.html")
	r.GET("/login", func(c *gin.Context) {
		c.HTML(http.StatusOK, "login.html", nil)
	})

	// 接受前端传过来的表单信息
	r.POST("/login", func(c *gin.Context) {
		// 方式一：
		username := c.PostForm("username")
		password := c.PostForm("password")
		//// 方式二：
		//username := c.DefaultQuery("username", "未知")
		//password := c.DefaultQuery("password", "***")
		//// 方式三：
		//username, ok := c.GetPostForm("username")
		//if !ok {
		//	username = "未知"
		//}
		//password, ok := c.GetPostForm("password")
		//if !ok {
		//	password = "***"
		//}
		c.JSON(http.StatusOK, gin.H{
			"姓名": username,
			"密码": password,
		}) // 输出json结果给调用方
	})
	r.Run(":8080")
}
```



## 获取json参数

当前端请求的数据通过JSON提交时，例如向`/json`发送一个POST请求，则获取请求参数的方式如下：

```go
r.POST("/json", func(c *gin.Context) {
	// 注意：下面为了举例子方便，暂时忽略了错误处理
	b, _ := c.GetRawData()  // 从c.Request.Body读取请求数据
	// 定义map或结构体
	var m map[string]interface{}
	// 反序列化
	_ = json.Unmarshal(b, &m)

	c.JSON(http.StatusOK, m)
})
```

更便利的获取请求参数的方式，参见下面的 **参数绑定** 小节。



## 获取path参数

请求的参数通过URL路径传递，例如：`http://localhost:8080/web/孙悟空/500`。 获取请求URL路径中的参数的方式如下：

**注意：URL的匹配不要冲突**

```go
package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func main(){
    r := gin.Default()
	r.GET("/web/:name/:age", func(c *gin.Context) {
		name := c.Param("name")
		age := c.Param("age")
		// 输出json结果给调用方
		c.JSON(http.StatusOK, gin.H{
			"name": name,
			"age":  age,
		})
	})
    
    r.GET("/date/:year/:month/:day", func(c *gin.Context) {
		year := c.Param("year")
		month := c.Param("month")
		day := c.Param("day")
		// 输出json结果给调用方
		c.JSON(http.StatusOK, gin.H{
			"year":  year,
			"month": month,
			"day":   day,
		})
	})

	r.Run(":8080")
}
```



## 参数绑定

为了能够更方便的获取请求相关参数，提高开发效率，我们可以基于请求的`Content-Type`识别请求数据类型并利用反射机制自动提取请求中`QueryString`、`form表单`、`JSON`、`XML`等参数到结构体中。 下面的示例代码演示了`.ShouldBind()`强大的功能，它能够基于请求自动提取`JSON`、`form表单`和`QueryString`类型的数据，并把值绑定到指定的结构体对象。

`ShouldBind`会按照下面的顺序解析请求中的数据完成绑定：

1. 如果是 `GET` 请求，只使用 `Form` 绑定引擎（`query`）。
2. 如果是 `POST` 请求，首先检查 `content-type` 是否为 `JSON` 或 `XML`，然后再使用 `Form`（`form-data`）。

`main.go`文件：

```go
package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

type Login struct {
	UserName string `form:"user" json:"user" `
	Password string `form:"pwd" json:"pwd" `
}

func main() {
	r := gin.Default()

	// 绑定Json示例：在postman->body->raw(选择JSON)中输入{"user":"tom", "pwd":"123456"}
	r.POST("/loginJson", func(c *gin.Context) {
		var login Login
		err := c.ShouldBind(&login)
		if err == nil {
			c.JSON(http.StatusOK, gin.H{
				"status":   "ok",
				"user":     login.UserName,
				"password": login.Password,
			})
		} else {
			c.JSON(http.StatusBadRequest, gin.H{"err": err.Error()})
		}
	})

	// 绑定form表单示例：http://localhost:8080/loginForm
	r.LoadHTMLFiles("./getParameter/parameterBinding/login2.html")
	r.GET("/loginForm", func(c *gin.Context) {
		c.HTML(http.StatusOK, "login2.html", nil)
	})

	r.POST("/loginForm", func(c *gin.Context) {
		var login Login
		// ShouldBind()会根据请求的Content-Type自行选择绑定器
		err := c.ShouldBind(&login)
		if err == nil {
			c.JSON(http.StatusOK, gin.H{
				"status":   "ok",
				"user":     login.UserName,
				"password": login.Password,
			})
		} else {
			c.JSON(http.StatusBadRequest, gin.H{"err": err.Error()})
		}
	})

	//绑定QueryString示例 (/loginQuery?user=jack&pwd=123456)
	r.GET("loginQuery", func(c *gin.Context) {
		var login Login
		// ShouldBind()会根据请求的Content-Type自行选择绑定器
		err := c.ShouldBind(&login)
		if err == nil {
			c.JSON(http.StatusOK, gin.H{
				"status":   "ok",
				"user":     login.UserName,
				"password": login.Password,
			})
		} else {
			c.JSON(http.StatusBadRequest, gin.H{"err": err.Error()})
		}
	})
	r.Run(":8080")

}

```

`login2.html`文件：

**注意：输入框的`name`要与结构体中的`tag`一致。**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>登录</title>
</head>
<body>
<form action="/loginForm" method="post">
    <div>
        <label for="username">username:</label>
        <input type="text" name="user" id="username">
    </div>
    <div>
        <label for="password">password:</label>
        <input type="text" name="pwd" id="password">
    </div>
    <div>
        <input type="submit" value="登录">
    </div>

</form>

</body>
</html>
```



# 文件上传

## 单个文件上传

文件上传前端页面代码`index.html`：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>单个文件上传</title>
</head>
<body>
<form action="/upload" method="post" enctype="multipart/form-data">
    <input type="file" name="f1">
    <input type="submit" value="上传">
</form>
</body>
</html>
```

后端gin框架部分代码`main.go`：

```go
package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
	"path"
)

func main() {
	r := gin.Default()
	// 处理multipart forms提交文件时默认的内存限制是32 MiB
	// 可以通过下面的方式修改
	// router.MaxMultipartMemory = 8 << 20  // 8 MiB

	r.LoadHTMLFiles("./fileUpload/index.html")
	r.GET("/index", func(c *gin.Context) {
		c.HTML(http.StatusOK, "index.html", nil)
	})

	r.POST("/upload", func(c *gin.Context) {
		// 从请求中读取文件
		f, err := c.FormFile("f1") // 从请求中获取携带的参数一样的
		if err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		} else {
			// 将读取到的文件保存在本地（服务端本地）
			//dst := fmt.Sprintf("./fileUpload/%s", f.Filename)
			dst := path.Join("./fileUpload/", f.Filename) // 存储路径
			c.SaveUploadedFile(f, dst)
			c.JSON(http.StatusOK, gin.H{"status": "ok"})

		}
	})

	r.Run(":8080")
}

```



## 多个文件上传

文件上传前端页面代码`index2.html`（与上一节不同的是，文件选择设置了多选）：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>多个文件上传</title>
</head>
<body>
<form action="/upload" method="post" enctype="multipart/form-data">
    <input type="file" name="f1" multiple="multiple">
    <input type="submit" value="上传">
</form>
</body>
</html>
```

后端gin框架部分代码`main.go`：

```go
package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"log"
	"net/http"
	"path"
)

func main(){
    r := gin.Default()
	// 处理multipart forms提交文件时默认的内存限制是32 MiB
	// 可以通过下面的方式修改
	// router.MaxMultipartMemory = 8 << 20  // 8 MiB

	r.LoadHTMLFiles("./fileUpload/index2.html")
	r.GET("/index2", func(c *gin.Context) {
		c.HTML(http.StatusOK, "index2.html", nil)
	})

	r.POST("/upload", func(c *gin.Context) {
		// Multipart form
		form, err := c.MultipartForm()
		if err != nil {
			fmt.Println(err)
		}
		files := form.File["f1"]
		for index, file := range files {
			log.Println(file.Filename)
			name := fmt.Sprintf("%d_%s", index, file.Filename)
			dst := path.Join("./fileUpload/", name)
			c.SaveUploadedFile(file, dst)
		}
		c.JSON(http.StatusOK, gin.H{
			"status":  "ok",
			"message": fmt.Sprintf("%d files uploaded!", len(files)),
		})

	})

	r.Run(":8080")
}
```



# 重定向

## HTTP重定向

```go
package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func main() {
	r := gin.Default()

	r.GET("/index", func(c *gin.Context) {
		// 访问http://localhost:8080/index 显示 {"status":"ok"}
		//c.JSON(http.StatusOK, gin.H{
		//	"status": "ok",
		//})
		// 访问http://localhost:8080/index 跳转到百度
		c.Redirect(http.StatusMovedPermanently, "https://www.baidu.com") // 重定向
	})

	r.Run(":8080")
}

```



## 路由重定向

```go
package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func main() {
	r := gin.Default()

	r.GET("/a", func(c *gin.Context) {
		// 访问http://localhost:8080/a 跳转到/b对应的路由处理函数
		c.Request.URL.Path = "/b" //把请求的URI修改
		r.HandleContext(c)        //继续后续的处理
	})

	r.GET("/b", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"message": "b",
		})
	})

	r.Run(":8080")
}

```



# 同步异步

- goroutine机制可以方便地实现异步处理
- 另外，在启动新的goroutine时，不应该使用原始上下文，必须使用它的只读副本

```go
package main

import (
	"github.com/gin-gonic/gin"
	"log"
	"net/http"
	"time"
)

func main() {
	r := gin.Default()
	// 异步
	r.GET("/long_async", func(c *gin.Context) {
		// 需要一个副本
		copyContext := c.Copy()
		// 异步处理
		go func() {
			time.Sleep(3 * time.Second)
			log.Println("异步执行：" + copyContext.Request.URL.Path)
		}()
		c.JSON(http.StatusOK, gin.H{"message": "long_async"})
	})

	// 同步
	r.GET("/long_sync", func(c *gin.Context) {
		time.Sleep(2 * time.Second)
		log.Println("同步执行：" + c.Request.URL.Path)
		c.JSON(http.StatusOK, gin.H{"message": "long_async"})
	})
	r.Run(":8080")
}

```



# Gin路由

## 普通路由

```go
r.GET("/index", func(c *gin.Context) {...})
r.POST("/index", func(c *gin.Context) {...})
r.PUT("/index", func(c *gin.Context) {...})
r.DELETE("/index", func(c *gin.Context) {...})
```

此外，还有一个可以匹配所有请求方法的`Any`方法如下：

```go
r.Any("/test", func(c *gin.Context) {...})
```

```go
package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func main(){
    r := gin.Default()
    r.Any("/index", func(c *gin.Context) {
		switch c.Request.Method {
		case "GET":
			c.JSON(http.StatusOK, gin.H{"method": "GET"})
		case http.MethodPost:
			c.JSON(http.StatusOK, gin.H{"method": "POST"})
		case http.MethodPut:
			c.JSON(http.StatusOK, gin.H{"method": "PUT"})
		case "DELETE":
			c.JSON(http.StatusOK, gin.H{"method": "DELETE"})
		}
	})
}
```

为没有配置处理函数的路由添加处理程序，默认情况下它返回404代码，下面的代码为没有匹配到路由的请求都返回`views/404.html`页面。

```go
r.NoRoute(func(c *gin.Context) {
		c.JSON(http.StatusNotFound, gin.H{"message": "页面不存在"})
	})
```



## 路由组

我们可以将拥有共同URL前缀的路由划分为一个路由组。习惯性一对`{}`包裹同组的路由，这只是为了看着清晰，你用不用`{}`包裹功能上没什么区别。

```go
package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func main(){
    r := gin.Default()
    userGroup := r.Group("/user")
	{
		userGroup.GET("/index", func(c *gin.Context) {
			c.JSON(http.StatusOK, gin.H{"message": "/user/index"})
		})
		userGroup.GET("/xxx", func(c *gin.Context) {
			c.JSON(http.StatusOK, gin.H{"message": "/user/xxx"})
		})
		userGroup.GET("/yyy", func(c *gin.Context) {
			c.JSON(http.StatusOK, gin.H{"message": "/user/yyy"})
		})
	}

	shopGroup := r.Group("/shop")
	{
		shopGroup.GET("/index", func(c *gin.Context) {
			c.JSON(http.StatusOK, gin.H{"message": "/shop/index"})
		})
		shopGroup.GET("/xxx", func(c *gin.Context) {
			c.JSON(http.StatusOK, gin.H{"message": "/shop/xxx"})
		})
		shopGroup.GET("/yyy", func(c *gin.Context) {
			c.JSON(http.StatusOK, gin.H{"message": "/shop/yyy"})
		})
	}

	r.Run(":8080")
}

```

路由组也是支持嵌套的，例如：

```go
shopGroup := r.Group("/shop")
	{
		shopGroup.GET("/index", func(c *gin.Context) {
			c.JSON(http.StatusOK, gin.H{"message": "/shop/index"})
		})
		shopGroup.GET("/xxx", func(c *gin.Context) {
			c.JSON(http.StatusOK, gin.H{"message": "/shop/xxx"})
		})
		shopGroup.GET("/yyy", func(c *gin.Context) {
			c.JSON(http.StatusOK, gin.H{"message": "/shop/yyy"})
		})
		// 嵌套路由组
		xxx := shopGroup.Group("/xxx")
		xxx.GET("/zzz", func(c *gin.Context) {
			c.JSON(http.StatusOK, gin.H{"message": "/shop/xxx/zzz"})
		})
	}
```

通常我们将路由分组用在划分业务逻辑或划分API版本时。



## 路由原理

Gin框架中的路由使用的是[httprouter](https://github.com/julienschmidt/httprouter)这个库。

其基本原理就是构造一个路由地址的前缀树。



# gin中间件

Gin框架允许开发者在处理请求的过程中，加入用户自己的钩子（Hook）函数。这个钩子函数就叫中间件，中间件适合处理一些公共的业务逻辑，比如登录认证、权限校验、数据分页、记录日志、耗时统计等。

## 定义中间件

Gin中的中间件必须是一个`gin.HandlerFunc`类型。

```go
// gin.go
type HandlerFunc func(*Context)
```

**`gin.Default`默认使用了两个中间件`Logger()`、`Recovery()`**

### 定义中间件实例1

```go
package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http"
)

// HandlerFunc
func indexHandler(c *gin.Context) {
	fmt.Println("index in...")
	c.JSON(http.StatusOK, gin.H{
		"msg": "index",
	})
}

// 定义一个中间件m1
func m1(c *gin.Context) {
	fmt.Println("m1 in...")
}

// 定义一个中间件m2
func m2() gin.HandlerFunc {
	return func(c *gin.Context) {
		fmt.Println("m2 in...")
	}
}

func main() {
	r := gin.Default()
	r.GET("/index", m1, m2(), indexHandler)
	r.Run(":8080")
}

```



### 记录接口耗时的中间件

例如我们像下面的代码一样定义一个统计请求耗时的中间件。

```go
package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http"
	"time"
)

// handlerFunc
func indexHandler(c *gin.Context) {
	fmt.Println("index in...")
	c.JSON(http.StatusOK, gin.H{
		"msg": "index",
	})
}

func StatCost() gin.HandlerFunc {
	// StatCost 是一个统计耗时请求耗时的中间件
	return func(c *gin.Context) {
		fmt.Println("StatCost in...")
		start := time.Now()
		// 可以通过c.Set在请求上下文中设置值，后续的处理函数能够取到该值
		c.Set("name", "赵子龙")
		// 调用该请求的剩余处理程序
		c.Next()
		// 不调用该请求的剩余处理程序
		// c.Abort()
		// 计算耗时
		cost := time.Since(start)
		fmt.Println("耗时：", cost)
	}
}

func main() {
	r := gin.Default()
	r.GET("/index", StatCost(), indexHandler)
	r.Run(":8080")

}

```



### 记录响应体的中间件

我们有时候可能会想要记录下某些情况下返回给客户端的响应数据，这个时候就可以编写一个中间件来搞定。

```go
package main

import (
	"bytes"
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http"
	"time"
)

type bodyLogWriter struct {
	gin.ResponseWriter               //嵌入gin框架ResponseWriter
	body               *bytes.Buffer // 记录用的response
}

// write 写入响应体数据
func (w bodyLogWriter) Write(b []byte) (int, error) {
	w.body.Write(b)                  //记录一份
	return w.ResponseWriter.Write(b) //真正写入响应
}

// ginBodyLogMiddleware 一个记录返回给客户端响应体的中间件
func ginBodyLogMiddleware(c *gin.Context) {
	blw := &bodyLogWriter{body: bytes.NewBuffer([]byte{}), ResponseWriter: c.Writer}
	c.Writer = blw                                    // 使用自定义的类型替换默认的
	c.Next()                                          // 执行业务逻辑
	fmt.Println("Response body:" + blw.body.String()) //事后按需记录返回的响应
}

// handlerFunc
func indexHandler(c *gin.Context) {
	fmt.Println("index in...")
	c.JSON(http.StatusOK, gin.H{
		"msg": "index",
	})
}

func main() {
	r := gin.Default()
	r.GET("/index", ginBodyLogMiddleware, indexHandler)
	r.Run(":8080")

}

```



### 跨域中间件cors

推荐使用社区的https://github.com/gin-contrib/cors 库，一行代码解决前后端分离架构下的跨域问题。

**注意：** 该中间件需要注册在业务处理函数前面。

这个库支持各种常用的配置项，具体使用方法如下。

```go
package main

import (
  "time"

  "github.com/gin-contrib/cors"
  "github.com/gin-gonic/gin"
)

func main() {
  router := gin.Default()
  // CORS for https://foo.com and https://github.com origins, allowing:
  // - PUT and PATCH methods
  // - Origin header
  // - Credentials share
  // - Preflight requests cached for 12 hours
  router.Use(cors.New(cors.Config{
    AllowOrigins:     []string{"https://foo.com"},  // 允许跨域发来请求的网站
    AllowMethods:     []string{"GET", "POST", "PUT", "DELETE",  "OPTIONS"},  // 允许的请求方法
    AllowHeaders:     []string{"Origin", "Authorization", "Content-Type"},
    ExposeHeaders:    []string{"Content-Length"},
    AllowCredentials: true,
    AllowOriginFunc: func(origin string) bool {  // 自定义过滤源站的方法
      return origin == "https://github.com"
    },
    MaxAge: 12 * time.Hour,
  }))
  router.Run()
}
```

当然你可以简单的像下面的示例代码那样使用默认配置，允许所有的跨域请求。

```go
func main() {
  router := gin.Default()
  // same as
  // config := cors.DefaultConfig()
  // config.AllowAllOrigins = true
  // router.Use(cors.New(config))
  router.Use(cors.Default())
  router.Run()
}
```



## 注册中间件

### Default()与New()

在gin框架中，我们可以为每个路由添加任意数量的中间件。

- **`gin.Default()`默认使用了两个中间件`Logger()`、`Recovery()`**。

- **`gin.New()`一个没有任何默认中间件的路由。**

### 为全局路由注册

```go
package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http"
	"time"
)

func StatCost() gin.HandlerFunc {
	// StatCost 是一个统计耗时请求耗时的中间件
	return func(c *gin.Context) {
		fmt.Println("StatCost in...")
		start := time.Now()
		// 可以通过c.Set在请求上下文中设置值，后续的处理函数能够取到该值
		c.Set("name", "赵子龙")
		// 调用该请求的剩余处理程序
		c.Next()
		// 不调用该请求的剩余处理程序
		// c.Abort()
		// 计算耗时
		cost := time.Since(start)
		fmt.Println("耗时：", cost)
	}
}

func m1(c *gin.Context) {
	fmt.Println("m1 in...")
}

func m2(c *gin.Context) {
	fmt.Println("m2 in...")
}

func main() {
	// 新建一个没有任何默认中间件的路由
	r := gin.New()
	// 注册一个全局中间件
	r.Use(StatCost(), m1, m2)

	r.GET("/test", func(c *gin.Context) {
		name := c.MustGet("name").(string) //从上下文取值
		fmt.Println("name:", name)
		c.JSON(http.StatusOK, gin.H{
			"message": "Hello world!",
		})
	})
	r.Run(":8080")
}
```



### 为某个路由单独注册

```go
package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http"
	"time"


// ...

func m3(c *gin.Context) {
	fmt.Println("m3 in...")
}

func main() {
	// 新建一个没有任何默认中间件的路由
	r := gin.New()
	// 注册一个全局中间件
	r.Use(StatCost(), m1, m2)

	r.GET("/test", func(c *gin.Context) {
		name := c.MustGet("name").(string) //从上下文取值
		fmt.Println("name:", name)
		c.JSON(http.StatusOK, gin.H{
			"message": "Hello world!",
		})
	})

	// 为/test2单独注册路由(可以注册多个)
	r.GET("/test2", m3, func(c *gin.Context) {
		name := c.MustGet("name").(string) //从上下文取值
		fmt.Println("name:", name)
		c.JSON(http.StatusOK, gin.H{
			"message": "Hello world 222!",
		})
	})

	r.Run(":8080")
}

```



### 为路由组注册中间件

为路由组注册中间件有以下两种方式：

方式一：

```go
userGroup := r.Group("/user", StatCost())
{
    userGroup.GET("/index",func(c *gin.Context) {...})
    ...
}
```

方式二：

```go
userGroup := r.Group("/user")
userGroup.Use(StatCost())
{
    userGroup.GET("/index",func(c *gin.Context) {...})
    ...
}
```



## Next()与Abort()

- `Next()`：Next 应该仅可以在中间件中使用，它在调用的函数中的链中执行**挂起**的函数，执行完成下面的函数，会反过来最后执行该中间件。
- `Abort()`：Abort 在被调用的函数中阻止挂起函数。注意这将不会停止当前的函数。例如，你有一个验证当前的请求是否是认证过的 Authorization 中间件。如果验证失败(例如，密码不匹配)，调用 Abort 以确保这个请求的其他函数不会被调用。也就是说执行该函数，会终止后面所有的该请求下的函数。

```go
package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http"
	"time"
)

func StatCost() gin.HandlerFunc {
	// StatCost 是一个统计耗时请求耗时的中间件
	return func(c *gin.Context) {
		fmt.Println("StatCost in...")
		start := time.Now()
		// 可以通过c.Set在请求上下文中设置值，后续的处理函数能够取到该值
		c.Set("name", "赵子龙")
		// 调用该请求的剩余处理程序
		c.Next()
		// 不调用该请求的剩余处理程序
		// c.Abort()
		// 计算耗时
		cost := time.Since(start)
		fmt.Println("耗时：", cost)
	}
}

func m1(c *gin.Context) {
	fmt.Println("m1 in...")
}

func m2(c *gin.Context) {
	c.Abort() //不调用该请求的剩余处理程序
	fmt.Println("m2 in...")
}

func m3(c *gin.Context) {
	fmt.Println("m3 in...")
}

func main() {
	// 新建一个没有任何默认中间件的路由
	r := gin.New()
	// 注册一个全局中间件
	r.Use(StatCost(), m1, m2, m3)

	r.GET("/test", func(c *gin.Context) {
        // 在m2中使用Abort()后，以下代码不会被执行
		name := c.MustGet("name").(string) //从上下文取值
		fmt.Println("name:", name)	
		c.JSON(http.StatusOK, gin.H{
			"message": "Hello world!",
		})
	})

	r.Run(":8080")
}

```

终端输出：

```
StatCost in...
m1 in...
m2 in...
耗时： 226.6µs
```



## 数据传递（获取上下文中的值）

当我们在中间件拦截并预先处理好数据之后，要如何将数据传递我们定义的处理请求的HTTP方法呢？可以使用`gin.Context`中的`Set()`方法，其定义如下，`Set()`通过一个key来存储作何类型的数据，方便下一层处理方法获取。

```go
func (c *Context) Set(key string, value interface{})
```

当我们在中间件中通过Set方法设置一些数值，在下一层中间件或HTTP请求处理方法中，可以使用下面列出的方法通过key获取对应数据。其中，gin.Context的Get方法返回`interface{}`，通过返回exists可以判断key是否存在。

```go
func (c *Context) Get(key string) (value interface{}, exists bool)
```

- 在中间件中设置值：

	```go
	func m1(c *gin.Context){
	    //...
	    c.Set("key","value")
	    //...
	}
	```

- 获取中间件中上下文设置过的值：

	两种方式：

	```go
	type any interface{}
	func (c *Context) MustGet(key string) any{...}
	func (c *Context) Get(key string) (value any, exists bool){...}
	```

	

	```go
	func m2(c *gin.Context){
	    //方式一：
	    v1 := c.MustGet("key").(string)
	    //方式二：
	    v2, isExists := c.Get("key")
	    if !isExists{
	        fmt.Println("该值不存在")
	    }
	}
	```

- 当我们确定通过Get方法获取应数据类型的值(`interface{}类型`)时，除了Get方法，还有下面的方法获取相应类型的值：

	```go
	func (c *Context) GetBool(key string) (b bool)
	func (c *Context) GetDuration(key string) (d time.Duration)
	func (c *Context) GetFloat64(key string) (f64 float64)
	func (c *Context) GetInt(key string) (i int)
	func (c *Context) GetInt64(key string) (i64 int64)
	func (c *Context) GetString(key string) (s string)
	func (c *Context) GetStringMap(key string) (sm map[string]interface{})
	func (c *Context) GetStringMapString(key string) (sms map[string]string)
	func (c *Context) GetStringMapStringSlice(key string) (smss map[string][]string)
	func (c *Context) GetStringSlice(key string) (ss []string)
	func (c *Context) GetTime(key string) (t time.Time)
	```



实例：

```go
package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http"
	"time"
)

func StatCost() gin.HandlerFunc {
	// StatCost 是一个统计耗时请求耗时的中间件
	return func(c *gin.Context) {
		fmt.Println("StatCost in...")
		start := time.Now()
		// 可以通过c.Set在请求上下文中设置值，后续的处理函数能够取到该值
		c.Set("name", "赵子龙")
		// 调用该请求的剩余处理程序
		c.Next()
		// 不调用该请求的剩余处理程序
		// c.Abort()
		// 计算耗时
		cost := time.Since(start)
		fmt.Println("耗时：", cost)
	}
}

func m1(c *gin.Context) {
	c.Set("valueM1", "m1中的值")
	fmt.Println("m1 in...")
}

func m2(c *gin.Context) {
	//c.Abort() //不调用该请求的剩余处理程序
	c.Set("valueM2", "m2中的值")
	fmt.Println("m2 in...")
}

func m3(c *gin.Context) {
	c.Set("valueM3", "m3中的值")
	fmt.Println("m3 in...")
}

func main() {
	// 新建一个没有任何默认中间件的路由
	r := gin.New()
	// 注册一个全局中间件
	r.Use(StatCost(), m1, m2, m3)

	r.GET("/test", func(c *gin.Context) {
		//从上下文取值
		name := c.MustGet("name").(string)
		valueM1 := c.MustGet("valueM1")
		valueM2, _ := c.Get("valueM2")
		valueM3, _ := c.Get("valueM3")

		fmt.Println("name:", name)
		fmt.Println("valueM1:", valueM1)
		fmt.Println("valueM2:", valueM2)
		fmt.Println("valueM3:", valueM3)
		c.JSON(http.StatusOK, gin.H{
			"message": "Hello world!",
		})
	})

	r.Run(":8080")
}

```

终端输出：

```
StatCost in...
m1 in...
m2 in...
m3 in...
name: 赵子龙
valueM1: m1中的值
valueM2: m2中的值
valueM3: m3中的值
耗时： 779.4µs
```



## 中间件注意事项

### gin默认中间件

`gin.Default()`默认使用了`Logger`和`Recovery`中间件，其中：

- `Logger`中间件将日志写入`gin.DefaultWriter`，即使配置了`GIN_MODE=release`。
- `Recovery`中间件会recover任何`panic`。如果有panic的话，会写入500响应码。

如果不想使用上面两个默认的中间件，可以使用`gin.New()`新建一个没有任何默认中间件的路由。

### gin中间件中使用goroutine

当在中间件或`handler`中启动新的`goroutine`时，**不能使用**原始的上下文（c *gin.Context），必须使用其只读副本（`c.Copy()`）。见前面章节的**同步异步**。



# 运行多个服务

可以利用`errgroup.Group`在多个端口运行多个服务。或者自行开启多个`goroutine`分别启动多个服务

安装`errgroup`：

```shell
go get -u golang.org/x/sync/errgroup
```

使用：

```go
package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"golang.org/x/sync/errgroup"
	"net/http"
)

var g errgroup.Group

func router1() http.Handler {
	engine := gin.Default()
	engine.GET("/", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"code":    http.StatusOK,
			"message": "Welcome server 01",
		})
	})
	return engine
}

func router2() http.Handler {
	engine := gin.Default()
	engine.GET("/", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"code":    http.StatusOK,
			"message": "Welcome server 02",
		})
	})
	return engine
}

func main() {
	server1 := &http.Server{
		Addr:    ":8080",
		Handler: router1(),
	}
	server2 := &http.Server{
		Addr:    ":8081",
		Handler: router2(),
	}
	// 借助 errgroup.Group或者自行开启两个goroutine分别启动两个服务
	g.Go(func() error {
		return server1.ListenAndServe()
	})

	g.Go(func() error {
		return server2.ListenAndServe()
	})

	err := g.Wait()
	if err != nil {
		fmt.Println("err:", err.Error())
	}

}

```

