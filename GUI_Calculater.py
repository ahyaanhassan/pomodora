from tkinter import *
import math

#-----------------------------------calculations--------------------------------------#
def press_1():
    one=1
    entry_column.insert(0,one)














#-----------------------------------UI-Setup--------------------------------------#
window = Tk()
window.title("GUI Calculater")
window.config(padx=100,pady=50,bg="white")


entry_column=Entry(width=20,font=('Arial 50 '))
entry_column.grid(column=0,row=0,columnspan=4)

button_1=Button(text=1,width=3,height=3,highlightthickness=0,bd=5,command=press_1)
button_1.grid(column=0,row=1)
button_2=Button(text=2,width=3,height=3,highlightthickness=0,bd=5)
button_2.grid(column=1,row=1)
button_3=Button(text=3,width=3,height=3,highlightthickness=0,bd=5)
button_3.grid(column=2,row=1)
button_4=Button(text=4,width=3,height=3,highlightthickness=0,bd=5)
button_4.grid(column=0,row=2)
button_5=Button(text=5,width=3,height=3,highlightthickness=0,bd=5)
button_5.grid(column=1,row=2)
button_6=Button(text=6,width=3,height=3,highlightthickness=0,bd=5)
button_6.grid(column=2,row=2)
button_7=Button(text=7,width=3,height=3,highlightthickness=0,bd=5)
button_7.grid(column=0,row=3)
button_8=Button(text=8,width=3,height=3,highlightthickness=0,bd=5)
button_8.grid(column=1,row=3)
button_9=Button(text=9,width=3,height=3,highlightthickness=0,bd=5)
button_9.grid(column=2,row=3)
button_0=Button(text=0,width=3,height=3,highlightthickness=0,bd=5)
button_0.grid(column=1,row=4)
button_point=Button(text=".",width=3,height=3,highlightthickness=0,bd=5)
button_point.grid(column=0,row=4)
button_eqauls=Button(text="=",width=3,height=3,highlightthickness=0,bd=5)
button_eqauls.grid(column=2,row=4)
button_plus=Button(text="+",width=3,height=3,highlightthickness=0,bd=5)
button_plus.grid(column=3,row=2)
button_multiply=Button(text="X",width=3,height=3,highlightthickness=0,bd=5)
button_multiply.grid(column=3,row=1)
button_divide=Button(text="/",width=3,height=3,highlightthickness=0,bd=5)
button_divide.grid(column=3,row=4)
button_minus=Button(text="-",width=3,height=3,highlightthickness=0,bd=5)
button_minus.grid(column=3,row=3)





window.mainloop()
