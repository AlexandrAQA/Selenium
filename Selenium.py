from selenium import webdriver
import time

webdriver = webdriver.Chrome(executable_path= "C:\Drivers\chromedriver.exe")
#webdriver = webdriver.Firefox( executable_path= "C:\Drivers\geckodriver.exe")
#webdriver = webdriver.Ie(executable_path= "C:\Drivers\IEDriverServer")
#webdriver.get("https://www.amazon.com/")


webdriver.get("http://demo.automationtesting.in/Windows.html")

print(webdriver.title) #returns the title of the page
print(webdriver.current_url) #returns URL of the page

webdriver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()

time.sleep(5)


#print(webdriver.page_source) #HTML code for the page (huge information)


#webdriver.close()  #closes only currently focussed browser tab
webdriver.quit()   #closes all tabs of the browser