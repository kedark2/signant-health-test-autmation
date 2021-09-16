import requests
from requests.auth import HTTPBasicAuth

def obtaining_token(host_address, user):
    response = requests.get(f"{host_address}/api/auth/token", auth=HTTPBasicAuth(user["username"], user["password"]))
    return response
        
def obtaining_token_wrong_username(host_address):
    response = requests.get(f"{host_address}/api/auth/token", auth=HTTPBasicAuth("wrong username", "wrong password"))
    return response

def getting_users(host_address, token):
    headers = {"Content-Type":"application/json","token": token}
    response = requests.get(f"{host_address}/api/users", headers=headers)
    return response

def getting_users_without_token(host_address):
    response = requests.get(f"{host_address}/api/users")
    print("stat ", response.status_code)
    return response

def getting_users_wrong_token(host_address):
    headers = {"Content-Type":"application/json","token": "wrong token"}
    response = requests.get(f"{host_address}/api/users", headers=headers)
    return response

def getting_user_info(host_address, user, token):
    headers = {"Content-Type":"application/json","token": token}
    username = user["username"]
    response = requests.get(f"{host_address}/api/users/{username}", headers=headers)
    return response

def getting_user_info_without_token(host_address, user):
    headers = {"Content-Type":"application/json"}
    username = user["username"]
    response = requests.get(f"{host_address}/api/users/{username}", headers=headers)
    return response

def getting_user_info_wrong_token(host_address, user):
    headers = {"Content-Type":"application/json","token": "wrong token"}
    username = user["username"]
    response = requests.get(f"{host_address}/api/users/{username}", headers=headers)
    return response

def update_user_info_wrong_token(host_address, user):
    headers = {"Content-Type":"application/json","token": "wrong token"}
    username = user["username"]
    data = {"firstname": "new name", "last name": "new last name", "phone":1234}
    response = requests.put(f"{host_address}/api/users/{username}", json=data, headers=headers)
    return response

def update_user_info_without_token(host_address, user):
    headers = {"Content-Type":"application/json"}
    username = user["username"]
    data = {"firstname": "new name", "last name": "new last name", "phone":1234}
    response = requests.put(f"{host_address}/api/users/{username}", json=data, headers=headers)
    return response

def update_user_info_wrongdataformat(host_address, user, token):
    headers = {"Content-Type":"application/json", "token":token}
    username = user["username"]
    data = {"first": "new name", "last name": "new last name", "phone":1234}
    response = requests.put(f"{host_address}/api/users/{username}", json=data, headers=headers)
    return response

def update_user_info(host_address, user, token):
    headers = {'Content-Type':'application/json','token': token}
    username = user["username"]
    data = {"firstname": "new name", "last name": "new last name", "phone":1234}
    response = requests.put(f"{host_address}/api/users/{username}", json=data, headers=headers)
    return response









 






