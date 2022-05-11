from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

#Selenium must be installed for this to work

#Input here the file location of chromedriver. 
driver = webdriver.Chrome()

i = driver.find_element(By.TAG_NAME, 'body')
i.send_keys("k")

#Your youtube link here.
driver.get()

while True:
	sleep()
	driver.refresh()
