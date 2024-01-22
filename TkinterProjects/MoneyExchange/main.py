from tkinter import *
from PIL import Image, ImageTk
#Screen
SCREEN = Tk()
SCREEN.title("Money Exchange")
SCREEN.geometry("450x200+600+300")
SCREEN.minsize(250,250)
SCREEN.iconbitmap("TkinterProjects/MoneyExchange/assets/money_bag.ico")
SCREEN.resizable(True,True)
SCREEN.config(bg="#6fc77e")

#Functions
def count_currency():
    amount_eur = float(amount_input.get()) / 24.58
    result_label["text"] = round(amount_eur,2)


#Input
amount_input = Entry(width=20, font=("Helvetica",15),borderwidth=5,relief="groove")
amount_input.grid(row=0,column=0)
amount_input.focus()

#Label
czk_currency = Label(text= "CZK", font=("Helvitca",14,"bold"),borderwidth=5,relief="groove")
czk_currency.grid(row=0,column=1,padx=20)

result_label = Label(text= "0", font=("Helvitca",14,"bold"),borderwidth=5,relief="groove")
result_label.grid(row=1,column=0, padx=20)

euro_currency = Label(text= "EUR", font=("Helvitca",14,"bold"),borderwidth=5,relief="groove")
euro_currency .grid(row=1,column=1, padx=20)

#Button
exchange_button = Button(text="Exchange",command = count_currency,borderwidth=5,relief="groove",font=("Helvitca",12,"bold"))
exchange_button.grid(row=0,column=2, padx=10)

# Načtení obrázku
image_path = "TkinterProjects/MoneyExchange/assets/skrblik.png"  # Nahraďte soubor a cestu k vašemu obrázku
img1 = Image.open(image_path)
img1 = img1.resize((200, 100))  # Přizpůsobení velikosti obrázku podle potřeby
photo = ImageTk.PhotoImage(img1)

# Vytvoření widgetu Label pro zobrazení obrázku
img1_label = Label(SCREEN, image=photo, borderwidth=5,bg="#6fc77e")
img1_label.grid(row=2, column=0,pady=80  )

#Main cycle 
SCREEN = mainloop()