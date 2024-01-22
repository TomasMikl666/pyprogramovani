from tkinter import *
from tkintermapview import *
from tkinter import ttk
import requests

def create_text_entries(frame, row, column, text):
    entry = Entry(frame, font=("Helvetica", 18), bg="#636dad", fg="white", readonlybackground="#636dad", insertbackground="white", bd=0)
    entry.grid(row=row, column=column, padx=10, pady=5)
    entry.insert(0, text)
    entry.bind("<Button-3>", lambda event: entry.clipboard_clear(), add='+')
    entry.bind("<ButtonRelease-3>", lambda event: entry.clipboard_append(entry.get()), add='+')
    return entry

def update_text_entries(latitude, longitude):
    latitude_entry.delete(0, END)
    latitude_entry.insert(0, f"Latitude: {latitude}")

    longitude_entry.delete(0, END)
    longitude_entry.insert(0, f"Longitude: {longitude}")

def iss_coordinates():
    response = requests.get('http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    print(latitude, longitude)
    map_widget.set_position(latitude, longitude)
    update_text_entries(latitude, longitude)

def slide(e):
    map_widget.set_zoom(slider.get())

def close_window():
    SCREEN.destroy()


# screen
SCREEN = Tk()
SCREEN.title('ISS Location APP')
SCREEN.geometry("900x900+500+50")
SCREEN.configure(bg="#6976c9")

# label
label = LabelFrame(SCREEN, bg="#636dad")
label.pack(pady=20)

# map
map_widget = TkinterMapView(label, width=800, height=600, corner_radius=0)
map_widget.set_position(36.1699, -115.1396) 
map_widget.set_zoom(5)
map_widget.pack()

# frames
frame1 = LabelFrame(SCREEN, bg="#636dad")
frame1.pack(pady=10)

frame2 = LabelFrame(SCREEN, bg="#636dad")
frame2.pack(pady=10)

frame3 = LabelFrame(SCREEN, bg="#636dad")
frame3.pack(pady=10)

# button
button = Button(frame1, text="ISS Location", font=("Helvetica", 18), command=iss_coordinates)
button.grid(row=0, column=0)

# slider
slider = ttk.Scale(frame1, from_=4, to=20, orient=HORIZONTAL, command=slide, value=20, length=220)
slider.grid(row=0, column=1, padx=10)

# text entries
latitude_entry = create_text_entries(frame2, row=0, column=2, text="")
longitude_entry = create_text_entries(frame3, row=0, column=3, text="")

# close button
close_button = Button(SCREEN, text="Close", font=("Helvetica", 18), command=close_window)
close_button.pack(pady=10)

SCREEN.mainloop()
