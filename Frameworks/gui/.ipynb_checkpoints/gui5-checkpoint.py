#displaying images using label python
from tkinter import *
from PIL import Image, ImageTk

mahmudul_root=Tk()
mahmudul_root.geometry("455x244")
image=Image.open("images\one.jpg")
photo=ImageTk.PhotoImage(image)
mahmudul_root.mainloop()