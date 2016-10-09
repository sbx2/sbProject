from csprReVer import *
from tkinter import *
from subprocess import call
basis = Tk()



csctrl = None

def command_read():
    global csctrl
    csctrl = CSreportController(readine.get())
    print(csctrl)
def command_addpd():
    csctrl.addPD(addPDe2.get(),int(addPDentry.get()))
    print([addPDe2.get(),int(addPDentry.get())])
    csctrl.calcTotalW()
    csctrl.calcTotalD()
    csctrl.oup('oup.csv')
    call(['csvlook','oup.csv'])


def command_setval():
    wt = setVALe_wt.get()
    pd = int(setVALe_pd.get())
    dt = setVALe_dt.get()
    mt = int(setVALe_mt.get())
    csctrl.setVal(wt,pd,dt,mt)
    csctrl.calcTotalW()
    csctrl.calcTotalD()
    csctrl.oup('oup.csv')
    call(['csvlook','oup.csv'])
ctrlf = Frame(basis)
csviewf = Frame(basis)
ctrlf.pack(side = LEFT,fill = Y)
csviewf.pack(fill = Y)


readinl = Label(ctrlf,text = "readfromfile")
readine = Entry(ctrlf)
readinb = Button(ctrlf,text='read',command = command_read)
readinl.grid(row = 0)
readine.grid(row = 0,column = 1)
readinb.grid(row = 0,column = 2)

addPDlabel = Label(ctrlf,text = 'add PD :')
addPDentry = Entry(ctrlf)
addPDl2 = Label(ctrlf,text = 'to wt :')
addPDe2 = Entry(ctrlf)
addPDbtn = Button(ctrlf,text = 'add',command = command_addpd)

addPDlabel.grid(row = 1)
addPDentry.grid(row = 1,column = 1)
addPDl2.grid(row = 1,column = 2)
addPDe2.grid(row = 1,column = 3)
addPDbtn.grid(row = 1,column = 4)

setVALl_wt = Label(ctrlf,text = 'wheel type:')
setVALe_wt = Entry(ctrlf)
setVALl_pd = Label(ctrlf,text = 'problem describe:')
setVALe_pd = Entry(ctrlf)
setVALl_dt = Label(ctrlf,text = 'date:')
setVALe_dt = Entry(ctrlf)
setVALl_mt = Label(ctrlf,text = 'amount:')
setVALe_mt = Entry(ctrlf)
setVALbt = Button(ctrlf,text = 'set',command = command_setval)

setVALl_wt.grid(row = 2)
setVALe_wt.grid(row = 2,column = 1)
setVALl_pd.grid(row = 2,column = 2)
setVALe_pd.grid(row = 2,column = 3)
setVALl_dt.grid(row = 2,column = 4)
setVALe_dt.grid(row = 2,column = 5)
setVALl_mt.grid(row = 2,column = 6)
setVALe_mt.grid(row = 2,column = 7)
setVALbt.grid(row = 2,column = 9)




basis.mainloop()
