from multiprocessing.connection import wait
import re
import struct
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import numpy as np
from io import BytesIO
from PIL import Image
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def png_bytes_to_numpy(png):
    """Convert png bytes to numpy array
    
    Example:  
    
    >>> fig = go.Figure(go.Scatter(x=[1], y=[1]))
    >>> plt.imshow(png_bytes_to_numpy(fig.to_image('png')))
    """
    return np.array(Image.open(BytesIO(png)))
def png_is_equal(png1, png2, threshold=1):
    mse = ((png1 - png2)**2).mean(axis=None)
    print('mse', mse)
    return mse < threshold
class PythonOrgSearch(unittest.TestCase):
    
    def test_1(self):
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        driver.get("https://smartcampus-1b31f.firebaseapp.com")
        driver.maximize_window()
        driver.implicitly_wait(5)
        enter_as_guest = driver.find_elements(By.CLASS_NAME, value="MuiButton-text")
        # print(enter_as_guest, len(enter_as_guest))
        enter_as_guest[1].click()

        # 等 map 出現
        # print(driver.find_elements(By.ID, "272A6A4D-35F4-4A32-8FBE-A148FACE4046"))
        # enter_as_guest = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "272A6A4D-35F4-4A32-8FBE-A148FACE4046"))
        # )
        time.sleep(5)
        driver.get_screenshot_as_file('./pic/test1_a.png')
        bfclick = driver.get_screenshot_as_png()
        bfarray = png_bytes_to_numpy(bfclick)
        locate = driver.find_elements(By.CLASS_NAME, value="jss64")
        # locate = driver.find_elements(By.CLASS_NAME, value="MuiButtonBase-root MuiFab-root jss64 MuiFab-sizeMedium MuiFab-secondary")
        # print(locate, len(locate))
        locate[0].click()
        time.sleep(5)
        driver.get_screenshot_as_file('./pic/test1_b.png')
        afclick = driver.get_screenshot_as_png()
        afarray = png_bytes_to_numpy(afclick)
        driver.quit()
        self.assertEqual(png_is_equal(bfarray, afarray), False)
    def test_2(self):
        options = webdriver.ChromeOptions()
        # close geolocation
        options.add_experimental_option("prefs", {"profile.default_content_setting_values.geolocation" :2})
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        driver.get("https://smartcampus-1b31f.firebaseapp.com")
        driver.maximize_window()
        driver.implicitly_wait(5)
        enter_as_guest = driver.find_elements(By.CLASS_NAME, value="MuiButton-text")
        enter_as_guest[1].click()
        time.sleep(5)
        driver.get_screenshot_as_file('./pic/test2_a.png')
        bfclick = driver.get_screenshot_as_png()
        bfarray = png_bytes_to_numpy(bfclick)
        locate = driver.find_elements(By.CLASS_NAME, value="jss64")
        # locate = driver.find_elements(By.CLASS_NAME, value="MuiButtonBase-root MuiFab-root jss64 MuiFab-sizeMedium MuiFab-secondary")
        # print(locate, len(locate))
        locate[0].click()
        time.sleep(5)
        driver.get_screenshot_as_file('./pic/test2_b.png')
        afclick = driver.get_screenshot_as_png()
        afarray = png_bytes_to_numpy(afclick)
        driver.quit()
        self.assertEqual(png_is_equal(bfarray, afarray), True)
    def test_4(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://smartcampus-1b31f.firebaseapp.com")
        driver.maximize_window()
        driver.implicitly_wait(5)
        enter_as_guest = driver.find_elements(By.CLASS_NAME, value="MuiButton-text")
        # print(enter_as_guest, len(enter_as_guest))
        enter_as_guest[1].click()

        time.sleep(4)
        target = '工程三館'
        search_box = driver.find_element(By.ID, "inputBase")
        search_box.send_keys(target)
        search_result = driver.find_element(By.CLASS_NAME, "pac-item")
        search_result.click()
        info = driver.find_elements(By.ID, "client-snackbar")
        self.assertEqual(len(info), 0)
        driver.quit()
    def test_5(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://smartcampus-1b31f.firebaseapp.com")
        driver.maximize_window()
        driver.implicitly_wait(5)
        enter_as_guest = driver.find_elements(By.CLASS_NAME, value="MuiButton-text")
        # print(enter_as_guest, len(enter_as_guest))
        enter_as_guest[1].click()

        time.sleep(4)
        target = '台北101'
        search_box = driver.find_element(By.ID, "inputBase")
        search_box.send_keys(target)
        search_result = driver.find_element(By.CLASS_NAME, "pac-item")
        search_result.click()
        info = driver.find_element(By.ID, "client-snackbar")
        self.assertEqual(info.text, '地址超過搜尋範圍')
        driver.quit()
    def tearDown(self):
        pass
        # self.driver.close()

if __name__ == "__main__":
    unittest.main()