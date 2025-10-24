import DAL
from pathlib import Path

def seed():
    DAL.create_table()
    # Add a few sample projects referencing existing images in images/ or assets/
    samples = [
        ("K & J Web Designs Work", "Operations & Marketing co-op projects summary.", "images/kj-logo.png"),
        ("CoorFab Marketing", "Marketing content and campaigns.", "images/coorfab-logo.webp"),
        ("Northwestern Mutual Internship", "Financial planning support and CRM updates.", "images/northwestern-logo.jpg"),
    ]
    for title, desc, img in samples:
        DAL.insert_project(title, desc, img)

if __name__ == '__main__':
    seed()
    print("Database initialized and seeded: projects.db")
