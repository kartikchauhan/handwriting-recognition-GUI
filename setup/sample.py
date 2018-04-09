import Tkinter as tk
import sys

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        toolbar = tk.Frame(self)
        toolbar.pack(side="top", fill="x")
        b1 = tk.Button(self, text="print to stdout", command=self.print_stdout)
        b2 = tk.Button(self, text="print to stderr", command=self.print_stderr)
        b1.pack(in_=toolbar, side="left")
        b2.pack(in_=toolbar, side="left")
        self.text = tk.Text(self, wrap="word")
        self.text.pack(side="top", fill="both", expand=True)
        self.text.tag_configure("stderr", foreground="#b22222")

        sys.stdout = TextRedirector(self.text, "stdout")
        sys.stderr = TextRedirector(self.text, "stderr")

    def print_stdout(self):
        '''Illustrate that using 'print' writes to stdout'''
        # print "this is stdout"
        sys.stdout.write("printing")

    def print_stderr(self):
        '''Illustrate that we can write directly to stderr'''
        sys.stderr.write("this is stderr\n")

class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")

app = ExampleApp()
app.mainloop()

# import Tkinter
# import sys

# def write(string):
#     text_box.config(state=Tkinter.NORMAL)
#     text_box.insert("end", string + "\n")
#     text_box.see("end")
#     text_box.config(state=Tkinter.DISABLED)

# root = Tkinter.Tk()

# text_box = Tkinter.Text(root, state=Tkinter.DISABLED)
# text_box.grid(row=0, column=0, columnspan=4)

# for i in range(0, 10):
#     write("i")

# root.mainloop()
