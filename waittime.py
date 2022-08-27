from selenium import webdriver
# from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
# service = FirefoxService(executable_path=GeckoDriverManager().install())
# options = Options()
# driver = webdriver.Firefox(service=service,options=options)




mywait = WebDriverWait(driver,40,ignored_exceptions=[Exception])

driver.get("https://www.google.com/")
driver.maximize_window()

searchbox=driver.find_element(By.NAME,"q")
searchbox.send_keys("Selenium")
searchbox.submit()

searchlink = mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
searchlink.click()
searchlink = mywait.until(EC.element_to_be_clickable((By.XPATH,"//h3[text()='Selenium']")))
searchlink.click()
#UPLOAD FILE

service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
driver.get("https://www.monsterindia.com/")
driver.find_element(By.CSS_SELECTOR,"a[class*='resume-btn']").click()

ele = driver.find_element(By.XPATH,"(//input[@type='file'])[1]")
ele.send_keys("C:\\Users\\dell\\Sample.txt")














































































































































































































































































































































































































































