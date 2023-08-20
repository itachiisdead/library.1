from tkinter import *
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


return_book=Tk()
return_book.title("Return Book")
style = Style()
def returnbook_window(root):
    root.update_idletasks()
    screen_width = root.winfo_screenwidth() 
    screen_height = root.winfo_screenheight()
    width=1200
    height=650
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

def back():
      return_book.destroy()
      import home


img_bg=Image.open('pics/back_ground.jpg')
bck_bg=ImageTk.PhotoImage(img_bg)    
pic_label=Label(return_book,image=bck_bg)
pic_label.place(x=0,y=0 )

 frame = Frame(return_book,bg='slategrey')
 frame.place(relx=0.1,rely=0.06,relwidth=0.8,relheight=0.85)

style.configure('W.TButton', font =
               ('georia', 10, 'bold'),
                foreground = 'black')

returnbook_window(return_book)
B_idl=Label(return_book,text="Book Id",font='8').place(x=300,y=100)
B_idE=Entry(font='10').place(x=450,y=100)

B_namel=Label(return_book,text="Book Name",font='8').place(x=300,y=200)
B_nameE=Entry(font='10').place(x=450,y=200)

B_authorl=Label(return_book,text="Author",font='8').place(x=300,y=300)
B_authorE=Entry(font='10').place(x=450,y=300)

Std_namel=Label(return_book,text="Student Name",font='8').place(x=300,y=400)
Std_nameE=Entry(font='10').place(x=450,y=400)

return_but=Button(return_book,text="return", style = 'W.TButton').place(x=800,y=150)
list_frame_but=Button(return_book,text="Borrowed Books", style = 'W.TButton').place(x=800,y=250)
back_but=Button(return_book,text='back',bg='indianred4',fg='white',font=('purisa',18),command=back).place(x=800,y=350)
return_book.resizable('false','false')

return_book.mainloop()

    
    
