# open terminal, type python --version

# Hello World
print("Hello, World!")

# Simple sum and assignment

2 + 2
2**3

a = 2 + 2

print(a)

# ----------------------------------
# Variables and Built-in Data Types in Python

# Numeric types
integer_var = 42  # Integer
float_var = 3.14  # Float
complex_var = 2 + 3j  # Complex number

# Numeric operations
sum_var = integer_var + float_var
difference = integer_var - 10
product = integer_var * 2
quotient = integer_var / 7
integer_division = integer_var // 7
modulus = integer_var % 7
power = integer_var**2

# Complex number operations
real_part = complex_var.real
imaginary_part = complex_var.imag
absolute_value = abs(complex_var)

# String
string_var = "Hello, Python!"
uppercase = string_var.upper()
lowercase = string_var.lower()
reversed_string = string_var[::-1]
repeated_string = string_var * 2
words = string_var.split(" ")

# String concatenation
greeting = "Hello"
name = "Mario"
full_greeting = greeting + ", " + name + "!"

# Boolean
bool_var = True
is_greater = 10 > 5
is_equal = 10 == 5
logical_and = True and False
logical_or = True or False

# NoneType
none_var = None

# List
list_var = [1, 2, 3, "Python", 5.5]
list_var.append("Workshop")
list_var.remove("Python")
list_var.insert(2, "Inserted")
popped_element = list_var.pop()
reversed_list = list_var[::-1]
sorted_list = sorted([3, 1, 4, 1, 5, 9])  # Works for numeric lists

# Tuple
tuple_var = (1, 2, 3, "Immutable", 5.5)
length_of_tuple = len(tuple_var)
sliced_tuple = tuple_var[1:4]
concatenated_tuple = tuple_var + (6, 7, 8)

# Set
set_var = {1, 2, 3, 3, 4, 5}
set_var.add(6)
set_var.discard(3)
union_set = set_var.union({7, 8})
intersection_set = set_var.intersection({2, 4, 6, 8})
difference_set = set_var.difference({4, 5})

# Dictionary
dict_var = {"name": "Mario", "role": "Instructor", "language": "Python"}
dict_var["age"] = 30
updated_role = dict_var.update({"role": "Lead Instructor"})
removed_item = dict_var.pop("language")
all_keys = dict_var.keys()
all_values = dict_var.values()
nested_dict = {"course": {"title": "Python Basics", "duration": "3 hours"}}
nested_value = nested_dict["course"]["title"]

# Type checking and conversion
integer_to_float = float(integer_var)
float_to_integer = int(float_var)
number_as_string = str(integer_var)
string_to_integer = int("42")

# Dynamic typing
dynamic_var = 42
dynamic_var = "Now a string!"  # Reassigned to a string
