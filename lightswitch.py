import tkinter as tk
from typing import Text
window = tk.Tk()

button = tk.Button(text='...', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schrijf hier tussen je code
button.config(text='switch light on')
window['bg'] = 'black'

def clickButton(event):
    if button.config('text')[-1] == 'switch light on':
        button.config(text='switch light off')
        window['bg'] = 'yellow'
        print ("the light is on")
    else:
        button.config(text='switch light on')
        print ("the light is off")
        window['bg'] = 'black'

button.bind("<Button-1>", clickButton)
# schrijf hier tussen je code
window.mainloop()