from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class Test():
    url="https://testautomationpractice.blogspot.com/"
    driver = webdriver.Firefox()


    def date(self):
        self.driver.get(self.url)
        date_id = "datepicker"
        date_value = self.driver.find_element(By.ID, value=date_id)
        date_value .send_keys("17/07/2022")
        time.sleep(3)

    def selectspeed(self):
        select = Select(self.driver.find_element(By.CSS_SELECTOR, "select#speed"))
        select.select_by_index(4)
        time.sleep(3)

    def selectfile(self):
        select_file = Select(self.driver.find_element(By.XPATH, value="//select[@id='files']"))
        select_file.select_by_visible_text('DOC file')
        time.sleep(3)

    def selectnumber(self):
        select_number = Select(self.driver.find_element(By.ID, "number"))
        select_number.select_by_index(3)
        time.sleep(3)

    def selectproduct(self):
        select_product = Select(self.driver.find_element(By.NAME, "products"))
        select_product.select_by_visible_text('Iphone')
        time.sleep(3)

    def selectanimal(self):
        select_animal = Select(self.driver.find_element(By.ID, "animals"))
        select_animal.select_by_value('babycat')
        self.driver.switch_to.frame("frame-one1434677811")
        time.sleep(3)

    def Firstname(self):
        name_xpath = "//input[@id='RESULT_TextField-1']"
        value = self.driver.find_element(By.XPATH,value=name_xpath)
        value.send_keys("kalai")
        time.sleep(3)

    def LastName(self):
        Lname_id = "RESULT_TextField-2"
        Lname_find = self.driver.find_element(By.ID,value=Lname_id)
        Lname_find .send_keys("vani")
        time.sleep(3)

    def Phno(self):
        Phno_xpath = "//input[@id='RESULT_TextField-3']"
        Phno_find = self.driver.find_element(By.XPATH,value=Phno_xpath)
        Phno_find.send_keys('7854635278')
        time.sleep(3)

    def country(self):
        country_xpath = "//input[@id='RESULT_TextField-4']"
        country_find = self.driver.find_element(By.XPATH,value=country_xpath)
        country_find.send_keys("tamil nadu")
        time.sleep(3)

    def city(self):
        city_css = "input#RESULT_TextField-5"
        ciyt_find = self.driver.find_element(By.CSS_SELECTOR,value=city_css )
        ciyt_find.send_keys("chennai")
        time.sleep(3)

    def email(self):
        email_id = "RESULT_TextField-6"
        email_find = self.driver.find_element(By.ID,value=email_id)
        email_find.send_keys("adcd@gmail.com")
        time.sleep(3)
        # driver.find_element(By.XPATH,"//tr[1]/td/label[contains(text(),'Male')]").click()

    def field2(self):
        field_path = "input#field2"
        field_find = self.driver.find_element(By.CSS_SELECTOR, value=field_path)
        field_find.send_keys("Hello!")
        time.sleep(3)



    def alert(self):
        self.driver.switch_to.default_content()
        alert_path="//button[contains(text(),'Click Me')]"
        self.driver.find_element(By.XPATH, value=alert_path).click()
        self.driver.switch_to.alert.accept()
        time.sleep(3)
        self.driver.maximize_window()


    def gender(self):

        gender = self.driver.find_element(By.CSS_SELECTOR, value="label[for='RESULT_RadioButton-7_1']")
        self.driver.execute_script("arguments[0].scrollIntoView();",gender)
        gender.click()


    def pickday(self):

        self.driver.switch_to.frame("frame-one1434677811")
        tables = self.driver.find_elements(By.XPATH, value="//div[@id='q15']/table/tbody/tr/td/label")

        for table in tables:
            if table.text == "Monday":
                print(table.text)
                table.click()


        select1 = Select(self.driver.find_element(By.CSS_SELECTOR, value="select#RESULT_RadioButton-9"))
        select1.select_by_value("Radio-2")
    def search(self):
        search_path = "Wikipedia1_wikipedia-search-input"
        search_find = self.driver.find_element(By.ID, value=search_path)
        search_find.send_keys("locators")
        time.sleep(3)



    def buttonclick(self):
        self.driver.switch_to.default_content()
        button_path = "//input[@class='wikipedia-search-button']"
        button_find = self.driver.find_element(By.XPATH, value=button_path)
        button_find.click()
        time.sleep(3)

    def getname(self):
        name1_xpath="designation[experience='3 year']"
        name1_find=self.driver.find_element(By.CSS_SELECTOR,value=name1_xpath)
        print(name1_find.text)
    def email1(self):
        mail_path="//email[contains(text(),'david@myemail.com')]"
        mail_find=self.driver.find_element(By.XPATH,value=mail_path)
        print(mail_find.text)
    def field1(self):
        field_path="input[value='Hello World!']"
        field_find=self.driver.find_element(By.CSS_SELECTOR,value=field_path)
        field_find.clear()

    def age(self):
        age_path="input#age"
        age_find=self.driver.find_element(By.CSS_SELECTOR,value=age_path)
        age_find.send_keys("22")

    def locatorsoftware(self):
        software_path = "//a[contains(text(),'Locator software')]"
        software_find = self.driver.find_element(By.XPATH, value=software_path)
        software_find.click()
        time.sleep(5)


s = Test()
s.date()
s.selectspeed()
s.selectfile()
s.selectnumber()
s.selectproduct()
s.selectanimal()
s.Firstname()
s.LastName()
s.Phno()
s.country()
s.city()
s.email()
s.gender()
s.alert()
s.field2()
s.search()
s.pickday()
s.buttonclick()
s.locatorsoftware()
s.search()
s.getname()
s.email1()
s.field1()
s.age()

