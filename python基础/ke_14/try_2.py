try:
    print("可能出来异常的代码")
except Exception as e:
    print("出现异常时执行的代码")

else:
    print("没有出现异常时执行的代码")
finally:
    print("无论是否出现异常,都会执行")
