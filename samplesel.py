
from selenium import webdriver
driver = webdriver.chrome("C:\Program Files\Google\Chrome\Application")
driver.get ("https://www.google.com")
driver.find_element_by_name("q").send_keys("selenium")
driver.find_element_by_name("btnl").click()
driver.click()
