from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()    #full size of the browser

driver.get("https://www.expedia.com/")
driver.find_element_by_id("tab-flight-tab-hp").click() #Flights Button
time.sleep(2)
driver.find_element_by_xpath('//*[@id="flight-origin-hp-flight"]').send_keys('MSQ')    #original
driver.find_element_by_xpath('//*[@id="flight-destination-hp-flight"]').send_keys('Vienna, Austria (VIE-Vienna Intl.)')    #Destination
time.sleep(2)
driver.find_element_by_id('flight-departing-hp-flight').clear()
driver.find_element_by_id('flight-departing-hp-flight').send_keys('02/14/2020')   #departure date
time.sleep(2)
driver.find_element_by_id('flight-returning-hp-flight').clear()
driver.find_element_by_id('flight-returning-hp-flight').send_keys('02/28/2020')    #return date
time.sleep(3)
driver.find_element_by_xpath('//*[@id="gcw-flights-form-hp-flight"]/div[7]/label/button').click()

#Explicit wait
wait = WebDriverWait(driver,20)   # == time.sleep(20
element = driver.find_element_by_xpath('//*[@id="stops"]/div/div[3]/div/label').click()
wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="stops"]/div/div[3]/div/label')))   #==ждать пока этот элемент не будет нажат

time.sleep(12)
driver.quit()