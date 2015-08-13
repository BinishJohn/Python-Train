# Waits
#1. Explicit Waits
	# An explicit wait is a code you define to wait for a certain condition to occur before proceeding further in the code.
	# WebDriverWait in combination with ExpectedCondition is one way we can acheive this

# Using unit test as framework with selenium
import unittest # framework derived from Java JUnit for organizing the test cases effientily
from selenium import webdriver # Base module for selenium automation
from selenium.webdriver.common.keys import keys # Module for keybord interactions.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_condition as EC

class SignUp(unittest.TestCase):

#The setup is part of initalization , this method will get called before every test function in this class. 
def setUp(self):
  self.driver = webdriver.Firefox()

# This is the Test Case metod. The test case method should always start with characters test. 
def test_sign_up(self):
  driver = self.driver # Create local reference to the driver
  driver.get("https://en.todoist.com")
  assert "To-do list and task manager. Free, easy, online and mobile: Todolist" in driver.title
# This wait for 10 seconds before throwing TimeoutException. WebdriverWait be default calls the ExpectedCondition every 500 milliseconds until it returns successfully.  
  try:
    get_started_link = WebdriverWait(driver,10).untill(EC.presence_of_element_located((By.link_text('Get Started - It\'s Free')))
    get_started_link.click()

'''
wait = WebDriverWait(driver,10)
get_started_link = wait.until(EC.element_to_be_clickable((By.ID,'id')))
'''
  finally:
    driver.close()


# The tearDown method will get called after every test method. This is place to cleanup actions. The quit method on driver exit the entire browser where as close will close a tab. 
def tearDown(self):
  self.driver.close()

if __name__ == '__main__' :
  unittest.main()


