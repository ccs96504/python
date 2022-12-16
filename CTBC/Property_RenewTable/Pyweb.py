# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 13:28:50 2021

@author: 昱竹
"""


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time


class PyWebClass:
    def __init__(self,WebLink):
        ##網頁初始職配置###
        

        chrome_options = Options()
       # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        
        ##初始參數配置####
        self.WebLink = WebLink
        self.driver.get(self.WebLink)
    def TimeOutWeb(self,WebID):
        try:
            WebDriverWait(self.WebLink, 1).until(EC.presence_of_element_located((By.ID, WebID)))
        except:
            print('time out')
    def TimeOutWebXpath(self,WebID):
        try:
            WebDriverWait(self.WebLink, 1).until(EC.presence_of_element_located((By.XPATH, WebID)))
        except:
            print('time out')
    
    
    
    def HomePage(self,Username,Password):
        
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/form/table[2]/tbody/tr/td[1]/div/table[1]/tbody/tr[3]/td[2]/input").send_keys(Username)
        self.driver.find_element_by_xpath("/html/body/form/table[2]/tbody/tr/td[1]/div/table[1]/tbody/tr[4]/td[2]/input").send_keys(Password)
        self.driver.find_element_by_xpath("/html/body/form/table[2]/tbody/tr/td[1]/div/table[1]/tbody/tr[7]/td[2]/input[1]").click()

        
    
    def renewPage(self):
        self.driver.get("http://assetmgt.ctbcbank.com/PRPT/PRPTCondonia.aspx")
        self.driver.find_element_by_xpath("/html/body/form/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td/div/input").click()
        self.driver.find_element_by_xpath("/html/body/form/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td/div/fieldset/table[1]/tbody/tr[1]/td[2]/select").click()
        self.driver.find_element_by_id("ctl00_ContentPlaceHolder1_ddlApplyCostCenter").click()
        Select(self.driver.find_element_by_id("ctl00_ContentPlaceHolder1_ddlApplyCostCenter")).select_by_visible_text(u"002105Z-資訊營運部-技術支援三科")
        self.driver.find_element_by_xpath("/html/body/form/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td/div/fieldset/table[1]/tbody/tr[2]/td[2]/textarea").send_keys("變更設備位置")
        
    def add_table(self,i,ID,Staff_ID,NewName):    
        self.driver.find_element_by_xpath("/html/body/form/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td/div/fieldset/table[2]/tbody/tr/td[1]/input[1]").click()
        self.driver.find_element_by_xpath("/html/body/form/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td/div/fieldset/table[5]/tbody/tr/td/table/tbody/tr["+str(i+2)+"]/td[2]/input").click()
        self.driver.find_element_by_xpath("/html/body/form/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td/div/fieldset/table[5]/tbody/tr/td/table/tbody/tr["+str(i+2)+"]/td[2]/input").send_keys(ID)
        self.driver.find_element_by_xpath("/html/body/form/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td/div/fieldset/table[5]/tbody/tr/td/table/tbody/tr["+str(i+2)+"]/td[3]/input").click()
        
        time.sleep(0.5)
        self.driver.find_element_by_id("KEEPER_ID_"+str(i+1)+"").clear()
        time.sleep(0.5)
        self.driver.find_element_by_id("KEEPER_ID_"+str(i+1)+"").send_keys(Staff_ID)
        time.sleep(0.5)
        self.driver.find_element_by_id("KEEPER_"+str(i+1)+"").clear()
        time.sleep(0.5)
        self.driver.find_element_by_id("KEEPER_"+str(i+1)+"").clear()
        self.driver.find_element_by_id("KEEPER_"+str(i+1)+"").send_keys(NewName)

    def save(self,i):    
        self.driver.find_element_by_xpath("/html/body/form/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td/div/fieldset/table[2]/tbody/tr/td[1]/input[2]").click()


 