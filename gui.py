from tkinter import *

class Application():

    def __init__(self, master):
        master.title("ScheduleApp")
        master.configure(background="#80bfff")

        self.title = Label(text="ScheduleApp", bg="#80bfff")
        self.title.grid(row=0)

        self.labelUsername = Label(master, text="Username:")
        self.labelUsername.grid(row=1, sticky=W)

        self.labelPassword = Label(master, text="Password:")
        self.labelPassword.grid(row=2, sticky=W)

        self.entryUsername = Entry(master)
        self.entryUsername.grid(row=1, column=1)

        self.entryPassword = Entry(master, show="*")
        self.entryPassword.grid(row=2, column=1)

        self.checkLoggedin = Checkbutton(master, text="Keep me logged in")
        self.checkLoggedin.grid(columnspan=2)

        self.logBtn = Button(master, text="Login", command=self.logIn_Click)
        self.logBtn.grid(row=4,column=0)

        self.quitBtn = Button(master, text="Quit", command=quit)
        self.quitBtn.grid(row=4,column=1)

    def logIn_Click(self):
        username = self.entryUsername.get()
        password = self.entryPassword.get()



root = Tk()

app = Application(root)

root.mainloop()