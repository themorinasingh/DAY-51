import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


#CONSTANTS
PROMISED_DOWN = 1000
PROMISED_UP = 200
CHROME_DRIVER_PATH = "Users/moes/Development/chromedriver"
TWITTER_EMAIL = 'theogmoe@cyberdude.com'
TWITTER_PASSWORD = 'ThankyouGod100%'
URL = "https://www.speedtest.net/"
TWITTER = 'https://x.com/'



class TwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=self.chrome_options.add_experimental_option('detach', True))
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(URL)
        sleep(3)
        go_button = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()
        sleep(40)
        down_speed = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.down = float(down_speed.text)
        up_speed = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.up = float(up_speed.text)
        time.sleep(20)


    def tweet_at_provider(self):
        self.get_internet_speed()

        if self.up < PROMISED_UP or self.down < PROMISED_DOWN:
            self.driver.get(TWITTER)
            time.sleep(2)
            sign_in = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a/div')
            sign_in.click()
            time.sleep(2)
            username = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
            username.send_keys(TWITTER_EMAIL)

            next_button = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span')
            next_button.click()

            time.sleep(10)
            password = self.driver.find_element(By.NAME, value='password')
            password.send_keys(TWITTER_PASSWORD)
            time.sleep(2)
            login_button = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div')
            login_button.click()

            #inouttng the tweet
            time.sleep(15)
            tweet_input = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
            tweet_input.send_keys(f"Hey Bell, why is my upload_speed: {self.up} and download_speed: {self.down}, i was promised a minimum of {PROMISED_UP}mbps up and {PROMISED_DOWN}mbps down #bellcanada")
            time.sleep(10)
            tweet_input.send_keys(Keys.COMMAND, Keys.ENTER)



            time.sleep(20)
