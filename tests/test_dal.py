def test_create_table(test_db):
    """Test that create_table creates the projects table"""
    import DAL
    with DAL.get_connection() as conn:
        # Check if table exists by trying to select from it
        cur = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='projects'")
        assert cur.fetchone() is not None

def test_insert_project(test_db, sample_project):
    """Test inserting a project"""
    import DAL
    project_id = DAL.insert_project(
        sample_project["title"],
        sample_project["description"],
        sample_project["imageFileName"]
    )
    assert project_id > 0

    # Verify project was inserted
    project = DAL.get_project(project_id)
    assert project["title"] == sample_project["title"]
    assert project["description"] == sample_project["description"]
    assert project["imageFileName"] == sample_project["imageFileName"]

def test_get_projects(test_db, sample_project):
    """Test retrieving all projects"""
    import DAL
    # Insert two projects
    DAL.insert_project(
        sample_project["title"],
        sample_project["description"],
        sample_project["imageFileName"]
    )
    DAL.insert_project(
        "Second Project",
        "Another description",
        "images/second.jpg"
    )

    projects = DAL.get_projects()
    assert len(projects) == 2
    assert projects[0]["title"] in ["Second Project", sample_project["title"]]
    assert projects[1]["title"] in ["Second Project", sample_project["title"]]

def test_get_project(test_db, sample_project):
    """Test retrieving a specific project"""
    import DAL
    project_id = DAL.insert_project(
        sample_project["title"],
        sample_project["description"],
        sample_project["imageFileName"]
    )

    project = DAL.get_project(project_id)
    assert project is not None
    assert project["title"] == sample_project["title"]

    # Test non-existent project
    assert DAL.get_project(999) is None