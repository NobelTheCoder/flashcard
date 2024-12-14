from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import os

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Adjust this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# File paths for the data folders
folder_name = "data_folder"
math_file_name = "Math.json"
english_file_name = "English.json"
math_file_path = os.path.join(folder_name, math_file_name)
english_file_path = os.path.join(folder_name, english_file_name)

# Ensure the folder and files exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

for file_path in [math_file_path, english_file_path]:
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump([], f)

# Define the request body model
class Block(BaseModel):
    question: str
    answer: str

# Function to read a specific block from a file
def read_specific_block(file_path, index):
    with open(file_path, "r") as f:
        data = json.load(f)
    
    if 0 <= index < len(data):
        return data[index]
    else:
        return None

# Function to get total number of blocks from a file
def get_total_blocks(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return len(data)

# Function to append a question-answer block to a file
def add_block(file_path, block: Block):
    with open(file_path, "r") as f:
        data = json.load(f)
    
    # Convert Block model to dict and append
    data.append(block.dict())
    
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    
    return {"message": "Block added successfully!"}

# FastAPI route to get a specific block by ID for Math
@app.get("/get/M/{id}")
def get_math_block(id: int):
    block = read_specific_block(math_file_path, id)
    if block:
        return block  # Return the block directly as a dictionary
    else:
        raise HTTPException(status_code=404, detail="Block not found in Math")

# FastAPI route to get a specific block by ID for English
@app.get("/get/E/{id}")
def get_english_block(id: int):
    block = read_specific_block(english_file_path, id)
    if block:
        return block  # Return the block directly as a dictionary
    else:
        raise HTTPException(status_code=404, detail="Block not found in English")

# FastAPI route to get total number of blocks for Math
@app.get("/total_blocks/M")
def total_math_blocks():
    total = get_total_blocks(math_file_path)
    return {"total_blocks": total}

# FastAPI route to get total number of blocks for English
@app.get("/total_blocks/E")
def total_english_blocks():
    total = get_total_blocks(english_file_path)
    return {"total_blocks": total}

# FastAPI route to add a new question-answer block to Math
@app.post("/add/M/")
def add_math_question_answer(block: Block):
    try:
        return add_block(math_file_path, block)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# FastAPI route to add a new question-answer block to English
@app.post("/add/E/")
def add_english_question_answer(block: Block):
    try:
        return add_block(english_file_path, block)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
