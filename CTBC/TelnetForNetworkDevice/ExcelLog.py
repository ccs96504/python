# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 09:51:53 2021

@author: Z00044060
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 10:13:48 2021

@author: Z00044060
"""

import xlsxwriter
import xlwings as xw
import re

IP_content = []
IP_dir = []

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

def WorkBook_EXCEL():
    workbook = xlsxwriter.Workbook('BRCH_VER.xls')
    worksheet = workbook.add_worksheet()
    
    
    
    merge_format = workbook.add_format({  #?¼å??¼å?
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'yellow'})
    
    cell_format = workbook.add_format()
    cell_format.set_bold(False)
    cell_format.set_font_color('red')
    
    # Merge 3 cells.
    worksheet.write('A1', 'Hostname', merge_format)
    worksheet.write('B1', 'IP address', merge_format)
    worksheet.write('C1', 'SN?', merge_format)
    worksheet.write('D1', 'DESCR', merge_format)
    worksheet.write('E1', 'PID', merge_format)
    
    
    workbook.close()



    

