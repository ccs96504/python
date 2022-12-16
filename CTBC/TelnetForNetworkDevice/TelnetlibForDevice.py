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

import telnetlib 


IP_content = []
command = 'show inventory'

AA = '123'
AA = AA.encode()
print(AA)

def Next_Hop(Acs_Account, Acs_Password, IP,Command,):
    #####
    IP = IP.encode()
    Command = str(Command+'\r\n').encode()
    Acs_Account = str(Acs_Account+'\r\n').encode()
    Acs_Password = str(Acs_Password+'\r\n').encode()

    ####

    telnet = telnetlib.Telnet('10.33.247.2',timeout=5)
    telnet.set_debuglevel(1)
    #跳板
    telnet.read_until(b'Username',timeout=3)
    telnet.write(Acs_Account)
    telnet.write(Acs_Password)
    status = True
    
    
    while(status):
            
        ##ACS帳號登入成功:
        try:
            telnet.open(IP,timeout=10)
            telnet.read_until(b'Username',timeout=3)
            
            telnet.write(Acs_Account)
            telnet.write(Acs_Password)
            
            telnet.write(b'ter len 0\r\n')
            telnet.write(Command)
            telreply = telnet.expect([],timeout = 5)[2].decode('utf-8', 'ignore').strip()
            if 'failed' in telreply:
                status = True
            else:
                return telreply,'ACS OK'
                status = False
                break
                telnet.close()
        except:
            status = True
            print("Time out!")
        
        ##Netteam帳號登入成功:
        try:
            
            telnet.open(IP,timeout=10)
            telnet.read_until(b'Username',timeout=3)
            
            telnet.write(b'acs\r\n')
            telnet.write(b'netteam\r\n')
            telnet.write(b'en\r\n')
            telnet.write(b'netteam\r\n')  
            
            telnet.write(b'ter len 0\r\n')
            telnet.write(Command)
            telreply = telnet.expect([],timeout = 5)[2].decode('utf-8', 'ignore').strip()
            if 'failed' in telreply:
                status = True
            else:
                return telreply,'netteam OK'
                status = False
                break
                telnet.close()
        except:
             status = True
             print("Time out!")
        ##無帳號登入成功:
        try:
            telnet.open(IP,timeout=10)
            telnet.read_until(b'Username',timeout=3)
            telnet.write(b'netteam\r\n')
            
            telnet.write(b'ter len 0\r\n')
            telnet.write(Command)
            telreply = telnet.expect([],timeout = 5)[2].decode('utf-8', 'ignore').strip()
            if 'failed' in telreply:
                status = True
            else:
                return telreply,'No user'
                status = False
                break
                telnet.close()
        except:
             status = True
             print("Time out!")

        if(status == True):
            print('connent Fail to'+str(IP))
            Fail_Log= 'Fail'
            return Fail_Log,'Fail'
        

