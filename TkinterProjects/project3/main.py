import requests
from tkinter import *

#Screen
SCREEN = Tk()
SCREEN.minsize(700,400)
SCREEN.resizable(False,False)
SCREEN.title("ISS Location")

#Function
def iss_coordinates():
    response = requests.get('http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()
    longitude = (data["iss_position"]["longitude"])
    latitude = (data["iss_position"]["latitude"])

    latitude_label.config(text=f"Latitude: {latitude}")
    longitude_label.config(text=f"Longitude: {longitude}")

#Create Canvas
CANVAS = Canvas(SCREEN,width=500, height=280,bg="red")
CANVAS.pack()
img = PhotoImage(file="TkinterProjects/MoneyExchange/assets/skrblik.png")
CANVAS.create_image(0,0,anchor="nw", image=img)

#Frame
coordinate_frame = Frame(SCREEN)
coordinate_frame.pack()

#Button
recount_button = Button(coordinate_frame,text="Actually coordinates of ISS:",command=iss_coordinates)
recount_button.pack()

#Labels

latitude_label = Label()
latitude_label.pack()

longitude_label = Label()
longitude_label.pack()

#Main Cycle
SCREEN.mainloop()

# #Request & Response
# response = requests.get('http://api.open-notify.org/iss-now.json')
# response.raise_for_status()

# #Printing data from url
# data = response.json()
# longitude = (data["iss_position"]["longitude"])
# latitude = (data["iss_position"]["latitude"])
# print(f"Souřadnice ISS latitude:{latitude}, longitude:{longitude}")
