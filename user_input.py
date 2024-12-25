# #input() = A function that prompts the user to enter data
# #   Returns the entered data as a string


# name = input("what is your name?: ")
# age = input("How old are you?:")

# age = int(age)
# age = age + 1

# print(f"Hello {name}")
# print("HAPPY BIRTHDAY!")
# print(f"You are {age} years")



# Exercise 1 Rectangle Area Calc

# length = float(input("Enter the length: "))
# width = float(input("Enter the width: "))
# area = length*width

# print(f"The area is: {area} unit^2")


#Exercise 2 Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is {total} BDT")
