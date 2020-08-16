from selenium.webdriver.common.by import By
from locators.locators import Locators
from testingdata.urls_input_data import Urlanddata

class HugoLandingPage:

  def __init__(self, browser):
    self.browser = browser

  def load(self):
    self.browser.get(Urlanddata.URL)

  def click_login_from_hugo(self):
    login_button = self.browser.find_element(*Locators.LOGIN_BUTTON)
    login_button.click()