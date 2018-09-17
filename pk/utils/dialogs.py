# -*- encoding: utf-8 -*-
from __future__ import (
    absolute_import,
    print_function, division,
    unicode_literals
)

__all__ = [ 'error', 'info' ]

try :
    import tkinter
    from tkinter import messagebox
except ImportError :
    import Tkinter as tkinter
    import tkMessageBox as messagebox        
        

def format_message(msg) :
    message = str(msg)
    if isinstance(msg, BaseException) :
        message = '{} : {}'.format(
            msg.__class__.__name__,
            ' '.join(map(str, msg.args))
        )

    return message    

def error(msg, title='Error') :
    message = format_message(msg)
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showerror(title=title, message=message)
    root.destroy()

def info(msg, title='Info') :
    message = format_message(msg)
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo(title=title, message=message)
    root.destroy()
