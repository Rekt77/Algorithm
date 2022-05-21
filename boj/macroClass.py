from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
import time

class Naver():
    def __init__(self,userID,userPW):
        self.userID = userID
        self.userPW = userPW
        self.urls = {}

    def add_urls(self,key,value):
        self.urls[key]=value

class webDriver():
    def __init__(self,url):
        self.driver = webdriver.Chrome(executable_path='chromedriver')
        self.url = url
        
    def NaverLogin(self,naver:Naver):
        tag_id = self.driver.find_element_by_name('id')
        tag_pw = self.driver.find_element_by_name('pw')

        tag_id.click()
        pyperclip.copy(naver.userID)
        tag_id.send_keys(Keys.CONTROL, 'v')
        tag_pw.click()
        pyperclip.copy(naver.userPW)
        tag_pw.send_keys(Keys.CONTROL, 'v')

        login_btn = self.driver.find_element_by_id('log.login')
        login_btn.click()
        time.sleep(2)

        try: 
            login_error = self.driver.find_element_by_css_selector('#err_common > div > p')
            return(login_error.text)
        except: 
            return('succes')

    def NaverReserv(self,naver:Naver):    
        self.driver.get(self.url)
        time.sleep(2)

        button = self.driver.find_element_by_class_name("btn_srch.on")
        button.click()
        time.sleep(2)
        if self.NaverLogin(naver) != 'succes':
            return "Failure"
        next_month = self.driver.find_element_by_class_name("calendar-btn.calendar-btn-next-mon")
        next_month.click()
        time.sleep(2)
        # 24일 calendar = self.driver.find_elements_by_class_name('num')[26]
        date = self.driver.find_elements_by_class_name('num')[1]
        #print(len(date))
        date.click()
        time.sleep(2)
        visit = self.driver.find_elements_by_class_name('anchor')[0]
        visit.click()
        time.sleep(2)
        people = self.driver.find_elements_by_class_name("btn_plus_minus.spr_book ico_plus3")[0]
        for _ in range(2):
            people.click()
        #submit = self.driver.find_element_by_class_name('btn')
        #submit.click()
        time.sleep(10)