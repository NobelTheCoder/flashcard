import json
import os

def read_subjects_json(file_path):
    """
    Reads the JSON file and returns its content as a single JSON block.
    
    Parameters:
        file_path (str): The path to the JSON file.
    
    Returns:
        dict: The content of the JSON file as a dictionary.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    with open(file_path, "r") as file:
        data = json.load(file)
    
    return data


# Define the file path
file_path = "data/subject.json"

# Call the function and store the result
try:
    subjects_data = read_subjects_json(file_path)

    # Print the full JSON data
    print("Subjects Data:")
    print(json.dumps(subjects_data, indent=4))

    # Extract subjects
    subjects = subjects_data.get("Subjects", {})

    # Print the number of subjects
    print(f"\nNumber of subjects: {len(subjects)}")

    # Print each subject and its ID
    print("\nSubjects and IDs:")
    for name, subject_id in subjects.items():
        print(f"{name}: {subject_id}")

except FileNotFoundError as e:
    print(e)
