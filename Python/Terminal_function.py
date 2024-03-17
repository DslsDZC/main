def Welcome_words():
    print("\nWelcome to DslsTermux!\n|nUse package:\n\n * Search for software packages: pkg search <query>\n * Install software package: pkg install <package>\n * Upgrade package: pkg upgrade\n\nOther repositories:\n\n * root: pkg install root-repo\n * X11: pkg install x11-repo\n\nAuthor QQ:2470305344")
    a = input("\n\033[1;32m ~ \033[0m" + "$ ")
    return a

def Judge(a):
    if a == "pkg install root-repo":
        print("Installation failed")


