from tkinter import *
from random import randint
from tkinter import messagebox

mfrm = Tk()
mfrm.title('Strong Password Generator')
mfrm.geometry('500x300')
mfrm.resizable(False,False)

my_password = chr(randint(33,126))

def new_rand():
    pw_entry.delete(0,END)
    pw_length = int(my_entry.get())
    my_password = ''

    for x in range(pw_length):
        my_password += chr(randint(33, 126))
    pw_entry.insert(0,my_password)

def clipper():
    mfrm.clipboard_clear()
    mfrm.clipboard_append(pw_entry.get())
    messagebox.showinfo('STRONG PASSWORD GENERATOR', 'PASSWORD COPIED SUCCESSFULLY')


lf = LabelFrame(mfrm, text = "How Many Characters?")
lf.pack(pady=20)

my_entry = Entry(lf, font='Helvetica 24')
my_entry.pack(pady=20, padx=20)
my_entry.focus_set()

pw_entry = Entry(mfrm, text='', font = 'Helvetica 24',bd=0,bg='systembuttonface')
pw_entry.pack(pady=20)

my_frame = Frame(mfrm)
my_frame.pack(pady=20)

my_button = Button(my_frame, text='Generate Strong Password', command = new_rand)
my_button.grid(row=0,column=0,padx=10)


clip_button=  Button(my_frame,text='Copy to Clipboard', command=clipper)
clip_button.grid(row=0, column=1, padx=10)

mfrm.mainloop()