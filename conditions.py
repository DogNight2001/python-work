# Q1)  inout from user and print charACTER WHOES ASKCII VALUES IS EVEN 

# charc=input("enter character ")
# for i in range(len(charc)) :
#     if ((ord(charc[i]))%2==0):
#         print(charc[i]," ascii value is ",ord(charc[i]))

#---------------------------------------------------------


#Q2 take 5 input and append all those in a list


# num_=int(input("enter a number: "))
# cal=[]
# for i in range(num_):
#    cal.append(input(f'enter list number {i+1}  :'))
# print(cal)    

#---------------------------------------------------------



#Q take n inuts form user and shud n=be n*2 odd-->datatypes   even -->values


n=int(input("number of list element : "))
val={}
for i in range (n) :
    data= input("enter datatype :  ")
    if data not in val:
        val[data]=[]
    val[data].append(input("enter value :  "))

print(val)    
   



