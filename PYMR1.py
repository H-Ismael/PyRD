# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 23:20:46 2019

@author: *****
"""
from win32 import win32gui
import os 
import time
import smtplib
import sendAndrecv
import pyautoguii
    
    
    
while True :
    
    
    try :
        
        hwnd = win32gui.FindWindow(None,'Spyder (Python 3.6)')
        win32gui.SetForegroundWindow(hwnd)
        try:
            
            sendAndrecv.cmdreceiver('(FROM "*****")','(SUBJECT "****")') #Try using subject name for each communication channel / task cmd
        except Exception:
            pass
    
        #time.sleep(1)
        pyautoguii.saveipcnsl()
        #pyautoguii.sceenshot()
        
        execpath="C:/****/******/Desktop/Rfile/pyremote***/ExchangeFolder/ToReceive/"
        
        pyautoguii.sceenshot()
        
        fllpth=[]
        for root, dirs, files in os.walk(os.path.abspath(execpath)):
            for file in files:
                fullpathz =os.path.join(root, file) 
                fllpth.append(fullpathz)
                #print(fullpathz)
                
        #print(fllpth)
        
        for file in fllpth :
            
            if file.find('.py') != -1 :
                    print('py found')
                    print(file)
                    
                    try :
                        
                        exec(open(file).read()) #execute what ever .py you want. This my need some setting of the environnement. 
                    except Exception :
                        
                        print(' ERROR DETECTED while exec ')
                        #print(Exception)
                    
                    
                    
                    
            else:
                    
                    print(file)
                    f = open(file , 'r')
                    notpy = f.read()
                    f.close()
                    print(notpy)
                    
                    
        time.sleep(1)
        
        sendAndrecv.sendfct()
        
        
        
    except smtplib.SMTPServerDisconnected :
        print('lost wirelss')
    except Exception:
        pass
    
    time.sleep(600)
