from tkinter import *

#window Creation / code inbetween window and window.mainloop() will apear on screen
window = Tk()
window.geometry("420x420") #Arguements placed in strings
window.title("Jamm's Calculator")
window_icon = PhotoImage(file="icon.png") #Loads image, cannot be a JPG file
window.iconphoto(True, window_icon)
window.config(background="#808080") #config is multi-functional used to make changes such as background color.

#Makes window visible
window.mainloop()