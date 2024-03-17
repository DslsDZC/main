import Terminal_function  # 导入Terminal_function模块

def name_judge():  # 定义函数name_judge
    try:
        name = input("Please enter your name: ")  # 获取用户输入的姓名
        key = input("Please enter the key of this studio: ")  # 获取用户输入的密钥
    except KeyboardInterrupt:  # 捕获键盘中断异常
        print("KeyboardInterrupt: Program terminated.")  # 打印异常信息
        return  # 返回

    if name.strip() == 'DZC':  # 判断去除空格后的姓名是否为'DZC'
        if key.strip() == "1qazxcvbnmlp0":  # 判断去除空格后的密钥是否为"1qazxcvbnmlp0"
            print("Hello " + name + "!")  # 打印欢迎信息
            print("Incorrect password!\nWelcome to the DZC terminal.")  # 打印提示信息
            Terminal_function.Welcome_words()  # 调用Terminal_function模块中的Welcome_words函数
        else:
            print("Incorrect password input")  # 打印密码错误提示
    else:
        print('Name input error')  # 打印姓名输入错误提示