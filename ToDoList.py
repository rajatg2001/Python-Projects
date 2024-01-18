#Question 1
from tkinter import *
root=Tk()
mainframe=Frame(root,width=70,bd=10,relief=FLAT,bg="salmon")
mainframe.pack()
root.title('TO DO List')
inner=Frame(mainframe,width=70,bd=10,relief=FLAT,bg="palegreen")
inner.pack()
l=Label(inner,text='TO DO LIST',font=('ariel',30))
l.grid(row=0,column=0)
e=Entry(inner,width=25,borderwidth=2,font=['ariel',24])
e.insert(0,'Add a task')
e.grid(row=1,column=1,columnspan=6,padx=10,pady=1)
lb=Listbox(inner,width=90,height=20)
def onclick():
    x=e.get()
    e.delete(0,END)
    e.insert(0,'Add a task')
    lb.insert(0,x)
def clear():
    global lb
    lb.delete(0,END)
def Deletesel() :
    selected = lb.curselection()
    pos = 0
    for i in selected:
        i_ = i - pos
        lb.delete( i_ )
        pos = pos + 1
add=Button(inner,text='ADD',padx=30,pady=20,relief=RIDGE,font=15,width=4,
 command=lambda:onclick())
ca=Button(inner,text='Clear All',padx=30,pady=20,relief=RIDGE,font=15,width=4,
 command=lambda:clear())
de=Button(inner,text='Delete',padx=30,pady=20,relief=RIDGE,font=15,width=4,
 command=lambda:Deletesel())
add.grid(row=3,column=0,pady=30)
lb.grid(row=5,column=0,columnspan=7,pady=40)
ca.grid(row=3,column=1)
de.grid(row=3,column=2)
lb.curselection()
root.mainloop()
