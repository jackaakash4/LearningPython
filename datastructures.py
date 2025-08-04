#list

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.remove("banana")

print(fruits)
print(len(fruits))
print(fruits[0])


#tuple

point = (10, 20)
x, y = point

print(x, y)

#set(unique element)

unique_number = {1, 2, 3, 2}
unique_number.add(4)

print("Set: ", unique_number)

#dictionary(Key-valued pairs)

person = {
    "name": "Aakash", 
    "age": 23,
}

print("Distionary: ", person)

for key, value in person.items():
    print(key, value)


