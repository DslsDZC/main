def input_a():
    a = input("\033[1;32m ~ \033[0m$ ")
    return a


def welcome_words():
    print("""
Welcome to DslsTermux!
Use package:

 * Search for software packages: pkg search <query>
 * Install software package: pkg install <package>

 * Upgrade package: pkg upgrade

Other repositories:

 * root: pkg install root-repo
 * X11: pkg install x11-repo

Author QQ:2470305344
""")
    input_a()
