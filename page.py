#from element import BasePageElement
from locators import LoginPageLocators, HomePageLocators

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.timeout=30

    def go_to(self):
        self.driver.get(self.url)


class LoginPage(BasePage):

    def __init__(self, driver):
        self.url = "https://www.hudl.com/login" 
        self.driver = driver

    def fill_email(self, email):
        email_elem = self.driver.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_elem.send_keys(email)
 
    def fill_password(self, password):
        password_elem = self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_elem.send_keys(password)

    def submit_login(self):
        login_btn = self.driver.find_element(*LoginPageLocators.SUBMIT_BTN)
        login_btn.click()

    def log_in_as(self, email, password):
        self.fill_email(email)
        self.fill_password(password)
        self.submit_login()

    def find_login_error(self):
        login_err_div = self.driver.find_element(*LoginPageLocators.LOGIN_ERROR)
        return login_err_div.text


class HomePage(BasePage):
    def __init__(self, driver):
        self.url="https://www.hudl.com/home"
        self.driver = driver
        self.driver.implicitly_wait(3)

    def find_coach_name(self): 
        self.driver.find_element(*HomePageLocators.NAVBAR)
        coachname_div = self.driver.find_element(*HomePageLocators.COACHNAME_ICON)
        return coachname_div.text
        

