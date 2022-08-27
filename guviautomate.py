from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Guvi:
    url="https://www.guvi.in/"
    driver=webdriver.Firefox()

    def new(self):
        self.driver.get(self.url)
        new_value=self.driver.find_element(By.XPATH,value="//h2[contains(text(),'For Corporates')]")
        print(new_value.text)

        explore_codekata=self.driver.find_element(By.XPATH,"//a[@class='btn btn-success btn-lg explore-course']")
        explore_codekata.click()

        // section[5] / div / div[1] / div / div[1] / div / div[2] / a[text() = 'Explore Codekata']
Guvi().new()
