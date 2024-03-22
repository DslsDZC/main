#  Copyright (c) 2024.
#  There is no copyright leakage in this studio. If any infringement is found, legal responsibility will be investigated.

# 定义终端文字颜色常量
COLOR_GREEN = "\033[1;32m"
COLOR_RESET = "\033[0m"

# 定义欢迎信息字符串
WELCOME_MESSAGE = """
Welcome to DslsTermux!
Use package:

 * Search for software packages: pkg search <query>
 * Install software package: pkg install <package>

 * Upgrade package: pkg upgrade

Other repositories:

 * root: pkg install root-repo
 * X11: pkg install x11-repo

Author QQ: 2470305344
"""


def input_a():
    # 获取用户输入，并在终端显示绿色提示符
    a = input(f"{COLOR_GREEN} ~ {COLOR_RESET}$ ")
    return a


def welcome_words():
    # 打印欢迎信息
    print(WELCOME_MESSAGE)
    # 返回用户输入的内容
    return input_a()
