import json

def load_json(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, "r") as file:
            data = json.load(file)  # Attempt to load JSON
        return data
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        return None

def fix_json(file_path):
    """Attempt to fix a malformed JSON file."""
    try:
        # Read the file content
        with open(file_path, "r") as file:
            content = file.read()
        
        # Fix known issues programmatically
        print("Fixing JSON...")
        content = content.replace("//", "")  # Remove comments
        content = content.replace('"29"', '29')  # Fix age type
        content = content.replace(']["', '", "')  # Add missing comma in the array
        content = content.replace('1100', '"1100"')  # Fix postal code type
        content = content.replace('"Mexico  ', '"Mexico"')  # Fix missing closing quote
        
        # Parse the fixed JSON
        fixed_data = json.loads(content)
        print("JSON Fixed Successfully!")
        return fixed_data
    except json.JSONDecodeError as e:
        print(f"Still Malformed JSON: {e}")
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None

def save_json(file_path, data):
    """Save corrected JSON data back to a file."""
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Corrected JSON saved to {file_path}")
    except Exception as e:
        print(f"Failed to save JSON: {e}")

if __name__ == "__main__":
    file_path = "malformed_data.json"
    corrected_file_path = "corrected_data.json"
    
    # Attempt to load the JSON
    print("Loading JSON...")
    data = load_json(file_path)
    
    if not data:
        # Fix the JSON if loading failed
        fixed_data = fix_json(file_path)
        if fixed_data:
            # Save the corrected JSON
            save_json(corrected_file_path, fixed_data)
