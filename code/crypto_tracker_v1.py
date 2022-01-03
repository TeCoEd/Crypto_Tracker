#cryptodisplay
#!/usr/bin/env python

import signal
import dothat.backlight as backlight
import dothat.lcd as lcd
import dothat.touch as nav

import requests
import datetime
from time import sleep
import math

# hue colour background for search
def rainbow():
    lcd.clear()
    lcd.set_cursor_position(2, 1)
    lcd.write("SEARCHING...") 

    x = 0
    rest = 275
    
    while rest > 0:
        x += 1

        backlight.sweep((x % 360) / 360.0)
        sleep(0.01)
        rest = rest - 1

backlight.rgb(255, 255, 255)
backlight.graph_off()

# stores the current and past value of crypto
global old_BTC 
global old_ETH 
old_BTC = (0)
old_ETH = float(0)

print ("Running")
#FIND CURRENT TIME
current_time = datetime.datetime.now()
date = current_time.strftime("%d-%m-%Y %H:%M")

# This needs to become a fucntion
lcd.set_cursor_position(3, 0)
lcd.write("WELCOME TO") #new line
lcd.set_cursor_position(1, 1)
lcd.write("CRYPTO TRACKER") #new line
lcd.set_cursor_position(0, 2)  #display the date
lcd.write(date)

#display the BTC value on the touch of the left button
@nav.on(nav.LEFT)
def handle_left(ch, evt):
    global old_BTC 
    lcd.clear()

    rainbow() #play the searching hue animation

    #FIND CURRENT TIME
    current_time = datetime.datetime.now()
    date = current_time.strftime("%d-%m-%Y %H:%M")

    ########################### BTC data and calculations ##############
    #FIND CURRENT BTC VALUE
    try:
        response_BTC = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    except:
        lcd.clear()
        backlight.rgb(255, 255, 255)
        print ("busy")
        lcd.set_cursor_position(0, 1)
        lcd.write("Error, please restart program", )
       
        
    current_BTC = response_BTC.json()
    current_BTC_value = (current_BTC["bpi"]["GBP"]["rate"])
    
    # Convert BTC value to an int so that it can be compared
    current_BTC_value = current_BTC_value.replace(",", "")
    ''' print (current_BTC_value)'''
    # Truncate the value
    current_BTC_value = math.trunc(float(current_BTC_value))
    # Convert to int for comparision
    current_BTC_value = int(current_BTC_value)

    lcd.clear()
  
    # Display BTC value on screen
    lcd.set_cursor_position(0, 0)
    lcd.write("BTC Value:", )
    lcd.set_cursor_position(0, 1) 
    lcd.write("GBP")
    lcd.set_cursor_position(4, 1)
    lcd.write(str(current_BTC_value))
    lcd.set_cursor_position(0, 2)
    lcd.write(date)

    increase_BTC = int(current_BTC_value) - int(old_BTC) #  FIND £ CHANGE

    # COMPARE THE NEW VALUES BTC
    if current_BTC_value > old_BTC:
        backlight.rgb(0, 255, 0)
        # DISPLAY THE INCREASE
               
        if increase_BTC > 0:
            print (increase_BTC)
            lcd.set_cursor_position(10, 1)
            lcd.write("+" + str(increase_BTC))
        else:
            pass
            
    elif current_BTC_value < old_BTC:
        backlight.rgb(255, 0, 0)
        print (current_BTC_value - old_BTC)
        if increase_BTC < 0:
            print (increase_BTC)
            lcd.set_cursor_position(10, 1)
            lcd.write("-" + str(increase_BTC))    
        else:
            pass
    else:
        pass
        backlight.rgb(255, 165, 0)
        print (current_BTC_value - old_BTC)

    # SAVE OLD VALUE TO COMPARE PRICE CHANGE
    old_BTC = (current_BTC_value)

@nav.on(nav.RIGHT)
def handle_right(ch, evt):
    global old_ETH 
    lcd.clear()

    rainbow() #searching animation

    #FIND CURRENT TIME
    current_time = datetime.datetime.now()
    date = current_time.strftime("%d-%m-%Y %H:%M")
    
    #FIND CURRENT ETH VALUE
    try:
        response_ETH = requests.get('https://api.coinbase.com/v2/prices/ETH-GBP/spot')
    except:
        lcd.clear()
        backlight.rgb(255, 255, 255)
        print ("busy")
        lcd.set_cursor_position(0, 1)
        lcd.write("Error, please restart program", )  
        
    current_ETH = response_ETH.json()
    current_ETH_value = float(current_ETH["data"]["amount"])

    lcd.clear()
    
    # Display ETH value on screen
    lcd.set_cursor_position(0, 0)
    lcd.write("ETH Value (GBP):", )
    #cd.set_cursor_position(0, 1) 
    #lcd.write('@')
    lcd.set_cursor_position(0, 1)
    lcd.write(str(current_ETH_value))
    lcd.set_cursor_position(0, 2)
    lcd.write(date)

    increase_ETH = int(current_ETH_value) - int(old_ETH)

    # COMPARE THE NEW VALUES ETH
    if current_ETH_value > old_ETH:
        backlight.rgb(0, 255, 0)

       # DISPLAY THE INCREASE
        if increase_ETH > 0:
            print (increase_ETH)
            lcd.set_cursor_position(9, 1)
            lcd.write("+" + str(increase_ETH))
        else:
            pass     
        
    elif current_ETH_value < old_ETH:
        backlight.rgb(255, 0, 0)
        if increase_ETH < 0:
            print (increase_ETH)
            lcd.set_cursor_position(9, 1)
            lcd.write("-" + str(increase_ETH))
        else:
            pass 
    else:
        pass
        backlight.rgb(255, 165, 0)

    # SAVE OLD VALUE TO COMPARE PRICE CHANGE
    old_ETH = (current_ETH_value)    
  
@nav.on(nav.BUTTON)
def handle_button(ch, evt):
    lcd.clear()

    #FIND CURRENT TIME
    current_time = datetime.datetime.now()
    date = current_time.strftime("%d-%m-%Y %H:%M")

    backlight.rgb(255, 255, 255)
    lcd.set_cursor_position(3, 0)
    lcd.write("WELCOME TO") #new line
    lcd.set_cursor_position(1, 1)
    lcd.write("CRYPTO TRACKER") #new line
    lcd.set_cursor_position(0, 2)  #display the date
    lcd.write(date)

## add litecoin
response_LTC = requests.get('https://api.coinbase.com/v2/prices/LTC-GBP')
print (response_LTC)


    
    
    



