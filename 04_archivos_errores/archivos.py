# File Handling Showcase

# 1. Writing to a File
def write_to_file(filename, content):
    with open(filename, "w") as file:  # "w" mode overwrites the file
        file.write(content)
    print(f"Content written to {filename}.")

# 2. Appending to a File
def append_to_file(filename, content):
    with open(filename, "a") as file:  # "a" mode appends to the file
        file.write(content)
    print(f"Content appended to {filename}.")

# 3. Reading from a File
def read_file(filename):
    with open(filename, "r") as file:  # "r" mode for reading
        content = file.read()
    print(f"Content of {filename}:\n{content}")

# 4. Reading Line by Line
def read_lines(filename):
    with open(filename, "r") as file:
        lines = file.readlines()  # Reads all lines into a list
    print(f"Lines in {filename}:")
    for i, line in enumerate(lines, start=1):
        print(f"{i}: {line.strip()}")

# 5. Working with Binary Files
def write_binary_file(filename, data):
    with open(filename, "wb") as file:  # "wb" mode for writing binary
        file.write(data)
    print(f"Binary data written to {filename}.")

def read_binary_file(filename):
    with open(filename, "rb") as file:  # "rb" mode for reading binary
        data = file.read()
    print(f"Binary data read from {filename}: {data}")

# 6. Checking if a File Exists
import os

def check_file_exists(filename):
    exists = os.path.exists(filename)
    print(f"Does {filename} exist? {'Yes' if exists else 'No'}")
    return exists

# 7. Renaming a File
def rename_file(old_name, new_name):
    os.rename(old_name, new_name)
    print(f"Renamed {old_name} to {new_name}.")

# 8. Deleting a File
def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} has been deleted.")
    else:
        print(f"{filename} does not exist and cannot be deleted.")

# 9. Working with File Paths
def show_file_path_details(filename):
    abs_path = os.path.abspath(filename)
    dir_name = os.path.dirname(abs_path)
    base_name = os.path.basename(abs_path)
    print(f"File Details for {filename}:")
    print(f"- Absolute Path: {abs_path}")
    print(f"- Directory Name: {dir_name}")
    print(f"- Base Name: {base_name}")

# Main Function to Demonstrate File Handling
if __name__ == "__main__":
    # File names for demonstration
    text_file = "example.txt"
    binary_file = "example.bin"
    renamed_file = "renamed_example.txt"

    # 1. Write to a file
    write_to_file(text_file, "Hello, World!\nThis is a Python file handling demo.\n")

    # 2. Append to a file
    append_to_file(text_file, "Appending more content to the file.\n")

    # 3. Read from a file
    read_file(text_file)

    # 4. Read line by line
    read_lines(text_file)

    # 5. Write and read binary file
    binary_data = b"\x42\x69\x6e\x61\x72\x79\x20\x64\x61\x74\x61\x21"
    write_binary_file(binary_file, binary_data)
    read_binary_file(binary_file)

    # 6. Check if a file exists
    check_file_exists(text_file)
    check_file_exists("nonexistent.txt")

    # 7. Rename a file
    rename_file(text_file, renamed_file)

    # 8. Delete a file
    delete_file(renamed_file)
    delete_file(binary_file)

    # 9. Show file path details
    show_file_path_details("example.txt")
