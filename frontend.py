from tkinter import *
from backend import Database

#Instantiate database object
database = Database()


def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass


def view_command():
    list1.delete(0, END)
    for row in database.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in database.search(task_text.get(), date_text.get(), time_text.get(), priority_text.get()):
        list1.insert(END, row)


def add_command():
    database.insert(task_text.get(), date_text.get(), time_text.get(), priority_text.get())
    list1.delete(0, END)
    list1.insert(END, (task_text.get(), date_text.get(), time_text.get(), priority_text.get()))


def update_command():
    database.update(selected_tuple[0], task_text.get(), date_text.get(), time_text.get(), priority_text.get())


def delete_command():
    database.delete(selected_tuple[0])


window = Tk()

# Create task label
l1 = Label(window, text="Task")
l1.grid(row=0, column=0)

# Create date label
l2 = Label(window, text="Date")
l2.grid(row=0, column=2)

# Create time label
l3 = Label(window, text="Time")
l3.grid(row=1, column=0)

# Create priority label
l4 = Label(window, text="Priority")
l4.grid(row=1, column=2)

# Create entry for user to name the task
task_text = StringVar()
e1 = Entry(window, textvariable=task_text)
e1.grid(row=0, column=1)

# Create entry for user to provide the date task is due
date_text = StringVar()
e2 = Entry(window, textvariable=date_text)
e2.grid(row=0, column=3)

# Create entry for user to provide the time task is due
time_text = StringVar()
e3 = Entry(window, textvariable=time_text)
e3.grid(row=1, column=1)

# Create entry for user to define the priority
priority_text = StringVar()
e4 = Entry(window, textvariable=priority_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

list1.bind('<<ListboxSelect>>', get_selected_row)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#View all tasks button
b1 = Button(window, text="View all tasks", width=12, command=view_command)
b1.grid(row=2, column=3)

#Search button
b2 = Button(window, text="Search", width=12, command=search_command)
b2.grid(row=3, column=3)

#Addd button
b3 = Button(window, text="Add task", width=12, command=add_command)
b3.grid(row=4, column=3)

#Updatebutton
b4 = Button(window, text="Update task", width=12, command=update_command)
b4.grid(row=5, column=3)

#Delete button
b5 = Button(window, text="Delete task", width=12, command=delete_command)
b5.grid(row=6, column=3)

#Close button
b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
