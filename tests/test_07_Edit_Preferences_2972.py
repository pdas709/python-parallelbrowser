import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from pages.LandingPage import HugoLandingPage
from pages.loginpage import Login_Page
from pages.preferences_page_object import Preferences
from pages.skills_page_object import Skills
from pages.summary_section_page_object import Summary_Section
from pages.certification_page_object import CertificationBottomofpage
from pages.porfilepicturesection_object import Profile_Picture_Section
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



def test_Edit_Preferences(browser):
    # Add Item to cart
    Landing_Page = HugoLandingPage(browser)
    Landing_Page.load()


    # Getting current URL source code 
    get_title = browser.title
    
    # Verify the title of this URL 
    assert "Hugo | Candidate" in get_title  

    Landing_Page.click_login_from_hugo() 



    #Verify that user can find the login button

    try:
      WebDriverWait(browser, 10).until(
          EC.element_to_be_clickable((By.NAME, 'submit')))
    except TimeoutException:
      raise Exception('Unable to find text in this element after waiting 10 seconds')

    #Verify Page title of Hugo Login Page
    get_title_again = browser.title

    assert "Sign In with Auth0" in get_title_again


    #Proceed the actions of our Login page

    log_in_page = Login_Page(browser)
    log_in_page.enter_email()
    log_in_page.enter_password()
    log_in_page.click_login_()
    
    

    #Verify an element to confirm user is logged in 
    try:
      WebDriverWait(browser, 10).until(
          EC.text_to_be_present_in_element((By.XPATH, '//*[@id="root"]/div/div/header/div/div[5]/button'), 'logout'))
    except TimeoutException:
      raise Exception('Unable to find text in this element after waiting 10 seconds')
    
    #Navigate to edit profile page
    profile_picture_section_ = Profile_Picture_Section(browser)
    profile_picture_section_.load_()
  
    #Verify video edit button on the edit profile page
    
    try:
      WebDriverWait(browser, 10).until(
          EC.visibility_of_element_located((By.XPATH, '//h3[contains(.,"Video Resume")]/parent::div/child::button')))
    except TimeoutException:
      raise Exception('Unable to find text in this element after waiting 10 seconds')
    
    #proceed with editing the preferences

    preferences_section_ = Preferences(browser)
    preferences_section_.clickontheeditbutton_preferences()
    preferences_section_.travel_remote()

    preferences_section_.travel_remote()
    preferences_section_.remote_option()

    try:
      checkboxindustry = preferences_section_.industry_selection_check()
      if checkboxindustry.is_displayed(): pass
    except NoSuchElementException:preferences_section_.industry_revenue_selection()


    #try:
    #  tab = preferences_section_.check_engineeringtab()
    #  if tab.is_displayed():preferences_section_.engineeringtab_cross()
    #except NoSuchElementException:preferences_section_.industry_field()
    
    #preferences_section_.industry_field()
    #preferences_section_.select_industry__dropdown()

    preferences_section_.addanother_location()
    #preferences_section_.entercty()

    preferences_section_.entercty()

    preferences_section_.click_outside_state_populates()

    try:
      WebDriverWait(browser, 10).until(
          EC.text_to_be_present_in_element_value((By.XPATH, '((//h4[contains(.,"Locations")]/parent::div/child::div/child::div/child::div/child::div)[last()]/child::div/child::div/child::div/child::div/child::div/child::div/child::input)[1]'), 'Gurugram'))
    except TimeoutException:
      raise Exception('Unable to find text in this element after waiting 10 seconds')


    preferences_section_.savebbutton()

    try:
      WebDriverWait(browser, 10).until(
          EC.visibility_of_element_located((By.XPATH, '(//span[contains(.,"Gurugram")])[last()]')))
    except TimeoutException:
      raise Exception('Unable to find text in this element after waiting 10 seconds')


    statetext = preferences_section_.verify_tttext()
    assert 'Gurugram' in statetext, f"Test Failed: Text did not match expected - State ."  