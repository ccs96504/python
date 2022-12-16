# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 11:43:26 2021

@author: Z00044060
"""


import re




def File(filepath):

    ###開起所有IP的資料夾#####
    f = open(filepath , encoding="utf-8")
    text = []
    for line in f:
        line.replace(" ","")
        text.append(line)
    
    ALL_IP = []
    partten = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
    for i in text:
        ALL_IP.extend(re.findall(partten, i))
        
    return ALL_IP
