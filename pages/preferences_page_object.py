from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators.locators import Locators
from testingdata.urls_input_data import Urlanddata
from testingdata.readfromxl import ReadWriteExcel
from tests.globals import initialize

class Preferences:
  
  def __init__(self, browser):
    self.browser = browser

  def clickontheeditbutton_preferences(self):
    editbutton0111 = self.browser.find_element(*Locators.EDITBOTTTON)
    editbutton0111.click()

  def travel_remote(self):
      uptoo100 = self.browser.find_element(*Locators.UPTO100)
      uptoo100.click()

  def remote_option(self):
      remoteoptioncheckk = self.browser.find_element(*Locators.REMOTEOPTIONCHECKBOX)
      remoteoptioncheckk.click()

  def industry_selection_check(self):
      box = self.browser.find_element(*Locators.MINMUMREVENUEFIELD)
      return box

  def industry_revenue_selection(self):
      minimumrevenue = self.browser.find_element(*Locators.MINMUMREVENUEFIELDCHECK)
      minimumrevenue.click()

  def check_engineeringtab(self):
      engineeringtab_ = self.browser.find_element_by_xpath(Locators.CHECKENGINEERINGTAB)
      return engineeringtab_

  def engineeringtab_cross(self):
      cross = self.browser.find_element(*Locators.CROSS)
      cross.click()

  def industry_field(self):
      industryfield = self.browser.find_element(*Locators.INDUSTRYTAB)
      industryfield.click()
      industryfield.send_keys(Keys.CONTROL + 'a')
      industryfield.send_keys(Keys.BACKSPACE)
      industryfield.send_keys(Urlanddata.INDUSTRY)

  def select_industry__dropdown(self):
      selectengi = self.browser.find_element(*Locators.SELECTENGINEERINGFROMDROPDOWN)
      selectengi.click()

  def addanother_location(self):
      addanotherlocaton = self.browser.find_element(*Locators.ADDANOTHERLOCATIION)
      addanotherlocaton.click()
  def savebbutton(self):
      savveebuttton = self.browser.find_element(*Locators.SAVVVVEBUTTON)
      savveebuttton.click()

  def entercty(self):
    cityname = self.browser.find_element(*Locators.CITYFIELD)
    cityname.click()
    #initialize.city = ReadWriteExcel.city(self)
    cityname.send_keys("Gurgaon")
   



  def enterstate(self):
      typestate = self.browser.find_element(*Locators.STATEFELD)
      typestate.send_keys(Urlanddata.STATE)
  
  def verify_tttext(self):
      ttt = self.browser.find_element_by_xpath(Locators.VERIFYTEXT).text
      return ttt

  def click_outside_state_populates(self):
      clickk = self.browser.find_element_by_xpath(Locators.CLICKOUTSIDELOCATION)
      clickk.click()