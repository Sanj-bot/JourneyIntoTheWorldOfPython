from tkinter import *
root=Tk()
root.title('My Box GUI')
root.iconbitmap('apple.ico')
my_label=Label(root,text="Hi")
my_label2=Label(root,text="How you doing today?")

my_label.pack()
my_label2.pack()