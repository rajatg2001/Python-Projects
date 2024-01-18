#3.

from tkinter import *

root=Tk()
root.geometry("300x200+600+200")
root.title("Temperature convertor")
root.grid()

fa=Frame(root,width=250,height=400,bd=10,bg="skyblue")
fa.place(anchor='ne',relx=0,rely=0)
fa.grid()

fb=Frame(root,width=250,height=1000,bd=10,bg="RED")
fb.place(anchor='ne',relx=0,rely=0)
fb.grid()

input_unit="Kelvin"
output_unit="Celcius"
def store_input_unit(set_temp):
    global input_unit
    input_unit=set_temp
def store_output_unit(set_temp):
    global output_unit
    output_unit=set_temp
result=0
def convert():
    global result
    inputNumber=float(input_entry.get())
    if input_unit=="Kelvin":
        if output_unit=="Celcius":
            result=inputNumber-273
        if output_unit=="Fahrenheit":
            result=1.8*(inputNumber)-273+32
        if output_unit=="Kelvin":
            result=inputNumber
            
    if input_unit=="Celcius":
        if output_unit=="Kelvin":
            result=inputNumber+273
        if output_unit=="Fahrenheit":
            result=1.8*(inputNumber)+32
        if output_unit=="Celcius":
            result=inputNumber
    if input_unit=="Fahrenheit":
        if output_unit=="Celcius":
            result=(inputNumber-32)*(5/9)
        if output_unit=="Kelvin":
            result=(inputNumber+459.67)*(5/9)
        if output_unit=="Fahrenheit":
             result=inputNumber
    global result_label
    result_label.destroy()
    result_label=Label(fb,text=result)
    result_label.grid(row=4,columnspan=2)
inputNumber=StringVar()

input_label=Label(fa,text="Enter Input temperature and Select Unit")
input_entry=Entry(fa,textvariable=inputNumber)
input_label.grid(row=0,columnspan=2)
input_entry.grid(row=1,column=0)
unit=["Kelvin","Celcius","Fahrenheit"]
vari=StringVar()
input_list=OptionMenu(fa,vari,*unit,command=store_input_unit)
vari.set(unit[0])
input_list.grid(row=1,column=1)

output_label=Label(fb,text="Select Output Unit")
output_label.grid(row=2)
unit2=["Kelvin","Celcius","Fahrenheit"]
varo=StringVar()
output_list=OptionMenu(fb,varo,*unit2,command=store_output_unit)
varo.set(unit2[1])
output_list.grid(row=2,column=1)

result_button = Button(fb, text ="Convert",command = convert)
result_button.grid(row = 3, columnspan = 2)

result_label=Label(fb,text="Result is Displayed Here")
result_label.grid(row=4,columnspan=2)
root.mainloop()
