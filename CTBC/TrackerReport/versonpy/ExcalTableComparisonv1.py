# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 15:40:49 2021

@author: 昱竹
"""



import pandas as pd
import re
class ExcelTableComparison:
    def __init__(self,ExcelLocal,DelList,TitleList):
            self.ExcelLocal = ExcelLocal
            self.DelList = DelList
            self.TitleList = TitleList
            
            
            

def check_IP(str):
	s = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
	str = s.search(str)
	return  not  bool(str)


def check_Brch_CD(str):
	s = re.compile(r'承德.*')
	str = s.search(str)
	return  bool(str)

def check_Brch_NK(str):
	s = re.compile(r'南港.*')
	str = s.search(str)
	return  bool(str)


main = pd.read_excel(r'C:\Users\昱竹\Desktop\TrackerReport\DLP\DLP整合(New)20210903184352.xls',0)
main.columns = main.iloc[6,:].tolist()#List main["偵測器名稱"]欄位
main = main.drop( [i for i in range(len(main.iloc[:,2].tolist())) if(check_IP(str(main.iloc[:,2].tolist()[i])))])#移除空值,與配IP數值





TotalBrch = list(set(main.iloc[:,0].tolist()))

another = []
NK = pd.DataFrame()
CD = pd.DataFrame()
writer = pd.ExcelWriter('multiple.xlsx', engine='xlsxwriter')
main.to_excel(writer,'全行',index=False)

#for i in range(len(TotalBrch)):
#    Expression_Comparison(TotalBrch[i],r'南港.*')

for i in range(len(TotalBrch)):
    if(check_Brch_NK(TotalBrch[i])):
        NK = NK.append(main[(main["偵測器名稱"] == TotalBrch[i])])
        NK.to_excel(writer,'南港',index =False)
    
    elif(check_Brch_CD(TotalBrch[i])):
        CD = CD.append(main[(main["偵測器名稱"] == TotalBrch[i])])
        CD.to_excel(writer,'承德',index =False)
    else:
        another.append(i)
        
    
for i in another:
    print(str(i)+'.'+str(TotalBrch[i]))
    main[(main["偵測器名稱"] ==  str(TotalBrch[i]))].to_excel(writer, TotalBrch[i],index=False)

writer.save()
writer.close()
      
