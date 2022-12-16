# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 15:23:20 2021

@author: Z00044060
"""

#引入模組
import os




def mkdir(path,Log,IP):

    folder = os.path.exists(path)

    if not folder:
        os.makedirs(path)
        print('-----建立成功-----')
        Log_txt = open(os.getcwd()+"\\"+path+"\\"+IP+'.txt','w')
        Log_txt.write(str(Log))
        Log_txt.close()
    else:
       # print(os.getcwd()) 顯示幕前路徑
        Log_txt = open(os.getcwd()+"\\"+path+"\\"+IP+'.txt','w')
        Log_txt.write(str(Log))
        Log_txt.close()
        
