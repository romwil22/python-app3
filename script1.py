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
listEntries.grid(row=2,)

window.mainloop()