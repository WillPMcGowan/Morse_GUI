from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO 
import time
import morse_code as mc
RPi.GPIO.setmode(RPi.GPIO .BCM)

## hardware settings
led = LED(14)

## tk and GUI setting
win = Tk()
win.title("Morse Code Blinker")
gui_font = tkinter.font.Font(family = "Arial", size = 12, weight = "bold")

# GUI layout
left_frame = Frame(win)
right_frame = Frame(win)
mid_frame = Frame(win)
left_frame.pack(side = LEFT)
right_frame.pack(side = RIGHT)
mid_frame.pack(side = RIGHT)

# assign variable to capture button variables
word = tkinter.StringVar()
# set to nothing first to make radio buttons look active

## Morse Code definitions
dih = .2
dah = .5
morse_break = .2
letter_break = 1
word_break = 2
## Morse code functions

# Blink each morse code symbol
def blink(morse):
    if morse == ".":
        led.on()
        time.sleep(dih)
        led.off()
        time.sleep(morse_break)
    elif morse == "-":
        led.on()
        time.sleep(dah)
        led.off()
        time.sleep(morse_break)
    else:
        print("Invalid character")
        
def blink_letter():
    word_getter = word.get().lower()
    if len(word_getter) > 12:
        print("Word too long!")
        return
    for letter in word_getter:
        for key, values in mc.letters.items():
            if key == letter:
                print("letter:", key, "| Morse code:", values)             
                for morse_code in values:
                    blink(morse_code)
                    
# Function to cleanly close the GUI
def close():
    RPi.GPIO.cleanup()
    win.destroy()

# Set up labels
label = Label(left_frame)
label.pack()
label.config(text = "Enter word ")

### BUTTONS ###

#RED RADIO BUTTON

ledButton = Button(win, text='Convert to morse code', font=gui_font, command=blink_letter, bg='bisque2', height=1)
ledButton.pack()

word = Entry(win, font=gui_font, width=19)
word.pack()

# EXIT BUTTON
exit_button = Button(win, text = "X", font = gui_font, command = close, bg = 'red', height = 1, width = 2)
exit_button.pack(side = RIGHT)

win.protocol("WM_DELETE_WINDOW", close) # attatch to close function and exit cleanly

win.mainloop() # keep GUI running 
