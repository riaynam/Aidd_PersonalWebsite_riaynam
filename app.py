from flask import Flask, render_template, request, redirect, url_for
from pathlib import Path
import DAL

# Serve static files from the `static/` directory. Place your images in `static/images/`.
app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route("/")
def home():
    # keep existing index.html in place but show a helpful page that links to Flask pages
    return render_template("index_proxy.html")


@app.route("/projects")
def projects():
    projects = DAL.get_projects()
    return render_template("projects.html", projects=projects)


@app.route("/add", methods=("GET", "POST"))
def add_project():
    error = None
    if request.method == "POST":
        title = (request.form.get("title") or "").strip()
        description = (request.form.get("description") or "").strip()
        image = (request.form.get("imageFileName") or "").strip()
        if not title or not description:
            error = "Title and Description are required."
        else:
            # Normalize image path to live under static/images/
            if image and not (image.startswith("images/") or image.startswith("static/")):
                image = f"images/{image}"
            if image.startswith("static/"):
                image = image[len("static/"):].lstrip("/")
            DAL.insert_project(title, description, image)
            return redirect(url_for("projects"))
    return render_template("add_project.html", error=error)


if __name__ == "__main__":
    DAL.create_table()
    app.run(debug=True)
