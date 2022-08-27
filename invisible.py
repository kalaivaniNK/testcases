from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()

# driver.implicitly_wait(10)
# driver.get("https://letcode.in/")
#
# driver.find_element(By.XPATH,"//a[normalize-space()='Log in']").click()
#
# driver.find_element(By.XPATH,"//input[@name='email']").send_keys("balapradeep17bco836@gmail.com")
# driver.find_element(By.XPATH,"//input[@placeholder='Enter password']").send_keys("17Bco836bala@")
#
# driver.find_element(By.XPATH,"//button[normalize-space()='LOGIN']").click()
#
#
my_wait = WebDriverWait(driver, 10)
# visible = driver.find_element(By.XPATH,"//div[@role='alertdialog']")
#
# my_wait.until(EC.visibility_of(visible))
# my_wait.until(EC.invisibility_of_element(visible))
#
# driver.find_element(By.XPATH,"//a[text()='Sign out']").click()

driver.get("https://www.flipkart.com/")
