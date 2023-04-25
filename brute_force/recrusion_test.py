# 재귀함수 테스트

def my_function(n):
    if n == 0:
        return
    else:
        for i in range(n):
            my_function(n-1)
            print(i, end=" ")

my_function(3)

# for i in range(3):
#   print(i)

#   my func1 = 0
#   my func2 = myfunc1 = 0 01
#   my func3 = myfunc2 = myfunc1 = 0 01 012