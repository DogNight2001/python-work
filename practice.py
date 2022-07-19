# val=input("enter string: ")
# freq={}
# for i in val.lower():
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(freq)            





# list_=[]
# while True:


#     x=input("enter operation : ")
#     command=x.split()
#     #print(command)
#     if x=="stop":
#         break
#     elif 'push' in x :
#         list_.append(command[1])
#     else:
       
           
#             i=list_.index((command[1]))
                
#             list_.pop(i)
#     print (list_)


map_={}
while True:
    list_=input("enter command : ")
    cond=list_.split()
    if cond[0]=='stop':
            break

    else :
        if cond[0] in map_  :
            print ("in if")
            map_[cond[0]].add(cond[1])
        else:
            print("in else")
            map_[cond[0]]={cond[1]}
    print(map_)                
