# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 15:51:02 2021

@author: Z00044060
"""

from tkinter import filedialog
import os


class App:
    def __init__(self,local):
            self.__local = local

    def Application(self):
        try:
            root = filedialog.Tk('比對程式')
            default_dir = self.__local
            major = filedialog.askopenfilename(title=u"選擇主要文件", initialdir=(os.path.expanduser(default_dir)))
            root.destroy()
            return major
        except:
            root.destroy()
            

#函式庫用法:

if __name__ == "__main__":
    value = App(r'D:\\')
    excel = value.Application()
    value1 = App(excel)
    excel2 = value1.Application()