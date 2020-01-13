# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 19:01:11 2019

@author: xxx
"""
import time 
import pyautogui


pyautogui.useImageNotFoundException


print(pyautogui.size())

def sceenshot():
    
    timestr = time.strftime("%Y%m%d-%H%M%S")
    
    shotpath = 'C:/******/******/Desktop/*****/**pyyremote***/ExchangeFolder/ToSend/screen'+timestr+'.png'
    pyautogui.screenshot(shotpath)
    
    
def saveipcnsl():
    
    pnjicone = 'C:/*******/******/Desktop/*****/**pyyremote***/ExchangeFolder/IPCONSOLpng.png'
    #decalage = pyautogui.Point(x+0 , 20)
    x, y = pyautogui.locateCenterOnScreen(pnjicone)
    #coorddecal = coordIn #+ decalage
    
    #print(y)
    pyautogui.click((x, y - 40), button = 'left', duration = 0.0)
    
    pyautogui.hotkey('ctrl', 's')
    time.sleep(2)
    
    searchbar = 'C:/*******/******/Desktop/*****/**pyyremote***/ExchangeFolder/barsearchpng.png'
    
    coordsearchbar = pyautogui.locateCenterOnScreen(searchbar)
    pyautogui.click(coordsearchbar,button='left')
    time.sleep(0.5)
    strtype1 = 'C:/*******/******/Desktop/*****/**pyyremote***/ExchangeFolder/'
    pyautogui.typewrite(strtype1)
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    
    savebutton = 'C:/*******/******/Desktop/*****/**pyyremote***/ExchangeFolder/savepng.png'
    coordsavebutton = pyautogui.locateCenterOnScreen(savebutton)
    pyautogui.click(coordsavebutton,button='left')
    pyautogui.press('left')
    pyautogui.hotkey('enter')
    
#saveipcnsl()

#saveipcnsl()

#pyautogui.moveTo(x, y, duration=scd)
