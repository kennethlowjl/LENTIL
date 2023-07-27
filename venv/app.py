from tkinter import *
from tkinter import messagebox

def submit_request():
    messagebox.showinfo("Success", "Help request submitted successfully")

def open_dropdown(category):
    for widget in root.winfo_children():
        widget.destroy()

    var = StringVar(root)
    choices = ['I\'m stuck', 'I can work around for now', 'Just for information']
    var.set('Select an option')

    drop_down = OptionMenu(root, var, *choices)
    drop_down.pack()

    comments = Entry(root)
    comments.insert(0, "Any additional comments")
    comments.pack()

    submit_button = Button(root, text="Submit Request", command=submit_request)
    submit_button.pack()

    return_main_button = Button(root, text="Return to Main Page", command=open_main_window)
    return_main_button.pack()

    return_help_button = Button(root, text="Return to Request Help Page", command=open_help_request_page)
    return_help_button.pack()

def open_help_request_page():
    for widget in root.winfo_children():
        widget.destroy()

    categories = ['IDE', 'Compiling', 'Libraries', 'Subversion', 'Trac', 'Java', 'Python', 'C', 'Assessment', 'Course Material']
    for i, category in enumerate(categories):
        button = Button(root, text=category, command=lambda category=category: open_dropdown(category))
        button.grid(row=i, column=0, sticky='w')

    return_button = Button(root, text="Return to Main Page", command=open_main_window)
    return_button.grid(row=len(categories), column=1, sticky='se')

def open_main_window():
    root.deiconify()  #show root window.
    
    #clear main window.
    for widget in root.winfo_children():
        widget.destroy()

    request_help_button = Button(root, text='Request Help', command=open_help_request_page)
    request_help_button.grid(row=1, column=1, sticky='se')

def check_login():
    if username_entry.get() == 'student1' and password_entry.get() == 'student1':
        messagebox.showinfo("Success", "Login Successful")
        #after successful login, destroy login window and open main window.
        login_window.destroy()
        open_main_window()
    else:
        messagebox.showerror("Error", "Invalid Credentials")

#create root window but keep it hidden until login is completed.
root = Tk()
root.geometry('500x500')
root.title('Main Page')
root.withdraw()

#create login window.
login_window = Toplevel(root)
login_window.geometry('300x150')
login_window.title('Login Page')

username_label = Label(login_window, text='Username')
username_label.pack()

username_entry = Entry(login_window)
username_entry.pack()

password_label = Label(login_window, text='Password')
password_label.pack()

password_entry = Entry(login_window, show='*')
password_entry.pack()


login_button = Button(login_window, text='Login', command=check_login)
login_button.pack()

#start app.py
root.mainloop()
