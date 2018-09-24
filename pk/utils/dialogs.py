# -*- encoding: utf-8 -*-
from __future__ import (
    absolute_import, print_function, division,
    unicode_literals
)

try :
    import tkinter
    from tkinter import messagebox
except ImportError :
    import Tkinter as tkinter
    import tkMessageBox as messagebox


class Dialogs :

    __shared_state = {}

    def __init__(self) :
        self.__dict__ = self.__shared_state
        self.make_root()

    def make_root(self) :
        try :
            self.root
        except AttributeError :
            self.root = tkinter.Tk()
            self.root.withdraw()

    def format_message(self, msg) :
        message = str(msg)
        if isinstance(msg, BaseException) :
            message = '{} : {}'.format(
            msg.__class__.__name__,
            ' '.join(map(str, msg.args))
        )

        return message
    
    @classmethod
    def error(cls, msg, title='Error') :
        dlg = cls()
        message = dlg.format_message(msg)
        messagebox.showerror(
            title=title,
            message=message,
            parent = dlg.root
        )

    @classmethod
    def warning(cls, msg, title='Warning') :
        dlg = cls()
        message = dlg.format_message(msg)
        messagebox.showwarning(
            title=title,
            message=message,
            parent = dlg.root
        )
        
    @classmethod
    def info(cls, msg, title='Info') :
        dlg = cls()
        message = dlg.format_message(msg)
        messagebox.showinfo(
            title=title,
            message=message,
            parent = dlg.root
        )
        
    @classmethod
    def question(cls, question, title='Question') :
        dlg = cls()
        message = str(question)
        return messagebox.askquestion(
            title=title,
            message=message,
            parent = dlg.root
        )

    @classmethod
    def okcancel(cls, question, title='Question') :
        dlg = cls()
        message = str(question)
        return messagebox.askokcancel(
            title=title,
            message=message,
            parent = dlg.root
        )

    @classmethod
    def retrycancel(cls, question, title='Question') :
        dlg = cls()
        message = str(question)
        return messagebox.askretrycancel(
            title=title,
            message=message,
            parent = dlg.root
        )

    @classmethod
    def yesno(cls, question, title='Question') :
        dlg = cls()
        message = str(question)
        return messagebox.askyesno(
            title=title,
            message=message,
            parent = dlg.root
        )
