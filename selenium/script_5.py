#Basic Script to Navigate and Perform Simple Actions.

from selenium import webdriver # Base module for selenium automation
from selenium.webdriver.common.keys import keys # Module for keybord interactions.
# An implicit wait is to tell webdriver to poll for a certain amount of time when trying to find an element or elements if they are not immediately available.

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://en.todoist.com")
assert "To-do list and task manager. Free, easy, online and mobile: Todolist" in driver.title
get_started_link = driver.find_element_by_link_text('Get Started - It\'s Free')
get_started_link.click()
driver.close()

