## Table of contents
* [General Info](#general-info)
* [Technologies & Tools](#technologies-&-tools)
* [Environment Setup](#environment-setup)
* [Running Tests](#running-tests)
* [Additional Info](#additional-info)

## General info
Test-Automation Project in Python was created for learning reasons and as my first major step in Test Automation area. After almost 2 years of mixed commercial experience of manual and automated test environments I decided to gain knowledge on how to write automated test scripts in Python using Selenium library.

I chose www.olx.pl - polish website for posting advertisments due to having a lot of potential ways of automating processes and different scenarios that may occurr.  
	
## Technologies & Tools

* Python: v3.10.5
* Selenium for Python: v4.1.3+
* PyTest: v7.1.1+
* Jenkins v2.355
* Docker v20.10.14

## Environment Setup

### 1. Setting up global parameters:
I have created special user account for testing purposes in order to not to use my private one. 
If you want to run this project by your own, you must create free account on olx.pl, 
and then fill in user credentials in utils/globals.py file. 

To run this project you may use both local WebDriver executable (default is safari) and remote WebDriver instance along with Selenium grid to run tests. 
That means you must specify IP address or localhost to connect to Selenium Hub with its connected nodes.

The whole config (global.py) file should look like this:
> * ```SEL_GRID_URL = '<ip_or_localhost>:4444/wd/hub'```
> * ```TEST_EMAIL = 'email@test.com'```
> * ```TEST_PASSWORD = 'password'```


### 2. Setting up virtual environment:
It is recommended to create separate virtual environment while running python projects.
Then you should open new terminal so it points on newly created venv. Then install all
required dependencies.

```
$ python -m venv .venv 
$ pip install -r requirements.txt
```
It is recommended to set up $PYTHTONPATH so it will run the project from the proper root path.
Second command in order to verify set up path.

```
$ export PYTHONPATH='<your-path-to-project>/Test-Automation/'
$ echo $PYTHONPATH
```

## Running Tests

To run specific module tests use this command:
```
pytest --browser=<browser_name> tests/unit/test_login::TestLogin
```
But you can also target specific test name:
```
pytest --browser=<browser_name> tests/unit/test_login::TestLogin::test_login_cookie
```
## Additional Info

Some tests skip login procedure and use saved cookies files to execute processes as logged in user.
If there is no such file those tests will fail. In order to prevent that it's important to 
run "test_login_valid_user" firstly, because it creates and saves cookie file in utils/cookies path.
