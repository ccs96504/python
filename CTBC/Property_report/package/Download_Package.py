# -*- coding: utf-8 -*-
"""
Created on Mon May 24 16:37:25 2021

@author: Z00044060
"""



from selenium import webdriver
from selenium.webdriver.common.keys import Keys  #鍵盤功能
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os
import sys
import time
import datetime
import pandas as pd
import xlsxwriter


start = time.time()
today=datetime.date.today()
today = today.strftime('%Y-%m-%d')



def Download_file(Download_path , Username,password):
    print('Download Path: '+Download_path)
    command = 'taskkill /f /im EXCEL.EXE*'
    os.system(command)
    
    
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
    
    print('Programe Ready ')
    
    #產生資料夾
    folder = os.path.exists(Download_path)
    if not folder:                  
       os.makedirs(Download_path)     
       time.sleep(1)    
       print("Add file")
    else:
    	print("There is this folder!")
    os.close
    
    ##開啟網頁
    chrome_options = Options()
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': r""+str(Download_path)}
    chrome_options.add_experimental_option('prefs', prefs)
  
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.maximize_window()
    driver.get('http://assetmgt.chinatrust.com.tw/Default.aspx?ReturnUrl=%2fReport%2fPRPTRptMaster.aspx')
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td[1]/div/table[1]/tbody/tr[3]/td[2]/input').send_keys(str(Username))
    driver.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td[1]/div/table[1]/tbody/tr[4]/td[2]/input').send_keys(str(password))
    driver.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td[1]/div/table[1]/tbody/tr[7]/td[2]/input[1]').click()
    time.sleep(2)
    driver.get('http://assetmgt.chinatrust.com.tw/Report/PRPTRptMaster.aspx')
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td/fieldset/table[2]/tbody/tr[3]/td[4]/input[1]').send_keys('002105')
    driver.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td/fieldset/table[2]/tbody/tr[9]/td[1]/input[1]').click()
    driver.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td/fieldset/table[2]/tbody/tr[9]/td[1]/input[1]').click()
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td/fieldset/table[2]/tbody/tr[11]/td[1]/a').click()
    time.sleep(10)
    driver.close()
    print('close...')


    folder = os.path.exists(Download_path)
    folder = os.listdir(Download_path)
    print(Download_path+"\\"+str(folder[0]))
    
    data=pd.read_html(Download_path+"\\"+str(folder[0]))
    New_report = data[0]
    workbook = xlsxwriter.Workbook(Download_path+"\\"+str(folder[0])+'x')
    worksheet = workbook.add_worksheet()
    # Create a format to use in the merged range.
    merge_format = workbook.add_format({  #格子格式
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'yellow'})
    
    cell_format = workbook.add_format()
    cell_format.set_bold(False)
    cell_format.set_font_color('red')
        
    
    for i in range(len(New_report.iloc[:,4])):
                for z in range(len(New_report.iloc[0,:])):
                    worksheet.write(chr(int(z)+65)+str(1+i), str(New_report.iloc[i,z]) )
    for i in range(len(New_report.iloc[0,:])):
        worksheet.write(chr(int(i)+65)+'1', New_report.iloc[0,i],merge_format )
    os.remove(Download_path+"\\"+str(folder[0]))
    workbook.close()
    
    return str(Download_path+"\\"+str(folder[0])+'x')

def excel_update(Download_file,Update_path):

    old_file = pd.read_excel(Download_file)
    old_file = old_file.where(old_file.notnull())
    new_file = pd.read_excel(Update_path)
    new_file = new_file.where(new_file.notnull())
    KEY = new_file.keys()
    
    print(KEY[18])
    
    for z in range(18,27):
        old_file[str(KEY[z])] = '' 
    
    
    for i in range(len(old_file)):
       for j in range(len(new_file)):
           if str(old_file.iloc[i,4])==str(new_file.iloc[j,4]):
               for z in range(18,27):
                   old_file.iloc[i,z] = new_file.iloc[j,z]
                   print(str(old_file.iloc[i,z]),end = ' ')
               print('\n')
               break        
    old_file.to_excel(Download_file)
    
    return old_file,new_file
    

    