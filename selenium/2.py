#navigates to python.org, using the search bar for 'pycon'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.python.org")

#search box
elem = driver.find_element_by_name("q")
#clear existing text
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
#time.sleep(8)

#driver.close()
