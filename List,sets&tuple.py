#collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set  = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple= () ordered and uncangeable. Duplicate OK. FASTER


fruits = ["apple","orange","bananna", "coconut"]

# print(fruit[::-1])

# for fruit in fruits:
#     print(fruit)

# print("apple" in fruits)
# print(dir(fruits))
# help(fruits)


# fruits[0] = "pineapple"
# fruits.append("pineapple")  adding in last of the list
# fruits.remove("apple") removing item from the list
# fruits.insert(0,"pineapple")  inserting item in the list
# fruits.sort() sorting by alphabetic order
# fruits.reverse() reversing backward from the last element of the list
# fruits.clear() for clearing elements 
# print(fruits.index("apple"))
# print(fruits.count("orange"))

# foo = [1,2,3]
# fruits.append(foo)
# foo.append(4)


# for fruit in fruits:
#     print(fruit)


## print all pair of numbers from a list

l=[1,2,3,4,5]

for i in range(len(l)):
    for j in range(i+1,len(l)):
        print(l[i],l[j])