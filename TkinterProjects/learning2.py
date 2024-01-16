from tkinter import *
from tkinter import *

#SCREEN
SCREEN = Tk()
SCREEN.title("Převod měn")
SCREEN.minsize(500,500)
SCREEN.resizable(True,True)

#Label1
label_1 = Label(text="First label", font=("Helvetica",20,"bold"))
#label_1.pack(side="bottom")
#label_1.place(x=0,y=0)
label_1.grid(row=0,column=0)


label_2 = Label(text="Second label", font=("Helvetica",20,"bold"))
#label_2.pack(side="bottom")
#label_2.place(x=250,y=250)
label_2.grid(row=1,column=1)

label_3 = Label(text="Third label", font=("Helvetica",20,"bold"))
#label_3.pack(side="bottom")
#label_3.place(x=300,y=200)
label_3.grid(row=2,column=2)

#Main Cycle
SCREEN.mainloop()