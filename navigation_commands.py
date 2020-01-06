from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time

'''This code does the following: firstly opens the first link,
 then opens the second, and then from 2 goes to the first and again goes to the second and prints
 their titles every iteration'''

webdriver = webdriver.Chrome(executable_path=("C:\Drivers\chromedriver.exe"))

webdriver.get("https://www.amazon.com/")     # 1 URL (amazon)
print(webdriver.title)
webdriver.get('https://www.onliner.by/')     # 2 URL (onliner)
time.sleep(3)

print(webdriver.title)
webdriver.back()
time.sleep(3)

print(webdriver.title)                       # again 1 URL (amazon)
webdriver.forward()
time.sleep(3)
print(webdriver.title)                       # again 2 URL (onliner)
webdriver.quit()