from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    EMAIL_FIELD = (By.ID, 'email')
    PASSWORD_FIELD =  (By.ID, 'password')
    SUBMIT_BTN = (By.ID, 'logIn')
    LOGIN_ERROR = (By.XPATH, "//div[@class='login-error-container']")

class HomePageLocators(object):
    COACHNAME_ICON = (By.XPATH, "//div[@class='hui-globaluseritem__display-name']")
    NAVBAR = (By.ID, 'ssr-webnav')

