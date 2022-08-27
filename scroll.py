from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
driver = webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
action = ActionChains(driver)
# driver.switch_to.frame("frame-one1434677811")
ele = driver.find_element(By.XPATH,"//h2[contains(text(),'Slider')]")
action.scroll_to_element(ele).perform()