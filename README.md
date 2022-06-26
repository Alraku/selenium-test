## Test-Automation Project in Python

## Table of contents
* [General Info](#general-info)
* [Technologies & Tools](#technologies-&-tools)
* [Environment Setup](#environment-setup)
* [Running Tests](#running-tests)
* [Additional Files](#additional-files)

## General info
This project was created for learning reasons and as my first major step in Test Automation area. After almost 2 years of mixed commercial experience of manual and automated test environments I decided to gain knowledge on how to write automated test scripts in Python using Selenium library.

I chose www.olx.pl - polish website for posting advertisments due to having a lot of potential ways of automating processes and different scenarios that may occurr.  
	
## Technologies & Tools

* Python: v3.9.10
* Selenium for Python: v4.1.3+
* PyTest: v7.1.1+
* Jenkins v2.355
* Docker v20.10.14

## Environment Setup

### 1. Setting global parameters
To run this project, you must create free account on olx.pl, ant then fill in credentials in utils/globals.py file. ```SEL_GRID_URL``` is an IP address of Selenium Grid that tests will be connecting to.

> * ```SEL_GRID_URL = '<ip_or_localhost>:4444/wd/hub'```
> * ```TEST_EMAIL = 'email@test.com'```
> * ```TEST_PASSWORD = 'password'```

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

## Running Tests

local remote
edge safari chrome

## Additional Files

For proper working of all tests it's important to run "test_login_valid_user" as first test because it creates and saves cookie file in utils/cookies that will be needed in tests that require user logged in.

You may also want to create your own test account and put login credentials in file with global values.
It is recommended to create such file as globals.py in utils/globals.py.