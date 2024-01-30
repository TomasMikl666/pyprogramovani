import requests
from tkinter import *

#SCREEN
SCREEN = Tk()
SCREEN.minsize(400,400)
SCREEN.resizable(False,False)
SCREEN.title("Insulting App")
SCREEN.config(bg="#BFD7FF")

#Functions
def insult_me():
    user_language = drop_down_lang.get()
    my_parameters = {
        "lang":user_language,
        "type":"json"
    }

    response = requests.get(f"https://evilinsult.com/generate_insult.php", params= my_parameters)
    response.raise_for_status()
    data = response.json()
    insult_label.config(text=data["insult"])

#Roller
drop_down_lang = StringVar(SCREEN)
drop_down_lang.set("cs")
drop_down_lang_options = OptionMenu(SCREEN, drop_down_lang, "cs","en","es","fr")
drop_down_lang_options.config(bg="#2ebf91", fg="white",font=("Arial",18) , activebackground="#1aad7f",activeforeground="#d7e0de")
drop_down_lang_options.pack(pady=10)

#Button
insult_button = Button(text="Insult me!",command=insult_me, bg="#2ebf91", fg="white",font=("Arial",18) , activebackground="#1aad7f",activeforeground="#d7e0de")
insult_button.pack(pady=10)

#Label
insult_label = Label(wraplength=250,bg="#9BB1FF", fg="white",font=("Arial",20))
insult_label.pack()


SCREEN.mainloop()