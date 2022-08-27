from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option("prefs",{"download_default_directory": "D:\download"})
driver = webdriver.Chrome(options=options)

driver.get("https://demo.automationtesting.in/FileDownload.html")

driver.maximize_window()
driver.find_element(By.ID,"textbox").send_keys("text file to be dowmlais")

driver.find_element(By.CSS_SELECTOR,"button#createTxt").click()
driver.find_element(By.XPATH,"//a[@id='link-to-download']").click()
time.sleep(5)

# driver.find_element(By.ID,"pdfbox").send_keys("download pdf")
# driver.find_element(By.XPATH,"//button[@id='createPdf']").click()
# # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# driver.find_element(By.XPATH,"//a[@id='pdf-link-to-download']").click()