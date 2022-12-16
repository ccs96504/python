# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 15:05:58 2021

@author: Z00044060
"""

import application 
import excal_table as ET
import Comparison as CP


#啟動應用程式
Main_Excel_location = application.App(r'D:\\')
Local = Main_Excel_location.Application()
Main_Comparison = ET.excel_table(Local)


Minor_Excel_location = application.App(Local)
Minor_Comparison = ET.excel_table(Minor_Excel_location.Application())


#實體化方法比對相似值

EXCEL = CP.Comparison(Minor_Comparison[0],Minor_Comparison[3],Local,Main_Comparison[1],Main_Comparison[2])
#EXCEL.ShowSameThing()
EXCEL.InputValueinsamething()
####

