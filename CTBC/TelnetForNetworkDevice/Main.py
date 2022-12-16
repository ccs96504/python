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

import TelnetlibForDevice  
import ExcelLog 
import pandas as pd
import re 
import Log_info

Device_List = []
Device_List = ExcelLog.txt_Location('NetworkDevice.txt')


df = pd.DataFrame( columns = ['IP','Hostname','SN序號','PID','DESCR','ACS狀態'])
value = 0
z = 0    
 
for i in range(len(Device_List)):
    Log = TelnetlibForDevice.Next_Hop('tw03077208z00044060','C1fg3ju8',Device_List[i],'show inventory')
    #產出Log資訊檔
    Log_info.mkdir('Log',Log[0],Device_List[i])
    
    
    if(Log[0]=='Fail'):
        print('Fail')
        
        SN_number = ['']
        DESCR = ['']
        PID = ['']
        Hostname = ['']
        ACS = Log[1]
        
    else:
        
        SN_number = re.findall(r'SN:.*?([A-Za-z_-][A-Za-z0-9_]*)', Log[0])
        DESCR = (re.findall(r'DESCR:.*?([A-Za-z_.-][A-Za-z0-9_. -]*)', Log[0]))
        PID = (re.findall(r'PID:.*?([A-Za-z0-9_. -]*)', Log[0]))
        Hostname = (re.findall(r'(.*?)[#>]', Log[0]))
        ACS = Log[1]
    
    
    for j in range(len(SN_number)): 
        z += 1 #雙迴圈總數
        df.loc[z]= [Device_List[i],Hostname[j],SN_number[j],PID[j],DESCR[j],ACS]
    df.to_excel('Network_Device.xlsx'  , index=False )
    
