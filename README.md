# 🏠 HBNB - AirBnB Clone v2

This repository contains a complete implementation of an AirBnB clone project, featuring both a command-line console interface and a Flask web application. This project demonstrates backend development, database management, web frameworks, and template rendering.

## 📋 Table of Contents
- [🏠 HBNB - AirBnB Clone v2](#-hbnb---airbnb-clone-v2)
  - [📋 Table of Contents](#-table-of-contents)
  - [🌟 Project Overview](#-project-overview)
  - [🚀 Features](#-features)
  - [🛠️ Installation \& Setup](#️-installation--setup)
    - [Prerequisites](#prerequisites)
    - [Quick Start](#quick-start)
  - [🌐 Flask Web Application](#-flask-web-application)
    - [Available Routes](#available-routes)
    - [Running Flask Applications](#running-flask-applications)
    - [Flask Project Structure](#flask-project-structure)
  - [💾 Console Application](#-console-application)
    - [Console Usage](#console-usage)
    - [Console Commands](#console-commands)
  - [🗄️ Storage Engines](#️-storage-engines)
  - [📁 Repository Structure](#-repository-structure)
  - [🧪 Testing](#-testing)
  - [🔧 Troubleshooting](#-troubleshooting)
  - [🤝 Contributing](#-contributing)
  - [👥 Authors](#-authors)

## 🌟 Project Overview

This project is a comprehensive web application inspired by AirBnB, implementing:

- **Backend Interface**: Command-line console for data management
- **Web Interface**: Flask-based web application with dynamic content
- **Database Integration**: Support for both file storage and MySQL database
- **Template Rendering**: Dynamic HTML generation with Jinja2
- **RESTful Design**: Clean URL routing and HTTP response handling

## 🚀 Features

### Console Features
- ✅ Object-oriented data model (User, State, City, Amenity, Place, Review)
- ✅ JSON serialization/deserialization for persistent storage
- ✅ CRUD operations via command-line interface
- ✅ Two storage engines: FileStorage and DBStorage

### Web Features
- ✅ Flask web framework implementation
- ✅ Dynamic route handling with parameters
- ✅ HTML template rendering with Jinja2
- ✅ Static file serving (CSS, images)
- ✅ Database integration for dynamic content
- ✅ Responsive web design

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.12+ 
- MySQL 5.7+ (for database storage)
- pip3 package manager

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ChristianTonny/alu-AirBnB_clone_v2.git
   cd alu-AirBnB_clone_v2
   ```

2. **Activate the virtual environment:**
   ```powershell
   # On Windows
   .venv\Scripts\Activate.ps1
   
   # On Linux/Mac
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install Flask SQLAlchemy mysqlclient
   ```

4. **Set up database (optional for advanced features):**
   ```bash
   # Create MySQL databases
   mysql -u root -p < setup_mysql_dev.sql
   mysql -u root -p < setup_mysql_test.sql
   ```

## 🌐 Flask Web Application

### Available Routes

| Route | Description | Example |
|-------|-------------|---------||
| `/` | Welcome page | `Hello HBNB!` |
| `/hbnb` | HBNB page | `HBNB` |
| `/c/<text>` | Display C + text | `/c/is_fun` → `C is fun` |
| `/python/<text>` | Display Python + text | `/python/is_cool` → `Python is cool` |
| `/number/<n>` | Display number (integers only) | `/number/89` → `89 is a number` |
| `/number_template/<n>` | HTML page with number | Dynamic HTML template |
| `/number_odd_or_even/<n>` | Check if number is odd/even | Dynamic HTML template |
| `/states_list` | List all states from DB | Dynamic state listing |
| `/cities_by_states` | States with their cities | Dynamic nested listing |
| `/states` | All states | Dynamic state listing |
| `/states/<id>` | Specific state details | State with cities |
| `/hbnb_filters` | Complete filters page | Full AirBnB-style interface |

### Running Flask Applications

**Basic Applications (No Database Required):**
```bash
# Activate virtual environment first
.venv\Scripts\Activate.ps1

# Run applications
python -m web_flask.0-hello_route
python -m web_flask.1-hbnb_route
python -m web_flask.2-c_route
python -m web_flask.3-python_route
python -m web_flask.4-number_route
python -m web_flask.5-number_template
python -m web_flask.6-number_odd_or_even
```

**Database Applications:**
```bash
# Set environment variables and run
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python -m web_flask.7-states_list

HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python -m web_flask.10-hbnb_filters
```

**Testing the Applications:**
```bash
# Test with curl
curl http://localhost:5000
curl http://localhost:5000/c/is_fun
curl http://localhost:5000/python/is_magic

# Or test with PowerShell
Invoke-WebRequest -Uri "http://localhost:5000" -UseBasicParsing
```

### Flask Project Structure
```
web_flask/
├── 0-hello_route.py          # Basic "Hello HBNB!" route
├── 1-hbnb_route.py           # Multiple routes
├── 2-c_route.py              # Variable routes with C
├── 3-python_route.py         # Variable routes with defaults
├── 4-number_route.py         # Integer validation
├── 5-number_template.py      # HTML templates
├── 6-number_odd_or_even.py   # Conditional templates
├── 7-states_list.py          # Database integration
├── 8-cities_by_states.py     # Nested data display
├── 9-states.py               # Dynamic state pages
├── 10-hbnb_filters.py        # Complete web interface
├── templates/                # Jinja2 HTML templates
│   ├── 5-number.html
│   ├── 6-number_odd_or_even.html
│   ├── 7-states_list.html
│   ├── 8-cities_by_states.html
│   ├── 9-states.html
│   └── 10-hbnb_filters.html
└── static/                   # CSS and images
    ├── styles/
    │   ├── 3-footer.css
    │   ├── 3-header.css
    │   ├── 4-common.css
    │   └── 6-filters.css
    └── images/
        ├── icon.png
        └── logo.png
```

## 💾 Console Application

The console application provides a command-line interface for managing AirBnB objects.

### Console Usage

1. **Start the console:**
   ```bash
   ./console.py
   ```

2. **Console prompt:**
   ```
   (hbnb) 
   ```

### Console Commands

| Command | Description | Example |
|---------|-------------|---------||
| `create` | Creates a new instance | `create User` |
| `show` | Displays an instance | `show User 1234-5678` |
| `destroy` | Deletes an instance | `destroy User 1234-5678` |
| `all` | Shows all instances | `all` or `all User` |
| `update` | Updates an instance | `update User 1234 name "John"` |
| `quit`/`EOF` | Exits the console | `quit` |

**Alternative Syntax:**
```bash
(hbnb) User.all()
(hbnb) User.count()
(hbnb) User.show("1234-5678")
(hbnb) User.destroy("1234-5678")
(hbnb) User.update("1234", "name", "John")
```

## 🗄️ Storage Engines

### FileStorage
- **File**: `models/engine/file_storage.py`
- **Storage**: JSON file (`file.json`)
- **Usage**: Development and testing

### DBStorage  
- **File**: `models/engine/db_storage.py`
- **Storage**: MySQL database
- **Usage**: Production environment

**Switch storage engines:**
```bash
# File storage (default)
export HBNB_TYPE_STORAGE=fs

# Database storage
export HBNB_TYPE_STORAGE=db
export HBNB_MYSQL_USER=hbnb_dev
export HBNB_MYSQL_PWD=hbnb_dev_pwd
export HBNB_MYSQL_HOST=localhost
export HBNB_MYSQL_DB=hbnb_dev_db
```

## 📁 Repository Structure

| Directory/File | Description |
|----------------|-------------|
| `console.py` | Command-line interface |
| `models/` | Data models and storage engines |
| `models/engine/` | FileStorage and DBStorage |
| `web_flask/` | Flask web applications |
| `web_static/` | Static HTML/CSS files |
| `tests/` | Unit tests |
| `setup_mysql_*.sql` | Database setup scripts |

**Key Model Classes:**
- `BaseModel` - Parent class for all models
- `User` - User account management
- `State` - Geographic states
- `City` - Cities within states  
- `Amenity` - Property amenities
- `Place` - Rental properties
- `Review` - User reviews

## 🧪 Testing

```bash
# Run all tests
python -m unittest discover tests

# Test specific modules
python -m unittest tests.test_models.test_base_model

# Test with coverage
python -m coverage run -m unittest discover tests
python -m coverage report
```

## 🔧 Troubleshooting

### Common Issues and Solutions

#### "ModuleNotFoundError: No module named 'flask'"
**Problem**: Flask is not installed or virtual environment is not activated.

**Solution**:
1. Activate the virtual environment:
   ```powershell
   .venv\Scripts\Activate.ps1
   ```
2. Install Flask:
   ```bash
   pip install Flask SQLAlchemy mysqlclient
   ```

#### "Unable to connect to the remote server"
**Problem**: Flask application is not running.

**Solution**:
1. Make sure the virtual environment is activated
2. Start the Flask application:
   ```bash
   python -m web_flask.0-hello_route
   ```
3. Test the endpoint:
   ```bash
   # In a new terminal
   Invoke-WebRequest -Uri "http://localhost:5000" -UseBasicParsing
   ```

#### Database Connection Issues
**Problem**: MySQL database not configured properly.

**Solution**:
1. Install MySQL server
2. Run setup scripts:
   ```bash
   mysql -u root -p < setup_mysql_dev.sql
   ```
3. Set environment variables:
   ```bash
   set HBNB_MYSQL_USER=hbnb_dev
   set HBNB_MYSQL_PWD=hbnb_dev_pwd
   set HBNB_MYSQL_HOST=localhost
   set HBNB_MYSQL_DB=hbnb_dev_db
   set HBNB_TYPE_STORAGE=db
   ```

#### Virtual Environment Issues
**Problem**: Virtual environment not working properly.

**Solution**:
1. Check if you're in the correct directory
2. Activate the environment:
   ```powershell
   .venv\Scripts\Activate.ps1
   ```
3. Verify activation (you should see `(.venv)` in your prompt)

### Getting Help
- Check the console output for detailed error messages
- Ensure all dependencies are installed in the virtual environment
- Verify Python and pip versions match the virtual environment
- Use `python --version` and `pip --version` to debug version mismatches

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

**Code Standards:**
- Follow PEP 8 style guidelines
- Add docstrings to all functions/classes
- Include unit tests for new features
- Use meaningful commit messages

## 👥 Authors

See [AUTHORS](./AUTHORS) file for the list of contributors to this project.

---

**📧 Contact:** For questions or support, please open an issue on GitHub.

**🌐 Live Demo:** Visit the deployed application at [your-domain.com](http://your-domain.com)

---
*This project is part of the ALU Software Engineering curriculum, focusing on web development fundamentals, database management, and software architecture principles.*