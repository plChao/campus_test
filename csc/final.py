from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
import base64

a = b'c3QyMDIyZmluYWxAZ21haWwuY29t'
a = base64.b64decode(a).decode('utf-8')
b = b'c3QyMDIyZmluYWxAbnljdQ=='
b = base64.b64decode(b).decode('utf-8')

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://smartcampus-1b31f.firebaseapp.com/map")
driver.set_window_size(425,700)
#login = WebDriverWait(driver,20).until(lambda d : d.find_element(by=By.CLASS_NAME, value='MuiTypography-root MuiTypography-subtitle1'))
#driver.implicitly_wait(10)
time.sleep(3)
"""
#訪客
login = driver.find_element(by=By.XPATH, value='//button[@style="margin-top: 30px; color: rgb(186, 186, 186); padding: 0px;"]')
login.click()

#login and finish the tutorial
next_page = driver.find_element(by=By.XPATH, value='//button[@class="MuiButtonBase-root MuiButton-root MuiButton-text jss6 MuiButton-textSizeLarge MuiButton-sizeLarge"]')
next_page.click()
next_page.click()
finish = driver.find_elements(by=By.XPATH, value='//button[@class="MuiButtonBase-root MuiButton-root MuiButton-text jss6 MuiButton-textSizeLarge MuiButton-sizeLarge"]')
#for i in finish:
#    print(i.text)
finish[1].click()

time.sleep(3)

button = driver.find_elements(by=By.XPATH, value='//span[@class="MuiFab-label"]')
#click the plus button
button[0].click()

login = driver.find_element(by=By.XPATH, value='//button[@style="margin-top: 30px; color: rgb(186, 186, 186); padding: 0px;"]')
assert '以訪客身分進入' == login.text
print("test case 7 finished")
"""
original_window = driver.current_window_handle
assert len(driver.window_handles) == 1
login = driver.find_element(by=By.XPATH, value='//h6[@class="MuiTypography-root MuiTypography-subtitle1"]')
login.click()
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
for i in driver.window_handles:
    if i != original_window:
        driver.switch_to.window(i)
        break
time.sleep(5)

driver.find_element(by=By.ID, value='identifierId').send_keys(a)
cont = driver.find_elements(by=By.XPATH, value='//span[@class="VfPpkd-vQzf8d"]')
cont[1].click()

time.sleep(5)
driver.find_element(by=By.XPATH, value='//input[@name="password"]').send_keys(b)
cont = driver.find_elements(by=By.XPATH, value='//span[@class="VfPpkd-vQzf8d"]')
cont[1].click()

driver.switch_to.window(original_window)
time.sleep(3)
if(len(driver.find_elements(by=By.XPATH, value='//button[@class="MuiButtonBase-root MuiButton-root MuiButton-text jss6 MuiButton-textSizeLarge MuiButton-sizeLarge"]'))):
    #login and finish the tutorial
    next_page = driver.find_element(by=By.XPATH, value='//button[@class="MuiButtonBase-root MuiButton-root MuiButton-text jss6 MuiButton-textSizeLarge MuiButton-sizeLarge"]')
    next_page.click()
    next_page.click()
    finish = driver.find_elements(by=By.XPATH, value='//button[@class="MuiButtonBase-root MuiButton-root MuiButton-text jss6 MuiButton-textSizeLarge MuiButton-sizeLarge"]')
    #for i in finish:
    #    print(i.text)
    finish[1].click()
    time.sleep(3)

button = driver.find_elements(by=By.XPATH, value='//span[@class="MuiFab-label"]')
#click the plus button
button[0].click()
check = driver.find_elements(by=By.XPATH, value='//span[@class="MuiTypography-root MuiListItemText-primary jss164 MuiTypography-body1 MuiTypography-displayBlock"]')
assert len(check) == 3
print("test case 6 done")

"""
content = driver.find_elements(by=By.TAG_NAME, value='p')
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
