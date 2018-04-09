import Tkinter
import sys

def write(string):
    text_box.config(state=Tkinter.NORMAL)
    text_box.insert("end", string + "\n")
    text_box.see("end")
    text_box.config(state=Tkinter.DISABLED)

def load_dataset():
    write("hey")

root = Tkinter.Tk()

text_box = Tkinter.Text(root, state=Tkinter.DISABLED)
text_box.grid(row=0, column=0, columnspan=4)

button_1 = Tkinter.Button(root, text="Load Dataset", command=load_dataset)
button_1.grid(row=1, column=0)

# button_2 = Tkinter.Button(root, text="2", command=lambda: choose(2))
# button_2.grid(row=1, column=1)

# button_3 = Tkinter.Button(root, text="3", command=lambda: choose(3))
# button_3.grid(row=1, column=2)

# button_4 = Tkinter.Button(root, text="4", command=lambda: choose(4))
# button_4.grid(row=1, column=3)

root.mainloop()