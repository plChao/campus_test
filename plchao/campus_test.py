from multiprocessing.connection import wait
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("prefs", {"profile.password_manager_enabled": False, "credentials_enable_service": False})

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://smartcampus-1b31f.firebaseapp.com")
driver.maximize_window()
driver.implicitly_wait(5)
enter_as_guest = driver.find_elements(By.CLASS_NAME, value="MuiButtonBase-root")
# try_enter_as_guest = driver.find_element(By.CSS_SELECTOR, "MuiButtonBase-root.MuiButton-root.MuiButton-text")
# print(try_enter_as_guest)

# 等 element 出現
# enter_as_guest = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "以訪客身分進入"))
#     )
print(enter_as_guest)
print(enter_as_guest[0].tag_name)
enter_as_guest[1].click()
locate = driver.find_elements(By.CLASS_NAME, value="MuiButtonBase-root")
print(locate, len(locate))
# locate = driver.find_elements(By.CLASS_NAME, value="MuiButtonBase-root MuiFab-root jss64 MuiFab-sizeMedium MuiFab-secondary")
# driver.execute_script("arguments[0].scrollIntoView();", news)
WebDriverWait(driver, 10).until(
        driver.execute_script("return document.readyState")
    )
driver.get_screenshot_as_file("before_click.png")
locate[0].click()
driver.get_screenshot_as_file("click.png")

# news_list = driver.find_elements(By.CLASS_NAME, "su-post")
# driver.execute_script("arguments[0].scrollIntoView();", news_list[0])
# news_list[0].click()
# title = driver.find_element(By.CLASS_NAME, "single-post-title.entry-title")
# contents = driver.find_elements(By.TAG_NAME, "p")
# print('title:')
# print(title.text)
# print('content:')
# for paragraph in contents:
#     print(paragraph.text)
# print('======')
# target = '310552011'
# driver.switch_to.new_window('tab')
# driver.get("https://www.google.com")
# assert len(driver.window_handles) == 2
# search_box = driver.find_element(By.CLASS_NAME, "gLFyf.gsfi")
# search_box.send_keys(target+'\n')
# search_result_list = driver.find_elements(By.CLASS_NAME, "LC20lb.MBeuO.DKV0Md")
# print('second result of ' + target)
# print(search_result_list[1].text)

# # with open('tmp.txt', 'w', encoding='UTF-8') as f:
# #     f.write(driver.page_source)

# driver.quit()