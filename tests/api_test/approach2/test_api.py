import unittest
import apitest

class TestApi(unittest.TestCase):
    USER_DATA = {"username":"user1", "password":"user1", "firstname":"firstname", "lastname":"lastname", "phone": 123456}
    WRONG_DATA = {"username":"newuser", "password":"passsword", "firstname":"first name", "lastname":"lastname"}
    BASE_URL = "http://localhost:8080"

    def test_obtaining_token(self):
        response = apitest.obtaining_token(self.BASE_URL, self.USER_DATA)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "SUCCESS")
        self.assertTrue(response.json()["token"])
        return response.json()["token"]
    
    def test_obtaining_token_wrong_data(self):
        response = apitest.obtaining_token(self.BASE_URL, self.WRONG_DATA)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["status"], "FAILURE")
    
    def test_obtaining_token_wrong_username(self):
        response = apitest.obtaining_token_wrong_username(self.BASE_URL)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["status"], "FAILURE")
        
    def test_getting_users_without_token(self):
        response = apitest.getting_users_without_token(self.BASE_URL)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["status"], "FAILURE")
    
    def test_getting_users_wrong_token(self):
        response = apitest.getting_users_wrong_token(self.BASE_URL)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["status"], "FAILURE")
    
    def test_getting_users(self):
        response = apitest.getting_users(self.BASE_URL, self.test_obtaining_token())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "SUCCESS")
        self.assertTrue(response.json()["payload"])

    def test_getting_user_info(self):
        response = apitest.getting_user_info(self.BASE_URL, self.USER_DATA, self.test_obtaining_token())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "SUCCESS")
        self.assertTrue(response.json()["payload"])
    
    def test_getting_user_info_without_token(self):
        response = apitest.getting_user_info_without_token(self.BASE_URL, self.USER_DATA)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["status"], "FAILURE")
    
    def test_getting_user_info_wrong_token(self):
        response = apitest.getting_user_info_wrong_token(self.BASE_URL, self.USER_DATA)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["status"], "FAILURE")
    
    def test_update_user_info_wrong_token(self):
        response = apitest.update_user_info_wrong_token(self.BASE_URL, self.USER_DATA)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["status"], "FAILURE")
    
    def test_update_user_info_without_token(self):
        response = apitest.update_user_info_without_token(self.BASE_URL, self.USER_DATA)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["status"], "FAILURE")
    
    def test_update_user_info_wrongdataformat(self):
        response = apitest.update_user_info_wrongdataformat(self.BASE_URL, self.USER_DATA, self.test_obtaining_token())
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json()["status"], "FAILURE")
    
    def test_update_user_info(self):
        response = apitest.update_user_info(self.BASE_URL, self.USER_DATA, self.test_obtaining_token())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "SUCCESS")
    
if __name__ == '__main__':
    unittest.main()

