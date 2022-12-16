def fun1():
    print("To jest fun1")

    def fun2(a):
        print(f"To jest funkcja fun2 {a}")

        def fun3():
            print("To jest funkcja 3")

        return fun3

    return fun2


xFun1 = fun1()
print(type(xFun1))
xFun1 = xFun1(1)
xFun1()
