## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project was made for learning reasons in order to gain knowledge and experience in Test Automation.
	
## Technologies
Project is created with:
* Python: 3.9.10
* Selenium for Python: 4.1.3+
* PyTest: 7.1.1+

versions of the packages might be updated within time
	
## Setup
To run this project, it is recommended to create virtual environment and then install all dependencies:

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