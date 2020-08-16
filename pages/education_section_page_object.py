from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from tests.globals import initialize
from testingdata.readfromxl import ReadWriteExcel
from locators.locators import Locators
from testingdata.urls_input_data import Urlanddata

class EducationSection:

    def __init__(self, browser):
      self.browser = browser

    def open_addanother_form_of_education(self):
        addanothereee = self.browser.find_element(*Locators.ADDANOTHERRRRRR)
        addanothereee.click()

    def type_university_name(self):
        universityname = self.browser.find_element(*Locators.UNIVERSITYFIELD)
        universityname.click()
        initialize.university = ReadWriteExcel.university(self)
        universityname.send_keys(initialize.university)

    def graduation_year_field(self):
        graduationyear = self.browser.find_element(*Locators.GRADUATIONYEARFIELD)
        graduationyear.click()
        yearrrr = self.browser.find_element(*Locators.YEARR)
        yearrrr.click()

    def degree_field(self):
        degreefield = self.browser.find_element(*Locators.DEGREEFIELD)
        degreefield.click()
        initialize.degree = ReadWriteExcel.degree(self)
        degreefield.send_keys(initialize.degree)

    def click_addd(self):
        clcikaddd = self.browser.find_element(*Locators.ADDBUTTTON)
        clcikaddd.click()

    def get_input_text_and_verify(self):
        inpt = self.browser.find_element_by_xpath(Locators.GETINPUTTEXTANDVEIFY1).text
        return inpt

    def click_edit_button(self):
        edittt_button = self.browser.find_element(*Locators.EDITTTBUTTON)
        edittt_button.click()

    def clear_university_name(self):
        university_fieldddd = self.browser.find_element(*Locators.EDITUNIVERSITYNAMEFIELD)
        university_fieldddd.send_keys(Keys.CONTROL + "a")
        university_fieldddd.send_keys(Keys.BACKSPACE)
    def save_educationfield_asitis(self):
        savve = self.browser.find_element(*Locators.SAVEBUTTONNNN)
        savve.click()
    def get_alerttt_text_and_verify(self):
        inpt = self.browser.find_element(*Locators.ALERTTTT).text
        return inpt
    def enter_new_university_name(self):
        university_fieldddd = self.browser.find_element(*Locators.EDITUNIVERSITYNAMEFIELD)   
        initialize.university = ReadWriteExcel.university(self)
        university_fieldddd.send_keys(initialize.university)
    
    def get_edited_text_and_verify(self):
        inpt2 = self.browser.find_element_by_xpath(Locators.GETEDITEDTEXTANDVERIFY1).text
        return inpt2

    def enterrhugetext(self):
        university_fieldddd = self.browser.find_element(*Locators.EDITUNIVERSITYNAMEFIELD)
        university_fieldddd.send_keys(Urlanddata.ENTERHUGETEXT)