username = "chaiandcode"

def func():
    # username = "chai"
    print(username)

print(username)
func()   


x = 99
# def func2(y):
#     z=x+y
#     return z

# result=func2(1)
# print(result)

# def func3():
#     global x
#     x=12
   
# func3()
# print(x)

def f1():
    x=88
    def f2():
        print(x)
    return f2
myresult=f1()
myresult()


def chaicodr(num):
    def actual(x):
        return x**num
    return actual

# def chaicodr(2):
#     def actual(x):
#         return x**2
#     return actual

f = chaicodr(2)
g=chaicodr(3)
print(f(3))
print(g(3))

