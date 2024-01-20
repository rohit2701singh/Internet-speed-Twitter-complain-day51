from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class TwitterFile:

    def __init__(self, login_id, login_password, username=""):
        """open Twitter website and complete login process. username start with @ and is unique to your account"""

        self.__login_id = login_id
        self.__login_pass = login_password
        self.__username = username

        self.__net_speed = None
        self.__promised_down = None
        self.__promised_up = None
        self.__msg = None
        self.__custom_message = None

        self.__driver = webdriver.Chrome(chrome_options)
        self.__driver.get("https://twitter.com/i/flow/login")

        WebDriverWait(self.__driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'))
        )

        time.sleep(5)

        twitter_login = self.__driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')

        twitter_login.click()
        twitter_login.send_keys(self.__login_id)
        time.sleep(3)
        twitter_login.send_keys(Keys.ENTER)
        time.sleep(5)

        def verification_and_password():
            """after additional security verification is filled or otherwise this will be called for password entry."""

            time.sleep(5)

            twitter_pass = self.__driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            twitter_pass.click()
            time.sleep(3)
            twitter_pass.send_keys(self.__login_pass)
            time.sleep(3)
            twitter_pass.send_keys(Keys.ENTER)

            print("successfully logged in to Twitter")

        verification = self.__driver.find_element(By.XPATH, '//*[@id="modal-header"]/span/span')  # ask for username or phone number before login(not every time)
        # print(verification.text)

        if verification.text == "Enter your phone number or username":

            try:

                find_verification_space = self.__driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
                if len(self.__username) == 0:
                    self.__username = input("please enter your phone number or username to verify it’s you: ").strip("@")
                    print("check progress in driver")

                time.sleep(3)
                find_verification_space.send_keys(self.__username)
                time.sleep(3)
                find_verification_space.send_keys(Keys.ENTER)
                print("verification completed.")

            except Exception as error:
                print(error)
            else:
                verification_and_password()

        else:
            verification_and_password()

    def internet_speed_complaint(self, speed: tuple, promised_down_speed, promised_up_speed, tweet=""):
        """if tweet not provided, by default message will be used. down_speed: download speed, up_speed: upload speed"""

        self.__net_speed = speed
        self.__promised_down = promised_down_speed
        self.__promised_up = promised_up_speed
        self.__msg = tweet

        if len(self.__msg) == 0:
            self.__msg = f"Hey Internet Provider, why is my internet speed {self.__net_speed[0]}down/{self.__net_speed[1]}up when I pay for {self.__promised_down}down/{self.__promised_up}up?"

        self.tweet_message(self.__msg)

    def tweet_message(self, message):
        """this will post your message on Twitter"""

        self.__custom_message = message

        try:
            WebDriverWait(self.__driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div/div'))
            )

            time.sleep(8)
            tweet_text_place = self.__driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div/div')
            tweet_text_place.click()
            time.sleep(3)

        except Exception as error:
            print(error)

        else:
            tweet_text_place.send_keys(self.__custom_message)
            time.sleep(10)

        try:
            post_button = self.__driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span')
            post_button.click()
            time.sleep(3)
            print("post successfully")

        except Exception as error:
            print(error)