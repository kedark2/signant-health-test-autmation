# CRF Demo web App

## Installation Instructions

To run the demo application you need:

Python 3.7
pip install the included requirements.txt
SQLite3, [SQLite 3](https://www.sqlite.org/), effectively any version should work.

To run the application start it after installing the requirements with:

```
On Windows:
   set FLASK_APP=demo_app

On Linux:
   export FLASK_APP=demo_app

flask init-db
flask run --host=0.0.0.0 --port=8080
```

Alternatively, a Dockerfile is provided.

## Acceptance Criteria

As a UI user I can:

1: Register through web portal

2: Review my own user information from the main view

As an API Consumer I can:

1: Review users registered in system

2: If authenticated I can get personal information of users

3: If authenticated I can update personal information of users

## API Brief

The Application exposes a simple API with the following routes:

| Route                 | Methods  | Authentication |
| --------------------- | -------- | -------------- |
| /api/auth/token       | GET      | Basic          |
| /api/users            | GET      | Token          |
| /api/users/{username} | GET, PUT | Token          |

### Headers

Your request headers should set at minimum:

```
'Content-Type': 'application/json'
```

### Authentication

Access to users information requires a Token based authentication.

To receive a token perform basic authentication against `/api/auth/token` using the username/password you registered with in the Web interface.

For example:

```
>>> curl -u username:1234 http://localhost:8080/api/auth/token
{
  "status": "SUCCESS",
  "token": "MzMyNjQyMzAzODMwNjk1Mzg1MDU4OTA3MTEyMDM3MTQ2NDg5Mzg2"
}
```

For subsequent accesses to endpoints requiring a token update your request headers to include it:

```
'Content-Type': 'application/json'
'Token': 'MzMyNjQyMzAzODMwNjk1Mzg1MDU4OTA3MTEyMDM3MTQ2NDg5Mzg2'
```

### General API responses

All API calls respond in the following scheme:

```
{'status': 'SUCCESS/FAILURE',
           'message': 'human readable message',
           'payload': {...}}
```

### Updating user information

Subject information can be updated by sending PUT requests with a simple payload like:

```

{'datapoint1': 'value',
 'datapoint2': 'value',
  ...}
```

## Testing Instructions

### UI TEST

UI test has been written in Robotframework, so to be able to run robot, you need to have `robotframework` and `robotframework-selenium2library` installed. If you have install requirement.txt through pip, it should be ok. If you haven't done so, you can install them seperately also. Remember to check the versions from requirement.txt

### Note: you need to have firefox installed and 'geckodriver' executable to be in PATH

To run robot, navigate to `ui_test` folder through command line or terminal and just run `robot -d reports registration.robot` first to test the registration and then `robot -d reports login.robot` to test the login.

### API TEST

#### Framework used

- Pytest

  Read about pytest on (https://docs.pytest.org/en/6.2.x/)

- unittest

  Read about unite test on (https://docs.python.org/3/library/unittest.html)

#### Libraries used

- requests

  Requests is a HTTP library for python. Read more about requests on (https://docs.python-requests.org/en/latest/)

PIP install requirement.txt if you have not done so yet. Follow the instruction to run the app and keep it running for the API testing.

POST and PUT requests are not working for the app so it is important for you to create user from UI with following data first.

- Username = user1
- Password = user1
- First Name = firstname
- Family Name = lastname
- Phone number = 123456

API test has been done in 2 approachs each one can be found inside `approach1` and `approach2` folders respectively. Both folders are inside `tests/api_test` folder

Approach 1 is the recomended one and it is done with pytest framework.

To run the test, simply navigate to `tests/api_test/approach1` folder from command line or termainal and run `pytest test_api.py`

For approach 2, which can be found in `approach2` folder, `apitest.py` contains normal api testing functions which responses of api endpoints. Unit test of those functions and various api endpoints testing also has been done in `test_api.py`.

To run the test, navigate to `tests/api/approach2`folder from command line or terminal and run `python test_api.py` or ``
