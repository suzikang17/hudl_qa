import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

class LogInTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.test_email = "suzikang17@gmail"

    def test_login_correct_credentials(self):
        # happy path -- correct page title
        driver = self.driver
        driver.get("https://www.hudl.com/login")
        email = driver.find_element_by_id("email")
        email.send_keys(test_email)
        password = driver.find_element_by_id("password")
        password.send_keys("t.WX7M*Cvcx!BKP")
        log_in_btn = driver.find_element_by_id("logIn")
        log_in_btn.click()
        time.sleep(3)
        self.assertIn("Home", driver.title)
        self.assertEqual(driver.current_url, "https://www.hudl.com/home")

    def test_correct_user_homepage(self):
        # happy path -- correct coach name
        driver = self.driver
        driver.implicitly_wait(3)
        driver.get("https://www.hudl.com/login")
        email = driver.find_element_by_id("email")
        email.send_keys(test_email)
        password = driver.find_element_by_id("password")
        password.send_keys("t.WX7M*Cvcx!BKP")
        log_in_btn = driver.find_element_by_id("logIn")
        log_in_btn.click()

        driver.find_element_by_id(
            "ssr-webnav"
        )  # just make sure we can find the navbar before grabbing html
        soup = BeautifulSoup(driver.page_source, "html.parser")
        coachname_div = soup.find("div", {"class": "hui-globaluseritem__display-name"})
        self.assertEqual("Coach K", coachname_div.span.text)

    def test_wrong_email(self):
        # assert that wrong email will not work
        driver = self.driver
        driver.get("https://www.hudl.com/login")
        email = driver.find_element_by_id("email")
        email.send_keys("sadjkl")
        password = driver.find_element_by_id("password")
        password.send_keys("beepbop")
        log_in_btn = driver.find_element_by_id("logIn")
        log_in_btn.click()
        self.assertNotIn("Home", driver.title)

    def test_wrong_password(self):
        # assert that wrong password will not work
        driver = self.driver
        driver.get("https://www.hudl.com/login")
        email = driver.find_element_by_id("email")
        email.send_keys(test_email)
        password = driver.find_element_by_id("password")
        password.send_keys("beepbop")
        log_in_btn = driver.find_element_by_id("logIn")
        log_in_btn.click()
        time.sleep(2)
        self.assertIn("Log In", driver.title)

    def test_empty(self):
        # assert that empty credentials will not work
        driver = self.driver
        driver.get("https://www.hudl.com/login")
        log_in_btn = driver.find_element_by_id("logIn")
        log_in_btn.click()
        time.sleep(2)
        self.assertIn("Log In", driver.title)

    def test_login_error_help(self):
        # assert that trying to login with wrong credentials
        # will pop-up a log-in error box with help text
        driver = self.driver
        driver.get("https://www.hudl.com/login")
        email = driver.find_element_by_id("email")
        email.send_keys(test_email)
        password = driver.find_element_by_id("password")
        password.send_keys("beepbop")
        log_in_btn = driver.find_element_by_id("logIn")
        log_in_btn.click()
        time.sleep(2)
        login_soup = BeautifulSoup(driver.page_source, "html.parser")
        login_error_div = login_soup.find("div", {"class": "login-error"})
        self.assertIsNotNone(login_error_div)
        self.assertEqual(
            "We didn't recognize that email and/or password. Need help?",
            login_error_div.p.text,
        )

    def test_login_error_righttime(self):
        # assert that login error doesn't exist when you haven't entered anything yet
        driver = self.driver
        driver.get("https://www.hudl.com/login")
        login_soup = BeautifulSoup(driver.page_source, "html.parser")
        login_error_div = login_soup.find("div", {"class": "login-error"})
        self.assertEqual(login_error_div.p.text, "")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
