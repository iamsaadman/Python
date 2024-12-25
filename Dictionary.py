#dictionary = a collection of {key:value} pairs
#             order and changeable. No duplicates

capitals = {"USA":"Washingtong D.C.",
            "Bangladesh":"Dhaka",
            "China":"Beijeing",
            "Russia":"Moscow"}


# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("Japan"))

# if capitals.get("Japan"):
#     print("That capital exists")
# else:
#     print("capital doesn't exists")

# capitals.update({"Germany":"Berlin"})
# capitals.update({"USA":"Detroit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()


#######  iterate  ##############
# keys = capitals.keys()

# for key in capitals.keys():
#     print(key)

######### Values ##############
# values = capitals.values()


# for value in capitals.values():
#      print(value)


# items = capitals.items()

# for key, value in capitals.items():
#     print(f"{key} : {value}")


## wite a code that counts the frequency of each letter in a sentence

sentence = "I study in UIU"

freq = {}

print(type(freq))

for i in range(len(sentence)):
    char = sentence[i]
    if char not in freq:
        freq[char] = 0
    freq[char] = freq[char]+1
    
    
for char in freq:
        print(f"{char}: {freq[char]}")
        
print(freq)       