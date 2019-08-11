from tkinter import *
def clear():
    for i in vdgts:i.destroy()
q=0
while True:
    if q==0:
        root = Tk()
        root.title('EngineRed')
        root.geometry('800x500+350+150')
        root.resizable(False,False)
        root.configure(bg='#333')
        vdgts = [Label(text='EngineRed 1.0', bg='#333', fg='#999', font='20')]
        vdgts[0].place(x=5, y=5)
    while q==0:root.update()
    while q==1:
        pass