from tkinter import *
import os

#login system with GUI
def GUI_login():
    cur_path = os.path.dirname(__file__)
    final_path = os.path.join(cur_path+"\\user_info\\")
    def register_user():
        username_info = username.get()
        password_info = password.get()
        cpassword_info = cpassword.get()

        if password_info == cpassword_info:
            with open(final_path+username_info+".txt","w") as f:
                f.write(username_info+":"+password_info)
                f.close()
                Button(screen1, text = "Back",height = "1", width = "10", command = screen1.destroy).pack()
            username_entry.delete(0,END)
            password_entry.delete(0,END)
            cpassword_entry.delete(0,END)
            Label(screen1, text = "Registration Success", fg = "green",font = ("Calibri",11)).pack()
        else:
            Label(screen1, text = "Password does not match", fg = "red",font = ("Calibri",11)).pack()

    def login_verify():
        username1 = username_verify.get()
        password1 = password_verify.get()
        username_entry1.delete(0, END)
        password_entry1.delete(0, END)
        value = os.path.exists(final_path+username1+".txt")
        if value == True:
            file = open(final_path+username1+".txt", "r")
            data   = file.readline()
            file.close()
            if data == username1+":"+password1:
                Button(screen2, text = "Start",height = "1", width = "10", command =screen.destroy).pack()
                Label(screen2, text = "Login Successful", fg = "green",font = ("Calibri",11)).pack()
                print("Welcome back,",username1)
            else:
                Label(screen2, text = "Incorrect password.", fg = "red",font = ("Calibri",11)).pack()
        else:
            Label(screen2, text = "Username does not exists", fg = "red",font = ("Calibri",11)).pack()

       
    def register():
        global screen1
        screen1 = Toplevel(screen)
        screen1.title("Register")
        screen1.geometry("300x250")
        windowWidth = screen1.winfo_reqwidth()
        windowHeight = screen1.winfo_reqheight()
        positionRight = int(screen1.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(screen1.winfo_screenheight()/2 - windowHeight/2)
        screen1.geometry("+{}+{}".format(positionRight,positionDown))
        
        global username
        global password
        global cpassword
        global username_entry
        global password_entry
        global cpassword_entry
        username = StringVar()
        password = StringVar()
        cpassword = StringVar()

        Label(screen1, text = "Please enter the details below.").pack()
        Label(screen1, text = "").pack()
        Label(screen1, text = "Enter a username").pack()
        username_entry = Entry(screen1, textvariable = username)
        username_entry.pack()
        Label(screen1, text = "Enter a password").pack()
        password_entry = Entry(screen1, textvariable = password, show = "*")
        password_entry.pack()
        Label(screen1, text = "Confirm password").pack()
        cpassword_entry = Entry(screen1, textvariable = cpassword, show = "*")
        cpassword_entry.pack()
        Label(screen1, text = "").pack()
        Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

    def login():
        global screen2
        screen2 = Toplevel(screen)
        screen2.title("Login")
        screen2.geometry("300x250")
        windowWidth = screen2.winfo_reqwidth()
        windowHeight = screen2.winfo_reqheight()
        positionRight = int(screen2.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(screen2.winfo_screenheight()/2 - windowHeight/2)
        screen2.geometry("+{}+{}".format(positionRight,positionDown))
        Label(screen2, text = "Please enter details below to login").pack()
        Label(screen2, text = "").pack()

        global username_verify
        global password_verify

        username_verify = StringVar()
        password_verify = StringVar()

        global username_entry1
        global password_entry1
        
        Label(screen2, text = "Username").pack()
        username_entry1 = Entry(screen2, textvariable = username_verify)
        username_entry1.pack()
        Label(screen2, text = "").pack()
        Label(screen2, text = "Password").pack()
        password_entry1 = Entry(screen2, textvariable = password_verify, show = "*")
        password_entry1.pack()
        Label(screen2, text = "").pack()
        Button(screen2, text="Login", width = 10, height =1, command = login_verify).pack()

    def main_screen():
        global screen
        screen = Tk()
        screen.geometry("300x250")
        screen.overrideredirect(True)

        def disable_event():
            pass
        windowWidth = screen.winfo_reqwidth()
        windowHeight = screen.winfo_reqheight()
        positionRight = int(screen.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(screen.winfo_screenheight()/2 - windowHeight/2)
        screen.title("Fit Mou")
        screen.geometry("+{}+{}".format(positionRight,positionDown))
        Label(text = "Fit Mou", bg = "grey", width = "300", height = "2", font = ("Calibri",13)).pack()
        Label(text = "").pack()
        Button(text = "Login", height = "2", width = "30", command = login).pack()
        Label(text = "").pack()
        Button(text = "Register", height = "2", width = "30", command = register).pack()

        screen.protocol("WM_DELETE_WINDOW", disable_event)
        screen.mainloop()

    main_screen()

