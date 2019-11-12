import json
import requests
import unittest

BASE_URL = "https://hudl.com/home/games"


class GetRequestTest(unittest.TestCase):
    def setUp(self):
        self.url = BASE_URL
        self.auth = {"username": "testuser", "password": "testpassword"}
        self.expected_payload = [
            {
                "gameId": "123456 ",
                "sqlId": "123456",
                "date": "2016-01-01T19:00:00",
                "opponent": "TestOpponent",
                "opponentId": "123456",
                "isHome": True,
                "gameType": 0,
                "categories": [],
            },
            {
                "gameId": "11111 ",
                "sqlId": "11111",
                "date": "2016-01-01T19:00:00",
                "opponent": "TestOpponent2",
                "opponentId": "99",
                "isHome": False,
                "gameType": 0,
                "categories": [],
            },
        ]

    def test_status_code(self):
        response = requests.get(self.url, auth=self.auth)
        self.assertEqual(response.status_code, 200)

    def test_response_content(self):
        response = requests.get(self.url, auth=test_auth)
        self.assertEqual(reponse.json(), self.expected_payload)

    def test_headers(self):
        response = requests.get(self.url, auth=self.auth)
        self.assertEqual(response.headers.get("content-type"), "application/json")

    def test_no_auth(self):
        response = requests.get(self.url)
        self.assertEqual(response.status_code, 401)

    def test_known_id(self):
        response = requests.get(self.url, auth=self.auth, params={"gameId": "123456"})
        self.assertEqual(response.json(), self.expected_payload)

    def test_wrong_id(self):
        response = requests.get(self.url, auth=test_auth, params={"gameId": "999999"})
        self.assertEqual(response.status_code, 404)


class PutRequestTest(unittest.TestCase):
    def setUp(self):
        self.updated_payload = {
            "gameId": "123456",
            "sqlId": "123456",
            "date": "2016-01-01T19:00:00",
            "opponent": "TestOpponent updated",
            "opponentId": "123456",
            "isHome": True,
            "gameType": 0,
            "categories": [],
        }
        self.url = BASE_URL + "/123456"  # gameId as endpoint
        self.auth = {"username": "testuser", "password": "testpassword"}

    def test_status_code(self):
        response = requests.put(url=self.url, auth=self.auth, json=self.payload)
        self.assertEqual(response.status_code, 200)

    def test_response_content(self):
        response = requests.put(url=self.url, auth=self.auth, json=self.updated_payload)
        self.assertEqual(response.json(), self.updated_payload)

    def test_invalid_date(self):
        new_payload = self.updated_payload
        new_payload["date"] = "1992-15-02 16:00:00"
        response = requests.put(url=self.url, auth=self.auth, json=new_payload)
        self.assertEqual(response.status_code, 403)

    def test_invalid_input_struct(self):
        bad_payload = {"blahblah": "beepbop"}
        response = requests.put(url=self.url, auth=self.auth, json=bad_payload)
        self.assertEqual(response.status_code, 403)


class PostRequestTest(unittest.TestCase):
    def setUp(self):
        self.url = BASE_URL
        self.payload = {
            "gameId": "123457",
            "sqlId": "123457",
            "date": "2016-01-01T19:00:00",
            "opponent": "Another opponent",
            "opponentId": "100",
            "isHome": False,
            "gameType": 0,
            "categories": [],
        }

    def test_status_code(self):
        response = requests.post(self.url, auth=self.auth, json=self.payload)
        self.assertEqual(response.status_code, 200)

    def test_response_content(self):
        response = requests.post(self.url, auth=self.auth, json=self.payload)
        self.assertEqual(response.json(), self.payload)

    def test_invalid_time(self):
        new_payload = self.payload
        new_payload["date"] = "1992-15-02 16:00:00"
        response = requests.post(self.url, auth=self.auth, json=invalid_payload)
        self.assertEqual(res.status_code, 403)

    def test_empty_body(self):
        response = request.post(self.url, json={})
        self.assertEqual(res.status_code, 403)


class DeleteRequestTest(unittest.TestCase):
    def setUp(self):
        self.url = BASE_URL

    def test_status_code(self):
        response = requests.delete(self.url + "/11111", auth=self.auth)
        self.assertEqual(response.status_code, 204)

    def test_content_empty(self):
        response = requests.delete(self.url + "/11111", auth=self.auth)
        self.assertEqual(len(response.json()), 0)

    def test_get_deleted_entry(self):
        response = requests.get(self.url + "/11111", auth=self.auth)
        self.assertEqual(response.status_code, 404)
