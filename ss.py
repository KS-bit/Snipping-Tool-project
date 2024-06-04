from tkinter import *
from tkinter import messagebox 
import pyautogui 
import os

m= Tk()
m.title("Screenshot")
m.geometry("700x500")

#screenshot button
def ss():
    my_ss = pyautogui.screenshot()
    
    path_label = Label(m,text="Path to Save the Screenshot")
    path_entry = Entry(m)
    file_label = Label(m,text="Name of file")
    file_entry = Entry(m)


    def l2():
        file_path = path_entry.get()+"\\"+file_entry.get()+".png"

        #function to save ss
        def save_file():
            my_ss.save(file_path)
            messagebox.showinfo("save","saved")
            m.destroy()

        #check if file exsist or not 
        if os.path.exists(file_path):
            duplcate_file= messagebox.askokcancel("Confirm save as",file_entry.get()+".png already exsist do you want to replace it")
            if duplcate_file:
                save_file()

        else:
            save_file()


    save_button1 = Button(m,text="Save",command=l2)

    path_label.place(x=150,y=100)
    path_entry.place(x=400,y=100)
    file_label.place(x=150,y=150)
    file_entry.place(x=400,y=150)
    save_button1.place(x=350,y=200)

ss_button = Button(m,text="+ New",command=ss)
ss_button.place(x=10,y=10)

m.mainloop()