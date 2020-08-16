from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators.locators import Locators
from testingdata.urls_input_data import Urlanddata

class Skills:
  
  def __init__(self, browser):
    self.browser = browser

  def load_(self):
    self.browser.get(self.URL)

  def clickontheeditbutton_skills(self):
    editbutton011 = self.browser.find_element(*Locators.EDITBUTTONSKILLS)
    editbutton011.click()

  def input_skills(self):
    inputfield = self.browser.find_element(*Locators.SKILLSINPUTFIELD)
    inputfield.click()
    inputfield.send_keys(Urlanddata.INPUTSKILLS)

  def selectfromdropdown(self):
    selectskill = self.browser.find_element(*Locators.SELECTSKILL)
    selectskill.click()

  def clicksave(self):
    saveve = self.browser.find_element(*Locators.SAVEBUTTON)
    saveve.click()

  def verify_skillsaved(self):
      inpttt = self.browser.find_element_by_xpath(Locators.VERIFYSKILLSAVED).text
      return inpttt

  def verify_alerttext(self):
      a_alertt = self.browser.find_element_by_xpath(Locators.VERIFYALERTTEXT).text
      return a_alertt