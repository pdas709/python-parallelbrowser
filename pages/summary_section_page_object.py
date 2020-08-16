from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tests.globals import initialize
from testingdata.readfromxl import ReadWriteExcel
from locators.locators import Locators
from testingdata.urls_input_data import Urlanddata

class Summary_Section:

  def __init__(self, browser):
    self.browser = browser

  def load_(self):
    self.browser.get(self.URL)

  def clickontheeditbutton_summary(self):
    editbutton011 = self.browser.find_element(*Locators.SUMMARYEDITBUTTON)
    editbutton011.click()

  def summaryfield(self):
      summary_field = self.browser.find_element(*Locators.SUMMARYINPUTFIELD)
      summary_field.click()
      summary_field.send_keys(Keys.CONTROL + 'a')
      summary_field.send_keys(Keys.ARROW_RIGHT)
      initialize.summary_field = ReadWriteExcel.summary_field(self)
      summary_field.send_keys(Keys.ENTER + initialize.summary_field)

  def longsummaryfield(self):
        longsummary_field = self.browser.find_element(*Locators.SUMMARYINPUTFIELD)
        longsummary_field.click()
        longsummary_field.send_keys(Keys.CONTROL + 'a')
        longsummary_field.send_keys(Keys.ARROW_RIGHT)
        longsummary_field.send_keys(Keys.ENTER + Urlanddata.LONGSUMMARYFIELD)

  def clearsummaryfield(self):
        clearsummary_field = self.browser.find_element(*Locators.SUMMARYINPUTFIELD)
        clearsummary_field.click()
        clearsummary_field.send_keys(Keys.CONTROL + 'a')
        clearsummary_field.send_keys(Keys.BACKSPACE)

  def availabilty_check(self):
      availabilitycheck = self.browser.find_element(*Locators.SUMMARYINPUTFIELD)
      availabilitycheck.click()
      availabilitycheck.click()

  def expected_rate(self):
      rate = self.browser.find_element(*Locators.RATEFIELD)
      rate.click()
      rate.send_keys(Keys.CONTROL + 'a')
      rate.send_keys(Keys.BACKSPACE)
      initialize.min_expected_rate = ReadWriteExcel.min_expected_rate(self)
      rate.send_keys(initialize.min_expected_rate)

  def clickk_save(self):
      ssavvvebutton = self.browser.find_element(*Locators.SAVEBBUTTTON)
      ssavvvebutton.click()

  def verify_summary_text(self):
      getsummarytext = self.browser.find_element_by_xpath(Locators.VERIFYSUMMARYTEXT).text
      return getsummarytext

  def verify_summary_char_limit_alert(self):
      aalertt = self.browser.find_element_by_xpath(Locators.VERIFYSUMMARYCHARLIMITALERT).text
      return aalertt

  def verify_summary_null_alert(self):
      a_alertt = self.browser.find_element_by_xpath(Locators.VERIFYSUMMARYNULLALERT).text
      return a_alertt
