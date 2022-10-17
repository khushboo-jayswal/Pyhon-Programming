from tkinter import *
from PIL import Image, ImageTk
class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fil=BOTH, expand=1)
        load = Image.open("RainPanda.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

root = Tk()
app = Window(root)
root.wm_title("Tkinter window")
root.geometry("200x120")
root.mainloop()