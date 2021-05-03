import selenium.webdriver as webdriver
from bs4 import BeautifulSoup as bs
import requests
url='https://specexams.com/BeesErp/Login.aspx'
driver = webdriver.Chrome()
driver.get(url)
username='17BK1A0571'
password='17BK1A0571'
email_element = driver.find_element_by_id('txtUserName')
email_element.send_keys(username) 

login_button = driver.find_element_by_id('btnNext')
login_button.click()

password_element = driver.find_element_by_id('txtPassword')
password_element.send_keys(password) 

login_button = driver.find_element_by_id('btnSubmit')
login_button.click()

urls=requests.get(url)
soup=bs(driver.page_source,"html.parser")
#download=soup.find(class_="container-fluid mt-4")

name=soup.find(id="ctl00_cpHeader_ucStud_lblStudentName")
attendance=soup.find(id="ctl00_cpStud_lblTotalPercentage")
warning_msg=soup.find(id="ctl00_cpStud_lblAttComment")

print("Hello"+name.text[11:])
print(attendance.text)
print(warning_msg.text[:-1])

