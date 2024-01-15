from tkinter import *

#Screen
SCREEN = Tk()
SCREEN.title = "Přepočet kurzu"
SCREEN.geometry("500x500+600+300")
SCREEN.resizable(width=True,height=True)
SCREEN.minsize(width = 400,height=400)
SCREEN.iconbitmap("TkinterProjects/project1/assets/money_bag.ico")
SCREEN.config(bg="#6fc77e")

#Label
currency1 = Label(SCREEN,text="Euro" ,bg="black",fg="white",font=("Cambria",20,"bold"),borderwidth=5,relief="groove")
currency1.pack(pady=(20,50))

currency2 = Label(SCREEN,text="CZK" ,bg="black",fg="white", font=("Cambria",20,"bold"))
currency2.pack()

#Button
def change_text():
    currency1["text"] = input1.get()
    input1.delete(0,END)

button1 = Button(SCREEN,text="AJAJA1",command=change_text)
button1.pack()

#Input
input1 = Entry(width=20)
input1.focus()
input1.pack()
input1.get()

#Text Field
text_field1 = Text(width=10,height=5)
text_field1.pack()
text_field1.get("1.0,",END)

#Main Cycle
SCREEN.mainloop()