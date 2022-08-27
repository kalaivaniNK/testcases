from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
import time

service = FirefoxService(executable_path=GeckoDriverManager().install())

driver = webdriver.Firefox(service=service)

driver.get("https://admin-demo.nopcommerce.com/")

driver.find_element(By.ID, value="Email").clear()
driver.find_element(By.CSS_SELECTOR, value="input#Password").clear()

driver.find_element(By.ID, value="Email").send_keys("admin@yourstore.com")

driver.find_element(By.CSS_SELECTOR, value="input#Password").send_keys("admin")

driver.find_element(By.CSS_SELECTOR, "button[class^='button-1']").click()
time.sleep(5)
driver.find_element(By.XPATH, value="//a[@href='#']//p[contains(text(),'Sales')]").click()

driver.find_element(By.XPATH, value="//a[@href='/Admin/Order/List']//p[contains(text(),'Orders')]").click()


# getTableRows = driver.find_elements(By.XPATH,"//table[@id='orders-grid']/tbody/tr")
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);");
# for i in getTableRows:
#     try:
#         getValue = i.find_elements(By.TAG_NAME,'td')
#         for j in getValue:
#             print(j.text)
#     except:
#         print("error")
#CLICK ALL THE CHECKBOXES
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);");
# time.sleep(5)
# # driver.find_element(By.XPATH,"//div[@class='dataTables_scrollHeadInner']//input[@type='checkbox']").click()
#
# driver.find_element(By.XPATH,"//table/thead/tr/th/input").click()

#CLICK ONLY THE CHECKBOX VALUE = 5
# time.sleep(5)
# driver.find_element(By.XPATH,"//div[@class='dataTables_scrollBody']//input[@value='5']").click()
#

#GETTING SPECIFIC VALUE
time.sleep(4)
get_value=driver.find_element(By.XPATH,"//table[@id='orders-grid']/tbody/tr[2]/td[4]")
print(get_value.text)

#getting cick the checkbox (using after value)
# time.sleep(5)
# driver.find_element(By.XPATH,"//td[text()='5']//preceding-sibling::td//input").click()
#click th link
# driver.find_element(By.XPATH,"//a[contains(text(),'victoria_victoria@nopCommerce.com')]").click()


