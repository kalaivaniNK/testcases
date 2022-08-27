from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://testautomationpractice.blogspot.com/")

actionchains = ActionChains(driver)
#drag and drop
source = driver.find_element(By.CSS_SELECTOR,"div#draggable")
destination = driver.find_element(By.CSS_SELECTOR,"div#droppable")
driver.maximize_window()
actionchains.drag_and_drop(source,destination).perform()

#double click(copy text in webpage pree double click)
element=driver.find_element(By.XPATH,"//button[contains(text(),'Copy Text')]")
actionchains.double_click(element).perform()

#drag an drop by offset( inwebpage move the slider)
# slider=driver.find_element(By.XPATH,"//div[@id='slider']/span")
# slider_view = driver.find_element(By.XPATH,"//h2[contains(text(),'Slider')]")
# driver.execute_script("arguments[0].scrollIntoView();",slider_view)
# ActionChains(driver).drag_and_drop_by_offset(slider,200,0).perform()
# time.sleep(5)

# driver.forward()
# driver.get("https://www.geeksforgeeks.org/")
#
# course_find=driver.find_element(By.XPATH,"//span[text()='Courses']")
# actionchains.click_and_hold(on_element=course_find).perform()

# click_alert=driver.find_element(By.XPATH,"//button[text()='Click Me']")
# time.sleep(5)
# actionchains.click(click_alert).perform()
# time.sleep(5)
# print(Alert(driver).text)
# Alert(driver).accept()
# time.sleep(3)

#resizable

resizable = driver.find_element(By.CSS_SELECTOR,"div[class*='ui-resizable-se ui-icon']")
resize_find = driver.find_element(By.XPATH,"//h2[text()='Resizable']")
driver.execute_script("arguments[0].scrollIntoView();",resize_find)
time.sleep(5)
actionchains.click_and_hold(resizable).move_by_offset(50,50).release().perform()


#sendkeys using alert

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.alert import Alert
#
# driver=webdriver.Firefox()
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
#
# driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
#
# Alert(driver).send_keys(keysToSend="hi")


