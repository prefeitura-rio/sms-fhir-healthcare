import json

def import_json_to_dictionary(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Unable to parse JSON file: '{file_path}'.")
    except Exception as e:
        print(f"An error occurred while importing JSON: {e}")
