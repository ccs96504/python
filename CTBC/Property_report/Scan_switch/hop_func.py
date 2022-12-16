# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 16:04:05 2021

@author: Z00044060
"""


import telnetlib
import time
import re

from pandas.core.frame import DataFrame

def telnet_IP(IP,account,password):
    try:
        command = 'show inventory'
        telnet = telnetlib.Telnet(IP)
        time.sleep(1)     
        telnet.write(((account + "\r\n" ).encode('ascii')))      #å¸³è?
        time.sleep(0.5)  
        telnet.write((password + "\r\n" ).encode('ascii')) #å¯ç¢¼
        time.sleep(0.5)  
        telnet.write(('ter len 0' + "\n" ).encode('ascii'))
        time.sleep(0.5)
        telnet.write((command + "\r\n" ).encode('ascii'))
        time.sleep(2)
        content = telnet.read_eager().decode()
        telnet.read_until(b'show inventory',timeout=30)
        telreply = telnet.expect([],timeout = 5)[2].decode('utf-8', 'ignore').strip()
        telreply = str(telreply)
        Hostname = (re.findall(r'(.*?)[.#>]', str(telreply))[0])   
        SN_number = re.findall(r'SN:.*?([A-Za-z_-][A-Za-z0-9_]*)', telreply)
     #   DESCR = (re.findall(r'DESCR:.*?([A-Za-z_-][A-Za-z0-9_. -]*)', telreply))
        PID = (re.findall(r'PID:.*?([A-Za-z0-9_. -]*)', telreply))
        telnet.write(('exit' + "\r\n" ).encode('ascii'))
        time.sleep(0.5)  
        content = telnet.read_eager().decode()
        
        data_SW = {"Hostname":Hostname,
                   "IP":IP,
                   "PID":PID,
                   "SN_number":SN_number,
     #              "DESCR":DESCR
                   }
        print(data_SW)
    except:
         
        data_SW = {"Hostname":"NoFound",
                   "IP":IP,
                   "PID":["NoFound"],
                   "SN_number":["NoFound"],
     #              "DESCR":["NoFound"]
                   }
        print(data_SW)
    switch_date = DataFrame(data_SW)
    #print(switch_date)
    return switch_date
'''

command = 'show inventory'
telnet = telnetlib.Telnet('10.248.240.73')
time.sleep(1)     
telnet.write((("tw03077208z00044060" + "\r\n" ).encode('ascii')))      #å¸³è?
time.sleep(0.5)  
telnet.write(("P1tk2mh9" + "\r\n" ).encode('ascii')) #å¯ç¢¼
time.sleep(0.5)  
telnet.write(('ter len 0' + "\n" ).encode('ascii'))
time.sleep(0.5)
telnet.write((command + "\r\n" ).encode('ascii'))
time.sleep(2)
content = telnet.read_eager().decode()
telnet.read_until(b'show inventory',timeout=30)
telreply = telnet.expect([],timeout = 5)[2].decode('utf-8', 'ignore').strip()
telreply = str(telreply)
Hostname = (re.findall(r'(.*?)[.#>]', str(telreply))[0])   
SN_number = re.findall(r'SN:.*?([A-Za-z_-][A-Za-z0-9_]*)', telreply)
DESCR = (re.findall(r'DESCR:.*?([A-Za-z_-][A-Za-z0-9_. -]*)', telreply))
PID = (re.findall(r'PID:.*?([A-Za-z0-9_. -]*)', telreply))
telnet.write(('exit' + "\r\n" ).encode('ascii'))
time.sleep(0.5)  
content = telnet.read_eager().decode()
data_SW = {"Hostname":Hostname,
           "IP":'10.248.240.73',
           "PID":PID,
           "SN_number":SN_number,
     #             "DESCR":DESCR
     }
print(data_SW)

'''