from tkinter import *
import db_app_backend

def get_selected_row(event):
    global selected_tuple
    index = list_box.curselection()[0]
    selected_tuple = list_box.get(index)
    
    title_entry.delete(0,END)
    title_entry.insert(END,selected_tuple[1])
    
    author_entry.delete(0,END)
    author_entry.insert(END,selected_tuple[2])
    
    price_entry.delete(0,END)
    price_entry.insert(END,selected_tuple[3])
    
    year_entry.delete(0,END)
    year_entry.insert(END,selected_tuple[4])


def view_command():
    list_box.delete(0,END)
    for row in db_app_backend.view():
        list_box.insert(END,row)

def search_command():
    list_box.delete(0,END)
    for row in db_app_backend.search(title_text.get(),author_text.get(),price_text.get(),year_text.get()):
        list_box.insert(END,row)

def add_command():
    db_app_backend.insert(title_text.get(),author_text.get(),price_text.get(),year_text.get())
    list_box.delete(0,END)
    list_box.insert(END,(title_text.get(),author_text.get(),price_text.get(),year_text.get()))

def delete_command():
    db_app_backend.delete(selected_tuple[0])
    title_entry.delete(0,END)
    author_entry.delete(0,END)
    price_entry.delete(0,END)
    year_entry.delete(0,END)
    list_box.delete(selected_tuple)

def update_command():
    db_app_backend.update(selected_tuple[0],title_text.get(),author_text.get(),price_text.get(),year_text.get())

#-------------------------------------------------------------------#
#-------------------------------------------------------------------#
#-------------------------------------------------------------------#
#-------------------------------------------------------------------#

window=Tk()
window.wm_title('BOOKS')
#-------------------------------------------------------------------#
title=Label(window,text="Title")
title.grid(row=0,column=0)

title_text=StringVar()
title_entry=Entry(window,textvariable=title_text)
title_entry.grid(row=0,column=1)
#-------------------------------------------------------------------#
author=Label(window,text="Author")
author.grid(row=0,column=3)

author_text=StringVar()
author_entry=Entry(window,textvariable=author_text)
author_entry.grid(row=0,column=4)
#-------------------------------------------------------------------#
price=Label(window,text="Price")
price.grid(row=1,column=0)

price_text=StringVar()
price_entry=Entry(window,textvariable=price_text)
price_entry.grid(row=1,column=1)
#-------------------------------------------------------------------#
year=Label(window,text="Year")
year.grid(row=1,column=3)

year_text=StringVar()
year_entry=Entry(window,textvariable=year_text)
year_entry.grid(row=1,column=4)

#-------------------------------------------------------------------#
#-------------------------------------------------------------------#
#-------------------------------------------------------------------#

view=Button(window,text="View All",width=12,command=view_command)
view.grid(row=3,column=4)

search=Button(window,text="Search Entry",width=12,command=search_command)
search.grid(row=4,column=4)

add=Button(window,text="Add Entry",width=12,command=add_command)
add.grid(row=5,column=4)

update=Button(window,text="Update Selected",width=12,command=update_command)
update.grid(row=6,column=4)

delete=Button(window,text="Delete Selected",width=12,command = delete_command)
delete.grid(row=7,column=4)

close=Button(window,text="Close",width=12,command=window.destroy)
close.grid(row=8,column=4)

sc1=Scrollbar(window)
sc1.grid(row=2,column=2,rowspan=6)

list_box=Listbox(window,height=6,width=55)
list_box.grid(row=2,column=0,rowspan=6,columnspan=2)

list_box.configure(yscrollcommand=sc1.set)
sc1.configure(command=list_box.yview)

list_box.bind('<<ListboxSelect>>',get_selected_row)
#bind is used to bind a function to a widget event
#-------------------------------------------------------------------#
window.mainloop()

