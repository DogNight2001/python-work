# x = lambda a:[i for i in range(a)]
# print(x(5))
# y = lambda a:[i*i for i in range(a)]
# print(y(5))      

def fun(n):
    return n%2==0

a=filter(fun,[1,3,56,45,7,443,67,5,564,345,3436,345,234,6,6,235,25,67,345,36,57,234,58,46,3])
print(list(a))