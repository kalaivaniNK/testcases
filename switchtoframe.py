from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def switchFrame():
    driver=webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")


    driver.find_element(By.ID,value="datepicker").send_keys("17/07/2022")

    select=Select(driver.find_element(By.CSS_SELECTOR,"select#speed"))
    select.select_by_index(4)

    select_file=Select(driver.find_element(By.XPATH,value="//select[@id='files']"))
    select_file.select_by_visible_text('DOC file')

    select_number=Select(driver.find_element(By.ID,"number"))
    select_number.select_by_index(3)

    select_product=Select(driver.find_element(By.NAME,"products"))
    select_product.select_by_visible_text('Iphone')

    select_animal=Select(driver.find_element(By.ID,"animals"))
    select_animal.select_by_value('babycat')

    driver.switch_to.frame("frame-one1434677811")

    driver.find_element(By.XPATH,"//input[@id='RESULT_TextField-1']").send_keys("kalai")

    driver.find_element(By.ID,"RESULT_TextField-2").send_keys("vani")

    driver.find_element(By.XPATH,"//input[@id='RESULT_TextField-3']").send_keys('7854635278')

    driver.find_element(By.XPATH,"//input[@id='RESULT_TextField-4']").send_keys("india")

    driver.find_element(By.CSS_SELECTOR,"input#RESULT_TextField-5").send_keys("tamil nadu")

    driver.find_element(By.ID,"RESULT_TextField-6").send_keys("adcd@gmail.com")

    driver.find_element(By.XPATH,"//table[@class='inline_grid choices']//label[contains(text(),'Female')]").click()
    time.sleep(5)



    checkbox = driver.find_element(By.CSS_SELECTOR,"label[for='RESULT_CheckBox-8_0']")
    checkbox.click()
    checkbox.is_selected()
    time.sleep(5)
    select1=Select(driver.find_element(By.ID,value="RESULT_RadioButton-9"))
    select1.select_by_value('Radio-2')
    driver.switch_to.default_content()


    driver.find_element(By.XPATH,value="//button[contains(text(),'Click Me')]").click()
    driver.switch_to.alert.accept()





    driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input").send_keys("locators")
    driver.find_element(By.CSS_SELECTOR, "input.wikipedia-search-button").click()
    driver.find_element(By.XPATH,"//a[contains(text(), 'Locator software')]").click()

    time.sleep(5)
    driver.find_element(By.ID, "field2").send_keys("Hello!")


switchFrame()