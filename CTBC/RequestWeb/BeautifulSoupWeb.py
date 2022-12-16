# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 13:25:50 2021

@author: Z00044060
"""

from bs4 import BeautifulSoup
import re

class BeautifulSoupWeb :
    def __init__(self):
        self.fp = open("log.txt", "w")
    
    #RQlist_Page = driver.page_source
    
    def Find_RQ_List(self,RQlist_Page):
        RQ_ID = []
        RQlist_bs = BeautifulSoup(RQlist_Page, 'html.parser')
        RQlist_id = RQlist_bs.find_all('a')
        RQlist_Page_text = [tag.get_text() for tag in RQlist_id]
        parttern = re.compile(r'\d{10}')
        for i in range(len(RQlist_Page_text)):
            RQ_ID.extend(re.findall(parttern,RQlist_Page_text[i]))
        print(RQ_ID)
        return RQ_ID
    
    def Find_Page_List(self,RQlist_Page):
        RQlist_bs = BeautifulSoup(RQlist_Page, 'html.parser')
        Firsr_Page = RQlist_bs.find_all('span',id="ctl00_ContentPlaceHolder1_RqPageSize")
        Firsr_Page = [(tag.get_text()) for tag in Firsr_Page]
        End_Page = RQlist_bs.find_all('span',id="ctl00_ContentPlaceHolder1_RqTotalPage")
        End_Page = [(tag.get_text()) for tag in End_Page]
        print('第'+Firsr_Page[0]+'頁/'+'共'+End_Page[0]+'頁')
        return Firsr_Page,End_Page
    def Page_Detail(self,Log_Page):
        
        Log_bs = BeautifulSoup(Log_Page, 'html.parser')
        RQ_Number = [tag.get_text() for tag in Log_bs.find_all('span' , id="ctl00_ContentPlaceHolder1_PubRqUserInfo1_lblRequestNumber")][0]
        RQ_Unit = [tag.get_text() for tag in Log_bs.find_all('span' , id="ctl00_ContentPlaceHolder1_PubRqUserInfo1_lblApplicantUnit")][0]
        QR_Staffmember = [tag.get_text() for tag in Log_bs.find_all('span' , id="ctl00_ContentPlaceHolder1_PubRqUserInfo1_lblApplicantID")][0]
        RQ_name = Log_bs.find('input', id="ctl00_ContentPlaceHolder1_PubRqUserInfo1_txtApplicant")["value"]
        RQ_content = [tag.get_text() for tag in Log_bs.find_all('textarea', id="ctl00_ContentPlaceHolder1_txtRequestContent")][0]
        dateline = Log_bs.find('input', id="ctl00_ContentPlaceHolder1_txtScheduleCompletedDate")["value"]
        annex = Log_bs.find('table', id="ctl00_ContentPlaceHolder1_GridViewAttachmentList")
        self.fp.write('###############################\n')
        self.fp.write('需求單編號:'+RQ_Number+'\n')
        self.fp.write('申請人單位:'+RQ_Unit+'\n')
        self.fp.write('申請人員編:'+QR_Staffmember+'\n')
        self.fp.write('申請人:'+RQ_name+'\n')
        self.fp.write('需求內容：:'+RQ_content+'\n')
        self.fp.write('預計完成:'+dateline+'\n')  
        print('需求單編號:'+RQ_Number+'\n')
        print('申請人單位:'+RQ_Unit+'\n')
        print('申請人員編:'+QR_Staffmember+'\n')
        print('申請人:'+RQ_name+'\n')
        print('需求內容：:'+RQ_content+'\n')
        print('預計完成:'+dateline+'\n')
        
        
        return [RQ_Number,RQ_Unit,QR_Staffmember,RQ_name,RQ_content,dateline,annex]

    def Find_Address(self,Address_Page):
        print('Find_UserAddress..')
        
        AddressList_bs = BeautifulSoup(Address_Page, 'html.parser')
        AddressList = [tag.get_text() for tag in AddressList_bs.find_all('td')]
        
        self.fp.write('####總務系統表單####\n')  
        for i in range(len(AddressList)):
            print(str(i)+'.'+str(AddressList[i]))
            self.fp.write(str(i)+'.'+str(AddressList[i])+'\n')  
        self.fp.write('####################\n')  
        return AddressList
    

    def Log_close(self):
        self.fp.write('###############################\n')
        self.fp.close()   