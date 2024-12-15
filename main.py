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

# Folder and file paths
folder_name = "data_folder"
file_eng = "English.json"
file_math = "Math.json"
file_eng_path = os.path.join(folder_name, file_eng)
file_math_path = os.path.join(folder_name, file_math)

# Ensure the folder and files exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

for file_path in [file_eng_path, file_math_path]:
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump([], f)

# Define the request body model
class Block(BaseModel):
    question: str
    answer: str

# Function to read a specific block
def read_specific_block(file_path, index):
    with open(file_path, "r") as f:
        data = json.load(f)
    
    if 0 <= index < len(data):
        return data[index]
    else:
        return None

# Function to get total number of blocks
def get_total_blocks(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return len(data)

# Function to append a question-answer block
def add_block(file_path, block: Block):
    with open(file_path, "r") as f:
        data = json.load(f)
    
    # Convert Block model to dict and append
    data.append(block.dict())
    
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    
    return {"message": "Block added successfully!"}

# FastAPI route to get a specific block by ID
@app.get("/get/{category}/{id}")
def get_block(category: str, id: int):
    if category == "E":
        file_path = file_eng_path
    elif category == "M":
        file_path = file_math_path
    else:
        raise HTTPException(status_code=400, detail="Invalid category")

    block = read_specific_block(file_path, id)
    if block:
        return block  # Return the block directly as a dictionary
    else:
        raise HTTPException(status_code=404, detail="Block not found")

# FastAPI route to get total number of blocks
@app.get("/total_blocks/{category}")
def total_blocks(category: str):
    if category == "E":
        file_path = file_eng_path
    elif category == "M":
        file_path = file_math_path
    else:
        raise HTTPException(status_code=400, detail="Invalid category")

    total = get_total_blocks(file_path)
    return {"total_blocks": total}

# FastAPI route to add a new question-answer block
@app.post("/add/{category}")
def add_question_answer(category: str, block: Block):
    if category == "E":
        file_path = file_eng_path
    elif category == "M":
        file_path = file_math_path
    else:
        raise HTTPException(status_code=400, detail="Invalid category")

    try:
        return add_block(file_path, block)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
