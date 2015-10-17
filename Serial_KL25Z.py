# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 20:08:29 2015

Seria data Read from KL25Z board

@author: maursilv
"""
import serial as serial
import time
from collections import deque



KL25Z = serial.Serial('COM10',115200,timeout=.1)    #Define os parametros da porta serial
time.sleep(1)

def SerialData():       
    while True:             
        data = KL25Z.readline()                     #Efetua a Leitura 
        if data:
            value = Ringbuffer(data)
            return value
            

def Ringbuffer(data):                               #Buffer Circular para armazenamento dos dados seriais
    d = deque('',1024)
    d.append(data)
    value = []
    if d.maxlen:
        datapop = d.pop()
        datapop = datapop.strip(';')
        datapop = datapop.strip('')
        datapop = datapop.strip('\n')
        datapop_l = datapop.split(';')
        value.append(float(datapop_l[0]))
        value.append(float(datapop_l[1]))
        value.append(float(datapop_l[2]))
    return value

