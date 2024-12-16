from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

# Path to your Vite build directory
vite_build_path = Path(__file__).parent / "dist"

# Serve static files from the "dist/assets" directory
app.mount("/assets", StaticFiles(directory=vite_build_path / "assets"), name="assets")

@app.get("/")
async def serve_index():
    # Serve the index.html file
    return FileResponse(vite_build_path / "index.html")

@app.get("/{path:path}")
async def serve_static_files(path: str):
    # Serve any other static files like CSS or JS
    file_path = vite_build_path / path
    if file_path.exists():
        return FileResponse(file_path)
    return FileResponse(vite_build_path / "index.html")  # Fallback to index.html for React Router
