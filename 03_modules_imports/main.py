# main.py

import importlib
import os
import sys

from modulos import *


# Function showcasing the module search path
def show_module_search_path():
    print("Python Module Search Path:")
    for path in sys.path:
        print(f"- {path}")

    # Check if a specific directory is in the search path
    custom_path = os.path.abspath("modulos")
    if custom_path in sys.path:
        print("\nCustom Path Found in Search Path")
    else:
        print(f"\nCustom Path Not Found. Adding: {custom_path}")
        sys.path.append(custom_path)
        print(f"Updated Module Search Path:\n- {custom_path}")


# Function demonstrating custom imports using sys.path modification
def custom_import_demo():
    print("\nCustom Import Demo:")

    # Ensure custom modules directory is in sys.path
    custom_path = os.path.abspath("modulos")
    if custom_path not in sys.path:
        sys.path.append(custom_path)

    # Dynamically import a module from the custom path
    try:
        custom_module = importlib.import_module("custom_module")
        message = custom_module.hello_world()
        print(f"Custom Module Import Successful: {message}")
    except ModuleNotFoundError:
        print("Custom Module Not Found. Ensure the path and module name are correct.")


# Function demonstrating module imports
def standard_library_demo():
    import modulos

    print(modulos.hello_world())
    from modulos import greet

    greet.hello_world()
    from .modulos.greet import hello_world

    hello_world()


# Function demonstrating standard library imports
def standard_library_demo():
    print("\nStandard Library Demo:")

    # Get the current working directory
    cwd = os.getcwd()
    print(f"Current working directory: {cwd}")


# Main function
if __name__ == "__main__":
    print("Python Module Search Path Demo")
    print("-" * 40)

    show_module_search_path()
    custom_import_demo()
    standard_library_demo()
