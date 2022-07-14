from os import system
"""
1. 将该文件复制到本地仓库目录下
2. 可以向 orderList 中添加 git 命令
"""

def init_git_config():
    """用于初始化git配置"""
    system("git remote add origin master https://github.com/CNA1949/golang_note")
    system("git config --global htttp.sslVerify \"false\"")

def do_git_order( orderList):
    """执行git指令并执行"""   
    init_git_config()
    for order in orderList:
        system(order)   #//执行每一项指令

if __name__=="__main__":
    orderList = [f"git add .", f"git commit -m 'golang_note'", "git push"]  # 指令列表
    do_git_order(orderList)
