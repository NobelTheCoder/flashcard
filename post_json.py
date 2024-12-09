from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

# Initialize FastAPI app
app = FastAPI()

# File path for the data
folder_name = "data_folder"
file_name = "data.json"
file_path = os.path.join(folder_name, file_name)

# Ensure the folder and file exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        json.dump([], f)

# Define the request body model
class Block(BaseModel):
    question: str
    answer: str

# Function to append a question-answer block
def add_block(block: Block):
    with open(file_path, "r") as f:
        data = json.load(f)
    
    # Convert Block model to dict and append
    data.append(block.dict())
    
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    
    return {"message": "Block added successfully!"}

# FastAPI route to add a new question-answer block
@app.post("/add/")
def add_question_answer(block: Block):
    try:
        return add_block(block)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
