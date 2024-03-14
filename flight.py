import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class Flight_search:
        
        #driver.implicitly_wait(10)
    def search(self,start,dest,go,back):
        driver = webdriver.Chrome("")
        driver.get("https://www.google.com/travel/flights")
        wait = WebDriverWait(driver,10,poll_frequency=1)

        self.start = driver.find_element(By.XPATH,"//input[@aria-label='從哪裡出發？']")
        self.start.clear()
        self.start.send_keys(start)

        wait.until(lambda d:driver.find_element(By.XPATH,"//*[@id='c2']/div[2]/div[1]").is_displayed())
        c = driver.find_element(By.XPATH,"//*[@id='c2']/div[2]/div[1]")
        c.click()

        self.destination = driver.find_element(By.XPATH,"//input[@aria-label='要去哪裡？ ']")
        self.destination.send_keys(dest)

        wait.until(lambda d:driver.find_element(By.XPATH,"//*[@id='c7']/div[2]/div[1]").is_displayed())
        c = driver.find_element(By.XPATH,"//*[@id='c7']/div[2]/div[1]")
        c.click()        

        wait.until(lambda d:driver.find_element(By.XPATH,"//input[@aria-label='去程']").is_displayed())
        self.go = driver.find_element(By.XPATH,"//input[@aria-label='去程']")
        self.go.send_keys(go)
        self.go.send_keys("\ue007")
        time.sleep(2)

        wait.until(lambda d:driver.find_element(By.XPATH,"//input[@aria-label='回程']").is_displayed())
        self.back = driver.find_element(By.XPATH,"//input[@aria-label='回程']")
        self.back.send_keys(back)
        self.back.send_keys("\ue007")
        time.sleep(2)

        wait.until(lambda d:driver.find_element(By.CLASS_NAME,"VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-Bz112c-M1Soyc.nCP5yc.AjY5Oe.LQeN7.TUT4y.zlyfOd").is_displayed())
        search = driver.find_element(By.CLASS_NAME,"VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-Bz112c-M1Soyc.nCP5yc.AjY5Oe.LQeN7.TUT4y.zlyfOd")
        search.click()

        wait.until(lambda d:driver.find_element(By.CLASS_NAME,"JMc5Xc").is_displayed())
        result = driver.find_elements(By.CLASS_NAME,"JMc5Xc")
        Flight_search.flight_extration(result,5)
    
    def flight_extration(text,num):
        if len(text)>num:
            text = text[0:num]
        for i in range(len(text)):
            text[i] = text[i].get_attribute("aria-label")
        
        print(text[0].split("。"))
