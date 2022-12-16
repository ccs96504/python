# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 17:07:06 2021

@author: 昱竹
"""


from bs4 import BeautifulSoup
import re

class BeautifulSoupWeb :
    def __init__(self):
        self.fp = open("log.txt", "w")
    
    #RQlist_Page = driver.page_source
    
    def Find_Application_number(self,Application_number_Page):
        

        Application_number = []
        Application_number_bs = BeautifulSoup(Application_number_Page, 'html.parser')
        Application_number_id = Application_number_bs.find_all('a')
        Application_number_text = [tag.get_text() for tag in Application_number_id]
        parttern = re.compile(r'[a-zA-Z0-9]+')
        for i in range(len(Application_number_text)):
            Application_number.extend(re.findall(parttern,Application_number_text[i]))
     #   "//*[@id="ctl00_ContentPlaceHolder1_GridViewPendingList"]/tbody/tr[2]/td[1]/a"

        return Application_number
    
    def Envelope_Reason(self,Envelope_Reason_Page):
        Reason = [tag.get('value') for tag in BeautifulSoup(Envelope_Reason_Page, 'html.parser').find_all('input',id="ctl00_ContentPlaceHolder1_txtAccessReason") ][0]
        return Reason
    
    