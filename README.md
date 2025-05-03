# Password-Strength-Analyzer-and-Costume-password-generator
Password Strength Analyzer and Custom Password Generator
# Overview
The Password Strength Analyzer and Custom Password Generator is a Flask-based web application designed to evaluate the strength of user-provided passwords and generate secure, customized passwords based on user inputs. The application assesses passwords for entropy, dictionary vulnerabilities, and data breach leaks, while also offering a unique password generation feature that incorporates personal preferences such as favorite color, actor, and school name. This project is hosted on PythonAnywhere for easy access and deployment.


# Features

Password Strength Analysis:
Entropy Calculation: Measures password complexity based on character set diversity.
Dictionary Vulnerability Check: Identifies if the password contains common words or patterns.
Leak Check: Queries the Have I Been Pwned API to check if the password has been exposed in data breaches.
Overall Strength: Combines entropy and dictionary vulnerability metrics for a comprehensive score.


Custom Password Generation:
Generates unique passwords using user inputs (favorite color, actor, and school name).
Incorporates special characters and ensures no duplicate characters for enhanced security.


User-Friendly Interface:
Built with Flask and styled HTML templates for an interactive experience.
Visual feedback through color-coded reports and animated buttons.


# Security Checks:
Validates username and password requirements (e.g., minimum length, character types).
Ensures passwords do not contain username substrings.


# Hosted on PythonAnywhere: Deployed on PythonAnywhere for reliable hosting and public access.

# Installation
Prerequisites
Ensure you have the following installed:

Python 3.8 or higher
pip (Python package manager)

Local Setup

Clone the Repository:
git clone https://github.com/your-username/password-strength-analyzer.git
cd password-strength-analyzer


Create a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:Create a requirements.txt file with the following content:
flask>=2.0.0
nltk>=3.6.0
requests>=2.25.0
pyenchant>=3.2.0

Install the dependencies:
pip install -r requirements.txt


Download NLTK Data:The application uses NLTK's word corpus for dictionary checks. Run:
python -m nltk.downloader words


# Directory Structure:Ensure the following structure:
password-strength-analyzer/
│
├── app.py                   # Main Flask application
├── templates/
│   ├── index.html           # Password input form
│   ├── password_report.html # Password strength report
│   ├── last.html            # Password generator form
├── requirements.txt         # Python dependencies
└── README.md               # This file



# Deployment on PythonAnywhere
The application is hosted on PythonAnywhere, a cloud-based platform for running Python applications. To deploy your own instance:

# Sign Up/Log In:
Create an account or log in at PythonAnywhere.


# Upload Files:
Use the PythonAnywhere "Files" tab to upload app.py, the templates/ folder (containing index.html, password_report.html, and last.html), and requirements.txt.


# Set Up a Web App:

Go to the "Web" tab and click "Add a new web app."
Choose "Flask" and select the Python version (e.g., 3.8 or higher).
Specify the path to app.py (e.g., /home/yourusername/password-strength-analyzer/app.py).


# Install Dependencies:

Open a Bash console in PythonAnywhere and navigate to your project directory:cd /home/yourusername/password-strength-analyzer
Install dependencies:pip install --user -r requirements.txt


# Configure WSGI:

In the "Web" tab, edit the WSGI configuration file (/var/www/yourusername_pythonanywhere_com_wsgi.py) to point to your Flask app. Example:import sys
path = '/home/yourusername/password-strength-analyzer'
if path not in sys.path:
    sys.path.append(path)
from app import app as application




# Reload the Web App:

In the "Web" tab, click the "Reload" button to apply changes.
Access your app at yourusername.pythonanywhere.com.



# Usage

Access the Hosted Application:
Visit the deployed app at yourusername.pythonanywhere.com (replace yourusername with your PythonAnywhere username).


# Analyze a Password:
On the homepage (/index), enter a username and password.
Submit to view a detailed report (/result) with entropy, dictionary vulnerability, leak status, and overall strength.


# Generate a Password:
Navigate to the password generator page via the "Generate New Password" button.
Enter your favorite color, actor, and school name.
Submit to receive a custom-generated password, which can be copied to the clipboard.



# Project Structure
password-strength-analyzer/
│
├── app.py                   # Main Flask application
├── templates/
│   ├── index.html           # Form for username and password input
│   ├── password_report.html # Displays password strength analysis
│   ├── last.html            # Form for custom password generation
├── requirements.txt         # Python dependencies
└── README.md               # This file

# Dependencies

Flask: Web framework for the application.
NLTK: For dictionary-based word checks.
Requests: For querying the Have I Been Pwned API.
PyEnchant: For enhanced dictionary checks (optional, depending on availability).
Standard Libraries: re, math, random, string, secrets, hashlib for password processing.

# Notes

Security: The application uses the Have I Been Pwned API for leak checks, which requires an internet connection.
Password Generation: Generated passwords include special characters and are designed to avoid duplicates, but users should verify strength using the analyzer.
Browser Compatibility: The HTML templates use modern CSS and JavaScript for animations and clipboard functionality, tested on recent browsers.
PythonAnywhere Hosting:
Free accounts on PythonAnywhere have limitations (e.g., limited CPU time, no custom domains). Consider upgrading for production use.
Ensure NLTK data is downloaded in the PythonAnywhere environment, as it is not included by default.


Error Handling: The application includes basic validation (e.g., username length, password requirements). Enhance error handling for production use.

# Contributing
Contributions are welcome! Please:

# Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m 'Add your feature').
Push to the branch (git push origin feature/your-feature).
Open a pull request.

# License
This project will be licensed under the MIT License later.
# Contact
For questions or feedback, please open an issue on the GitHub repository or contact kgunakatakam614@gmail.com .
