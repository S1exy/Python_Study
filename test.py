i = 0  # 在全局作用域中定义i
def increment():
    global i  # 在函数内部声明i为全局变量
    i += 1  # 修改全局变量i的值

increment()


def m():
    if i == 1:
        print(i)

m()