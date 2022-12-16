# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 15:40:49 2021

@author: 昱竹
"""



import pandas as pd
import re
class ExcelTableComparison:
    def __init__(self,ExcelLocal,DelList,TitleList):
            self.FilterBrch = ['南港','行政','台中營運','承德']
            self.ExcelLocal = ExcelLocal
            self.DelList = DelList
            self.TitleList = TitleList
            
            self.Buffer = 0
                
    
    def check_IP(self,str):
    	s = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
    	str = s.search(str)
    	return  not  bool(str)
    
    
    def Filter_Brch(self,str,Bach):

        A = (""+Bach+".*")
        #print(A)
        s = re.compile( r'{}'.format(A))
        str = s.search(str)
        return bool(str)


    
    def AddSheet_Filter_Brch(self,TotalBrch,Brch):
        print('Filter..')
        Filter_table = []
        for i in range(len(Brch)):
            self.Default = pd.DataFrame()
            for j in range(len(TotalBrch)):
                if((self.Filter_Brch(self.TotalBrch[j],Brch[i]))):    
                    Filter_table.append(self.TotalBrch[j])
                    self.Default = self.Default.append(self.main[(self.main["偵測器名稱"] == self.TotalBrch[j])])
                    self.Default.to_excel(self.writer,Brch[i],index =False)
        return Filter_table

    
    def ComparisonTable(self):
        self.another = []
        self.main = pd.read_excel(self.ExcelLocal,self.DelList)
        self.main.columns = self.main.iloc[6,:].tolist()#List main["偵測器名稱"]欄位
        self.main = self.main.drop( [i for i in range(len(self.main.iloc[:,2].tolist())) if(self.check_IP(str(self.main.iloc[:,2].tolist()[i])))])#移除空值,與配IP數值
        self.TotalBrch = list(set(self.main.iloc[:,0].tolist()))
        self.writer = pd.ExcelWriter('multiple.xlsx', engine='xlsxwriter')
        self.main.to_excel(self.writer,'全行',index=False)

        Fiter = self.AddSheet_Filter_Brch(self.TotalBrch,self.FilterBrch)
        Remain =list(set(self.TotalBrch) - set(Fiter))
        self.AddSheet_Filter_Brch(self.TotalBrch,Remain)
        self.writer.save()
        self.writer.close()
          

if __name__ == "__main__":
    AA = ExcelTableComparison(r'C:\Users\昱竹\Desktop\TrackerReport\DLP\DLP整合(New)20210903184352.xls', 0, '')
    AA.ComparisonTable()