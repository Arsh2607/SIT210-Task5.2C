from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)

## pinmode setup

led_r = LED(15)
led_g = LED(18)
led_y = LED(23)

## GUI DEF

win = Tk() ## create tk window
win.title("Task 5.2C")
mfont = tkinter.font.Font(family = 'Helvetica',size = 12,weight ="bold")

## Functions

def led_r_toggle():
    if led_r.is_lit:
        led_r.off()
        led_r_button["text"] = "RED"
    else:
        led_r.on()
        led_g.off()
        led_y.off()
        
        led_r_button["text"] = "RED_ON"
        led_g_button["text"] = "GREEN"
        led_y_button["text"] = "YELLOW"


def led_g_toggle():
    if led_g.is_lit:
        led_g.off()
        led_g_button["text"] = "GREEN"
    else:
        led_g.on()
        led_y.off()
        led_r.off()
        led_r_button["text"] = "RED"
        led_g_button["text"] = "GREEN_ON"
        led_y_button["text"] = "YELLOW"


def led_y_toggle():
    if led_y.is_lit:
        led_y.off()
        led_y_button["text"] = "YELLOW"
    else:
        led_y.on()
        led_r.off()
        led_g.off()
        led_r_button["text"] = "RED"
        led_g_button["text"] = "GREEN"
        led_y_button["text"] = "YELLOW_ON"


def exit_toggle():
    RPi.GPIO.cleanup()
    win.destroy()
    
## Buttons

led_r_button = Button(win,text = 'RED' ,font = mfont,command = led_r_toggle,bg = 'red',height = 1,width = 24)
led_r_button.grid(row = 0,column =1)

led_g_button = Button(win,text = 'GREEN' ,font = mfont,command = led_g_toggle,bg = 'green',height = 1,width = 24)
led_g_button.grid(row = 1,column =1)

led_y_button = Button(win,text = 'YELLOW' ,font = mfont,command = led_y_toggle,bg = 'yellow',height = 1,width = 24)
led_y_button.grid(row = 2,column =1)

exit_button = Button(win,text = 'EXIT' ,font = mfont,command = exit_toggle,bg = 'bisque2',height = 1,width = 24)
exit_button.grid(row = 3,column =1)

win.mainloop()



