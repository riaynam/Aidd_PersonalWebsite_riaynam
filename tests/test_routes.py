def test_home_page(client):
    """Test the home page returns 200"""
    response = client.get('/')
    assert response.status_code == 200

def test_projects_page(client, test_db, sample_project):
    """Test the projects page displays projects from the database"""
    import DAL
    # Add a sample project
    DAL.insert_project(
        sample_project["title"],
        sample_project["description"],
        sample_project["imageFileName"]
    )

    response = client.get('/projects')
    assert response.status_code == 200
    # Check if project title appears in the response
    assert sample_project["title"].encode() in response.data
    assert sample_project["description"].encode() in response.data

def test_add_project_get(client):
    """Test the add project form page"""
    response = client.get('/add')
    assert response.status_code == 200
    assert b'Add Project' in response.data

def test_add_project_post(client, test_db):
    """Test adding a new project via POST"""
    data = {
        'title': 'New Test Project',
        'description': 'Project added through form',
        'imageFileName': 'test.jpg'
    }
    response = client.post('/add', data=data, follow_redirects=True)
    assert response.status_code == 200
    
    # Check if new project appears in projects page
    assert b'New Test Project' in response.data
    assert b'Project added through form' in response.data
    assert b'images/test.jpg' in response.data

def test_add_project_validation(client, test_db):
    """Test form validation for required fields"""
    # Missing title
    data = {
        'description': 'Test description',
        'imageFileName': 'test.jpg'
    }
    response = client.post('/add', data=data)
    assert response.status_code == 200
    assert b'Title and Description are required' in response.data

    # Missing description
    data = {
        'title': 'Test Title',
        'imageFileName': 'test.jpg'
    }
    response = client.post('/add', data=data)
    assert response.status_code == 200
    assert b'Title and Description are required' in response.data