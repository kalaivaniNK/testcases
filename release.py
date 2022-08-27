from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains



driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://testautomationpractice.blogspot.com/")

actionchains = ActionChains(driver)
#drag and drop
source = driver.find_element(By.CSS_SELECTOR,"div#draggable")
destination = driver.find_element(By.CSS_SELECTOR,"div#droppable")
actionchains.click_and_hold(source)
actionchains.release(destination)
actionchains.perform()