from tkinter import *
from tkintermapview import *
from tkinter import ttk
import requests

marker_2 = None  # Add this line to create a variable for the last marker

def create_text_entries(frame, row:int, column:int, text:str):
    entry = Entry(frame, font=("Helvetica", 18), bg="#636dad", fg="white", readonlybackground="#636dad", insertbackground="white", bd=0)
    entry.grid(row=row, column=column, padx=10, pady=5)
    entry.insert(0, text)
    entry.bind("<Button-3>", lambda event: entry.clipboard_clear(), add='+')
    entry.bind("<ButtonRelease-3>", lambda event: entry.clipboard_append(entry.get()), add='+')
    return entry

def update_text_entries(latitude:float, longitude:float) -> Entry:
    latitude_entry.delete(0, END)
    latitude_entry.insert(0, f"Latitude: {latitude}")

    longitude_entry.delete(0, END)
    longitude_entry.insert(0, f"Longitude: {longitude}")

def iss_coordinates():
    global marker_2  
    response = requests.get('http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    # Delete the last marker
    if marker_2 is not None:
        map_widget.delete(marker_2)

    # set a position marker
    marker_2 = map_widget.set_marker(latitude, longitude)
    marker_2.set_text("ISS Location")

    print(latitude, longitude)
    map_widget.set_position(latitude, longitude)
    update_text_entries(latitude, longitude)

def slide():
    map_widget.set_zoom(slider.get())

def close_window():
    SCREEN.destroy()

# styles
MAIN_COLOR = "#6976c9"
SECOND_COLOR = "#636dad"
MAIN_FONT = "Helvetica"

# screen
SCREEN = Tk()
SCREEN.title('ISS Location APP')
SCREEN.geometry("900x900+500+50")
SCREEN.configure(bg=MAIN_COLOR)
SCREEN.iconbitmap("TkinterProjects/ISSLocator/assets/satelit.ico")

# label
label = LabelFrame(SCREEN, bg=SECOND_COLOR )
label.pack(pady=20)

# map
map_widget = TkinterMapView(label, width=800, height=600, corner_radius=0)
map_widget.set_position(36.1699, -115.1396) 
map_widget.set_zoom(5)
map_widget.pack()

# frames
frame1 = LabelFrame(SCREEN, bg=SECOND_COLOR)
frame1.pack(pady=10)

frame2 = LabelFrame(SCREEN, bg=SECOND_COLOR)
frame2.pack(pady=10)

frame3 = LabelFrame(SCREEN, bg=SECOND_COLOR)
frame3.pack(pady=10)

# button
iss_button = Button(frame1, text="ISS Location", font=(MAIN_FONT, 18), command=iss_coordinates)
iss_button.grid(row=0, column=0)

# slider
slider = ttk.Scale(frame1, from_=4, to=20, orient=HORIZONTAL, command=slide, value=20, length=220)
slider.grid(row=0, column=1, padx=10)

# text entries
latitude_entry = create_text_entries(frame2, row=0, column=2, text="")
longitude_entry = create_text_entries(frame3, row=0, column=3, text="")

# close button
close_button = Button(SCREEN, text="Close", font=(MAIN_FONT, 18), command=close_window)
close_button.pack(pady=10)

SCREEN.mainloop()