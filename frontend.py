"""

A program that stores this book information:
Title, Author
Year, ISBN

user can:

view all records
search an entry
add entry
update entry
delete entry
close

"""

from tkinter import *
import backend


# book inventory functions
def view_command():
    listEntries.delete(0,END)
    for row in backend.view():
        listEntries.insert(END, row)
        
def search_command():
    listEntries.delete(0,END)
    for row in backend.search(titleEntry.get(),authorEntry.get(),yearEntry.get(),isbnEntry.get()):
        listEntries.insert(END,row)
        
def add_command():
    backend.insert(titleEntry.get(),authorEntry.get(),yearEntry.get(),isbnEntry.get())
    listEntries.delete(0,END)
    listEntries.insert(END,(titleEntry.get(),authorEntry.get(),yearEntry.get(),isbnEntry.get()))
        
def get_selected_row(event):
    try:
        global selectedTuple
        index = listEntries.curselection()[0]
        selectedTuple = listEntries.get(index)
        tEntry.delete(0,END)
        tEntry.insert(END,selectedTuple[1])
        aEntry.delete(0,END)
        aEntry.insert(END,selectedTuple[2])
        yEntry.delete(0,END)
        yEntry.insert(END,selectedTuple[3])
        iEntry.delete(0,END)
        iEntry.insert(END,selectedTuple[4])
    except IndexError:
        pass

    
def delete_command():
    backend.delete(selectedTuple[0])
    
def update_command():
    backend.update(selectedTuple[0],titleEntry.get(),authorEntry.get(),yearEntry.get(),isbnEntry.get())
    

# window GUI
window = Tk()
window.wm_title("Books Database")

# label section
titleLabel = Label(window, text="Title:")
authorLabel = Label(window, text="Author:")
yearLabel = Label(window, text="Year:")
isbnLabel = Label(window, text="ISBN:")



# entry section
titleEntry = StringVar()
tEntry = Entry(window,textvariable=titleEntry)

authorEntry = StringVar()
aEntry = Entry(window,textvariable=authorEntry)

yearEntry = StringVar()
yEntry = Entry(window,textvariable=yearEntry)

isbnEntry = StringVar()
iEntry = Entry(window,textvariable=isbnEntry)

# button section
viewButton = Button(window,text="View books",width=12,command=view_command)
searchButton = Button(window,text="Search book",width=12,command=search_command)
addButton = Button(window,text="Add book",width=12,command=add_command)
updateButton = Button(window,text="Update book",width=12,command=update_command)
deleteButton = Button(window,text="Delete book",width=12,command=delete_command)
closeButton = Button(window,text="Close",width=12,command=window.destroy)


# list entry section
listEntries = Listbox(window,height=6,width=35)

#scroll bar section
listScrollBar = Scrollbar(window)

# grid section

# buttons
viewButton.grid(row=2,column=3)
searchButton.grid(row=3,column=3)
addButton.grid(row=4,column=3)
updateButton.grid(row=5,column=3)
deleteButton.grid(row=6,column=3)
closeButton.grid(row=7,column=3)

# labels
titleLabel.grid(row=0,column=0)
authorLabel.grid(row=0,column=2)
yearLabel.grid(row=1,column=0)
isbnLabel.grid(row=1,column=2)

# entries
tEntry.grid(row=0,column=1)
aEntry.grid(row=0,column=3)
yEntry.grid(row=1,column=1)
iEntry.grid(row=1,column=3)

# list entry
listEntries.grid(row=2,rowspan=6, column=0,columnspan=2)

# scroll bar
listScrollBar.grid(row=2,rowspan=6,column=2)

# configure section
listEntries.configure(yscrollcommand=listScrollBar.set)
listScrollBar.configure(command=listEntries.yview)

# bind section
listEntries.bind("<<ListboxSelect>>",get_selected_row)

window.mainloop()