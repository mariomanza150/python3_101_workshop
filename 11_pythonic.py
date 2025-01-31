# Pythonic Script: Refactored and Improved

# 1. Using list comprehension for filtering
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]

# 2. Using the `zip` function for dictionary creation
keys = ["name", "age", "location"]
values = ["Alice", 30, "New York"]
my_dict = dict(zip(keys, values))

# 3. Using `enumerate` for indexed iteration
items = ["apple", "banana", "cherry"]
for index, item in enumerate(items):
    print(f"{index}: {item}")

# 4. Using `dict.get()` for safe key access with defaults
person = {"name": "Bob", "age": 25}
name = person.get("name", "Unknown")
age = person.get("age", "Unknown")

# 5. Simplifying nested conditionals
role = "admin"
access = "granted" if age >= 18 else "denied"
print(f"{role.capitalize()} access {access}.")

# 6. Using f-strings for string formatting
first_name = "John"
last_name = "Doe"
full_name = f"{first_name} {last_name}"

# 7. Using a single f-string for formatted output
print(
    f"Details:\nName: {name}\nAge: {age}\nLocation: {my_dict.get('location', 'Unknown')}"
)


# 8. Avoiding global variables and encapsulating state in a class
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


counter = Counter()
counter.increment()
counter.increment()
print(f"Count is now: {counter.count}")

# 9. Using the built-in `max()` function
max_number = max(numbers)
print(f"Maximum number is: {max_number}")

# 10. Using a context manager for file handling
with open("example.txt", "w") as file:
    file.write("This is a sample file.")
