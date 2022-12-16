# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 10:33:51 2021

@author: 昱竹
"""


import ReadExcel
import Pyweb
import re
import Log_info
import datetime
class main:
    def __init__(self):
        f = open('init.txt','r')
        init_value = f.readlines()
        self.Excel_Path = re.findall(r'[^\\/:*?<>|\r\n]+$',init_value[0])[0]
        self.Web_Link = re.findall('[a-zAz]+://[^\s]*',init_value[1])[0]
        self.account =  re.findall('[A-Za-z0-9]+$',init_value[2])[0]
        self.password = re.findall(':.*?.*',init_value[3])[0][1:]

    def start(self):
                
        self.RE = ReadExcel.ReadExcel(self.Excel_Path)
        self.PW = Pyweb.PyWebClass(self.Web_Link)
        self.PW.HomePage(self.account, self.password)
        self.PW.renewPage()
        self.TD = self.RE.ReadExcel()
        for i in range(len(self.TD[0])):
          print( self.TD[1][i])
          self.PW.add_table(i, self.TD[0][i],self.TD[1][i],self.TD[2][i])



if __name__ == "__main__":
    try:
        MA = main()
        MA.start()
    except  Exception as e:
        print(e)
        Log_info.mkdir("Log",str(e),datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+"-Log.txt")

