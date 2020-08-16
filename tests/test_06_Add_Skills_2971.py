import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from pages.LandingPage import HugoLandingPage
from pages.loginpage import Login_Page
from pages.skills_page_object import Skills
from pages.summary_section_page_object import Summary_Section
from pages.certification_page_object import CertificationBottomofpage
from pages.porfilepicturesection_object import Profile_Picture_Section
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



def test_Add_Skills(browser):
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
    
    #proceed with adding skills

    skills_section_ = Skills(browser)
    skills_section_.clickontheeditbutton_skills()
    skills_section_.input_skills()
    #Verify Suggestions Drop-Down

    try:
      WebDriverWait(browser, 10).until(
          EC.presence_of_element_located((By.CLASS_NAME, 'StyledTextInput__StyledSuggestions-sc-1x30a0s-4.egXMJf')))
    except TimeoutException:
      raise Exception('Unable to find text in this element after waiting 10 seconds')

    skills_section_.selectfromdropdown()
    skills_section_.clicksave()
    
    time.sleep(3)
    skillsavedtext = skills_section_.verify_skillsaved()
    assert 'LOADER' in skillsavedtext, f"Test Failed: Alert did not match expected - LOADER."  


    