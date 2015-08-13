#Basic Script to Navigate and Perform Simple Actions.

from selenium import webdriver # Base module for selenium automation
from selenium.webdriver.common.keys import keys # Module for keybord interactions.

driver = webdriver.Firefox()
driver.get("https://en.todoist.com")
assert "To-do list and task manager. Free, easy, online and mobile: Todolist" in driver.title
get_started_link = driver.find_element_by_link_text('Get Started - It\'s Free')
get_started_link.click()
driver.close()

