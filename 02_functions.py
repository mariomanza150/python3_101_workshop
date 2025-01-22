# Function with no arguments and no return value
def greet():
    print("Hello! Welcome to the Python function showcase.")


# Function with arguments and no return value
def personalized_greet(name):
    print(f"Hello, {name}! Glad to have you here.")


# Function with arguments and a return value
def add_numbers(a, b):
    return a + b


# Function with a default argument
def introduce_yourself(name="Guest"):
    print(f"My name is {name}.")


# Function using variable-length arguments (*args)
def list_skills(*skills):
    """Prints a list of skills."""
    print("Your skills are:")
    for skill in skills:
        print(f"- {skill}")


# Function using keyword arguments (**kwargs)
def profile_summary(**kwargs):
    print("Profile Summary:")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")


# Function with a nested function
def outer_function(number):
    def square(x):
        return x * x

    return square(number)


# Recursive function
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


# Lambda function (anonymous function)
square = lambda x: x * x

# Main program
if __name__ == "__main__":
    greet()
    personalized_greet("Mario")

    result = add_numbers(5, 10)
    print(f"5 + 10 = {result}")

    introduce_yourself("Alice")
    introduce_yourself()

    list_skills("Python", "Django", "Machine Learning", "Photography")

    profile_summary(name="Mario", role="Developer", location="Mexico")

    number = 4
    print(
        f"The square of {number} using a nested function is {outer_function(number)}."
    )

    print(f"Factorial of 5 is {factorial(5)}.")

    print(f"The square of 7 using a lambda function is {square(7)}.")
