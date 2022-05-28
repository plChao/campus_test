from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://smartcampus-1b31f.firebaseapp.com/map")
driver.set_window_size(425,700)
#login = WebDriverWait(driver,20).until(lambda d : d.find_element(by=By.CLASS_NAME, value='MuiTypography-root MuiTypography-subtitle1'))
#driver.implicitly_wait(10)
time.sleep(3)
#訪客
login = driver.find_element(by=By.XPATH, value='//button[@style="margin-top: 30px; color: rgb(186, 186, 186); padding: 0px;"]')
#google 登入

#driver.find_element(by=By.ID, value='identifierId').send_keys('st2022final@gmail.com')
#driver.find_element(by=By.NAME, value='password').send_keys('st2022final@nycu')
login.click()

next_page = driver.find_element(by=By.XPATH, value='//button[@class="MuiButtonBase-root MuiButton-root MuiButton-text jss6 MuiButton-textSizeLarge MuiButton-sizeLarge"]')
next_page.click()
next_page.click()

"""
print(goal.text)
goal.click()
content = driver.find_elements(by=By.TAG_NAME, value='p')
for i in content:
    print(i.text)
driver.switch_to.new_window('tab')
driver.get("https://www.google.com.tw")
driver.find_element(By.NAME, "q").send_keys("310555032" + Keys.ENTER)
title = driver.find_elements(by=By.TAG_NAME, value='h3')
test = driver.find_elements(by=By.CLASS_NAME, value= 'LC20lb MBeuO DKV0Md')
#print(test)
#print(title)
for i in title:
    a = i.text
print(title[2].text)
driver.quit()
#goal_list[0].click()
#driver.back()
#driver.forward()
#driver.refresh()
#driver.quit()
"""
