from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
import time


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/")

actionchains = ActionChains(driver)

driver.find_element(By.XPATH,"//input[@id='txtUsername']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@id='txtPassword']").send_keys("admin123")
driver.find_element(By.XPATH,"//input[@id='btnLogin']").click()

leave = driver.find_element(By.XPATH,"//a[@id='menu_leave_viewLeaveModule']")
configure = driver.find_element(By.XPATH,"//a[@id='menu_leave_viewMyLeaveList']")


actionchains.move_to_element(leave).click().perform()
time.sleep(5)
actionchains.move_to_element(configure).click().perform()
actionchains.






