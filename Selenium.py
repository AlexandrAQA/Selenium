from selenium import webdriver
from selenium.webdriver.common.keys import Keys

webdriver = webdriver.Chrome(executable_path= "C:\Drivers\chromedriver.exe")
#webdriver = webdriver.Firefox( executable_path= "C:\Drivers\geckodriver.exe")
#webdriver = webdriver.Ie(executable_path= "C:\Drivers\IEDriverServer")


#webdriver.get("https://www.amazon.com/")
webdriver.get("http://demo.automationtesting.in/Windows.html")

print(webdriver.title)

print(webdriver.current_url)

#print(webdriver.page_source) #HTML code for the page (huge information)
print("Finish of the First part")
webdriver.close()