# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 13:31:11 2021

@author: 昱竹
"""

import pandas as pd

class ReadExcel:
    def __init__(self,Local):
        self.excel_fileexcel_file = pd.read_excel(Local)
        self.Property_NB = []
        self.custodian = []
        self.Staff_ID =[]
    def ReadExcel(self):
        self.Property_NB  = self.excel_fileexcel_file['財產編號'].tolist()
        self.Staff_ID  = self.excel_fileexcel_file['員編'].tolist()
        self.custodian = self.excel_fileexcel_file['新保管人'].tolist()
        return self.Property_NB,self.Staff_ID,self.custodian 