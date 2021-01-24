from tkinter import *

main_window = Tk()
main_window.title('Phone Book')


def saving(n, p):
    print(n, p)
    file = open('C:/Users/Albin/Desktop/Phonebook.txt', 'a+')
    file.close()


def add():
    add_window = Toplevel(main_window)
    add_window.title('Add Contact')
    name = Label(add_window, text='Name')
    name.pack()
    name_enter = Entry(add_window, width=25)
    name_enter.pack()
    phone = Label(add_window, text='Phone number')
    phone.pack()
    phone_enter = Entry(add_window, width=25)
    phone_enter.pack()
    n = name_enter.get()
    p = phone_enter.get()
    save = Button(add_window, text='Save', command=saving(n, p))
    save.pack()


def search():
    search_window = Toplevel(main_window)
    search_window.title('Search Contact')
    s_name = Label(search_window, text='Name')
    s_name.pack()
    s_name_enter = Entry(search_window, width=25)
    s_name_enter.pack()
    search_bu = Button(search_window, text='Search')
    search_bu.pack()


bu1 = Button(main_window, text='Search Contact', command=search)
bu1.pack()

bu2 = Button(main_window, text='Add Contact', command=add)
bu2.pack()

main_window.mainloop()
