from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import threading
import os

app = FastAPI()

# Mount the static files directory
app.mount("/dist", StaticFiles(directory="dist/assets"), name="dist")

# Serve the React app's index.html
@app.get("/{full_path:path}")
def serve_react_app(full_path: str):
    # Try to serve the requested file
    full_file_path = f"dist/{full_path}"
    
    # If the file exists, serve it, otherwise fallback to the index.html
    if os.path.isfile(full_file_path):
        return FileResponse(full_file_path)
    
    # If it's a directory, serve the index.html (React single-page app)
    if os.path.isdir(full_file_path):
        return FileResponse("dist/index.html")

    # If file is not found, fallback to index.html
    return FileResponse("dist/index.html")

# Example API endpoint
@app.get("/api/data")
def get_data():
    return {"message": "Hello from FastAPI!"}

# Function to run the FastAPI app
def start_server():
    uvicorn.run(app, host="0.0.0.0", port=5000)

if __name__ == "__main__":
    # Start the FastAPI server in a separate thread
    threading.Thread(target=start_server).start()
