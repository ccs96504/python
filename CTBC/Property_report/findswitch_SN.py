# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 16:08:52 2021

@author: Z00044060
"""

import time
import datetime
from Scan_switch import hop_func
import re

start = time.time()
today=datetime.date.today()
today = today.strftime('%Y-%m-%d')


f = open(r'D:\Property_report\Scan_switch\switch_ip-.txt')
text_IP = []
for line in f:
    IP_ = re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])', line)
    text_IP.append(IP_[0])
BBB = {}
CCC = {}
for i in range(len(text_IP)):
    if i == 0:
        AAA = hop_func.telnet_IP(text_IP[i],'tw03077208z00044060','P1tk2mh9')
        BBB= AAA.copy()
    elif i>=1:
        AAA = hop_func.telnet_IP(text_IP[i],'tw03077208z00044060','P1tk2mh9')
        CCC= AAA.copy()
        BBB.update(CCC)
#print(BBB)

BBB.to_excel('foundSN_'+str(today)+'.xlsx')