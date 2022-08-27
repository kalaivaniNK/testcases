from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.page_load_strategy = "normal"
options.platform_name ='windows'
options.browser_version = "103"
driver = webdriver.Chrome(options=options)
driver.get("https://www.guvi.com")


#acceptInsecureCerts
#chrome

# from selenium.webdriver.chrome.options import Options
# options = Options()
# # options.add_argument('ignore-certificate-errors')
# options.accept_insecure_certs = True
# driver = webdriver.Chrome(options=options)
# driver.get('https://self-signed.badssl.com/')

#firefox
#
# from selenium.webdriver.firefox.options import Options
# options = Options()
# # options.add_argument('ignore-certificate-errors')
# options.accept_insecure_certs = True
# driver = webdriver.Firefox(options=options)
# driver.get('https://self-signed.badssl.com/')


# driver.close()