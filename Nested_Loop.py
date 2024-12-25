# for x in range(1,10):
#     print(x,end=" ")


row = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns "))
symbol = input("Enter a symbol to use")


for x in range(row):
    for y in range(columns):
        print(symbol,end="")
        
    print()    

# for x in range(3):
#     for y in range(1, 10):
#         print(x, end=" ")                                    

# print() 