from tkinter import * 
from tkinter import filedialog
import pyautogui, keyboard
from PIL import Image, ImageTk

m= Tk()
m.title("Screenshot")
m.geometry("600x300")

c = Canvas(m,height=200,width=550,bg="white")
c.create_text(275,100,text='Press ctrl+r to take and save a screenshot',font=('Arial', 10))
#screenshot button
def ss():
    my_ss = pyautogui.screenshot()
    def savefile():
        filetype_ = [('PNG','*.png'),('JPG','*.jpg'),('JPEG','*.jpeg')]
        file = filedialog.asksaveasfilename(filetypes=filetype_,defaultextension=('PNG','*.png'))
        my_ss.save(file)


    select_path = Button(m,text ="Save",command=savefile)
    select_path.place(x=90,y=10)

ss_button = Button(m,text="+ New",command=ss)
ss_button.place(x=10,y=10)

#function for shortcupt
def ss_save():
    my_ss = pyautogui.screenshot()
    filetype_ = [('PNG','*.png'),('JPG','*.jpg'),('JPEG','*.jpeg')]
    file = filedialog.asksaveasfilename(filetypes=filetype_,defaultextension=('PNG','*.png'))
    my_ss.save(file)

keyboard.add_hotkey('ctrl+r', ss_save)

c.place(y=15,relx=.5, rely=.5,anchor= CENTER)

m.mainloop()