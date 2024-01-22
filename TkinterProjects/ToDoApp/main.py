from tkinter import *
from customtkinter import *

#SCREEN
SCREEN = CTk()
SCREEN.title("TO-DO manager")
SCREEN.geometry("750x325+600+300")
SCREEN.iconbitmap("TkinterProjects/ToDoApp/assets/todoicon.ico")
SCREEN.minsize(750,325)
SCREEN.resizable(False,False)

#Fonts and colours
main_font = ("Times New Roman",12)
main_colour= "#4e99a6"
button_color = "#dba95e"


#Functions
def add_text():
    list_box.insert(END,user_input.get())
    user_input.delete(0,END)

def remove_text_item():
    list_box.delete(ANCHOR)

def clear_all_list():
    list_box.delete(0,END)

def save_list():
     with open("tasks.txt", "w") as file:
         my_tasks = list_box.get(0,END)
         for one_task in my_tasks:
            if one_task.endswith("\n"):
                file.write(f"{one_task}")
            else:
                file.write(f"{one_task}\n")

def open_tasks():
    try:
        with open("tasks.txt","r") as file:
            for one_line in file:
                list_box.insert(END, one_line)
    except:
        print("Error in function for opening file: tasks.txt")

#Frames
input_frame = CTkFrame(SCREEN)
text_frame = CTkFrame(SCREEN)
button_frame = CTkFrame(SCREEN)
input_frame.pack() 
text_frame.pack()
button_frame.pack()

#Input Frame
user_input = CTkEntry(input_frame,width=550)
user_input.grid(row=0,column=0,padx=5,pady=5)
user_input.focus()

add_button = CTkButton(input_frame, text="Add", command=add_text,font=("Times New Roman", 20))
add_button.grid(row=0,column=1,padx=5,pady=5,ipadx=20)

#Scrollbar
text_scrollbar = Scrollbar(text_frame)
text_scrollbar.grid(row=0,column=1,sticky=NS)

#Text frame
list_box = Listbox(text_frame,width=122,height=15,bg="#91c1db", yscrollcommand=text_scrollbar.set)
list_box.grid(row=0,column=0)

#Scollbar&ListBox connection
text_scrollbar.config(command=list_box.yview)

#Button Frame
remove_button = CTkButton(button_frame,text="Remove",command=remove_text_item,font=("Times New Roman", 20))

remove_button.grid(row=0,column=0,padx=2,pady=10,ipadx=21)

clear_button = CTkButton(button_frame,text="Clear",command=clear_all_list,font=("Times New Roman", 20))
clear_button.grid(row=0,column=1,padx=2,pady=10,ipadx=21)

save_button = CTkButton(button_frame,text="Save",command= save_list,font=("Times New Roman", 20))
save_button.grid(row=0,column=2,padx=2,pady=10,ipadx=21)

quit_button = CTkButton(button_frame,text="Quit",command=SCREEN.destroy,font=("Times New Roman", 20))
quit_button.grid(row=0,column=3,padx=2,pady=10,ipadx=21)

#Reload list to list_box
open_tasks()

#Main Cycle
SCREEN.mainloop()