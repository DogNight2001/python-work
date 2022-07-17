
def sqrt():
  q=int(input("what range of square root number you want to print from:-\n"))  
  w=int(input("TO:-"))  
  for i in range(q,w):
    with open(f"Square_Root_Of_Numbers_from_{q}_to _{w}.txt","a") as f:
      f.write(f"{i}={i**0.5}\n")
def square(): 
 q=int(input("what range of square number you want to print\n"))
 w=int(input("TO:-")) 
 for i in range(q,w):
    with open(f"square_of_numbers_from_{q}_to_{w}.txt","a")as f:
        f.write(f"{i}²={i*i}\n")
def table():
  q=int(input("what range of  number table  you want to print\n"))
  w=int(input("TO:-"))
  with open(f"multiplication table from{q}to{w}.txt","w")as f: 
   for i in range (q,w+1):
    
        for j in range (1,11):
           f.write(f"{i}X{j}={i*j}\n")
           if j==10:
               f.write("--------------------------------------------\n")
        
you=input("What you want to print in your text file \n1)Tables\n2)Square\n3)Square root(sqrt) \n")           
if  "tables" in you:
    table()        
elif  "square" in you:
    square()
elif "sqrt" in you:
    sqrt()           
        
          
