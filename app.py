from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from DAL import init_db, get_all_projects, insert_project
import os

app = Flask(__name__, static_folder="static")

# Ensure database and table exist on startup
init_db()


@app.route("/")
def root_index():
    # Serve existing static index page
    return send_from_directory(".", "index.html")


@app.route("/projects")
def projects():
    projects_list = get_all_projects()
    return render_template("projects.html", projects=projects_list)


@app.route("/add", methods=["GET", "POST"]) 
def add_project():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        image_file_name = request.form.get("image_file_name", "").strip()
        if title and description and image_file_name:
            insert_project(title, description, image_file_name)
            return redirect(url_for("projects"))
        # basic fallback: reload form if invalid
        return redirect(url_for("add_project"))
    # GET -> serve the form page; we reuse the existing HTML file path for convenience
    # If you prefer a template, create templates/add_project.html and render it instead
    return send_from_directory(".", "contact.html")


# Convenience routes to serve existing static top-level files during development
@app.route("/styles.css")
def styles_root():
    return send_from_directory(".", "styles.css")


@app.route("/script.js")
def script_root():
    return send_from_directory(".", "script.js")


@app.route("/assets/<path:filename>")
def assets(filename: str):
    return send_from_directory("assets", filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
