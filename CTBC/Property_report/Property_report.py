# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 09:32:56 2021

@author: Z00044060
"""
import sys

sys.path.append("D:\Property_report\package")

 
import time
import datetime
import os
import pandas as pd

from package import Download_Package

start = time.time()
today=datetime.date.today()
today = today.strftime('%Y-%m-%d')

###所需資訊
Download_path = 'D:\\Property_report\\Download\\'+str(today)
Username = 'z00044060'
Password = '0602Love0113@'
Update_path =  'D:\\Property_report\\Download\\Update\\'+str('NewList.xlsx')

###
os.system('taskkill /f /im EXCEL.EXE*')

###引用方法
Download_file = Download_Package.Download_file(Download_path,Username,Password)
Download_Package.excel_update(Download_file,Update_path)


folder = os.path.exists(Download_path)
folder = os.listdir(Download_path)
old_file = pd.read_excel((Download_path+"\\"+str(folder[0])))

fliter = (old_file["地點"] != "V")
new = old_file[fliter]
new.to_excel('error_'+str(today)+'.xlsx')






