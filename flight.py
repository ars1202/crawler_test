import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import re
chrome_options = Options()
#chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com/travel/flights")
wait = WebDriverWait(driver,10,poll_frequency=1)
class Flight_search:
    
    def input_data(code,text,find):

        if find=="xpath":
            wait.until(lambda d:driver.find_element(By.XPATH,code).is_displayed())
            tmp = driver.find_element(By.XPATH,code)
        elif find=="class":
            wait.until(lambda d:driver.find_element(By.CLASS_NAME,code).is_displayed())
            tmp = driver.find_element(By.CLASS_NAME,code)
        
        tmp.clear()
        tmp.send_keys(text)
        return tmp

    def click_button(code,find):
        if find=="xpath":
            wait.until(lambda d:driver.find_element(By.XPATH,code).is_displayed())
            button = driver.find_element(By.XPATH,code)
        elif find=="class":
            wait.until(lambda d:driver.find_element(By.CLASS_NAME,code).is_displayed())
            button = driver.find_element(By.CLASS_NAME,code)            
        button.click()
        return button        
        #driver.implicitly_wait(10)
    def search(self,start,dest,go,back):
        
        Flight_search.input_data("//input[@aria-label='從哪裡出發？']",start,"xpath")

        Flight_search.click_button("//*[@id='c2']/div[2]/div[1]","xpath")

        Flight_search.input_data("//input[@aria-label='要去哪裡？ ']",dest,"xpath")

        Flight_search.click_button("//*[@id='c7']/div[2]/div[1]","xpath")        

        self.go = Flight_search.input_data("//input[@aria-label='去程']",go,"xpath")
        self.go.send_keys("\ue007")
        time.sleep(2)

        self.back = Flight_search.input_data("//input[@aria-label='回程']",back,"xpath")
        self.back.send_keys("\ue007")
        time.sleep(2)

        Flight_search.click_button("VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-Bz112c-M1Soyc.nCP5yc.AjY5Oe.LQeN7.TUT4y.zlyfOd","class")

        Flight_search.click_button("JMc5Xc","class")
        
        wait.until(lambda d:driver.find_element(By.CLASS_NAME,"JMc5Xc").is_displayed())
        result = driver.find_elements(By.CLASS_NAME,"JMc5Xc")
        Flight_search.flight_extration(result,10)
    
    def flight_extration(text,num):
        if len(text)>num:
            text = text[0:num]
        for i in range(len(text)):
            text[i] = text[i].get_attribute("aria-label")
        
            print(text[i].split("。"))
