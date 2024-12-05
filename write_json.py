import json
import os

def manage_data(file_name, question, answer, imav, imgsrc=None):
    """
    Appends user data to a JSON file.
    
    Parameters:
        file_name (str): Path to the JSON file.
        question (str): The question input by the user.
        answer (str): The answer input by the user.
        imav (int): Integer (0 or 1) indicating if imgsrc is applicable.
        imgsrc (str or None): The image source if imav is 1, else None.
    
    Returns:
        list: The updated data list.
    """
    # Load existing data if the file exists
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    # Create a new entry
    entry = {
        "question": question,
        "answer": answer,
        "imav": imav,
        "imgsrc": imgsrc if imav == 1 else None,
    }

    # Append the entry to the data list
    data.append(entry)

    # Save data to the JSON file
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

    return data


# Inputs outside the function
file_name_input = input("Enter the file name (with path): ").strip()

while True:
    # Collect user inputs
    question_input = input("Enter a question: ").strip()
    answer_input = input("Enter an answer: ").strip()

    # Input validation for imav
    while True:
        try:
            imav_input = int(input("Enter imav (0 or 1): ").strip())
            if imav_input in (0, 1):
                break
            else:
                print("Please enter 0 or 1 only.")
        except ValueError:
            print("Please enter a valid integer (0 or 1).")

    # Optional imgsrc input
    imgsrc_input = None
    if imav_input == 1:
        imgsrc_input = input("Enter imgsrc: ").strip()

    # Call the function to update data
    updated_data = manage_data(file_name_input, question_input, answer_input, imav_input, imgsrc_input)

    print("Entry added successfully!")

    # Ask if the user wants to add another entry
    add_another = input("Do you want to add another entry? (yes/no): ").strip().lower()
    if add_another != "yes":
        print("Exiting...")
        break
