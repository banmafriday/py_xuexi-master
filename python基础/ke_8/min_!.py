def fun1():
    print("1")


def fun2():
    print("2")


def main():
    if 1 == 1:
        fun2()


if __name__ == '__main__':  # 当直接执行当前文件运行的语句，将被其他文件引入时不执行
    main()
