from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from tests.globals import initialize
from testingdata.readfromxl import ReadWriteExcel
from locators.locators import Locators
from testingdata.urls_input_data import Urlanddata

class WorkExperienceSection:

    def __init__(self, browser):
      self.browser = browser

    def open_addanother_form_of_work_Experience(self):
        addanothereee = self.browser.find_element(*Locators.ADDANOTHERRRR)
        addanothereee.click()

    def type_companyname(self):
        companynamefielddd = self.browser.find_element(*Locators.COMPANYNAMEFIELD)
        companynamefielddd.click()
        initialize.company = ReadWriteExcel.company(self)
        companynamefielddd.send_keys(initialize.company)

    def type_longcompanyname(self):
        companynamefielddd = self.browser.find_element(*Locators.COMPANYNAMEFIELD)
        companynamefielddd.click()
        companynamefielddd.send_keys(Urlanddata.LONGCOMPANYNAME)

    def type_job_title(self):
        jobtitlefield = self.browser.find_element(*Locators.JOBTITLEFIELD)
        jobtitlefield.click()
        initialize.role = ReadWriteExcel.role(self)
        jobtitlefield.send_keys(initialize.role)

    def job_dates(self):
        startdate = self.browser.find_element(*Locators.STARTDATE)
        startdate.click()
        march = self.browser.find_element(*Locators.MARCH)
        march.click()
    
    def job_description(self):
        jobdescription = self.browser.find_element(*Locators.JOBDESCRIPTION)
        jobdescription.click()
        initialize.job_description = ReadWriteExcel.job_description(self)
        jobdescription.send_keys(initialize.job_description)

    def click_add(self):
        addbuttonnn = self.browser.find_element(*Locators.ADDBUTTONN)
        addbuttonnn.click()

    def get_input_text_and_verifyy(self):
        inpt = self.browser.find_element_by_xpath(Locators.INPUTTEXTVERIFY).text
        #elem_text = inpt.getText()
        return inpt

    def click_editt_buttton(self):
        edittt_button = self.browser.find_element(*Locators.EDITBUTTTON)
        edittt_button.click()

    def come_to_description_field_and_update(self):
        descriptionnn = self.browser.find_element(*Locators.DESCRIPTIONFIELD)
        descriptionnn.click()
        descriptionnn.send_keys(Keys.CONTROL + 'a')
        descriptionnn.send_keys(Keys.ARROW_RIGHT)
        descriptionnn.send_keys(Keys.ENTER + '•')
        initialize.job_description = ReadWriteExcel.job_description(self)
        descriptionnn.send_keys(initialize.job_description)

    def save_edited_form(self):
        click_savvve = self.browser.find_element(*Locators.SAVVVEBUTTON)
        click_savvve.click()

    def get_edited_saved_text_and_verifyy(self):
        inpt = self.browser.find_element_by_xpath(Locators.EDITEDSAVEDTEXTVERIFY).text
        return inpt

    def allertttt_text_and_verifyy(self):
        alerrrt = self.browser.find_element_by_xpath(Locators.ALERTTEXTVERIFY1).text
        return alerrrt

    def allertttttttt_text_and_verifyy(self):
        alerrrrrt = self.browser.find_element_by_xpath(Locators.ALERTTEXTVERIFY2).text
        return alerrrrrt