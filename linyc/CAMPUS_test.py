from multiprocessing.connection import wait
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest



class PythonOrgSearch(unittest.TestCase):
    def test_1(self):
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        print("Mission1------------")
        driver.get("https://smartcampus-1b31f.firebaseapp.com")
        driver.maximize_window()
        # login and get into map
        time.sleep(5)
        enter_as_guest = driver.find_elements(By.CLASS_NAME, value="MuiButton-text")
        enter_as_guest[1].click()
        time.sleep(5)
        # click the show filter button next to hamburger
        showFilter = driver.find_element(By.XPATH, value="//*[@id='root']/div/div[2]/div/form/div/button[2]/span[1]/img")
        showFilter.click()

        filter_buttons = driver.find_elements(By.CLASS_NAME, value="MuiButton-sizeSmall")
        self.assertEqual(len(filter_buttons), 0)
        print("--------------- Mission1 Completed ---------------")
        time.sleep(5)
        driver.quit()

    def test_2(self):
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # mission1
        print("Mission2------------")
        driver.get("https://smartcampus-1b31f.firebaseapp.com")
        driver.maximize_window()
        time.sleep(5)
        # login and get into map
        enter_as_guest = driver.find_elements(By.CLASS_NAME, value="MuiButton-text")
        enter_as_guest[1].click()

        time.sleep(5)

        # click filter button
        filter_buttons = driver.find_elements(By.CLASS_NAME, value="MuiButton-sizeSmall")
        filter_buttons[2].click()

        # count img after filter 
        counter = 0
        listImages = driver.find_elements(By.TAG_NAME, value="img")
        for x in listImages: 
            if "https://maps.gstatic.com/mapfiles/transparent.png" == x.get_attribute("src"):
                counter = counter + 1

        # 15 yellow, 10 purple
        # print(counter,"-------")
        self.assertEqual(counter, 25)
        print("--------------- Mission2 Completed ---------------")
        time.sleep(5)
        driver.quit()

    def test_3(self):
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        print("Mission3------------")
        driver.get("https://smartcampus-1b31f.firebaseapp.com")
        driver.maximize_window()
        time.sleep(5)
        enter_as_guest = driver.find_elements(By.CLASS_NAME, value="MuiButton-text")
        enter_as_guest[1].click()
        time.sleep(5)
        # click detailed filter button
        filter_buttons = driver.find_elements(By.CLASS_NAME, value="MuiButton-sizeSmall")
        filter_buttons[0].click()

        
        time.sleep(3)
        filter_detail_buttons = driver.find_elements(By.CLASS_NAME, value="MuiButton-containedSizeSmall")
        filter_detail_buttons[4].click()
        time.sleep(3)
        filter_detail_buttons = driver.find_elements(By.CLASS_NAME, value="MuiButton-containedSizeSmall")
        filter_detail_buttons[7].click()
        time.sleep(3)
        filter_detail_buttons = driver.find_elements(By.CLASS_NAME, value="MuiButton-containedSizeSmall")
        filter_detail_buttons[13].click()
        time.sleep(3)
        filter_detail_buttons = driver.find_elements(By.CLASS_NAME, value="MuiButton-contained")
        filter_detail_buttons[17].click()
        time.sleep(3)

        # count img after filter 
        counter = 0
        listImages = driver.find_elements(By.TAG_NAME, value="img")
        for x in listImages: 
            if "https://maps.gstatic.com/mapfiles/transparent.png" == x.get_attribute("src"):
                counter = counter + 1
        self.assertEqual(counter, 21)
        print("--------------- Mission3 Completed ---------------")
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    unittest.main()