from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import xlrd 

loc = input("Enter the path/name of the file : ") 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 
no=[]
for i in range(sheet.nrows): 
    no.append(int(sheet.cell_value(i, 0))) 
driver = webdriver.Chrome(r'chromedriver')
string = sys.argv[1]
ar= no[0]
for i in no:
    if len(str(i))==10:
        a="https://api.whatsapp.com/send?phone=91"+str(i)
        driver.get(a)
        time.sleep(3)  
        clbutton = driver.find_element_by_id("action-button")
        clbutton.click()
        time.sleep(3)  
        ckbutton = driver.find_element_by_xpath("//a[contains(text(),'use WhatsApp Web')]")
        ckbutton.click()
        time.sleep(20)  
        message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
        message.send_keys(string)
        sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
        sendbutton.click()
        print ("Message sent to",i)
        time.sleep(10)  

