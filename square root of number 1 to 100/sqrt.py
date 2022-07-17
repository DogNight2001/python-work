
for i in range(1,1001):

    with open("Square_Root_Of_Numbers_1_to_1000.txt","a") as f:
      f.write(f"{i}={i**0.5}\n")
