# 1	安装工具：

**安装编译器：**

```
https://github.com/protocolbuffers/protobuf/releases
```

**配置环境变量：将解压过后的`bin`文件夹路径加入到系统的`Path`**

**安装`go`专用的`protoc`的生成器：**

```
go get -u github.com/golang/protobuf/protoc-gen-go
```

安装后会在`GOPATH`目录下生成可执行文件，`protobuf`的编译器插件`protoc-gen-go.exe`，执行`protoc`，命令会自动调用这个插件。

**安装`grpc`：**

```shell
go get -u google.golang.org/grpc
```

**安装第三方库：**

```
go install github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway@latest
go install github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger@latest
go install github.com/golang/protobuf/protoc-gen-go@latest
( 或者go install google.golang.org/protobuf@latest)
go install github.com/envoyproxy/protoc-gen-validate@latest(外部终端)
go get -u github.com/envoyproxy/protoc-gen-validate@latest（内部终端）
```



```
# 生成*.pb.go
protoc --go_out=plugins=grpc:../(目标文件夹) *.proto
# 生成包含数据验证的*pb.validate.go
protoc --go_out=plugins=grpc:../(目标文件夹) --validate_out=lang=go:../(目标文件夹) *.proto
# 生成 *.pb.gw.go
protoc --grpc-gateway_out=logtostderr=true:../(目标文件夹) *.proto
```





# 2	创建和编译proto文件：

**创建proto文件**

```protobuf
// 指定当前proto语法的版本，有proto2和proto3
syntax = "proto3";
//option go_package = "path;name"; path表示生成的go文件的存放地址，会自动生成目录的
//name 表示生成的go文件所属的包名
option go_package = "../service";
//指定*.pb.go文件生成出来的package，一般与上面的path相同
package service;

// 消息 传输对象
message User{
  string username = 1;
  int32 age = 2;
}
```

**编译`*.proto`文件：**

```
protoc --go_out=../service *.proto	//生成 *.pb.go
//含有grpc服务主体
protoc --go_out=plugins=grpc:../(目标文件夹) *.proto
```

# 3	序列化与反序列化：

**序列化：**将数据结构或对象转换成二进制串的过程。

**反序列化：**将在序列化过程中所产生的二进制串转换成数据结构或对象的过程。

```go
// demo
func main() {
	user := &service.User{
		Username: "zhongxi",
		Age:      22,
	}

	// 序列化的过程
	marshal, err := proto.Marshal(user)
	if err != nil {
		panic(err)
	}

	// 反序列化过程
	newUser := &service.User{}
	err = proto.Unmarshal(marshal, newUser)
	if err != nil {
		panic(err)
	}
	fmt.Println(newUser.String())
}

```

# 4	proto文件介绍：

```protobuf
// 指定当前proto语法的版本，有proto2和proto3
syntax = "proto3";
//option go_package = "path;name"; path表示生成的go文件的存放地址，会自动生成目录的
//name 表示生成的go文件所属的包名
option go_package = "../service";
//指定*.pb.go文件生成出来的package，一般与上面的path相同
package service;
```

## 4.1	message：

**`message`:** `protobuf`中定义一个消息类型是通过关键字`message`字段指定的。**消息**就是需要传输的数据格式的定义。

`message`关键字类似于`C++`和`Java`中的`class`，`go`中的`struct`。

例如：

```protobuf
message User{
	string username = 1;
	int32 age = 2;
}
```

在消息中承载的数据分别对应于每个字段，其中每个字段都有一个名字和一种类型。

## 4.2 	字段规则：

- **`required`：**proto2版本消息体中必填字段，不设置会导致编译解码异常，proto3版本可忽略。
- **`optional`：**消息体中可选字段。编译后在go中对应的指针类型。
- **`repeated`：**消息体中可重复字段，重复的值的顺序会被保留在go中，重复的会被定义为切片。

```protobuf
message User{
  string username = 1;
  int32 age = 2;
  optional string password = 3;
  repeated string addresses = 4;
}
```

## 4.3	字段映射：

| .proto Type | Notes                                                        | C++ Type | Python Type | Go Type |
| :---------: | ------------------------------------------------------------ | -------- | ----------- | ------- |
|   double    |                                                              | double   | float       | float64 |
|    float    |                                                              | float    | float       | float32 |
|    int32    | 使用变长编码，对于负值的效率很低，如果域有可能有负值，请使用sint64替代 | int32    | int         | int32   |
|   uint32    | 使用变长编码                                                 | int32    | int/long    | uint32  |
|    unit     | 使用变长编码                                                 | uint32   | int/long    | uint64  |
|   sint32    | 使用变长编码，这些编码在负值时比int32高效得多                | int32    | int         | int32   |
|   sint64    | 使用变长编码，有符号的整型值。编码时比通常的int64高效。      | int64    | int/long    | int64   |
|   fixed32   | 总是4个字节，如果数值总是比228大的话，这个类型会比uint32高效。 | uint32   | int         | uint32  |
|   fixed64   | 总是8个字节，如果数值总是比256大的话，这个类型会比uint64高效。 | uint64   | int/long    | uint64  |
|  sfixed32   | 总是4个字节                                                  | int32    | int         | int32   |
|  sfixed64   | 总是8个字节                                                  | int64    | int/long    | int64   |
|    bool     | 布尔类型                                                     | bool     | bool        | bool    |
|   string    | 一个字符串必须是UTF-8编码或者7-bit ASCII编码的文本。         | string   | str/unicode | string  |
|    bytes    | 可能包含任意顺序的字节数据。                                 | string   | str         | []byte  |



## 4.4	默认值：

`protobuf3`删除了`protobuf2`中用来设置默认值的`default`关键字，取而代之的是`protobuf3`为各类型定义的默认值，也就是约定的默认值，如下表所示：

| 类型     | 默认值                                                       |
| -------- | ------------------------------------------------------------ |
| bool     | false                                                        |
| 类型     | 0                                                            |
| string   | 空字符串""                                                   |
| 枚举enum | 第一个枚举元素的值，因为Protobuf3强制要求第一个枚举元素的值必须是0，所以枚举的默认值就是0 |
| message  | 不是null，而是DEFAULT_INSTANCE                               |

## 4.5	标识号：

**标识号：**在消息体的定义中，每个字段都必须要有一个唯一的标识号，标识号是`[0,2^29-1]`范围内的一个整数。

```protobuf
message Person{
	string name = 1;
	int32 id = 2;
	optional string email = 3;
	repeated string phone = 4;
}
```

上面`name = 1`，`id = 2`，`email = 3`，`phones = 4`中的1,2,3,4就是标识号。

## 4.6	定义多个消息类型：

一个proto文件中可以定义多个消息类型：

```protobuf
message UserRequest{
  string username = 1;
  int32 age = 2;
  optional string password = 3;
  repeated string addresses = 4;
}

message UserResponse{
  string username = 1;
  int32 age = 2;
  optional string password = 3;
  repeated string addresses = 4;
}
```

## 4.7	嵌套消息：

可以在消息类型中定义、使用其他消息类型，下面的例子中，`Person`消息就定义在`PersonInfo`消息内：

```protobuf
message PersonInfo{
  message Person{
    string name = 1;
    int32 height = 2;
    repeated int32 weight = 3;
  }
  repeated Person info = 1;
}
```

如果想在`Person`的父消息类型的外部使用这个消息类型，需要以`PersonInfo.Person`的形式使用它：

```protobuf
message PersonMessage{
  PersonInfo.Person info = 1;
}
```

当然，也可以将消息嵌套任意多层，如 :

~~~protobuf
message Grandpa { // Level 0
    message Father { // Level 1
        message son { // Level 2
            string name = 1;
            int32 age = 2;
    	}
	} 
    message Uncle { // Level 1
        message Son { // Level 2
            string name = 1;
            int32 age = 2;
        }
    }
}
~~~

## 4.8	定义服务(Service)

如果想要将消息类型用在RPC系统中，可以在.proto文件中定义一个RPC服务接口，protocol buffer 编译器将会根据所选择的不同语言生成服务接口代码及存根。

```protobuf
// 定义了一个RPC服务，该方法接收SearchRequest返回SearchResponse
service SearchService {
	//rpc 服务的函数名 （传入参数）返回（返回参数）
	rpc Search (SearchRequest) returns (SearchResponse);
}
```



# 5	gRPC实例

## 5.1	项目文件目录结构：

- `cert`
- `client`
	- `auth`
	- `service`
		- `product.pb.go`
		- `product_grpc.pb.go`
	- `grpc_client.go`
- `pbfiles`
	- `product.proto`
	- `user.proto`
- `service`
	- `product.go`
	- `prodict.pb.go`
	- `prodict_grpc.pb.go`
	- `user.pb.go`
- `grpc_server.go`



## 5.2	RPC和gRPC：

RPC（Remote Procedure Call）远程过程调用协议，一种通过网络从远程计算机上请求服务，而不需要了解底层网络技术的协议。RPC它假定某些协议的存在，例如TCP/UDP等，为通信程序之间携带信息数据。在OSI网络七层模型中，RPC跨越了传输层和应用层，RPC使得开发包括网络分布式多程序在内的应用程序更加容易。

过程是什么？ 过程就是业务处理、计算任务，更直白的说，就是程序，就是像调用本地方法一样调用远程的过程。RPC采用客户端/服务端的模式，通过request-response消息模式实现。

gRPC 里**客户端**应用可以像调用本地对象一样直接调用另一台不同的机器上**服务端**应用的方法，使得您能够更容易地创建分布式应用和服务。与许多 RPC 系统类似，gRPC 也是基于以下理念：定义一个**服务**，指定其能够被远程调用的方法（包含参数和返回类型）。在服务端实现这个接口，并运行一个 gRPC 服务器来处理客户端调用。在客户端拥有一个**存根**能够像服务端一样的方法。

官方网站：https://grpc.io/

底层协议：

* HTTP2: https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md
* GRPC-WEB ： https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-WEB.md



## 5.3	实例：

### 5.2.1	服务端：

`pbfiles`文件夹下面创建`product.proto`文件：

```protobuf
// 这个就是protobuf的中间文件

// 指定的当前proto语法的版本，有2和3
syntax = "proto3";
option go_package="../service";

// 指定等会文件生成出来的package
package service;

// 定义request model
message ProductRequest{
  int32 prod_id = 1; // 1代表顺序
}

// 定义response model
message ProductResponse{
  int32 prod_stock = 1; // 1代表顺序
}

// 定义服务主体
service ProdService{
  // 定义方法
  rpc GetProductStock(ProductRequest)
  returns(ProductResponse);
}
```

进入到`pbfile`文件夹下面进行编译：

```shell
protoc --go_out=plugins=grpc:../service product.proto
```

服务端：

`grpc_server.go`

```go
// grpc_server.go
func main() {
	rpcServer := grpc.NewServer()

	//注册服务端
	service.RegisterProdServiceServer(rpcServer, service.ProductService)
	//启动监听
	listener, err := net.Listen("tcp", ":8080")
	if err != nil {
		log.Fatal("启动监听出错", err)
	}
	//启动服务
	err = rpcServer.Serve(listener)
	if err != nil {
		log.Fatal("启动服务出错", err)
	}
	fmt.Println("启动grpc服务端成功！")
}
```

`service/product.go`

```go
// service/product.go
type productService struct {
}

var ProductService = &productService{}

func (p *productService) GetProductStock(c context.Context, r *ProductRequest) (*ProductResponse, error) {
	// 实现具体的业务逻辑
	stock := p.GetStockById(r.ProdId) //根据id返回库存
	return &ProductResponse{ProdStock: stock}, nil
}

func (p *productService) GetStockById(id int32) int32 {
	return 100
}
```

### 5.2.2	客户端：

新建`client/service`目录，把上述生成的`product.pb.go` 复制过来

```go
// grpc_client.go
package main

import (
	"context"
	"fmt"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
	"log"
	"ms-proto/service"
)

func main() {
	// 1. 新建连接，端口是服务端开放的8080端口
	// 没有证书会报错
	conn, err := grpc.Dial(":8080", grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatal("服务端出错，连接不上", err)
	}

	//退出时关闭链接
	defer conn.Close()

	// 2. 调用Product.pb.go中的NewProdServiceClient方法
	productServiceClient := service.NewProdServiceClient(conn)

	// 3. 直接像调用本地方法一样调用GetProductStock方法
	requset := &service.ProductRequest{ProdId: 123}
	response, err3 := productServiceClient.GetProductStock(context.Background(), requset)
	if err3 != nil {
		log.Fatal("查询库存出错: ", err3)
	}

	fmt.Println("查询成功，ProdStock = ", resp.ProdStock)
}
```







# 6	认证（生成SAN证书）

安装`openssl`，网站下载：http://slproweb.com/products/Win32OpenSSL.html

配置环境变量：将bin目录配置到系统的环境变量中。

**go 1.17版本后都需要使用SAN证书。**

```
key：服务器上的私钥文件，用于对发送给客户端数据的加密，以及对从客户端接收到数据的解密。
csr：证书签名请求文件，用于提交给证书颁发机构（CA）对证书签名。
crt：由证书颁发机构（CA）签名后的证书，或者是开发者自签名的证书，包含证书持有人的信息，持有人的公钥，以及签署者的签名等信息。
pem：是基于Base64编码的证书格式，扩展名包括PEM、CRT和CER。
```

**1.创建一个用于存放证书的目录，并将`openssl`安装目录的`bin`目录下的`openssl.cnf`文件拷贝到该目录。**

**2.生成私钥文件`ca.key`：**

当前目录下进入`cmd`

```shell
## 需要输人密码
openssl genrsa -des3 -out ca.key 2048
```

**3.生成公钥：**

- **创建证书请求，生成`ca.csr`：**

	```shell
	openssl req -new -key ca.key -out ca.csr
	```

- **生成`ca.crt`：**

	```shell
	openssl x509 -req -days 365 -in ca.csr -signkey ca.key -out ca.crt
	```

**4.修改`openssl.cnf`文件配置：**

```
1. 取消 copy_extensions = copy 前的注释符号 '#'
2. 取消 req_extensions = v3_req 前的注释符号 '#'
3. 找到 [ v3_req ]，添加 subjectAltName = @alt_names
4. 添加新的标签 [ alt_names ]，和标签字段：
	DNS.1 = *.zhongxi.com
	DNS.2 = *.org.zhongxi.com	// 可选
```

**5.生成证书私钥`server.key`：**

```shell
openssl genpkey -algorithm RSA -out server.key
```

**6.通过私钥`server.key`生成证书请求文件`server.csr`：**

```shell
openssl req -new -nodes -key server.key -out server.csr -days 3650 -config ./openssl.cnf -extensions v3_req
```

**7.生成SAN证书：**

```shell
openssl x509 -req -days 365 -in server.csr -out server.pem -CA ca.crt -CAkey ca.key -CAcreateserial -extfile ./openssl.cnf -extensions v3_req
```

**什么是SAN？**

SAN（Subject Alternative Name）是 SSL 标准 x509 中定义的一个扩展。使用了 SAN 字段的 SSL 证书，可以扩展此证书支持的域名，使得一个证书可以支持多个不同域名的解析。

--------------------------------------------------------------------------------------------------------------------------------------



**方式二生成SAN：**

1.把`openssl.cnf`拷贝到证书存放目录，并配置`openssl.cnf`：

```
找到 [ CA_default ], 取消 copy_extensions = copy 的注释
找到 [ req ]，取消 req_extension = v3_req 的注释
找到 [ v3_req ]，添加 subjectAltName = @alt_names
添加新的标签 [ alt_names ]，并添加标签字段
DNS.1 = localhost
```

2.生成`CA`根证书：

```
# 生成 ca.key
OpenSSL> genrsa -des3 -out ca.key 2048

# 生成 ca.pem
OpenSSL> req -new -x509 -days 365 -key ca.key -out ca.pem
或者
# 生成 ca.crt
OpenSSL> req -new -x509 -key ca.key -out ca.crt -days 365

(# 生成 ca.csr
OpenSSL> req -new -key ca.key -out ca.csr)
```

3.生成证书私钥`server.key` 和`client.key`：

```
OpenSSL> genpkey -algorithm RSA -out server.key
OpenSSL> genpkey -algorithm RSA -out client.key
```

4.通过私钥`server.key`和`client.key`生成证书请求文件`server.csr`和`client.csr`：

```
C  => Country
ST => State
L  => City
O  => Organization
OU => Organization Unit
CN => Common Name (证书所请求的域名)
```

```
OpenSSL> req -new -nodes -key server.key -out server.csr -days 365 -subj "/CN=localhost" -config D:\DevelopmentSoftWare\OpenSSL-Win64\SAN\openssl.cnf -extensions v3_req

OpenSSL> req -new -nodes -key client.key -out client.csr -days 365 -subj "/CN=localhost" -config D:\DevelopmentSoftWare\OpenSSL-Win64\SAN\openssl.cnf -extensions v3_req
```

5.生成`SAN`证书`server.pem`和`client.pem`：

```
OpenSSL> x509 -req -days 365 -in server.csr -out server.pem -CA ca.pem -CAkey ca.key -CAcreateserial -extfile D:\DevelopmentSoftWare\OpenSSL-Win64\SAN\openssl.cnf -extensions v3_req

OpenSSL> x509 -req -days 365 -in client.csr -out client.pem -CA ca.pem -CAkey ca.key -CAcreateserial -extfile D:\DevelopmentSoftWare\OpenSSL-Win64\SAN\openssl.cnf -extensions v3_req
```

6.将`test.key`和`test.pem`拷贝到项目新建文件夹`keys`下，并加载服务端和客户端代码：

```go
// 服务端
creds, err := credentials.NewServerTLSFromFile("test.pem", "test.key")
// 客户端
creds,err := credentials.NewClientTLSFromFile("test.pem","*.org.zhongxi.com")
```



# 7	应用证书

## 7.1	单向认证

### 7.1.1	服务端应用证书

**使用到`server.key`和`server.pem`**

```go
// grpc_server.go
package main

import (
	"fmt"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
	"log"
	"ms-proto/service"
	"net"
)

func main() {
	// 添加证书
	creds, err := credentials.NewServerTLSFromFile("cert/server.pem", "cert/server.key")
	if err != nil {
		log.Fatal("证书生成错误", err)
	}
	//创建gRPC实例，将服务注册到gRPC服务器上
	rpcServer := grpc.NewServer(grpc.Creds(creds))
	service.RegisterProdServiceServer(rpcServer, service.ProductService)
	//启动监听
	listener, err := net.Listen("tcp", ":8080")
	if err != nil {
		log.Fatal("启动监听出错", err)
	}
	//启动服务
	err = rpcServer.Serve(listener)
	if err != nil {
		log.Fatal("启动服务出错", err)
	}
	fmt.Println("启动grpc服务端成功！")
}

```

### 7.1.2	客户端应用证书

**使用到`server.pem`**

```go
package main

import (
	"context"
	"fmt"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
	"log"
	"ms-proto/service"
)

func main() {
	// 添加证书
	creds, err1 := credentials.NewClientTLSFromFile("cert/server.pem", "*.zhongxi.com")
	if err1 != nil {
		log.Fatal("证书错误", err1)
	}
	// 1. 新建连接，端口是服务端开放的8080端口
	// 无认证
	//conn, err2 := grpc.Dial(":8080", grpc.WithTransportCredentials(insecure.NewCredentials()))
	// 有认证
	conn, err2 := grpc.Dial(":8080", grpc.WithTransportCredentials(creds))
	if err2 != nil {
		log.Fatal("服务端出错，连接不上", err2)
	}

	//退出时关闭链接
	defer conn.Close()

	// 2. 调用Product.pb.go中的NewProdServiceClient方法
	productServiceClient := service.NewProdServiceClient(conn)

	// 3. 直接像调用本地方法一样调用GetProductStock方法
	requset := &service.ProductRequest{ProdId: 123}
	response, err3 := productServiceClient.GetProductStock(context.Background(), requset)
	if err3 != nil {
		log.Fatal("查询库存出错: ", err3)
	}

	fmt.Println("查询成功，ProdStock = ", resp.ProdStock)
}
```



## 7.2	双向认证

**客户端生成公钥和私钥**

**1.私钥:**

```shell
openssl genpkey -algorithm RSA -out client.key
```

**2.证书请求文件：**

```shell
openssl req -new -nodes -key client.key -out client.csr -days 3650 -config ./openssl.cnf -extensions v3_req
```

**3.SAN证书：**

```shell
openssl x509 -req -days 365 -in client.csr -out client.pem -CA ca.crt -CAkey ca.key -CAcreateserial -extfile ./openssl.cnf -extensions v3_req
```

### 7.2.1	服务端应用证书：

```go
package main

import (
	"crypto/tls"
	"crypto/x509"
	"fmt"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
	"io/ioutil"
	"log"
	"ms-proto/service"
	"net"
)

func main() {
	// 添加证书-双向认证
	// 从证书相关文件中读取和解析信息，得到证书公钥、密钥对
	cert, err1 := tls.LoadX509KeyPair("cert/server.pem", "cert/server.key")
	if err1 != nil {
		log.Fatal("证书读取错误", err1)
	}
	// 创建一个新的、空的 CertPool
	certPool := x509.NewCertPool()
	ca, err2 := ioutil.ReadFile("cert/ca.crt")
	if err2 != nil {
		log.Fatal("ca证书读取错误", err2)
	}
	// 尝试解析所传入的 PEM 编码的证书，如果解析成功会将其加到 CertPool 中，便于后面的使用
	certPool.AppendCertsFromPEM(ca)
	// 构建基于 TLS 的 TransportCredentials 选项
	creds := credentials.NewTLS(&tls.Config{
		//设置证书链，允许包含一个或多个
		Certificates: []tls.Certificate{cert},
		//要求必须校验客户端的证书，可以根据实际情况选用以下参数
		ClientAuth: tls.RequireAndVerifyClientCert,
		//设置根证书的集合，校验方式使用 ClientAuth 中设定的模式
		ClientCAs: certPool,
	})

	//创建gRPC实例，将服务注册到gRPC服务器上
	rpcServer := grpc.NewServer(grpc.Creds(creds))
	service.RegisterProdServiceServer(rpcServer, service.ProductService)
	//启动监听
	listener, err := net.Listen("tcp", ":8080")
	if err != nil {
		log.Fatal("启动监听出错", err)
	}
	//启动服务
	err = rpcServer.Serve(listener)
	if err != nil {
		log.Fatal("启动服务出错", err)
	}
	fmt.Println("启动grpc服务端成功！")
}

```



### 7.2.2	客户端应用证书：

```go
package main

import (
	"context"
	"crypto/tls"
	"crypto/x509"
	"fmt"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
	"io/ioutil"
	"log"
	"ms-proto/service"
)

func main() {
	// 添加证书-双向认证
	// 从证书相关文件中读取和解析信息，得到证书公钥、密钥对
	cert, err1 := tls.LoadX509KeyPair("cert/client.pem", "cert/client.key")
	if err1 != nil {
		log.Fatal("证书读取错误", err1)
	}
	// 创建一个新的、空的 CertPool
	certPool := x509.NewCertPool()
	ca, err2 := ioutil.ReadFile("cert/ca.crt")
	if err2 != nil {
		log.Fatal("ca证书读取错误", err2)
	}
	// 尝试解析所传入的 PEM 编码的证书，如果解析成功会将其加到 CertPool 中，便于后面的使用
	certPool.AppendCertsFromPEM(ca)
	// 构建基于 TLS 的 TransportCredentials 选项
	creds := credentials.NewTLS(&tls.Config{
		//设置证书链，允许包含一个或多个
		Certificates: []tls.Certificate{cert},
		//要求必须校验客户端的证书，可以根据实际情况选用以下参数
		ServerName: "*.zhongxi.com",
		RootCAs:    certPool,
	})

	// 1. 新建连接，端口是服务端开放的8080端口
	// 无认证
	//conn, err2 := grpc.Dial(":8080", grpc.WithTransportCredentials(insecure.NewCredentials()))
	// 有认证
	conn, err2 := grpc.Dial(":8080", grpc.WithTransportCredentials(creds))
	if err2 != nil {
		log.Fatal("服务端出错，连接不上", err2)
	}

	//退出时关闭链接
	defer conn.Close()

	// 2. 调用Product.pb.go中的NewProdServiceClient方法
	productServiceClient := service.NewProdServiceClient(conn)

	// 3. 直接像调用本地方法一样调用GetProductStock方法
	requset := &service.ProductRequest{ProdId: 123}
	response, err3 := productServiceClient.GetProductStock(context.Background(), requset)
	if err3 != nil {
		log.Fatal("查询库存出错: ", err3)
	}

	fmt.Println("查询成功，ProdStock = ", resp.ProdStock)
}
```



## 7.3	Token认证

### 7.3.1	服务端添加用户名密码的校验

需要实现一个拦截器：

```go
type UnaryServerInterceptor func(ctx context.Context, req interface{}, info *UnaryServerInfo, handler UnaryHandler) (resp interface{}, err error)
```

再实现一个认证方法`Auth`：

```go
func Auth(ctx context.Context) error {
	// 实际上，就是拿到传输的用户名和密码
	md, ok := metadata.FromIncomingContext(ctx)
	if !ok {
		return fmt.Errorf("missing credentials")
	}
	var user string
	var password string

	if val, ok := md["user"]; ok {
		user = val[0]
	}
	if val, ok := md["password"]; ok {
		password = val[0]
	}
	if user != "admin" || password != "admin" {
		return status.Errorf(codes.Unauthenticated, "token不合法")
	}
	return nil
}

```

**应用：**

```go
// grpc_server.go
package main

import (
	"context"
	"fmt"
	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/metadata"
	"google.golang.org/grpc/status"
	"log"
	"ms-proto/service"
	"net"
)

func main() {
	// 实现token认证，需要合法的用户名和密码
	//实现一个拦截器
	var authInterceptor grpc.UnaryServerInterceptor
	authInterceptor = func(
		ctx context.Context,
		req interface{},
		info *grpc.UnaryServerInfo,
		handler grpc.UnaryHandler,
	) (resp interface{}, err error) {
		// 拦截普通方法请求，验证Token
		err = Auth(ctx)
		if err != nil {
			return
		}
		//继续处理请求
		return handler(ctx, req)
	}
	//----------------------------------------
	//创建gRPC实例，将服务注册到gRPC服务器上
	//rpcServer := grpc.NewServer(grpc.Creds(creds))
	//token认证
	rpcServer := grpc.NewServer(grpc.UnaryInterceptor(authInterceptor))

	service.RegisterProdServiceServer(rpcServer, service.ProductService)
	//启动监听
	listener, err := net.Listen("tcp", ":8080")
	if err != nil {
		log.Fatal("启动监听出错", err)
	}
	//启动服务
	err = rpcServer.Serve(listener)
	if err != nil {
		log.Fatal("启动服务出错", err)
	}
	fmt.Println("启动grpc服务端成功！")
}

func Auth(ctx context.Context) error {
	// 实际上，就是拿到传输的用户名和密码
	md, ok := metadata.FromIncomingContext(ctx)
	if !ok {
		return fmt.Errorf("missing credentials")
	}
	var user string
	var password string

	if val, ok := md["user"]; ok {
		user = val[0]
	}
	if val, ok := md["password"]; ok {
		password = val[0]
	}
	if user != "admin" || password != "admin" {
		return status.Errorf(codes.Unauthenticated, "token不合法")
	}
	return nil
}

```

### 7.3.2	客户端实现

**客户端需要实现`PerRPCCredentials`接口：**

```go
type PerRPCCredentials interface {
	// GetRequestMetadata gets the current request metadata, refreshing
	// tokens if required. This should be called by the transport layer on
	// each request, and the data should be populated in headers or other
	// context. If a status code is returned, it will be used as the status
	// for the RPC. uri is the URI of the entry point for the request.
	// When supported by the underlying implementation, ctx can be used for
	// timeout and cancellation. Additionally, RequestInfo data will be
	// available via ctx to this call.
	// TODO(zhaoq): Define the set of the qualified keys instead of leaving
	// it as an arbitrary string.
	GetRequestMetadata(ctx context.Context, uri ...string) (map[string]string, error)
	// RequireTransportSecurity indicates whether the credentials requires
	// transport security.
	RequireTransportSecurity() bool
}
```

`GetRequestMetadata` 方法返回认证需要的必要信息，`RequireTransportSecurity` 方法表示是否启用安全链接，在生产环境中，一般都是启用的，但为了测试方便，暂时这里不启用了。

**实现接口：**

在`client/auth`文件夹下创建一个`auth.go`：

```go
package auth

import "context"

type Authentication struct {
	User     string
	Password string
}

func (a *Authentication) GetRequestMetadata(context.Context, ...string) (map[string]string, error) {
	return map[string]string{
		"user":     a.User,
		"password": a.Password,
	}, nil
}

func (a *Authentication) RequireTransportSecurity() bool {
	//一般开启，此处暂不开启
	return false
}

```

**应用：**

```go
// grpc_client.go
package main

import (
	"context"
	"fmt"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
	"log"
	"ms-proto/client/auth"
	"ms-proto/service"
)

func main() {
	//token认证
	token := &auth.Authentication{
		User:     "admin",
		Password: "admin",
	}

	// 1. 新建连接，端口是服务端开放的8080端口
	// 无认证
	//conn, err2 := grpc.Dial(":8080", grpc.WithTransportCredentials(insecure.NewCredentials()))
	// 有认证
	//conn, err2 := grpc.Dial(":8080", grpc.WithTransportCredentials(creds))
	conn, err2 := grpc.Dial(":8080",
		grpc.WithTransportCredentials(insecure.NewCredentials()), grpc.WithPerRPCCredentials(token))
	if err2 != nil {
		log.Fatal("服务端出错，连接不上", err2)
	}

	//退出时关闭链接
	defer conn.Close()

	// 2. 调用Product.pb.go中的NewProdServiceClient方法
	productServiceClient := service.NewProdServiceClient(conn)

	// 3. 直接像调用本地方法一样调用GetProductStock方法
	requset := &service.ProductRequest{ProdId: 123}
	response, err3 := productServiceClient.GetProductStock(context.Background(), requset)
	if err3 != nil {
		log.Fatal("查询库存出错: ", err3)
	}

	fmt.Println("查询成功，ProdStock = ", resp.ProdStock)
}

```



# 8	新版本编译器

前面使用的proto的go生成器，安装的编译器是：

```shell
go get -u github.com/golang/protobuf/protoc-gen-go
```

新的方式，需要使用`--go_out=plugins=grpc` 来去进行生成，而在`golang.org`方式中，弃用了这种方式，使用`protoc-gen-go`将不在支持`gRPC service`的定义，需要使用新的插件`protoc-gen-go-grpc`。

## 8.1	使用google.golang.org/protobuf

1.安装最新版本的插件：

```shell
$ go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
$ go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
```

安装完成后会在`GOPATH`下的`bin`目录下生成：

```
protoc-gen-go.exe
protoc-gen-go-grpc.exe
```

2.利用`proto`文件重新生成go文件：

```shell
protoc  --go_out=./service --go-grpc_out=./service  pbfiles\product.proto
```

在`server`文件夹下会生成：

```
product.pb.go
product_grpc.pb.go
```



## 8.2	import的使用

在`product.proto`中的`message ProductRespone`中使用`user.proto`中的`message User`，需要用`import`导入其路径：

```protobuf
// product.proto
syntax = "proto3";

import "pbfiles/user.proto";

option go_package="../service";
package service;
//...
message ProductResponse{
  int32 prod_stock = 1; // 1代表顺序
  User user = 2;  //使用外部文件中的消息
}
//...
```

在`product.go`中应用：

```go
package service

import "context"

type productService struct {
}

var ProductService = &productService{}

func (p *productService) GetProductStock(c context.Context, r *ProductRequest) (*ProductResponse, error) {
	// 实现具体的业务逻辑
	stock := p.GetStockById(r.ProdId) //根据id返回库存
	user := User{Username: "zhongxi"}
	return &ProductResponse{ProdStock: stock, User: &user}, nil
}

func (p *productService) GetStockById(id int32) int32 {
	return id
}

func (p *productService) mustEmbedUnimplementedProdServiceServer() {}


```

客户端`grpc_client.go`修改：

```go
// grpc_client.go
/*
	...
*/

fmt.Println("查询成功，ProdStock = ", response.ProdStock, response.User)
```

## 8.3	Any的使用

以`product.proto`为例，在`product.proto`中导入`google/protobuf/any.proto`，并增加一个`Content`消息，在`ProductResponse`中使用：

```protobuf
// product.proto
// 指定的当前proto语法的版本，有2和3
syntax = "proto3";
import "pbfiles/user.proto";
// 使用Any类型，需要导入这个
import "google/protobuf/any.proto";
option go_package="../service";

// 指定*.pb.go文件生成出来的package
package service;

// 定义request model
message ProductRequest{
  int32 prod_id = 1; // 1代表顺序
}

message Content{
  string msg = 1;
}

// 定义response model
message ProductResponse{
  int32 prod_stock = 1; // 1代表顺序
  User user = 2;  //使用外部文件中的消息
  google.protobuf.Any data = 3;
}

// 定义服务主体
service ProdService{
  // 定义方法
  rpc GetProductStock(ProductRequest) returns(ProductResponse);
}
```

在`product.go`中增加修改：

```go
// product.go
/*
	...
*/

func (p *productService) GetProductStock(c context.Context, r *ProductRequest) (*ProductResponse, error) {
	// 实现具体的业务逻辑
	stock := p.GetStockById(r.ProdId) //根据id返回库存
	user := User{Username: "zhongxi"}
    
	content := Content{Msg: "zhongxi msg..."}
	//转换成any类型
	c_any, _ := anypb.New(&content)
	return &ProductResponse{ProdStock: stock, User: &user, Data: c_any}, nil
}

/*
	...
*/

```

客户端`grpc_client.go`打印修改：

```go
// grpc_client.go
/*
	...
*/
fmt.Println("查询成功，ProdStock = ", response.ProdStock, response.User, response.Data)
```

# 9	stream（流）

在 HTTP/1.1 的时代，同一个时刻只能对一个请求进行处理或者响应，换句话说，下一个请求必须要等当前请求处理完才能继续进行。

```
HTTP/1.1需要注意的是，在服务端没有response的时候，客户端是可以发起多个request的，但服务端依旧是顺序对请求进行处理, 并按照收到请求的次序予以返回。
```

HTTP/2 的时代，多路复用的特性让一次同时处理多个请求成为了现实，并且同一个 TCP 通道中的请求不分先后、不会阻塞，HTTP/2 中引入了流(Stream) 和 帧(Frame) 的概念，当 TCP 通道建立以后，后续的所有操作都是以流的方式发送的，而二进制帧则是组成流的最小单位，属于协议层上的流式传输。

```
HTTP/2 在一个 TCP 连接的基础上虚拟出多个 Stream, Stream 之间可以并发的请求和处理, 并且 HTTP/2 以二进制帧 (frame) 的方式进行数据传送, 并引入了头部压缩 (HPACK), 大大提升了交互效率
```

## 9.1	定义

```protobuf
// 普通 RPC
rpc SimplePing(PingRequest) returns (PingResponse);
// 客户端流式 RPC
rpc ClientStreamPing(stream PingRequest) returns (PingResponse);
// 服务器端流式 RPC
rpc ServerStreamPing(PingRequest) returns (stream PingResponse);
// 双向流式 RPC
rpc BothStreamPing(stream PingRequest) returns (stream PingResponse);
```

`stream`关键字，当该关键字修饰参数时，表示这是一个客户端流式的 `gRPC` 接口；当该参数修饰返回值时，表示这是一个服务器端流式的 `gRPC` 接口；当该关键字同时修饰参数和返回值时，表示这是一个双向流式的 `gRPC` 接口。

## 9.2	客户端流

以`product.proto`为例，在`service ProdService`中添加客户端流定义方法：

```protobuf
// product.proto
// ...
// 定义服务主体
service ProdService{
  // 定义方法
  rpc GetProductStock(ProductRequest) returns(ProductResponse);
  //定义客户端流方法
  rpc UpdateProductStockClientStream(stream ProductRequest) returns(ProductResponse);
}
```

在`product.go`中实现具体的`UpdateProductStockClientStream`方法：

```go
// product.go
func (p *productService) UpdateProductStockClientStream(stream ProdService_UpdateProductStockClientStreamServer) error {
	count := 0
	for {
		// 源源不断地接受客户端发送过来的信息
		recv, err := stream.Recv()
		if err != nil {
			if err == io.EOF {
				return nil
			}
			return err
		}
		fmt.Println("服务端接收到的流", recv.ProdId, count)
		count++
		if count > 10 {
			response := &ProductResponse{ProdStock: recv.ProdId}
			err = stream.SendAndClose(response)
			if err != nil {
				return err
			}
			return nil
		}
	}
}
```

客户端`grpc_client.go`代码修改：

```go
package main

import (
	"context"
	"fmt"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
	"log"
	"ms-proto/client/auth"
	"ms-proto/service"
)

func main() {
	//token认证
	token := &auth.Authentication{
		User:     "admin",
		Password: "admin",
	}

	// 1. 新建连接，端口是服务端开放的8080端口
	//token认证
	conn, err2 := grpc.Dial(":8080",
		grpc.WithTransportCredentials(insecure.NewCredentials()), grpc.WithPerRPCCredentials(token))
	if err2 != nil {
		log.Fatal("服务端出错，连接不上", err2)
	}

	//退出时关闭链接
	defer conn.Close()

	// 2. 调用Product.pb.go中的NewProdServiceClient方法
	productServiceClient := service.NewProdServiceClient(conn)

	// 3. 直接像调用本地方法一样调用GetProductStock方法
	//requset := &service.ProductRequest{ProdId: 123}
	//response, err3 := productServiceClient.GetProductStock(context.Background(), requset)
	//if err3 != nil {
	//	log.Fatal("查询库存出错: ", err3)
	//}
	//
	//fmt.Println("查询成功，ProdStock = ", response.ProdStock, response.User, response.Data)
	stream, err := productServiceClient.UpdateProductStockClientStream(context.Background())
	if err != nil {
		log.Fatal("获取流出错：", err)
	}
	response := make(chan struct{}, 1)
	go prodRequest(stream, response)
	select {
	case <-response:
		recv, err3 := stream.CloseAndRecv()
		if err3 != nil {
			log.Fatal(err3)
		}
		stock := recv.ProdStock
		fmt.Println("客户端收到响应：", stock)
	}
}

func prodRequest(stream service.ProdService_UpdateProductStockClientStreamClient, response chan struct{}) {
	count := 0
	for {
		request := &service.ProductRequest{
			ProdId: 123,
		}
		err := stream.Send(request)
		if err != nil {
			log.Fatal(err)
		}
		//time.Sleep(time.Second)
		count++
		if count > 10 {
			response <- struct{}{}
			break
		}
	}
}

```

## 9.3	服务端流

以`product.proto`为例，在`service ProdService`中添加服务端流定义方法：

```protobuf
// product.proto
// ...
// 定义服务主体
service ProdService{
  // 定义方法
  rpc GetProductStock(ProductRequest) returns(ProductResponse);
  //定义客户端流方法
  rpc UpdateProductStockClientStream(stream ProductRequest) returns(ProductResponse);
  //定义服务端流方法
  rpc GetProductStockServerStream(ProductRequest) returns(stream ProductResponse);
}

```

在`product.go`中实现具体的`GetProductStockServerStream`方法：

```go
func (p *productService) GetProductStockServerStream(request *ProductRequest, stream ProdService_GetProductStockServerStreamServer) error {
	count := 0
	for {
		response := &ProductResponse{ProdStock: request.ProdId}
		err := stream.Send(response)
		if err != nil {
			return nil
		}
		time.Sleep(time.Second)
		count++
		if count > 10 {
			return nil
		}
	}
}
```

客户端`grpc_client.go`代码修改：

```go
package main

import (
	"context"
	"fmt"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
	"io"
	"log"
	"ms-proto/client/auth"
	"ms-proto/service"
	"time"
)

func main() {
	//token认证
	token := &auth.Authentication{
		User:     "admin",
		Password: "admin",
	}

	// 1. 新建连接，端口是服务端开放的8080端口
    //token认证
	conn, err2 := grpc.Dial(":8080",
		grpc.WithTransportCredentials(insecure.NewCredentials()), grpc.WithPerRPCCredentials(token))
	if err2 != nil {
		log.Fatal("服务端出错，连接不上", err2)
	}

	//退出时关闭链接
	defer conn.Close()

	// 2. 调用Product.pb.go中的NewProdServiceClient方法
	productServiceClient := service.NewProdServiceClient(conn)

	// 3. 直接像调用本地方法一样调用GetProductStock方法
	requset := &service.ProductRequest{ProdId: 123}
	//response, err3 := productServiceClient.GetProductStock(context.Background(), requset)
	//if err3 != nil {
	//	log.Fatal("查询库存出错: ", err3)
	//}
	//
	//fmt.Println("查询成功，ProdStock = ", response.ProdStock, response.User, response.Data)
	//
	stream, err := productServiceClient.GetProductStockServerStream(context.Background(), requset)
	if err != nil {
		log.Fatal("获取流出错：", err)
	}
	for {
		recv, err3 := stream.Recv()
		if err3 != nil {
			if err3 == io.EOF {
				fmt.Println("客户端数据接收完成")
				err4 := stream.CloseSend()
				if err != nil {
					log.Fatal(err4)
				}
				break
			}
			log.Fatal(err3)
		}

		fmt.Println("客户端收到的流：", recv.ProdStock)
	}
}

```

## 9.4	双向流

以`product.proto`为例，在`service ProdService`中添加双向流定义方法：

```protobuf
// product.proto
// ...
// 定义服务主体
service ProdService{
  // 定义方法
  rpc GetProductStock(ProductRequest) returns(ProductResponse);
  // 定义客户端流方法
  rpc UpdateProductStockClientStream(stream ProductRequest) returns(ProductResponse);
  // 定义服务端流方法
  rpc GetProductStockServerStream(ProductRequest) returns(stream ProductResponse);
  // 定义双向流方法
  rpc SayHelloStream(stream ProductRequest) returns(stream ProductResponse);
}
```

在`product.go`中实现具体的`SayHelloStream`方法：

```go
func (p *productService) SayHelloStream(stream ProdService_SayHelloStreamServer) error {
	for {
		recv, err := stream.Recv()
		if err != nil {
			return nil
		}
		fmt.Println("服务端收到客户端的消息", recv.ProdId)
		time.Sleep(time.Second)
		rsp := &ProductResponse{ProdStock: recv.ProdId}
		err = stream.Send(rsp)
		if err != nil {
			return nil
		}
	}
}
```

客户端`grpc_client.go`代码修改：

```go
package main

import (
	"context"
	"fmt"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
	"log"
	"ms-proto/client/auth"
	"ms-proto/service"
	"time"
)

func main() {
	//token认证
	token := &auth.Authentication{
		User:     "admin",
		Password: "admin",
	}

	// 1. 新建连接，端口是服务端开放的8080端口
	//token认证
	conn, err2 := grpc.Dial(":8080",
		grpc.WithTransportCredentials(insecure.NewCredentials()), grpc.WithPerRPCCredentials(token))
	if err2 != nil {
		log.Fatal("服务端出错，连接不上", err2)
	}

	//退出时关闭链接
	defer conn.Close()

	// 2. 调用Product.pb.go中的NewProdServiceClient方法
	productServiceClient := service.NewProdServiceClient(conn)

	// 3. 直接像调用本地方法一样调用GetProductStock方法
	//双向流
	stream, err := productServiceClient.SayHelloStream(context.Background())
	if err != nil {
		log.Fatal("获取流出错：", err)
	}
	for {
		requset := &service.ProductRequest{ProdId: 123}
		err = stream.Send(requset)
		if err != nil {
			log.Fatal(err)
		}
		time.Sleep(time.Second)
		recv, err3 := stream.Recv()
		if err3 != nil {
			log.Fatal(err)
		}
		fmt.Println("客户端收到的流信息：", recv.ProdStock)

	}
}


```

