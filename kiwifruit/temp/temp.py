#!/usr/bin/env python
# -*- coding:utf-8 -*- 

'''
Created on 2019年8月19日
@author: Max Wu
'''
import tushare as ts
import logging

class Temp(object):
    def __init__(self):
        self.name = 'Hello World'
    
    def testOne(self):
        logging.warn(self.name)

    def testTwo(self):
        df = ts.get_realtime_quotes('000581') #Single stock symbol
        logging.warn(df)
