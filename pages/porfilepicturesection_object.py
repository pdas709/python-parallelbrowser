from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tests.globals import initialize
from testingdata.readfromxl import ReadWriteExcel
from locators.locators import Locators
from testingdata.urls_input_data import Urlanddata

class Profile_Picture_Section:

  def __init__(self, browser):
    self.browser = browser

  def load_(self):
    self.browser.get(Urlanddata.URLPROFILEPAGE)

  def top_mostsectionofprofilepicture(self):
    editbutton001 = self.browser.find_element(*Locators.PROFILEPICTURESECTIONEDITBUTTON)
    editbutton001.click()

  def edit_fieldsinthetopmostsectionofprofilepicture(self):
    crossbuttonprofilepicturesectionn = self.browser.find_element(*Locators.CROSSBUTTONPROFILEPICTURESECTION)
    crossbuttonprofilepicturesectionn.click()

  def clickaddanotherprofilepicturesection(self):
    addanotherprofilepicturesection = self.browser.find_element(*Locators.ADDANOTHERPROFILEPICTURESECTIONN)
    addanotherprofilepicturesection.click()

  def inputfield_profilepicturesection(self):
    entervalueprofilepicturesection = self.browser.find_element(*Locators.INPUTFIELDPROFILEPICTURESECTION)
    entervalueprofilepicturesection.send_keys(Keys.LEFT_CONTROL + 'a')
    initialize.profile_pictureSection = ReadWriteExcel.profile_pictureSection(self)
    entervalueprofilepicturesection.send_keys(initialize.profile_pictureSection)

  def click_save_profilepicturesection(self):
    savvebuttonprofilepicturesection = self.browser.find_element(*Locators.SAVEBUTTONPROFILEPICTURESECTON)
    savvebuttonprofilepicturesection.click()

  def get_input_text_and_verifyyyyy(self):
      inpt = self.browser.find_element_by_xpath(Locators.GETINPUTTEXTANDVERIFYELEMENT).text
      #elem_text = inpt.getText()
      return inpt

  def newinputfield_profilepicturesection_fromaddanother(self):
    entervaluse_tonew_field = self.browser.find_element(*Locators.NEWINPUTFIELDFROMADDANOTHER)
    entervaluse_tonew_field.click()
    initialize.profile_pictureSection = ReadWriteExcel.profile_pictureSection(self)
    entervaluse_tonew_field.send_keys(initialize.profile_pictureSection)

  def longinput_profilepicturesection(self):
      enterlongvaluse_tonew_field = self.browser.find_element(*Locators.NEWINPUTFIELDFROMADDANOTHER)
      enterlongvaluse_tonew_field.click()
      enterlongvaluse_tonew_field.send_keys(Urlanddata.LONGINPUT)

  def get_input_text_fromaddanother(self):
      inpt = self.browser.find_element_by_xpath(Locators.GETINPUTTEXTFROMADDANOTHER).text
      return inpt

  def get_null_alert(self):
      on_null = self.browser.find_element_by_xpath(Locators.GETNULLALERT).text
      return on_null

  def get_char_limit_alert(self):
      on_char_limit = self.browser.find_element_by_xpath(Locators.GETCHARLIMITALERT).text
      return on_char_limit