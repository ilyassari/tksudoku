import tkinter
from tkinter import ttk, messagebox
from tkinter.ttk import Combobox

from models import Row, Column, Region, Cell

root = tkinter.Tk()
root.geometry("750x500+100+100")
root.title("Sudoku Solver")
# root.iconbitmap('icon.ico')

cells_frame = tkinter.Frame(root, width=450, height=450)
cells_frame.place(x=20, y=40)
cells_frame.configure(bg='blue')

cell_buttons = list()
sudo = Cell.create_cells()
# global selected_cell
selected_cell = sudo['cells'][0]

def select_cell(row, column):
    id = 9 * row + column
    selected_cell = sudo['cells'][id]
    print(row)
    print(column)
    print(id)

for r in range(9):
    for c in range(9):
        value = sudo['cells'][(r*9)+c].value
        value = f'{value}' if value != 0 else ' '
        cell_buttons.append(tkinter.Button(cells_frame,
                                text=f"{value}",
                                font="Consolas 10",
                                width=3, height=2,
                                command=lambda: select_cell(r, c)
                                ))
        cell_buttons[-1].grid(row=r,column=c,padx=0,pady=0,sticky="W")


entry_frame = tkinter.Frame(root, width=220, height=240)
entry_frame.place(x=500, y=40)
entry_frame.configure(bg='yellow')

text_frame = tkinter.Frame(entry_frame, width=200, height=80)
text_frame.place(x=10, y=0)
text_frame.configure(bg='blue')

button_frame = tkinter.Frame(entry_frame, width=200, height=160)
button_frame.place(x=10, y=80)
button_frame.configure(bg='red')

entry_buttons = list()

def send_value(val):
    select_cell.value = val

for r in range(3):
    for c in range(3):
        val = (r * 3) + c + 1
        entry_buttons.append(tkinter.Button(button_frame,
                                text=f"{val}",
                                font="Consolas 22",
                                width=2, height=1,
                                command=lambda: send_value(val),
                                ))
        entry_buttons[-1].grid(row=r,column=c,
                                padx=1, pady=1,
                                ipadx=0, ipady=0,
                                )

selected_cell_label = tkinter.Label(text_frame,
                                text=f"{selected_cell.id}".ljust(16),
                                font="Consolas 8"
                                )
selected_cell_label.grid(row=0,column=0,padx=5,pady=5,sticky="W")
