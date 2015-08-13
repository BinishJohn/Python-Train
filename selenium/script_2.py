#Keeping the business function unites as functions.

from selenium import webdriver # Base module for selenium automation
from selenium.webdriver.common.keys import keys # Module for keybord interactions.

global driver
def setup_script():
  driver = webdriver.Firefox()
  driver.get("https://en.todoist.com")
  assert "To-do list and task manager. Free, easy, online and mobile: Todolist" in driver.title

def sign_up():
  get_started_link = driver.find_element_by_link_text('Get Started - It\'s Free')
  get_started_link.click()
  full_name_txt = driver.find_element_by_id('full_name')
  full_name_txt.send_keys("Binish John")
  email_txt = driver.find_element_by_id('email')
  email_txt.send_keys("binish.john@nttdata.com")
  password_txt = driver.find_element_by_id('password')
  password_txt.send_keys("Password@123")
  create_account_button = driver.find_element_by_css_selector('#submit_button > span')
  create_account_button.click() 

def cleanup_script():
  driver.close()


def testcase():
  setup_script()
  sign_up()
  cleanup_script()

# Locating Element
#1 find_element_by_id  - id of element
#2 find_element_by_name - name of element
#3 find_element_by_css_selector 
#4 find_element_by_xpath - Xpath is the language used for locating nodes in an XML document. Absolute xpath contain location of element from the root(html).
#5 find_element_by_linktext
#6 find_element_by_partial_link_text
#7 find_element_by_tag_name
#8 find_element_by_class_name

	# Locating Elements ( use find_elements instead of find_element )
	# If no matching element found then 'NoSuchElementException' will be raised.


