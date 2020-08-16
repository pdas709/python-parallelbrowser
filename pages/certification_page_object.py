from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from tests.globals import initialize
from testingdata.readfromxl import ReadWriteExcel
import openpyxl
from locators.locators import Locators
from testingdata.urls_input_data import Urlanddata

class CertificationBottomofpage:
    
    def __init__(self, browser):
      self.browser = browser

    def open_addanother_form_of_certifications(self):
        addanotheree = self.browser.find_element(*Locators.ADDANOTHERRR)
        addanotheree.click()

    def add_the_certification1(self):
        certificationfield = self.browser.find_element(*Locators.CERTOIFICATIONFIELDNEW)
        initialize.addcert = ReadWriteExcel.readandADDCertificate(self)
        certificationfield.send_keys(Keys.LEFT_CONTROL + 'a')
        certificationfield.send_keys(initialize.addcert)

    def clickaddcertification(self):
        addbuttoncert = self.browser.find_element(*Locators.SAVEBUTTONCERTI)
        addbuttoncert.click()

    def get_input_text_and_verifyyy(self):
        inpt = self.browser.find_element_by_xpath(Locators.GETINPUTTEXTANDVERIFY1).text
        #elem_text = inpt.getText()
        return inpt

    def click_edit_button_certification(self):
        editbutttonn = self.browser.find_element(*Locators.EDITTBUTTON)
        editbutttonn.click()

 
    def edit_the_certification(self):
        certificationfielddd = self.browser.find_element(*Locators.CERTOIFICATIONFIELDEDIT)
        certificationfielddd.send_keys(Keys.LEFT_CONTROL + 'a')
        initialize.editcert = ReadWriteExcel.editCertification(self) 
        certificationfielddd.send_keys(initialize.editcert)
        certyearfield = self.browser.find_element(*Locators.CERTYEARFIELD)
        certyearfield.click()
        selectyear = self.browser.find_element(*Locators.SELECTYEAR2)
        selectyear.click()


    def get_input_text_and_verifyyyii(self):
        inpt = self.browser.find_element_by_xpath(Locators.GETINPUTTEXTANDVERIFY2).text
        #elem_text = inpt.getText()
        return inpt

    def cleartextfromcertification(self):
        certificationfielddd = self.browser.find_element(*Locators.CERTOIFICATIONFIELDEDIT)
        certificationfielddd.send_keys(Keys.LEFT_CONTROL + 'a') 
        certificationfielddd.send_keys(Keys.BACKSPACE)      

    def get_alert_text_and_verifyyyii(self):
        alertt = self.browser.find_element(*Locators.ALERTFIELD).text
        return alertt

    def enterhugetextcertification(self):
        certificationfielddd = self.browser.find_element(*Locators.CERTOIFICATIONFIELDEDIT)
        certificationfielddd.send_keys(Urlanddata.HUGETEXT)        
