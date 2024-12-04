from tkinter import *
window=Tk()
window.title("Event handler")
window.geometry("400x400")

def key_press(event):
    print(event.char)

window.bind("<Key>",key_press)

def click_me(event):
    print("\nThe button was clicked")

button=Button(master=window,text="Press me")
button.pack()
window.bind("<Button-1>",click_me)
window.mainloop()