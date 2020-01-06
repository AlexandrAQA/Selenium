from selenium import webdriver
import time

webdriver = webdriver.Chrome(executable_path=("C:\Drivers\chromedriver.exe"))

webdriver.get('https://www.onliner.by/')     #Get URL
sign_in = webdriver.find_element_by_xpath('//*[@id="userbar"]/div[2]/div/div/div[1]').click()  #Find and Click on Sign_in Button

email = webdriver.find_element_by_xpath('//*[@id="auth-container"]/div/div[2]/div/form/div[1]/div/div[2]/div/div/div/div/input')   #To get email field
email.send_keys('mrgmgrv@gmail.com')  #Enter your email
time.sleep(2)  #Waiting

password = webdriver.find_element_by_xpath("//*[@id='auth-container']/div/div[2]/div/form/div[2]/div/div/div/div/input")  #To get password field
password.send_keys('mrgmgrv@gmail.com')  #Enter your password
time.sleep(2)

webdriver.find_element_by_xpath('//*[@id="auth-container"]/div/div[2]/div/form/div[3]/button').click()     #Click on the Sign-in Button and Go to Home Page


time.sleep(3)
webdriver.quit() #Closing




