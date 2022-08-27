from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
# file = driver.find_element(By.CSS_SELECTOR,"label[for='RESULT_FileUpload-10']")
driver.switch_to.frame("frame-one1434677811")

time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='RESULT_FileUpload-10']").send_keys("D:\download.jfif")
