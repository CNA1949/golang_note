# 笔记介绍

笔记参考来源：

[GORM入门指南 | 李文周的博客 (liwenzhou.com)](https://www.liwenzhou.com/posts/Go/gorm/)

[GORM 指南 | GORM - The fantastic ORM library for Golang, aims to be developer friendly.](https://gorm.io/zh_CN/docs/)

---



# 安装gorm框架及数据库驱动

安装gorm：

```shell
go get -u gorm.io/gorm
或者
go get -u github.com/jinzhu/gorm
```

安装数据库驱动（使用什么数据库就安装相应的数据库驱动）：

```shell
go get -u gorm.io/driver/mysql	# mysql数据库驱动
go get -u gorm.io/driver/sqlite # sqlite数据库驱动
go get -u gorm.io/driver/sqlserver	# sql server数据库驱动
go get -u gorm.io/driver/postgres # PostgreSQL数据库驱动
```



**注意：以下章节均使用的是`gorm.io/gorm`和`gorm.io/driver`**

---



# 连接数据库

GORM 官方支持的数据库类型有： MySQL, PostgreSQL, SQlite, SQL Server



## 连接MySQL

`dsn`：`username:password@tcp(localhost:3306)DBbaseName?charset=utf8mb4&parseTime=True&loc=Local`

```go
import (
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

func main() {
	dsn := "root:123456@tcp(localhost:3306)/gorm_demo_db?charset=utf8mb4&parseTime=True&loc=Local"
	db, err := gorm.Open(mysql.Open(dsn), &gorm.Config{})
}
```

MySQL 驱动程序提供了 [一些高级配置](https://github.com/go-gorm/mysql) 可以在初始化过程中使用，例如：

```go
import (
	"fmt"
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)
func main(){
    dsn := "root:123456@tcp(localhost:3306)/gorm_demo_db?charset=utf8mb4&parseTime=True&loc=Local"
db, err := gorm.Open(mysql.New(mysql.Config{
    DSN:                       dsn,   // DSN data source name
    DefaultStringSize:         256,   // string 类型字段的默认长度
    DisableDatetimePrecision:  true,  // 禁用 datetime 精度，MySQL 5.6 之前的数据库不支持
    DontSupportRenameIndex:    true,  // 重命名索引时采用删除并新建的方式，MySQL 5.7 之前的数据库和 MariaDB 不支持重命名索引
    DontSupportRenameColumn:   true,  // 用 `change` 重命名列，MySQL 8 之前的数据库和 MariaDB 不支持重命名列
    SkipInitializeWithVersion: false, // 根据当前 MySQL 版本自动配置
}), &gorm.Config{})
}

```

**现有的数据库连接**

GORM 允许通过一个现有的数据库连接来初始化 `*gorm.DB`

```go
import (
	"database/sql"
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

func main() {
	dsn := "root:123456@tcp(localhost:3306)/gorm_demo_db?charset=utf8mb4&parseTime=True&loc=Local"
	sqlDB, err := sql.Open("mysql", dsn)
	gormDB, err = gorm.Open(mysql.New(mysql.Config{
		Conn: sqlDB,
	}), &gorm.Config{})
}
```





---



## 连接SQL Server

```go
import (
  "gorm.io/driver/sqlserver"
  "gorm.io/gorm"
)
func main(){
    dsn := "sqlserver://root:123456@localhost:9930?database=gorm_demo_db"
    db, err := gorm.Open(sqlserver.Open(dsn), &gorm.Config{})
}
```



---



## 连接PostgreSQL

```go
import (
  "gorm.io/driver/postgres"
  "gorm.io/gorm"
)
func main(){
    dsn := "host=localhost user=root password=123456 dbname=gorm_demo_db port=9920 sslmode=disable TimeZone=Asia/Shanghai"
	db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
}

```

我们使用 [pgx](https://github.com/jackc/pgx) 作为 postgres 的 database/sql 驱动，默认情况下，它会启用 prepared statement 缓存，你可以这样禁用它：

```go
db, err := gorm.Open(postgres.New(postgres.Config{
  DSN: "user=root password=123456 dbname=gorm_demo_db port=9920 sslmode=disable TimeZone=Asia/Shanghai",
  PreferSimpleProtocol: true, // disables implicit prepared statement usage
}), &gorm.Config{})
```

**现有的数据库连接**

GORM 允许通过一个现有的数据库连接来初始化 `*gorm.DB`

```go
import (
  "database/sql"
  "gorm.io/driver/postgres"
  "gorm.io/gorm"
)

func main(){
    dsn := "host=localhost user=root password=123456 dbname=gorm_demo_db port=9920 sslmode=disable TimeZone=Asia/Shanghai"
    sqlDB, err := sql.Open("pgx", dsn)
    gormDB, err := gorm.Open(postgres.New(postgres.Config{
      Conn: sqlDB,
    }), &gorm.Config{})
}

```



---



## 连接SQLite

待完善......



---



## 连接池

GORM 使用 [database/sql](https://pkg.go.dev/database/sql) 维护连接池

```go
dsn := "root:123456@tcp(localhost:3306)/gorm_demo_db?charset=utf8mb4&parseTime=True&loc=Local"
sqlDB, err := sql.Open("mysql", dsn)

// SetMaxIdleConns 设置空闲连接池中连接的最大数量
sqlDB.SetMaxIdleConns(10)

// SetMaxOpenConns 设置打开数据库连接的最大数量。
sqlDB.SetMaxOpenConns(100)

// SetConnMaxLifetime 设置了连接可复用的最大时间。
sqlDB.SetConnMaxLifetime(time.Hour)
```



---



# GORM Model定义

在使用ORM工具时，通常我们需要在代码中定义模型（Models）与数据库中的数据表进行映射，在GORM中模型（Models）通常是正常定义的结构体、基本的go类型或它们的指针。 同时也支持`sql.Scanner`及`driver.Valuer`接口（interfaces）。



## gorm.Model

为了方便模型定义，GORM内置了一个`gorm.Model`结构体。`gorm.Model`是一个包含了`ID`, `CreatedAt`, `UpdatedAt`, `DeletedAt`四个字段的Golang结构体。

```go
// gorm.Model 的定义
type Model struct {
    ID        uint           `gorm:"primaryKey"`
    CreatedAt time.Time
    UpdatedAt time.Time
    DeletedAt gorm.DeletedAt `gorm:"index"`
}
```

你可以将它嵌入到你自己的模型中：

```go
// 将 `ID`, `CreatedAt`, `UpdatedAt`, `DeletedAt`字段注入到`User`模型中
type User struct {
    gorm.Model
    Name string
}
```

当然你也可以完全自己定义模型：

```go
// 不使用gorm.Model，自行定义模型
type User struct {
    ID   int
    Name string
}
```



---



## 模型定义示例

```go
type User struct {
    gorm.Model
    Name         string
    Age          sql.NullInt64
    Birthday     *time.Time
    Email        string  `gorm:"type:varchar(100);unique_index"`
    Role         string  `gorm:"size:255"` // 设置字段大小为255
    MemberNumber *string `gorm:"unique;not null"` // 设置会员号（member number）唯一并且不为空
    Num          int     `gorm:"AUTO_INCREMENT"` // 设置 num 为自增类型
    Address      string  `gorm:"index:addr"` // 给address字段创建名为addr的索引
    IgnoreMe     int     `gorm:"-"` // 忽略本字段
}
```



---



## 默认值

可以通过tag定义字段的默认值：

```go
tyep User struct {
    Name string	`gorm:"default:'佚名'"`
    Age int64
}
```

**注意：**通过tag定义字段的默认值，在创建记录时候生成的 SQL 语句会排除没有值或值为 零值 的字段。 在将记录插入到数据库后，Gorm会从数据库加载那些字段的默认值。

例如：

```go

var user = User{Name:"", Age:22}
db.Create(&user)
```

上面代码实际执行的SQL语句是`INSERT INTO users("age") values('22');`，排除了零值字段`Name`，而在数据库中这一条数据会使用设置的默认值`佚名`作为Name字段的值。

**注意：**所有字段的零值, 比如`0`, `""`,`false`或者其它`零值`，都不会保存到数据库内，但会使用他们的默认值。 如果你想避免这种情况，可以考虑使用指针或实现 `Scanner/Valuer`接口，比如：

**使用指针方式实现零值存入数据库**

```go
// 使用指针
tyep User struct {
    Name *string	`gorm:"default:'佚名'"`
    Age int64
}

user := User{Name:new(string), Age:22}
db.Create(&user) // 此时数据库中该记录name字段的值就是''
```

**使用Scanner/Valuer接口方式实现零值存入数据库**

```go
// 使用 Scanner/Valuer
type User struct {
	Name sql.NullString `gorm:"default:'小王子'"` // sql.NullString 实现了Scanner/Valuer接口
	Age  int64
}
user := User{Name: sql.NullString{"", true}, Age:22}
db.Create(&user)  // 此时数据库中该条记录name字段的值就是''
```



---



## 结构体标记（tags）

使用结构体声明模型时，标记（tags）是可选项。gorm支持以下标记:



### 支持的结构体标记（Struct tags）



| 结构体标记（Tag） |                           描述                           |
| :---------------: | :------------------------------------------------------: |
|      Column       |                         指定列名                         |
|       Type        |                      指定列数据类型                      |
|       Size        |                  指定列大小, 默认值255                   |
|    PRIMARY_KEY    |                      将列指定为主键                      |
|      UNIQUE       |                      将列指定为唯一                      |
|      DEFAULT      |                       指定列默认值                       |
|     PRECISION     |                        指定列精度                        |
|     NOT NULL      |                    将列指定为非 NULL                     |
|  AUTO_INCREMENT   |                   指定列是否为自增类型                   |
|       INDEX       | 创建具有或不带名称的索引, 如果多个索引同名则创建复合索引 |
|   UNIQUE_INDEX    |         和 `INDEX` 类似，只不过创建的是唯一索引          |
|     EMBEDDED      |                     将结构设置为嵌入                     |
|  EMBEDDED_PREFIX  |                    设置嵌入结构的前缀                    |
|         -         |                        忽略此字段                        |



### 关联相关标记（Correlation tags）



|        结构体标记（Tag）         |                描述                |
| :------------------------------: | :--------------------------------: |
|            MANY2MANY             |             指定连接表             |
|            FOREIGNKEY            |              设置外键              |
|      ASSOCIATION_FOREIGNKEY      |            设置关联外键            |
|           POLYMORPHIC            |            指定多态类型            |
|        POLYMORPHIC_VALUE         |             指定多态值             |
|       JOINTABLE_FOREIGNKEY       |          指定连接表的外键          |
| ASSOCIATION_JOINTABLE_FOREIGNKEY |        指定连接表的关联外键        |
|        SAVE_ASSOCIATIONS         |    是否自动完成 save 的相关操作    |
|      ASSOCIATION_AUTOUPDATE      |   是否自动完成 update 的相关操作   |
|      ASSOCIATION_AUTOCREATE      |   是否自动完成 create 的相关操作   |
|    ASSOCIATION_SAVE_REFERENCE    | 是否自动完成引用的 save 的相关操作 |
|             PRELOAD              |    是否自动完成预加载的相关操作    |



---



## 主键、表名、列名的约定



### 主键（Primary Key）

GORM 默认会使用名为ID的字段作为表的主键。

```go
type User struct {
    ID   string // 名为`ID`的字段会默认作为表的主键
    Name string
}

// 使用`AnimalID`作为主键
type Animal struct {
    AnimalID int64 `gorm:"primary_key"`
    Name     string
    Age      int64
}
```



### 表名（Table Name）

表名默认就是结构体名称的复数，例如：

```go
type User struct {} // 默认表名是 `users`

// 将 User 的表名设置为 `profiles`
func (User) TableName() string {
    return "profiles"
}

func (u User) TableName() string {
    if u.Role == "admin" {
        return "admin_users"
    } else {
        return "users"
    }
}

// 禁用默认表名的复数形式，如果置为 true，则 `User` 的默认表名是 `user`
db.SingularTable(true)
```

也可以通过`Table()`指定表名：

```go
// 使用User结构体创建名为`deleted_users`的表
db.Table("deleted_users").CreateTable(&User{})

var deleted_users []User
db.Table("deleted_users").Find(&deleted_users)
//// SELECT * FROM deleted_users;

db.Table("deleted_users").Where("name = ?", "jinzhu").Delete()
//// DELETE FROM deleted_users WHERE name = 'jinzhu';
```

GORM还支持更改默认表名称规则：

```go
gorm.DefaultTableNameHandler = func (db *gorm.DB, defaultTableName string) string  {
    return "prefix_" + defaultTableName;
}
```



### 列名（Column Name）

列名由字段名称进行下划线分割来生成：

```go
type User struct {
    ID        uint      // column name is `id`
    Name      string    // column name is `name`
    Birthday  time.Time // column name is `birthday`
    CreatedAt time.Time // column name is `created_at`
    XxxYyyZzz string	// column name is `xxx_yyy_zzz`
}
```

可以使用结构体tag指定列名：

```go
type Animal struct {
    AnimalId    int64     `gorm:"column:beast_id"`         // set column name to `beast_id`
    Birthday    time.Time `gorm:"column:day_of_the_beast"` // set column name to `day_of_the_beast`
    Age         int64     `gorm:"column:age_of_the_beast"` // set column name to `age_of_the_beast`
}
```



---



## 时间戳跟踪

GORM内置了一个`gorm.Model`结构体：

```go
type Model struct {
    ID        uint           `gorm:"primaryKey"`
    CreatedAt time.Time
    UpdatedAt time.Time
    DeletedAt gorm.DeletedAt `gorm:"index"`
}
```



### CreatedAt

如果模型有 `CreatedAt`字段，该字段的值将会是初次创建记录的时间。

```
db.Create(&user) // `CreatedAt`将会是当前时间

// 可以使用`Update`方法来改变`CreateAt`的值
db.Model(&user).Update("CreatedAt", time.Now())
```



### UpdatedAt

如果模型有`UpdatedAt`字段，该字段的值将会是每次更新记录的时间：

```go
db.Save(&user) // `UpdatedAt`将会是当前时间

db.Model(&user).Update("name", "jinzhu") // `UpdatedAt`将会是当前时间
```



### DeletedAt

如果模型有`DeletedAt`字段，调用`Delete`删除该记录时，将会设置`DeletedAt`字段为当前时间，而不是直接将记录从数据库中删除。



---



# GORM数据表操作

## 创建数据表

GORM支持Migration特性，支持根据Go Struct结构自动生成对应的表结构。可以使用`AutoMigrate()`和`Migrator().CreateTable()`创建数据表。

**注意：**GORM 的AutoMigrate函数，仅支持建表，不支持修改字段和删除字段，避免意外导致丢失数据。

### 使用`AutoMigrate()`建表

```go
func (db *DB) AutoMigrate(dst ...interface{}) error {
	return db.Migrator().AutoMigrate(dst...)
}
或者:
func (Migrator) AutoMigrate(dst ...interface{}) error
```

通过`db.AutoMigrate()`可以快速建表，如果表已经存在不会重复创建。

```go
// 根据User结构体，自动创建表结构
db.AutoMigrate(&User{})	// 方式一

db.Migrator().AutoMigrate(&User{}) //方式二

// 一次创建User、Product、Order三个结构体对应的表结构
db.AutoMigrate(&User{}, &Product{}, &Order{})
db.Migrator().AutoMigrate(&User{}, &Product{}, &Order{})

// 可以通过Set设置附加参数，下面设置表的存储引擎为InnoDB
db.Set("gorm:table_options", "ENGINE=InnoDB").AutoMigrate(&User{})
```



### 使用`Migrator().CreateTable()`建表

`db.Migrator().CreateTable()`需要判断是否表已经创建，如果已经存在，创建会报错。

检测表是否已经创建：

```go
// 检测User结构体对应的表是否存在
db.Migrator().HasTable(&User{})

// 检测表名users是否存在
db.Migrator().HasTable("users")
```

创建表：

```go
// 根据User结构体建表
db.Migrator().CreateTable(&User{})
```



---



## Migrator接口详解

### AutoMigrate方法

```go
func (Migrator) AutoMigrate(dst ...interface{}) error
```

```go
// 根据User结构体，自动创建表结构
db.Migrator().AutoMigrate(&User{}) //方式二
```

**注：**AutoMigrate方法会自动检测表是否存在，若存在不会再创建表。



### CreateTable方法

```go
func (Migrator) CreateTable(dst...interface{}) error
```

```go
// 根据User结构体创建数据表
m := db.Migrator()	// 返回的是一个Migrator接口，Migrator接口里面有很多方法
m.CreateTable(&User{})

// 上面两行可以合并
db.Migrator().CreateTable(&User{})

// 等效于:
db.AutoMigrate(&User{}) //与db.Migrator().CreateTable(&User{})的差异见上节
```

**注：**CreateTable方法不会自动检测表是否存在，使用前建议使用HasTable方法检测。



### HasTable方法

```go
func (Migrator) HasTable(dst interface{}) bool
```

HasTable方法用于检测数据表是否已经存在于数据库中，有一下两种检测方式：

**传入结构体名字**

通过**结构体的名字**的方式去查找数据库里是否存在指定的表：

```go
db.Migrator().HasTable(&User{})
```

**传入数据表名**

通过**数据表的真实名字**去查找数据库里是否存在指定的表：

```go
db.Migrator().HasTable("users")
```



### DropTable方法

```go
func (Migrator) DropTable(dst ...interface{}) error
```

用于删除表。有两种方式：

**传入结构体名字**

```go
db.Migrator().DropTable(&User{})
```

**传入数据表名**

```go
db.Migrator().DropTable("users")
```



### RenameTable方法

```go
func (Migrator) RenameTable(oldName, newName interface{}) error
```

用于重命名表，有两种方式：

**传入数据表名**

```go
db.Migrator().RenameTable("oldName","newName")
```

**传入结构体名字**

```go
db.Migrator().RenameTable(&OldName{},"newName")
// 或者：
db.Migrator().RenameTable(&OldName{},&NewName{})
```



### 列系列方法

```go
func (Migrator) AddColumn(dst interface{}, field string) error
func (Migrator) DropColumn(dst interface{}, field string) error
func (Migrator) AlterColumn(dst interface{}, field string) error
func (Migrator) MigrateColumn(dst interface{}, field *schema.Field, columnType ColumnType) error
func (Migrator) HasColumn(dst interface{}, field string) bool
func (Migrator) RenameColumn(dst interface{}, oldName, field string) error
func (Migrator) ColumnTypes(dst interface{}) ([]ColumnType, error)
```



```go
// 添加 name 字段
db.Migrator().AddColumn(&User{}, "Name")
// 删除 name 字段
db.Migrator().DropColumn(&User{}, "Name")
// 修改 name 字段
db.Migrator().AlterColumn(&User{}, "Name")
// 检查字段是否存在
db.Migrator().HasColumn(&User{}, "Name")
// 重命名字段
db.Migrator().RenameColumn(&User{}, "Name", "NewName")
db.Migrator().RenameColumn(&User{}, "name", "new_name")
// 获取字段类型
db.Migrator().ColumnTypes(&User{}) ([]*sql.ColumnType, error)
```



---



# CRUD接口

CRUD通常指数据库的增加(Create)、检索(Retrieve)、更新(Update)和删除(Delete)。



## 创建

### 定义模型并建表

首先定义模型并建表：

```go
type User struct {
	ID        uint   `gorm:"primaryKey;auto_increment"` // 主键自增
	Name      string `gorm:"default:'佚名'"`              // name字段默认值：佚名
	Age       int64
	CreatedAt time.Time // 记录创建时会自动赋值为记录创建的时间
}

err := db.Migrator().AutoMigrate(&User{}) // 创建数据表
if err != nil {
    fmt.Println("建表失败：", err.Error())
}
```



### 创建记录

```go
// 主键id是自增的，不用设置值
user := User{
		Name: "小瓜皮",
		Age:  22,
	}

result := db.Create(&user)
// 捕获插入异常
defer func(tx *gorm.DB) {
		recover()
		if tx.Error != nil { // 说明捕获到错误
			fmt.Println("err=", tx.Error)
		}
	}(result)	// result.Error	返回插入时出现的异常信息

fmt.Println("插入记录条数：", result.RowsAffected) // 返回插入记录的条数
```



### 用指定的字段创建记录

创建记录并更新给出的字段：

```go
db.Select("ID", "Age", "CreatedAt").Create(&user)
// INSERT INTO `users` (`id`,`age`,`created_at`) VALUES ("1001",22,"2022-08-17 09:38:05.921")
```

创建一个记录且一同忽略传递给略去的字段值：

```go
db.Omit("Name", "Age", "CreatedAt").Create(&user)
// INSERT INTO `users` (`id`) VALUES ("1001")
```



### 批量插入

要有效地插入大量记录，请将一个 `slice` 传递给 `Create` 方法。 GORM 将生成单独一条SQL语句来插入所有数据，并回填主键的值，钩子方法也会被调用。

```go
var users = []User{{Name: "小瓜皮", Age: 22}, {Name: "小菜鸡", Age: 20}, {Name: "小傻瓜", Age: 18}}
result := db.Create(&users)
```

使用`CreateInBatches()`分批次创建，可以指定每批的数量：

```go
// 总共创建1000条数据，分10批创建，每批次创建100条数据
var users = []User{{Name: "瓜皮_1", Age: 20}, ...., {Name: "瓜皮_1000", Age: 22}}
db.CreateInBatches(&users,100)
```

