# def greets():
#     print("hello world")
#     return 'hi mars'




# def factorial(n):
#     fact=1
#     for i in range(1,int(n)+1):
#         fact =fact*i
#     return fact

# print(factorial(input("enter number: ")))    



# def table(n):
#     for i in range(int(11)):
#         print(f'{n} * {i} = {int(n)*i}')

# table(input("enter number: "))  #  s


# val=(input("enter a string: "))
# def up(val):

#     if val.isupper:
#         return True
#     if val.islower:
#         return False
# up(val)        




# def asci(string):
#     total=0
#     for i in string:
#         total +=ord(i)
#     return total
# val ='ssssssssssssssss'
# print(asci(val))







# def id(namee,paass):
#     x=namee[:4]
#     y=paass[-4:]
#     return x+y
# print(id('laafhvajfbawfhjawbhf','12345678'))    





def func(val):
    countt=1
    
    for i in range(len(val)-1):
        if ord(val[i])+1==ord(val[i+1]):
            countt +=1
       
    return countt
print(func('aaabcder'))            
   


