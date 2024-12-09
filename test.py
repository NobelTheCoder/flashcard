import os
import json

# Ensure the folder and file exist
folder_name = "data_folder"
file_name = "data.json"
file_path = os.path.join(folder_name, file_name)

# Create the folder and file if not exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        json.dump([], f)

# Function to append a question-answer block
def add_block():
    with open(file_path, "r") as f:
        data = json.load(f)
    
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")
    
    block = {"question": question, "answer": answer}
    data.append(block)
    
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    
    print("Block added successfully!")

# Function to read all blocks
def read_all_blocks():
    with open(file_path, "r") as f:
        data = json.load(f)
    if data:
        for i, block in enumerate(data):
            print(f"Block [{i}]:")
            print(f"  Question: {block['question']}")
            print(f"  Answer: {block['answer']}")
    else:
        print("No blocks available.")

# Function to read a specific block by index
def read_specific_block(index):
    with open(file_path, "r") as f:
        data = json.load(f)
    
    if 0 <= index < len(data):
        block = data[index]
        print(f"Block [{index}]:")
        print(f"  Question: {block['question']}")
        print(f"  Answer: {block['answer']}")
    else:
        print("Invalid index. Block does not exist.")

# Main menu
def main():
    while True:
        print("\nChoose an option:")
        print("1. Add a question-answer block")
        print("2. Read all blocks")
        print("3. Read a specific block")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_block()
        elif choice == "2":
            read_all_blocks()
        elif choice == "3":
            try:
                index = int(input("Enter the block index: "))
                read_specific_block(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
