# Using unit test as framework with selenium
import unittest # framework derived from Java JUnit for organizing the test cases effientily
from selenium import webdriver # Base module for selenium automation
from selenium.webdriver.common.keys import keys # Module for keybord interactions.


class SignUp(unittest.TestCase):

#The setup is part of initalization , this method will get called before every test function in this class. 
def setUp(self):
  self.driver = webdriver.Firefox()

# This is the Test Case metod. The test case method should always start with characters test. 
def test_sign_up(self):
  driver = self.driver # Create local reference to the driver
  driver.get("https://en.todoist.com")
  assert "To-do list and task manager. Free, easy, online and mobile: Todolist" in driver.title
  get_started_link = driver.find_element_by_link_text('Get Started - It\'s Free')
  get_started_link.click()
  full_name_txt = driver.find_element_by_id('full_name')
  full_name_txt.send_keys("Binish John")
  email_txt = driver.find_element_by_id('email')
  email_txt.send_keys("binish.john@nttdata.com")
  password_txt = driver.find_element_by_id('password')
  password_txt.send_keys("Password@123")
  create_account_button = driver.find_element_by_css('#submit_button > span')
  create_account_button.click()
  driver.save_screenshot('screen-shot.png') 


# The tearDown method will get called after every test method. This is place to cleanup actions. The quit method on driver exit the entire browser where as close will close a tab. 
def tearDown(self):
  self.driver.close()
  self.driver.quit()

if __name__ == '__main__' :
  unittest.main()


