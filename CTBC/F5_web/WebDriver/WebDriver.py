# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 16:20:53 2021

@author: Z00044060
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys  #鍵盤功能
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


from urllib.request import urlopen
from bs4 import BeautifulSoup

import time
        
def http(Link):
    def TimeOutWeb(WebID):
        try:
            element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, WebID)))
            return element
        except:
            print('time out')
    def TimeOutWebXpath(WebID):
        try:
            element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, WebID)))
            return element
        except:
            print('time out')

    options = webdriver.ChromeOptions()
 #   options.add_argument('--headless')
    options.add_argument("user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'")
    driver = webdriver.Chrome("D:\函式庫\WebDriver\chromedriver.exe", options=options)
    driver.maximize_window()

    driver.get(Link)
    try:
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/form/input[1]").send_keys('netteam')
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/form/input[2]").send_keys('ctcbnetteam')
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/form/button").click()
        time.sleep(1)
   
        driver.find_element_by_id("mainmenu-system").click()
        driver.find_element_by_id("mainmenu-system-globals").click()
        #driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[1]/div[1]/div[8]/a").click()
        #driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[1]/div[1]/div[8]/ul/li[1]").click()
        
        time.sleep(1)
        TimeOutWebXpath("/html/body/div[1]/div[4]/div[2]/div[2]/iframe")
        
        driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div[2]/iframe"))
        Hostname = driver.find_element_by_xpath("/html/body/div[1]/form/div[1]/table/tbody/tr[1]/td[2]").text
        SN = driver.find_element_by_xpath("/html/body/div[1]/form/div[1]/table/tbody/tr[2]/td[2]").text
        driver.switch_to_default_content()
        driver.find_element_by_id("logout").click()
        driver.close()
        
        Table = [Link[8:],Hostname,SN]
        
        return Table
    except:
        driver.close()
        print('login Fail')
        Table = [Link[8:],'Login fail',' ']
        return Table
        

