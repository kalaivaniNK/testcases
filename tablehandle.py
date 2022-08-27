from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("https://testautomationpractice.blogspot.com/")


#GETTING HOW MANY ROWS ARE THERE
# getTableRows = driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr")
# print(len(getTableRows))



#GETTING FIRST COLUMN VALUE
getTableRows = driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr")

for i in getTableRows:
    try:
        print(i.find_element(By.TAG_NAME,'td').text)

    except:
        print("error")


#GETTING ALL VALUES IN TABLE (WITHOUT HEADING)
# getTableRows = driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr")
#
# for i in getTableRows:
#     try:
#         getTableColumn = i.find_elements(By.TAG_NAME,'td')
#         for j in getTableColumn:
#              print(j.text)
#     except:
#         print("error")


#GETTING SPECIFIC VALUE
# getTableRows = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[2]/td[3]")
# print(getTableRows.text)

#GETTING TITLE ONLY
# getTableRows = driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr[1]")
#
# for i in getTableRows:
#     try:
#         getTopic = i.find_elements(By.TAG_NAME,'th')
#         for j in getTopic:
#             print(j.text)
#     except:
#         print("error")


