#function = A block of reusable code
#           place() after the function to invoke it


# def happy_birthday(name , age):
#     print(f"Happy birthday to {name}!")
#     print(f"You are {age} years old!")
#     print(f"Happy birthday to you!")
#     print()
    
    
# happy_birthday("Saadman",20)
# happy_birthday("Jahid",27)
# happy_birthday("Nisha",40)    


# def display_invoice(username , amount , due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")
    
    
# display_invoice("Saadman",5000,'19th february,2025')    

# def add(x,y):
#     z = x+y
#     return z

# def subtract(x,y):
#      z = x-y
#      return z
 
# def mul(x,y):
#     z = x*y
#     return z

# def div(x,y):
#     z = x/y
#     return z 

# print(add(1,2))
# print(subtract(1,2))
# print(mul(1,2))
# print(div(1,2))


# def hello(name):
#     name = name.capitalize()
#     print('Hello',name)

# hello('fariha')


def minmax(arr):
  return min(arr), max(arr)

list = [1, 0, 9, 8, -1]
min1 , max1 = minmax(list)
print(f'min: {min1}, max: {max1}')

a = minmax(list)
print(a[0], a[1])