from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import os
import json

app = FastAPI()

# Allow CORS from localhost:5173 (React app URL)
origins = [
    "http://localhost:5173",  # React development server
]

# Add CORSMiddleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specific origins (or "*" for all origins)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Directory to save files
UPLOAD_DIR = "files"
DATA_FILE = "data.json"

# Ensure directories exist
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload")
async def upload_file(
    question: str = Form(...),
    answer: str = Form(...),
    file: UploadFile = File(None)  # Make file optional
):
    # Generate timestamp in the format: yearmonthdayhourminutesec
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    
    # Prepare the data entry
    entry = {
        "question": question,
        "answer": answer,
    }

    if file:
        # Save the file if uploaded
        file_extension = file.filename.split('.')[-1]
        new_filename = f"{timestamp}.{file_extension}"
        file_path = os.path.join(UPLOAD_DIR, new_filename)

        with open(file_path, "wb") as f:
            f.write(await file.read())

        # Generate the file URL
        file_url = f"http://127.0.0.1:8000/{UPLOAD_DIR}/{new_filename}"
        entry["file_url"] = file_url
        message = "File uploaded successfully"
    else:
        # If no file, set file_url to indicate no image
        entry["file_url"] = "imgav: BAD"
        message = "No file uploaded"
    
    # Save the data to the JSON file
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(entry)

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

    return JSONResponse(content={"message": message, "data": entry})

# Serve the uploaded files
from fastapi.staticfiles import StaticFiles

app.mount(f"/{UPLOAD_DIR}", StaticFiles(directory=UPLOAD_DIR), name="files")
