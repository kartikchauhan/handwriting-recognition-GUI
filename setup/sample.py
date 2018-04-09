from tkinter import *

root = Tk()
root.title("sample program")

def print_item_from_list(event):
    print(event.widget.config("text")[-1])


list = [1, 2, 3, 4, 5]
seclist = []
print(list)
for i in range(0,5):
    variable = list[i]
    sample = Label(text=variable)
    sample.pack()
    sample.bind('<Enter>', print_item_from_list)

root.mainloop()