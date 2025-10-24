## Personal Website — Projects App (Flask + SQLite)

### Setup
1. Place your project images in `static/images/` (e.g., `static/images/example.jpg`).
2. (Optional) Create a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. Run the app:
   ```powershell
   python app.py
   ```

### Usage
- Go to http://127.0.0.1:5000/projects to view all projects (pulled from the database).
- Go to http://127.0.0.1:5000/add to add a new project. Enter Title, Description, and the image filename (e.g., `example.jpg`).
- After adding, the new project will appear immediately on the Projects page.

### Notes
- Images must be placed in `static/images/` manually (drag and drop).
- No image upload via the form yet (can be added later).
- The database is created automatically if missing; the table is ensured on first use.