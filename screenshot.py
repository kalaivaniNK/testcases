from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://admin-demo.nopcommerce.com/")
# driver.save_screenshot("D:\workout images\img.png")

driver.save_full_page_screenshot("D:\workout images\picture.png")