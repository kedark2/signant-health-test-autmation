import requests
from requests.auth import HTTPBasicAuth
import os
import pytest

@pytest.fixture(scope="session")
def host_address():
    #SET API ADDRESS AS AN ENVIRONMENT VARIABLE
    return os.environ.get("API_ADDRESS", "http://localhost:8080")

@pytest.fixture(scope="session")
def user(host_address):
    #REMEMBER TO CREATE USER WITH SAME DETAILS AS use_dict FROM GUI AS POST REQUEST IS NOT WORKING
    user_dict = {"username":"user1", "password":"user1", "firstname":"firstname", "lastname":"lastname", "phone":123456}
    headers = {'Content-Type':'application/json'}
    response = requests.get(f"{host_address}/api/auth/token", auth=HTTPBasicAuth(user_dict["username"], user_dict["password"]))
    if response.status_code != 200:
        response = requests.post(f"{host_address}/register", json=user_dict, allow_redirects=False, headers=headers)
        assert response.status_code == 200
    return user_dict
 
@pytest.fixture(scope="session")
def token(host_address, user):
    response = requests.get(f"{host_address}/api/auth/token", auth=HTTPBasicAuth(user["username"], user["password"]))
    assert response.status_code == 200
    assert response.json()["token"]
    token = response.json()["token"]
    return  token

def test_obtaining_token(host_address, user):
    response = requests.get(f"{host_address}/api/auth/token", auth=HTTPBasicAuth(user["username"], user["password"]))
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["status"] == "SUCCESS"
    assert response_data["token"]


def test_obtaining_token_wrong_username(host_address):
    response = requests.get(f"{host_address}/api/auth/token", auth=HTTPBasicAuth("wrong username", "wrong password"))
    assert response.status_code == 401
    response_data = response.json()
    assert response_data["status"] == "FAILURE"

def test_getting_users(host_address, token):
    headers = {"Content-Type":"application/json","token": token}
    response = requests.get(f"{host_address}/api/users", headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["status"] == "SUCCESS"
    assert response_data["payload"]

def test_getting_users_without_token(host_address):
    response = requests.get(f"{host_address}/api/users")
    assert response.status_code == 401
    response_data = response.json()
    assert response_data["status"] == "FAILURE"

def test_getting_user_info(host_address, user, token):
    headers = {"Content-Type":"application/json","token": token}
    username = user["username"]
    response = requests.get(f"{host_address}/api/users/{username}", headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["status"] == "SUCCESS"
    assert response_data["payload"]
    assert response_data["payload"]["firstname"] == user["firstname"]

def test_getting_user_info_without_token(host_address, user):
    headers = {"Content-Type":"application/json"}
    username = user["username"]
    response = requests.get(f"{host_address}/api/users/{username}", headers=headers)
    assert response.status_code == 401
    response_data = response.json()
    assert response_data["status"] == "FAILURE"

def test_getting_user_info_wrong_token(host_address, user, token):
    headers = {"Content-Type":"application/json","token": "wrong token"}
    username = user["username"]
    response = requests.get(f"{host_address}/api/users/{username}", headers=headers)
    response_data = response.json()
    assert response.status_code == 401
    assert response_data["status"] == "FAILURE"

def test_getting_user_info_wrong_username(host_address, user, token):
    headers = {"Content-Type":"application/json","token": token}
    response = requests.get(f"{host_address}/api/users/wronguser", headers=headers)
    assert response.status_code == 401
    response_data = response.json()
    assert response_data["status"] == "FAILURE"

def test_update_user_info(host_address, user, token):
    headers = {'Content-Type':'application/json','token': token}
    username = user["username"]
    data = {"firstname": "new name", "last name": "new last name", "phone":1234}
    response = requests.put(f"{host_address}/api/users/{username}", json=data, headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["status"] == "SUCCESS"

def test_update_user_info_wrong_token(host_address, user):
    headers = {'Content-Type':'application/json','token': "wrong token"}
    username = user["username"]
    data = {"firstname": "new name", "last name": "new last name", "phone":1234}
    response = requests.put(f"{host_address}/api/users/{username}", json=data, headers=headers)
    assert response.status_code == 401
    response_data = response.json()
    assert response_data["status"] == "FAILURE"

def test_update_user_info_without_token(host_address, user):
    headers = {'Content-Type':'application/json'}
    username = user["username"]
    data = {"firstname": "new name", "last name": "new last name", "phone":1234}
    response = requests.put(f"{host_address}/api/users/{username}", json=data, headers=headers)
    assert response.status_code == 401
    response_data = response.json()
    assert response_data["status"] == "FAILURE"

def test_update_user_info_wrong_dataformat(host_address, user, token):
    headers = {'Content-Type':'application/json', "token":token}
    username = user["username"]
    data = {"firstnames": "new name", "last name": "new last name", "phone":1234}
    response = requests.put(f"{host_address}/api/users/{username}", json=data, headers=headers)
    assert response.status_code == 422
    response_data = response.json()
    assert response_data["status"] == "FAILURE"






 






