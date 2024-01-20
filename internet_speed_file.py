from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InternetSpeed:
    def __init__(self):
        """open speedtest website and starts test"""

        self.__download_speed = None
        self.__upload_speed = None

        self.__driver = webdriver.Chrome(chrome_options)
        self.__driver.get("https://www.speedtest.net/")

        try:
            time.sleep(10)
            pop_up = self.__driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
            pop_up.click()
        except Exception as error:
            print("error1", error)
        else:
            start_button = self.__driver.find_element(By.CLASS_NAME, "start-text")
            time.sleep(3)
            start_button.click()

            self.__speed_detail()

    def __speed_detail(self):
        """after completion of test, return download and upload speed."""

        WebDriverWait(self.__driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]'))
        )

        time.sleep(60)  # checking download and upload speed
        print("waiting complete")
        try:

            download_tag = self.__driver.find_element(By.CSS_SELECTOR, "div.result-item-download div.result-data")
            self.__download_speed = download_tag.text

            upload_tag = self.__driver.find_element(By.CSS_SELECTOR, "div.result-item-upload div.result-data")
            self.__upload_speed = upload_tag.text

            print(f"speed: {self.__download_speed}, {self.__upload_speed}")

            return self.__download_speed, self.__upload_speed

        except Exception as error:
            print(error)

    def get_speed_detail(self):
        """return a tuple of download and upload speed"""
        return self.__download_speed, self.__upload_speed
