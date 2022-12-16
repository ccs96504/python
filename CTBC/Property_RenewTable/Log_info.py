# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 15:23:20 2021

@author: Z00044060
"""

#引入模組
import os
import re



def mkdir(path,Log,Logname):

    folder = os.path.exists(path)

    if not folder:
        os.makedirs(path)
        print('-----建立成功-----')
        Log_txt = open(os.getcwd()+"\\"+path+"\\"+Logname+'.txt','w')
        for i in Log:
            Log_txt.write(i)
            
        Log_txt.close()
    else:
       # print(os.getcwd()) 顯示幕前路徑
        Log_txt = open(os.getcwd()+"\\"+path+"\\"+Logname+'.txt','w')
        for i in Log:
            Log_txt.write(i)
        Log_txt.close()
        
        
def txt_Location(loacl):
    f = open(loacl)
    text_IP = []
    IP_List = []
    for line in f:
        IP_ = re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])', line)
        text_IP.append(IP_)

        
    for i in range(len(text_IP)):
        IP_List.append(str(text_IP[i][0]))
 
    return IP_List