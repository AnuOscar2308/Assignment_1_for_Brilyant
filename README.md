# Assignment_1_for_Brilyant

This project is a simple Flask web application that supports user registration, login, and form submission. Users can register an account, log in, and submit their personal information (name, age, bio), which is stored in a database. Only authenticated users can access the form and view submitted profiles.

Features:
- User Registration
- User Login
- Profile Submission
- Profile Viewing

Project Setup:
- Python 3.6+
- Virtual Environment(optional)
- Libraries:
    - Flask
    - Flask-SQLAlchemy
    - Flask-Login
    - Flask-WTF
    - Werkzeug
- Steps to setup:
    - Clone the repository
    - Set up a virtual environment
    - Install all required libraries
    - Create and configure the database
    - Run the application: python app.py
    - Access the application

Directory Structure:

/project_directory

    ├── app.py   
    
    ├── templates/  
    
    │   ├── home.html
    
    │   ├── login.html
    
    │   ├── register.html
    
    │   ├── form.html
    
    │   └── display.html
    
    └── instance
    
        └── final_users.db
           
