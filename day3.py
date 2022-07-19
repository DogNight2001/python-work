# Q1  take input from user suvh as "add 4 5"or "div 25 5" and preform the task 


# val=input("enter your operation and operants: ")
# list_=val.split()
# if list_[0] == 'add':
    
#     print(f'addistion of {list_[1]} + {list_[2]} = {int(list_[1])+int(list_[2])}')

# if list_[0] == 'sub':
    
#     print(f'subtraction of {list_[1]} - {list_[2]} = {int(list_[1])-int(list_[2])}')
# if list_[0] == 'multi':
    
#     print(f'multiplication of {list_[1]} * {list_[2]} = {int(list_[1])*int(list_[2])}')
# if list_[0] == 'div':
    
#     print(f'division of {list_[1]} / {list_[2]} = {int(list_[1])/int(list_[2])}')            




# Q2   to preform "add 2 3 4 5 6 7" or "sub 3 4 5 6 7"

# val=input("enter your operation and operants: ")
# list_=val.split()
# if list_[0] == 'add':
#     add_=0
#     for i in range(1,len(list_)):
      
#       add_ +=  int(list_[i])
#     print(add_)


# if list_[0] == 'mul':
#     mul_=1
#     for i in range(1,len(list_)):
      
#       mul_ *= int(list_[i])
#     print(mul_)      







# n= int(input("enter number: "))
# fact=1
# for i in range(1,n+1):
#     fact *= i
# print(fact)



# val= input("enter string: ")
# if (int(val) == int(val[-1::-1])):
#     print("palindrome")



n=int(input("enter number of character: "))
str_=""
for i in range( n):
    x=int(input(f"enter {i+1} charcter: "))
    str_=str_+(chr(x))
print(str_)