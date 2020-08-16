import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from pages.LandingPage import HugoLandingPage
from pages.loginpage import Login_Page
from pages.certification_page_object import CertificationBottomofpage
from pages.porfilepicturesection_object import Profile_Picture_Section
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import string
import random
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver import Firefox
from selenium.webdriver import Edge
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

import json
@pytest.fixture(scope='session')
def config():
  with open('config.json') as config_file:
    data = json.load(config_file)
  return data

@pytest.fixture
def browser(config):
  if config['browser'] == 'chrome':
    options = Options()
    driver = webdriver.Chrome(options=options)
  elif config['browser'] == 'firefox':
    driver = Firefox()
  elif config['browser'] == 'edge':
    driver = Edge()
  else:
    raise Exception(f'"{config["browser"]}" is not a supported browser')
  driver.maximize_window() 
  driver.implicitly_wait(config['wait_time'])
  yield driver
  driver.quit()


  if config['browser'] == 'chrome':
        with open("config.json", "r") as jsonFile:
            data = json.load(jsonFile)
        #tmp = data["browser"]
        data['browser'] = 'firefox'
        with open("config.json", "w") as jsonFile:
            json.dump(data, jsonFile)
  elif config['browser'] == 'firefox':
        with open("config.json", "r") as jsonFile:
            data = json.load(jsonFile)
        #tmp = data["browser"]
        data["browser"] = "chrome"
        with open("config.json", "w") as jsonFile:
            json.dump(data, jsonFile)




'''
@pytest.fixture()
def browser():
  options = Options()
  #options.add_argument("--headless") # Runs Chrome in headless mode.
  #options.add_argument('--disable-gpu')  # applicable to windows os only
  #options.add_argument('start-maximized') # 
  #options.add_argument('disable-infobars')
  #options.add_argument("--disable-extensions")
  driver = webdriver.Chrome(options=options)
  driver.implicitly_wait(10)
  yield driver
  driver.quit()
  

  options = FirefoxOptions()
  #options.add_argument('-headless')
  driver = Firefox(executable_path='geckodriver', options=options)
  #driver = Firefox()
  driver.implicitly_wait(10)
  yield driver
  driver.quit()
'''