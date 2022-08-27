from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://www.facebook.com/")

driver.find_element(By.ID,"email").send_keys("kalaipbc@gmail.com")
action = ActionChains(driver)

action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

action.send_keys(Keys.TAB).perform()

action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
action.send_keys(Keys.ENTER).perform()

