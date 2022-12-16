# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 16:23:12 2021

@author: Z00044060
"""

import pandas as pd

def excel_table(local):
    print(local)
    sheet = pd.ExcelFile(local)
    sheet_list= sheet.sheet_names
    for i in range(len(sheet_list)):
        print(str(i)+'.'+str(sheet_list[i]))
    SHEET = int(input('輸入SHEET表:'))
    main = pd.read_excel(local,SHEET)
    index = main.columns.tolist()
    
    for i in range(len(index)):
        print(str(i)+'.'+str(index[i]))
    EXCEL_TABLE = int(input('輸入EXCEL_TABLE欄位:'))
    Comparison_List =main[index[EXCEL_TABLE]].tolist()
    
    #main
    return Comparison_List,SHEET,EXCEL_TABLE,main



#if __name__ == "__main__":
#    value = excel_table(r'D:\ctbc\外據點財產申請v2.xlsx')
