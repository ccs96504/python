# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 16:29:17 2021

@author: Z00044060
"""


# -*- coding: utf-8 -*-




import sys
sys.path.append(r"D:\函式庫\WebDriver")
sys.path.append(r"D:\函式庫\RdTxt")
import pandas as pd
import WebDriver
import RdTxt
import sys
import os
command = 'taskkill /f /im chromedriver.exe'
os.system(command)

Filevalue = RdTxt.File(r"D:\F5_web\fail_IP.html")
Filevalue_set = set(Filevalue)
Filevalue = list(Filevalue_set)

table = WebDriver.http('https://'+str(Filevalue[0]))

df = pd.DataFrame([(table[0],table[1],table[2])], columns = ['IP','Hostname','SN序號'])
for i in range(1,len(Filevalue)):
    try:
        table = WebDriver.http('https://'+str(Filevalue[i]))
        df.loc[i]= [table[0],table[1],table[2]]
        df.to_csv('F5_table.csv',index= False)

    except:
        df.to_csv('F5_table.csv',index= False)
