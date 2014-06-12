# -*- coding: utf-8 -*-

__author__ = 'carsten'

import converter
import os
import ttk
import tkFileDialog
import Tkinter as tk


class Application(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.master.title('😃')  # smiley :)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.quit_button = ttk.Button(self, text='Convert...', command=self.select_file)
        self.quit_button.grid(padx=10, pady=4, sticky=tk.N+tk.E+tk.S+tk.W)

    @staticmethod
    def select_file():
        filename = tkFileDialog.askopenfilename(filetypes=[('CSV', '.csv')])
        if os.path.exists(filename):
            print os.path.abspath(filename)
            converter.analyze(filename)
        # very simple exit
        exit(0)


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

    #converter.analyze('/Users/carsten/Dropbox/__work__/tmp/travelCSV/bookingsummary_06.06.14_package.csv')