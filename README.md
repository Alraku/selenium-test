## Table of contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Additional-Files](#additional-files)

## General info
This project was made for learning reasons in order to gain knowledge and experience in Test Automation.
	
## Technologies
Project is created mainly with:
* Python: 3.9.10
* Selenium for Python: 4.1.3+
* PyTest: 7.1.1+

versions of the packages might be updated within time
	
## Setup
To run this project, it is recommended to create virtual environment and then install all dependencies (please refer to requirements.txt file within project file tree):

```
$ python -m venv .venv 
# open new terminal after that so it will point on newly created venv.
$ pip install <dependencies>
```

It is recommended to set up $PYTHTONPATH so it will run the project from the proper root path.

```
$ export PYTHONPATH='<your-path-to-project>/Test-Automation/'
```

Then verify that path by executing:

```
$ echo $PYTHONPATH
```

## Additional Files

For proper working of all tests it's important to run "test_login_valid_user" as first test because it creates and saves cookie file in utils/cookies that will be needed in tests that require user logged in.

You may also want to create your own test account and put login credentials in file with global values.
It is recommended to create such file as globals.py in utils/globals.py.