from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

def test():
    driver=webdriver.Firefox()
    driver.get("https://admin-demo.nopcommerce.com/")

    driver.find_element(By.ID, value="Email").clear()
    driver.find_element(By.CSS_SELECTOR, value="input#Password").clear()

    driver.find_element(By.ID,value="Email").send_keys("admin@yourstore.com")

    driver.find_element(By.CSS_SELECTOR,value="input#Password").send_keys("admin")

    driver.find_element(By.CSS_SELECTOR,"button[class^='button-1']").click()
    time.sleep(5)
    driver.find_element(By.XPATH,value="//a[@href='#']//p[contains(text(),'Sales')]").click()

    driver.find_element(By.XPATH,value="//a[@href='/Admin/Order/List']//p[contains(text(),'Orders')]").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR,value="input#StartDate").send_keys("17/07/2022")
    driver.find_element(By.CSS_SELECTOR,"input#EndDate").send_keys("18/07/2022")
    select1=Select(driver.find_element(By.ID,"WarehouseId"))
    select1.select_by_value('2')
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,value='input#search-product-name').send_keys("car")
    time.sleep(5)
    driver.find_element(By.XPATH,value="//ul/li[1]/div[contains(text(),'Lenovo Thinkpad X1 Carbon Laptop')]").click()


    select_vendor=Select(driver.find_element(By.ID,value="VendorId"))
    select_vendor.select_by_index(2)

    driver.find_element(By.ID,value="BillingPhone").send_keys('6764539378')

    driver.find_element(By.NAME,value="BillingEmail").send_keys("hijk@gmail.com")

    driver.find_element(By.XPATH,value="//input[@id='BillingLastName']").send_keys("fjk")

    select_country=Select(driver.find_element(By.ID,value="BillingCountryId"))
    select_country.select_by_visible_text("India")
    #
    select_paymentmethod=Select(driver.find_element(By.CSS_SELECTOR,"select#PaymentMethodSystemName"))
    select_paymentmethod.select_by_value('Payments.Manual')

    driver.find_element(By.ID,"OrderNotes").send_keys("hijklm")

    driver.find_element(By.CSS_SELECTOR,"input[id^= 'GoDirectly']").send_keys("yes")

    driver.find_element(By.CSS_SELECTOR,"input.k-input[aria-describedby='OrderStatusIds_taglist']").click()
    driver.find_element(By.XPATH,"//li[contains(text(),'Processing')]").click()

    driver.find_element(By.CSS_SELECTOR,"input.k-input[aria-describedby='PaymentStatusIds_taglist']").click()
    driver.find_element(By.XPATH,"//li[contains(text(),'Paid')]").click()

    driver.find_element(By.CSS_SELECTOR,"input.k-input[aria-describedby='ShippingStatusIds_taglist']").click()
    driver.find_element(By.XPATH,"//li[contains(text(),'Shipped')]").click()


    driver.find_element(By.CSS_SELECTOR,"button[id$='by-number']").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR,value="button[class*='btn-primary']").click()




test()