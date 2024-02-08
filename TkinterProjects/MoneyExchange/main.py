from tkinter import *
import requests

#Link for API: https://apilayer.com/marketplace/exchangerates_data-api

#Settings
main_color = "#2ebf91"
active_color = "#1aad7f"
main_font= "Helvetica"
main_font_size = 18
bg_color = "#6fc77e"
#Screen
SCREEN = Tk()
SCREEN.title("Money Exchange")
SCREEN.geometry("550x150+600+300")
SCREEN.minsize(550,150)
SCREEN.iconbitmap("TkinterProjects/MoneyExchange/assets/money_bag.ico")
SCREEN.resizable(True,True)
SCREEN.config(bg=bg_color)

#Functions
def count_currency():
    try:
        currency_from = drop_down_currency1.get()
        currency_to = drop_down_currency2.get()
        amount = float(user_input.get())

        #API
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"

        payload = {}
        headers= {
        "apikey": "your_api_key"
        }
        response = requests.request("GET", url, headers=headers, data = payload)

        response.raise_for_status()
        data_result = response.json()
        result_label.config(text=data_result["result"])
        
    except:
        result_label.config(text="Enter the amount")


#Input
user_input = Entry(width=20, font=(main_font,15),borderwidth=5,relief="groove",justify=CENTER)
user_input.grid(row=0,column=0,padx=5)
user_input.focus()

#Roller1
drop_down_currency1 = StringVar(SCREEN)
drop_down_currency1.set("CZK")
drop_down_currency_options1 = OptionMenu(SCREEN, drop_down_currency1, "CZK","EUR","USD","ARS")
drop_down_currency_options1.config(bg=main_color, fg="white",font=(main_font,main_font_size) , activebackground=active_color,activeforeground="#d7e0de")
drop_down_currency_options1.grid(row=0,column=1,padx=20,pady=5)

#Roller2
drop_down_currency2 = StringVar(SCREEN)
drop_down_currency2.set("EUR")
drop_down_currency_options2 = OptionMenu(SCREEN, drop_down_currency2, "CZK","EUR","USD","ARS")

drop_down_currency_options2.config(bg=main_color, fg="white",font=(main_font,main_font_size) , activebackground=active_color,activeforeground="#d7e0de")
drop_down_currency_options2.grid(row=1,column=1,padx=20,pady=5)

#Label
result_label = Label(text= "0", font=(main_font,14,"bold"),borderwidth=5,relief="groove",bg=main_color, fg="white",activebackground=active_color,activeforeground="#d7e0de")
result_label.grid(row=1,column=0, padx=20)

#Button
exchange_button = Button(text="Exchange",command = count_currency,borderwidth=5,relief="groove",font=(main_font,main_font_size,"bold"),bg=main_color, fg="white",activebackground=active_color,activeforeground="#d7e0de")
exchange_button.grid(row=0,column=2, padx=10,pady=10)



#Main cycle 
SCREEN = mainloop()