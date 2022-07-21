

# def readin():
#     list_ =[]   
#     val=open("data.txt","r")
#     val=val.readlines()
#     for i in range(len(val)):
#         list_.append(val[i].split())
#     return list_

# val=(readin())   
# dic={}
# for i in range(len(val)):
#     if val[i][0] in dic:
#         dic[val[i][0]].add(val[i][1])
#     else:
#         dic[val[i][0]]={val[i][1]}    
# print(dic) 




def readin():
     val=open("data.txt","r")
     val=val.read()
    #  print(val.split())
     return val.split()

val=readin()

dics={}
for i in  (val):
    if i in dics:
        dics[i]+=1
    else:
        dics[i]=1    
print(dics)
file2=open('data2.txt','w')
for k,v in dics.items():

    file2.write(k+' :'+str (v)+'\n')
# for i in range(int(val)):
  
#     if val[i] in dis:
#         dis[i]+=val[i][2]
#     else:
#         dis[val[i][1]]=val[i][2]    
