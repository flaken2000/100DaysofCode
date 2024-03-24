from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class InternetSpeedTwitterBot:

    def __init__(self):
        self.destination_data = {}

        # Keep browser open
        self.edge_options = webdriver.EdgeOptions()
        self.edge_options.add_experimental_option("detach", True)

        self.driver = webdriver.Edge(options=self.edge_options)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(4)
        self.go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        self.go_button.click()
        time.sleep(45)
        print("finished sleep")
        speeds = self.driver.find_elements(By.CSS_SELECTOR, ".result-data-large")
        return speeds[0].text, speeds[1].text
