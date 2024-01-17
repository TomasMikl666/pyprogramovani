from tkinter import *

#SCREEN
SCREEN = Tk()
SCREEN.title("TO-DO manager")
SCREEN.geometry("450x450+600+300")
SCREEN.iconbitmap("TkinterProjects/project2/assets/todoicon.ico")
SCREEN.minsize(400,400)
SCREEN.resizable(False,False)

#Fonts and colours
main_font = ("Times New Roman",12)
main_colour= "#4e99a6"
button_color = "#dba95e"
SCREEN.config(bg=main_colour)

#Functions
def add_text():
    list_box.insert(END,user_input.get())
    user_input.delete(0,END)

def remove_text_item():
    list_box.delete(ANCHOR)

def clear_all_list():
    list_box.delete(0,END)

#Frames
input_frame = Frame(SCREEN, bg=main_colour)
text_frame = Frame(SCREEN, bg=main_colour)
button_frame = Frame(SCREEN, bg=main_colour)
input_frame.pack()
text_frame.pack()
button_frame.pack()

#Input Frame
user_input = Entry(input_frame,width=35,borderwidth=3,font=main_font)
user_input.grid(row=0,column=0,padx=5,pady=5)
user_input.focus()

add_button = Button(input_frame, text="Add",borderwidth=2, font=main_font,bg=button_color, command=add_text)
add_button.grid(row=0,column=1,padx=5,pady=5,ipadx=20)

#Scrollbar
text_scrollbar = Scrollbar(text_frame)
text_scrollbar.grid(row=0,column=1,sticky=NS)

#Text frame
list_box = Listbox(text_frame,width=45,height=15,font=main_font,borderwidth=3,bg="#91c1db", yscrollcommand=text_scrollbar.set)
list_box.grid(row=0,column=0)

#Scollbar&ListBox connection
text_scrollbar.config(command=list_box.yview)

#Button Frame
remove_button = Button(button_frame,text="Remove",borderwidth=2,font=main_font,bg=button_color,command=remove_text_item)
remove_button.grid(row=0,column=0,padx=2,pady=10,ipadx=21)

clear_button = Button(button_frame,text="Clear",borderwidth=2,font=main_font,bg=button_color,command=clear_all_list)
clear_button.grid(row=0,column=1,padx=2,pady=10,ipadx=21)

save_button = Button(button_frame,text="Save",borderwidth=2,font=main_font,bg=button_color)
save_button.grid(row=0,column=2,padx=2,pady=10,ipadx=21)

quit_button = Button(button_frame,text="Quit",borderwidth=2,font=main_font,bg=button_color,command=SCREEN.destroy)
quit_button.grid(row=0,column=3,padx=2,pady=10,ipadx=21)

#Main Cycle
SCREEN.mainloop()