from selenium import webdriver
from time import sleep

#Selenium must be installed for this to work

# Input here the file location of chromedriver. 
driver = webdriver.Chrome()

l = driver.find_element_by_tag_name('body')
l.send_keys("k")

# Your youtube link here.
driver.get()

while True:
	sleep()
	driver.refresh()