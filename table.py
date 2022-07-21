def tables(n):
    with open(f'newfldr/table of{n}.txt','w') as t:
        for i in range(11):
            val=n*i
            t.write(str(val)+'\n')
tables(int(input("enter number: ")))