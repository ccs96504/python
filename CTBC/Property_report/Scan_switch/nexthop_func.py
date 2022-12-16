# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 15:53:48 2021

@author: Z00044060
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 10:13:48 2021

@author: Z00044060
"""
#C:\Users\z00044060\Desktop\è¨­å?åºè??¥è©¢?¢ç??¨\ç¶²è·¯è¨­å??æ¬åºè??°æ¯¯å¼æ???

import telnetlib
import time
import re
import xlsxwriter
import xlwings as xw


IP_content = []
IP_dir = []

##IP
f = open(r'D:\Property_report\Scan_switch\switch_ip.txt')
text_IP = []
for line in f:
    IP_ = re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])', line)
    text_IP.append(IP_)


for i in range(len(text_IP)):
    ip = (text_IP[i][0])
    print(ip)



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
worksheet.write('C1', 'åºè?', merge_format)
worksheet.write('D1', 'DESCR', merge_format)
worksheet.write('E1', 'PID', merge_format)


workbook.close()
        
####3    
#########

IP_content = []

command = 'show inventory'

telnet = telnetlib.Telnet('10.33.247.2')

#LOGS = telnet.set_debuglevel(1)

time.sleep(1)     
telnet.write((('tw03077208z00044060' + "\r\n" ).encode('ascii')))      #å¸³è?
time.sleep(0.5)  
telnet.write(('S4hu6dm1' + "\r\n" ).encode('ascii')) #å¯ç¢¼
time.sleep(0.5)  



wb = xw.Book('BRCH_VER.xls')
sheet = wb.sheets['Sheet1']  #?¸æ??¨å??ä?

        
SN_number= [] 
DESCR = []
PID = []
Hostname= []
value = 0
z = 0     
#context = []
for i in range(len(text_IP)):
    IP = text_IP[i][0]
    print('連線:'+text_IP[i][0])
    
    telnet.write((text_IP[i][0] + "\r\n" ).encode('ascii'))
    print('!!!!!!!!!!!!!!!!!!!!!!!!!')  
#    telnet.read_until(b"Username:",timeout=5)
    S =str(telnet.read_some())
    print(S)
    VALUE =S.find('Username')
              #  SN_number = re.findall(r'SN:.*?([A-Za-z_-][A-Za-z0-9_]*)', telreply)
    print(VALUE)
    
    print(telnet.read_very_eager())
    print('已加入ACS')
        
    time.sleep(1)     
    #telnet.write((('tw03077208z00044060' + "\r\n" ).encode('ascii')))   #å¸³è?
    time.sleep(1)  
    #telnet.write(('R4kj8xm2' + "\r\n" ).encode('ascii')) #å¯ç¢¼
    print('未加入ACS')
    telnet.write((('acs' + "\r\n" ).encode('ascii')))   #å¸³è?
    time.sleep(1)  
    token = 'netteam'
    telnet.write((token + "\r\n" ).encode('ascii'))          


    

    S = ''
    telnet.write(('ter len 0' + "\n" ).encode('ascii'))
    time.sleep(0.5)
    telnet.write((command + "\r\n" ).encode('ascii'))
    time.sleep(2)

    content = telnet.read_eager().decode()
    
    telnet.read_until(b'show inventory',timeout=30)
    telreply = telnet.expect([],timeout = 5)[2].decode('utf-8', 'ignore').strip()
    telreply = str(telreply)
    
    
    Hostname = (re.findall(r'(.*?)[.#>]', str(telreply)))
    print('連線主機:'+str(Hostname))
    try:
        if (str(Hostname[0]) == 'TW-TPE-NKA-9F-F8-OOB-2960X-1'):
            print('連線失敗!')
            SN_number = 'No Found'
            DESCR = 'No Found'
            PID ='No Found'
            Hostname = '連線失敗'
            z += 1
            value = z + 1
            sheet.range('A'+str(value)).value = Hostname
            sheet.range('B'+str(value)).value = IP
            sheet.range('C'+str(value)).value = SN_number
            sheet.range('D'+str(value)).value = DESCR
            sheet.range('E'+str(value)).value = PID
            wb.save()
                    
    
    
        elif (str(Hostname[0]) != 'TW-TPE-NKA-9F-F8-OOB-2960X-1'):
            
            print(Hostname[0]+'連線成功!')
            SN_number = re.findall(r'SN:.*?([A-Za-z_-][A-Za-z0-9_]*)', telreply)
            DESCR = (re.findall(r'DESCR:.*?([A-Za-z_-][A-Za-z0-9_. -]*)', telreply))
            PID = (re.findall(r'PID:.*?([A-Za-z0-9_. -]*)', telreply))
            Hostname = (re.findall(r'(.*?)[#>]', telreply))
            
            print(SN_number)
            print(DESCR)
            print(PID)
            print(Hostname)
            for j in range(len(SN_number)):     
                z += 1
                value = z + 1
                sheet.range('A'+str(value)).value = Hostname[0]
                print(str(value) , 'i='+str(IP) , 'j='+str(j))
                sheet.range('B'+str(value)).value = IP
                sheet.range('C'+str(value)).value = str((SN_number[j]))
                sheet.range('D'+str(value)).value = str((DESCR[j]))
                sheet.range('E'+str(value)).value = str((PID[j]))
                wb.save()
            telnet.write(('exit' + "\r\n" ).encode('ascii')) #å¯ç¢¼
            time.sleep(0.5)  
            content = telnet.read_eager().decode()
    except:
        if (str(Hostname) == '[]'):
            print('連線失敗!')
            SN_number = 'No Found'
            DESCR = 'No Found'
            PID ='No Found'
            Hostname = '連線失敗'
            z += 1
            value = z + 1
            sheet.range('A'+str(value)).value = Hostname
            sheet.range('B'+str(value)).value = IP
            sheet.range('C'+str(value)).value = SN_number
            sheet.range('D'+str(value)).value = DESCR
            sheet.range('E'+str(value)).value = PID
            wb.save()

wb.save()

#?¢é?
telnet.write(('exit' + "\r\n" ).encode('ascii')) #å¯ç¢¼
time.sleep(0.5)  
content = telnet.read_eager().decode()

'''




    

