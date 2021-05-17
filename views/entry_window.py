'''
import tkinter
from tkinter import ttk, messagebox
from tkinter.ttk import Combobox

# from models import Row, Column, Region, Cell
from .main_window import sudo

entry = tkinter.Tk()
entry.title("Select Value")
entry.geometry("180x200")

text_frame = tkinter.Frame(entry, width=180, height=40)
text_frame.place(x=0, y=0)
text_frame.configure(bg='blue')

r = 0
c = 0
cell = sudo['cells'][(r*9)+c]

cell_info = tkinter.Label(text_frame,
    # text=f"id = {cell.id}, row = {cell.row}, column = {cell.column}",
    text='re re re',
    bg="yellow", font="Ariel 12", width=160
    )
cell_info.place(x=10, y=10)



button_frame = tkinter.Frame(entry, width=180, height=160)
button_frame.place(x=0, y=40)
button_frame.configure(bg='red')

b_1 = tkinter.Button(button_frame, text="1", width=2, height=1, font="Arial 16", command='').grid(row=0,column=0,padx=1,pady=1,ipadx=1,ipady=1)
b_2 = tkinter.Button(button_frame, text="2", width=2, height=1, font="Arial 16", command='').grid(row=0,column=1,padx=1,pady=1,ipadx=1,ipady=1)
b_3 = tkinter.Button(button_frame, text="3", width=2, height=1, font="Arial 16", command='').grid(row=0,column=2,padx=1,pady=1,ipadx=1,ipady=1)
b_4 = tkinter.Button(button_frame, text="4", width=2, height=1, font="Arial 16", command='').grid(row=1,column=0,padx=1,pady=1,ipadx=1,ipady=1)
b_5 = tkinter.Button(button_frame, text="5", width=2, height=1, font="Arial 16", command='').grid(row=1,column=1,padx=1,pady=1,ipadx=1,ipady=1)
b_6 = tkinter.Button(button_frame, text="6", width=2, height=1, font="Arial 16", command='').grid(row=1,column=2,padx=1,pady=1,ipadx=1,ipady=1)
b_7 = tkinter.Button(button_frame, text="7", width=2, height=1, font="Arial 16", command='').grid(row=2,column=0,padx=1,pady=1,ipadx=1,ipady=1)
b_8 = tkinter.Button(button_frame, text="8", width=2, height=1, font="Arial 16", command='').grid(row=2,column=1,padx=1,pady=1,ipadx=1,ipady=1)
b_9 = tkinter.Button(button_frame, text="9", width=2, height=1, font="Arial 16", command='').grid(row=2,column=2,padx=1,pady=1,ipadx=1,ipady=1)
'''
