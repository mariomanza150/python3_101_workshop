# Unpythonic Script: Can you make this better?

# 1.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

# 2.
keys = ["name", "age", "location"]
values = ["Alice", 30, "New York"]
my_dict = {}
for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

# 3.
items = ["apple", "banana", "cherry"]
index = 0
for item in items:
    print(f"{index}: {item}")
    index += 1

# 4.
person = {"name": "Bob", "age": 25}
if "name" in person:
    name = person["name"]
else:
    name = "Unknown"

if "age" in person:
    age = person["age"]
else:
    age = "Unknown"

# 5.
role = "admin"
if role == "admin":
    if age >= 18:
        print("Admin access granted.")
    else:
        print("Admin access denied.")
else:
    if age >= 18:
        print("User access granted.")
    else:
        print("User access denied.")

# 6.
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name

# 7.
print("Details:")
print("Name: " + name)
print("Age: " + str(age))
print("Location: " + my_dict["location"])

# 8.
global_count = 0

def increment_count():
    global global_count
    global_count += 1

increment_count()
increment_count()
print("Global count is now:", global_count)

# 9.
def find_maximum(nums):
    max_value = nums[0]
    for num in nums:
        if num > max_value:
            max_value = num
    return max_value

max_number = find_maximum(numbers)
print("Maximum number is:", max_number)

# 10.
file = open("example.txt", "w")
file.write("This is a sample file.")
file.close()
