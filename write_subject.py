import json
import os

def create_subjects_json(file_path, num_subjects, subjects_data):
    """
    Creates a JSON file with subjects and their IDs.
    
    Parameters:
        file_path (str): The path where the JSON file will be saved.
        num_subjects (int): The number of subjects.
        subjects_data (list of tuples): A list containing tuples of (subject, subject_id).
    """
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Convert subjects data into a dictionary
    subjects = {subject: subject_id for subject, subject_id in subjects_data}

    # Prepare the JSON structure
    data = {"Subjects": subjects}

    # Write to the JSON file
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Subjects successfully written to {file_path}")


# Input outside the function
file_path = "data/subject.json"

# Number of subjects
while True:
    try:
        num_subjects = int(input("Enter the number of subjects: ").strip())
        if num_subjects > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Please enter a valid integer.")

# Collecting subjects and IDs
subjects_data = []
for i in range(1, num_subjects + 1):
    subject = input(f"Enter the name of subject {i}: ").strip()
    subject_id = input(f"Enter the ID for {subject}: ").strip()
    subjects_data.append((subject, subject_id))

# Call the function
create_subjects_json(file_path, num_subjects, subjects_data)
