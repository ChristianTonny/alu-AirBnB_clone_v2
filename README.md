# 🏠 HBNB - AirBnB Clone v2

This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

---

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](https://github.com/ChristianTonny/alu-AirBnB_clone_v2/blob/master/AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests](https://github.com/ChristianTonny/alu-AirBnB_clone_v2/tree/master/tests) | All class-defining modules are unittested |
| 3. Make BaseModel | [/models/base_model.py](https://github.com/ChristianTonny/alu-AirBnB_clone_v2/blob/master/models/base_model.py) | Defines a parent class to be inherited by all model classes|
| 4. Update BaseModel w/ kwargs | [/models/base_model.py](https://github.com/ChristianTonny/alu-AirBnB_clone_v2/blob/master/models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation|
| 5. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/ChristianTonny/alu-AirBnB_clone_v2/blob/master/models/engine/file_storage.py) [/models/__init__.py](https://github.com/ChristianTonny/alu-AirBnB_clone_v2/blob/master/models/__init__.py) [/models/base_model.py](https://github.com/ChristianTonny/alu-AirBnB_clone_v2/blob/master/models/base_model.py) | Defines a class to manage persistent file storage system|
| 6. Console 0.0.1 | [console.py](https://github.com/ChristianTonny/alu-AirBnB_clone_v2/blob/master/console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| 7. Console 0.1 | [console.py](https://github.com/ChristianTonny/alu-AirBnB_clone_v2/blob/master/console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class | [console.py](https://github.com/ChristianTonny/alu-AirBnB_clone_v2/blob/master/console.py) [/models/engine/file_storage.py](https://github.com/ChristianTonny/alu-AirBnB_clone_v2/blob/master/models/engine/file_storage.py) [/models/user.py](https://github.com/ChristianTonny/alu-AirBnB_clone_v2/blob/master/models/user.py) | Dynamically implements a user class |
| 9. More Classes | [/models/user.py](https://github.com/ChristianTonny/alu-AirBnB_clone_v2/blob/master/models/user.py) [/models/place.py](https://github.com/ChristianTonny/alu-AirBnB_clone_v2/blob/master/models/place.py) [/models/city.py](https://github.com/ChristianTonny/alu-AirBnB_clone_v2/blob/master/models/city.py) [/models/amenity.py](https://github.com/ChristianTonny/alu-AirBnB_clone_v2/blob/master/models/amenity.py) [/models/state.py](https://github.com/ChristianTonny/alu-AirBnB_clone_v2/blob/master/models/state.py) [/models/review.py](https://github.com/ChristianTonny/alu-AirBnB_clone_v2/blob/master/models/review.py) | Dynamically implements more classes |
| 10. Console 1.0 | [console.py](https://github.com/ChristianTonny/alu-AirBnB_clone_v2/blob/master/console.py) [/models/engine/file_storage.py](https://github.com/ChristianTonny/alu-AirBnB_clone_v2/blob/master/models/engine/file_storage.py) | Update the console and file storage system to work dynamically with all  classes update file storage |
<br>
<br>
<center> <h2>General Use</h2> </center>

1. First clone this repository.

3. Once the repository is cloned locate the "console.py" file and run it as follows:
```
/AirBnB_clone$ ./console.py
```
4. When this command is run the following prompt should appear:
```
(hbnb)
```
5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

##### Commands
    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)


##### Alternative Syntax
Users are able to issue a number of console command using an alternative syntax:

	Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands: 

    * all - Shows all objects the program has access to, or all objects of a given class

	* count - Return number of object instances by class

    * show - Shows an object based on class and UUID

	* destroy - Destroys an object based on class and UUID

    * update - Updates existing attributes an object based on class name and UUID

<br>
<br>
<center> <h2>Examples</h2> </center>
<h3>Primary Command Syntax</h3>

###### Example 0: Create an object
Usage: create <class_name>
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```
###### Example 1: Show an object
Usage: show <class_name> <_id>

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```
###### Example 2: Destroy an object
Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   
```
###### Example 3: Update an object
Usage: update <class_name> <_id>
```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```
<h3>Alternative Syntax</h3>

###### Example 0: Show all User objects
Usage: <class_name>.all()
```
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