#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import partial
from tkinter import *
import os


def strip(string):
    return string.replace('*', '').strip().split(' ')[0]


def get_all():
    Outputfileobject = os.popen('rbenv install --list')
    Output = Outputfileobject.read()
    Outputfileobject.close()
    arr = list(map(strip, Output.split('\n')))
    arr.pop()
    return arr


def get_current():
    Outputfileobject = os.popen('rbenv global')
    Output = Outputfileobject.read()
    Outputfileobject.close()
    arr = list(map(strip, Output.split('\n')))
    arr.pop()
    return arr


def get_installed():
    Outputfileobject = os.popen('rbenv versions')
    Output = Outputfileobject.read()
    Outputfileobject.close()
    arr = list(map(strip, Output.split('\n')))
    arr.pop()
    return arr


def install(window, i):
    os.system('rbenv install ' + i)
    generate_data(window)


def use(window, i):
    os.system('rbenv global ' + i)
    generate_data(window)


def generate_data(window):
    row = 1
    for i in get_all():
        row += 1
        Label(window, text=i, bg="black", fg='white').grid(row=row, column=1)
        if i in get_installed():
            Label(window, text='Installed', bg="black", fg='white').grid(row=row, column=2)
            if i in get_current():
                Label(window, text='Used', bg="black", fg='white').grid(row=row, column=3)
            else:
                Button(window, text="Use", highlightbackground="black",
                       command=partial(use, window, i)).grid(row=row, column=3)
        else:
            Button(window, text="Install", highlightbackground="black",
                   command=partial(install, window, i)).grid(row=row, column=2)


def main():
    window = Tk()
    window.configure(bg='black')
    window.title('rbenv gui')
    generate_data(window)
    window.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
