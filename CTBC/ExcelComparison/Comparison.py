# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 17:19:21 2021

@author: 昱竹
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 10:54:29 2021

@author: 昱竹
"""




import pandas as pd

class Comparison:
  
    def __init__(self,Minor_Comparison,Minor_EXCEL,Main_Local,Main_sheet,Main_EXCEL_TABLE):
            self.Minor_Comparison = Minor_Comparison
            self.Minor_EXCEL = Minor_EXCEL
            self.Main_Local= Main_Local
            self.sheet= Main_sheet
            self.EXCEL_TABLE =Main_EXCEL_TABLE
          #  print(str(self.Minor_Comparison)+' '+str(self.Minor_EXCEL)+' '+str(self.Main_Local)+' '+str(self.sheet)+' '+str(self.EXCEL_TABLE))



    def type_color(self,val): 
        for i in range(len(self.Minor_Comparison)):
            if str(val) == str(self.Minor_Comparison[i]) :
                color = 'green'
                break
            else:
                color='red'
        return f'background-color: {color}'

    def ShowSameThing(self):
        main = pd.read_excel(self.Main_Local,self.sheet)
        index = main.columns.tolist()
        NEW_DFSTYLE = main.style.applymap(self.type_color, subset=pd.IndexSlice[:,[index[self.EXCEL_TABLE]]])       
        NEW_DFSTYLE.to_excel(self.Main_Local,index=False)
        print('ShowSameThing OK')

    def InputValueinsamething(self):
        #複製欄位
        main = pd.read_excel(self.Main_Local,self.sheet)
        val = main[main.columns.tolist()[self.EXCEL_TABLE]].values.tolist()
        NEW_DFSTYLE = main.style.applymap(self.type_color, subset=pd.IndexSlice[:,[main.columns.tolist()[self.EXCEL_TABLE]]])       
        main['貼上'] = ''
        index = (self.Minor_EXCEL.columns.tolist())
        print('====複製貼上功能=====')
        for i in range(len(index)):
            print(str(i)+'.'+str(index[i]))
        EXCEL_TABLE = int(input('複製EXCEL_TABLE欄位:'))
        #Comparison_List = self.Minor_EXCEL[index[EXCEL_TABLE]].tolist()
        
       # print(val)
        print(str(self.Minor_Comparison) )
        for i in range(len(self.Minor_Comparison)):
            for j in range(len(val)):
                if str(val[j]) == str(self.Minor_Comparison[i]) :
                    
                    main.iloc[j,(len(main.columns.tolist())-1)] = self.Minor_EXCEL.iloc[i,EXCEL_TABLE]
                    print(main.iloc[j,(len(main.columns.tolist())-1)])
                    break

     
        NEW_DFSTYLE = main.style.applymap(self.type_color, subset=pd.IndexSlice[:,[main.columns.tolist()[self.EXCEL_TABLE]]])       
        NEW_DFSTYLE.to_excel(self.Main_Local,index=False)
        


#函式庫用法:


#if __name__ == "__main__":
#    test = pd.read_excel('D:\ctbc\外據點財產申請v2.xlsx',0)
#    value = Comparison(['10407945','10408083','234'],test,'D:\ctbc\外據點財產申請v1.xlsx',0,4)
#    value.ShowSameThing()
#    value.InputValueinsamething()





