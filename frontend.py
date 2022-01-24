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

window = Tk()

titleLabel = Label(window, text="Title:")
titleLabel.grid(row=0,column=0)

titleEntry = StringVar()
tEntry = Entry(window,textvariable=titleEntry)
tEntry.grid(row=0,column=1)

authorLabel = Label(window, text="Author:")
authorLabel.grid(row=0,column=2)

authorEntry = StringVar()
aEntry = Entry(window,textvariable=authorEntry)
aEntry.grid(row=0,column=3)

yearLabel = Label(window, text="Year:")
yearLabel.grid(row=1,column=0)

yearEntry = StringVar()
yEntry = Entry(window,textvariable=yearEntry)
yEntry.grid(row=1,column=1)

isbnLabel = Label(window, text="ISBN:")
isbnLabel.grid(row=1,column=2)

isbnEntry = StringVar()
iEntry = Entry(window,textvariable=isbnEntry)
iEntry.grid(row=1,column=3)

listEntries = Listbox(window,height=6,width=35)
listEntries.grid(row=2,rowspan=6, column=0,columnspan=2)

listScrollBar = Scrollbar(window)
listScrollBar.grid(row=2,rowspan=6,column=2)

listEntries.configure(yscrollcommand=listScrollBar.set)
listScrollBar.configure(command=listEntries.yview)

viewButton = Button(window,text="View all books",width=12)
viewButton.grid(row=2,column=3)

searchButton = Button(window,text="Search book",width=12)
searchButton.grid(row=3,column=3)

addButton = Button(window,text="Add book",width=12)
addButton.grid(row=4,column=3)

updateButton = Button(window,text="Update book",width=12)
updateButton.grid(row=5,column=3)

deleteButton = Button(window,text="Delete book",width=12)
deleteButton.grid(row=6,column=3)

closeButton = Button(window,text="Close",width=12)
closeButton.grid(row=7,column=3)


window.mainloop()