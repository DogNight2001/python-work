for i in range(1,1001):
    with open("square_of_numbers_from_1_to_1000.txt","a")as f:
        f.write(f"{i}²={i*i}\n")
