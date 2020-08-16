from selenium.webdriver.common.by import By
from locators.locators import Locators
from testingdata.urls_input_data import Urlanddata

class Login_Page:

    def __init__(self, browser):
      self.browser = browser

    def enter_email(self):
        emailfield = self.browser.find_element(*Locators.EMAILFIELD)
        emailfield.send_keys(Urlanddata.USER_NAME)

    def enter_password(self):
        passwordfield = self.browser.find_element(*Locators.PASSWORDFIELD)
        passwordfield.send_keys(Urlanddata.PW)

    def click_login_(self):
    
      login_button = self.browser.find_element(*Locators.LOGINBUTTON)
      login_button.click()