# -*- coding: utf-8 -*-

__author__ = 'carsten'

import converter

import ttk
import tkFileDialog
import Tkinter as tk

class Application(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.master.title('😃') # smiley :)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        self.quit_button = ttk.Button(self, text='Convert...', command=self.select_file)
        self.quit_button.grid(padx=10, pady=4, sticky=tk.N+tk.E+tk.S+tk.W)

    def select_file(self):
        filename = tkFileDialog.askopenfilename()
        converter.analyze(filename)


if __name__ == '__main__':
    # define root
    root = tk.Tk()
    root.resizable(0,0)
    root.geometry('+500+400')
    root.attributes("-topmost", True)

    # init app
    app = Application(root)
    app.focus()
    app.mainloop()