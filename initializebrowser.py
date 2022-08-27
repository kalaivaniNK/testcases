from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from jproperties import Properties

def call_browser(browser):
    config = Properties()
    with open("C:\\Users\\dell\\PycharmProjects\\testcase\\config.properties", "rb") as configFile:
        config.load(configFile)
        return config.get(browser).data


def test_code(browsertype):

    if browsertype == "chrome":
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browsertype == "firefox":
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    driver.get("https://www.guvi.in/")

test_code(call_browser("browser"))
