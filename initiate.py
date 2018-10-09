from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class initiate():
    def driver(self):
        baseUrl = ""
        driver = webdriver.Chrome(executable_path='/Users/QuintonMills/Desktop/SeleniumKitchen/chromedriver')
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(2)
ff = initiate()
ff.driver()

