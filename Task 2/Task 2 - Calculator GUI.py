import tkinter
from tkinter import *

mfrm = Tk()
mfrm.title('Simple Calculator')
mfrm.geometry('570x600')
mfrm.resizable(False,False)
mfrm.configure(bg= 'black')
label_result = Label(mfrm,width=25, height=2, text='', font='times 30 bold')
label_result.pack()

equation = ''
def show(value):
    global equation
    equation += value
    label_result.configure(text=equation)

def clear():
    global equation
    equation=''
    label_result.configure(text=equation)

def calculate():
    global equation
    result = ''
    if equation !='':
        try:
            result = eval(equation)
        except :
            result = 'error'
            equation=''
    label_result.config(text=result)


Button(mfrm, text='C', width=5, height=1, font= 'times 30 bold', bd=1, fg='#fff', bg='#3697f5', command = lambda: clear()).place(x=10,y=100)
Button(mfrm, text='/', width=5, height=1, font= 'times 30 bold', bd=1, fg='#fff', bg='#2a2d36', command = lambda: show('/')).place(x=150,y=100)
Button(mfrm, text='%', width=5, height=1, font= 'times 30 bold', bd=1, fg='#fff', bg='#2a2d36', command = lambda: show('%')).place(x=290,y=100)
Button(mfrm, text='*', width=5, height=1, font= 'times 30 bold', bd=1, fg='#fff', bg='#2a2d36', command = lambda: show('*')).place(x=430,y=100)

Button(mfrm, text='7', width=5, height=1, font= 'times 30 bold', bd=1, fg='#fff', bg='#2a2d36', command = lambda: show('7')).place(x=10,y=200)
Button(mfrm, text='8', width=5, height=1, font= 'times 30 bold', bd=1, fg='#fff', bg='#2a2d36', command = lambda: show('8')).place(x=150,y=200)
Button(mfrm, text='9', width=5, height=1, font= 'times 30 bold', bd=1, fg='#fff', bg='#2a2d36', command = lambda: show('9')).place(x=290,y=200)
Button(mfrm, text='-', width=5, height=1, font= 'times 30 bold', bd=1, fg='#fff', bg='#2a2d36', command = lambda: show('-')).place(x=430,y=200)

Button(mfrm, text='4', width=5, height=1, font= 'times 30 bold', bd=1, fg='#fff', bg='#2a2d36', command = lambda: show('4')).place(x=10,y=300)
Button(mfrm, text='5', width=5, height=1, font= 'times 30 bold', bd=1, fg='#fff', bg='#2a2d36', command = lambda: show('5')).place(x=150,y=300)
Button(mfrm, text='6', width=5, height=1, font= 'times 30 bold', bd=1, fg='#fff', bg='#2a2d36', command = lambda: show('6')).place(x=290,y=300)
Button(mfrm, text='+', width=5, height=1, font= 'times 30 bold', bd=1, fg='#fff', bg='#2a2d36', command = lambda: show('+')).place(x=430,y=300)

Button(mfrm, text='1', width=5, height=1, font= 'times 30 bold', bd=1, fg='#fff', bg='#2a2d36', command = lambda: show('1')).place(x=10,y=400)
Button(mfrm, text='2', width=5, height=1, font= 'times 30 bold', bd=1, fg='#fff', bg='#2a2d36', command = lambda: show('2')).place(x=150,y=400)
Button(mfrm, text='3', width=5, height=1, font= 'times 30 bold', bd=1, fg='#fff', bg='#2a2d36', command = lambda: show('3')).place(x=290,y=400)
Button(mfrm, text='0', width=11, height=1, font= 'times 30 bold', bd=1, fg='#fff', bg='#2a2d36', command = lambda: show('0')).place(x=10,y=500)

Button(mfrm, text='.', width=5, height=1, font= 'times 30 bold', bd=1, fg='#fff', bg='#2a2d36', command = lambda: show('.')).place(x=290,y=500)
Button(mfrm, text='=', width=5, height=3 , font= 'times 30 bold', bd=1, fg='#fff', bg='#fe9037', command = calculate).place(x=430,y=400)

mfrm.mainloop()