#locate elements by their HTML name attribute
from selenium import webdriver
driver= webdriver.Chrome()
driver.get("file:///C:/Users/ocben/automation/selenium/page.html")
username = driver.find_element_by_name('username')
print("My input element is:")
print(username)
driver.close()
