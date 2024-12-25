# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can' t be negative")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old")    


# n = 0
# while True:
#     print(n)
#     # n++, n--, --n, ++n is not supported
#     n += 1
#     n = n+1
#     n = n-1
#     n -= 1
#     n *= 2
#     n /= 2
#     n += 1
#     if n == 5: break


i = 1
while i < 100:
    if i % 10 == 0:
        print(i)
    elif i % 23 == 0:
        print(i, 'need to break')
        break
    i += 3