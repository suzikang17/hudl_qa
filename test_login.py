import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

import page

class LogInTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.test_email = "suzikang17@gmail.com"
        self.test_password = "t.WX7M*Cvcx!BKP"

    def test_login_correct_credentials(self):
        # happy path -- correct page title
        login_page = page.LoginPage(self.driver)
        login_page.go_to()
        login_page.log_in_as(self.test_email, self.test_password)
        time.sleep(2)
        self.assertIn("Home", self.driver.title)
        self.assertEqual(self.driver.current_url, "https://www.hudl.com/home")

    def test_correct_user_homepage(self):
        # happy path -- correct coach name
        login_page = page.LoginPage(self.driver)
        login_page.go_to()
        login_page.log_in_as(self.test_email, self.test_password)
        home_page = page.HomePage(self.driver)
        coachname_txt = home_page.find_coach_name()
        self.assertEqual("Coach K", coachname_txt)

    def test_wrong_email(self):
        # assert that wrong email will not work
        login_page = page.LoginPage(self.driver)
        login_page.go_to()
        login_page.log_in_as("sadjkl", "beepbop")

        self.assertNotIn("Home", driver.title)

    def test_wrong_password(self):
        # assert that wrong password will not work
        login_page = page.LoginPage(self.driver)
        login_page.go_to()
        login_page.log_in_as(self.test_email, "beepbop")

        time.sleep(2)
        self.assertIn("Log In", driver.title)

    def test_empty(self):
        # assert that empty credentials will not work
        login_page = page.LoginPage(self.driver)
        login_page.go_to()
        login_page.submit_login()

        self.assertIn("Log In", driver.title)

    def test_login_error_help(self):
        # assert that trying to login with wrong credentials
        # will pop-up a log-in error box with help text
        login_page = page.LoginPage(self.driver)
        login_page.go_to()
        login_page.log_in_as(self.test_email, "beepbop")
        #self.assertIsNotNone(login_error_div)
        time.sleep(2)
        login_error_text = login_page.find_login_error()
        self.assertEqual(
            "We didn't recognize that email and/or password. Need help?",
            login_error_text
        )

    def test_login_error_righttime(self):
        # assert that login error doesn't exist when you haven't entered anything yet
        login_page = page.LoginPage(self.driver)
        login_page.go_to()
        login_page.log_in_as(self.test_email, "beepbop")
        #self.assertIsNotNone(login_error_div)
        time.sleep(2)
        login_error_text = login_page.find_login_error()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
