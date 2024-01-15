from tkinter import *

#Screen
SCREEN = Tk()
SCREEN.title = "Přepočet kurzu"
SCREEN.geometry("500x500+600+300")
SCREEN.resizable(width=True,height=True)
SCREEN.minsize(width = 400,height=400)
SCREEN.iconbitmap("TkinterProjects/project1/assets/money_bag.ico")
SCREEN.config(bg="black")

#Label
currency1 = Label(SCREEN,text="Euro" ,bg="black",fg="white",font=("Cambria",20,"bold"),borderwidth=5,relief="groove")
currency1.pack(pady=(20,50))

currency2 = Label(SCREEN,text="CZK" ,bg="black",fg="white", font=("Cambria",20,"bold"))
currency2.pack()
#Main Cycle
SCREEN.mainloop()