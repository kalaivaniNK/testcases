from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By




def test_code(browsertype):

    if browsertype == "chrome":
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browsertype == "firefox":
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)

        driver.get("https://testautomationpractice.blogspot.com/")
        # ele = driver.find_element(By.XPATH,"//h2[text()='XPath Axes']")
        # driver.execute_script("arguments[0].scrollIntoView();", ele)

        # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);");

        # driver.get("https://demo.opencart.com/")
        # # ele = driver.find_element(By.NAME,"search")
        # # driver.execute_script("arguments[0].setAttribute('style','border: 2px solid red;');", ele);
        #
        # driver.save_screenshot("homepage.png")

        driver.get("https://www.flipkart.com/")
        # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);");







test_code("firefox")