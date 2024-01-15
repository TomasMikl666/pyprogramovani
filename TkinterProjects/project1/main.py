from tkinter import *

#Screen
SCREEN = Tk()
SCREEN.title("Money Exchange")
SCREEN.geometry("600x400+600+300")
SCREEN.minsize(width = 500 ,height = 400)
SCREEN.resizable(width = True ,height = True)
SCREEN.iconbitmap("TkinterProjects/project1/assets/money_bag.ico")
SCREEN.config(bg = "#6fc77e")

#Label - TEXT
greet_labe = Label(SCREEN,text="Greetings", bg = "white",fg="black",font=("Helvetica", 16, "italic"))
greet_labe.pack()

#Label -Euro 
currency1 =Label(SCREEN,text="Euro", bg = "white",font=("Helvetica", 16, "italic"))
currency1.pack()


#Main Cycle
SCREEN.mainloop()