from tkinter import *
import tkinter.messagebox

import random
import math

import pymysql as sql

db = sql.connect("localhost", "root", "admin123", "bank")

c = db.cursor()


class Application:

    def __init__(self, master):
        self.master = master
        self.pas = ""
        self.user = ""
        self.input = ""
        self.main = Frame(master, width=800, height=720)
        self.main.pack(side=TOP)

        self.heading = Label(self.main, text="Admin", fg='steelblue', font='arial 40 bold')
        self.heading.place(x=150, y=0)

        self.name = Label(self.main, text="Username", font='arial 18 bold')
        self.name.place(x=0, y=60)

        self.namenet = Entry(self.main, width=30)
        self.namenet.place(x=280, y=62)

        self.name1 = Label(self.main, text="Password", font='arial 18 bold')
        self.name1.place(x=0, y=100)

        self.namenet1 = Entry(self.main, width=30)
        self.namenet1.place(x=280, y=102)

        self.search = Button(self.main, text="Login", width=12, height=1, bg='steelblue', command=self.search_db)
        self.search.place(x=350, y=150)

    def search_db(self):
        self.input = self.namenet.get()

        sql = "select * from bank where Username='%s'" % self.input
        c.execute(sql)
        self.res = c.fetchall()
        for self.row in self.res:
            self.user = self.row[0]
            self.pas = self.row[1]

        self.input1 = self.namenet1.get()
        if (self.input1 == self.pas):
            Dashboard(root, self.input)
            self.main.destroy()
        else:
            tkinter.messagebox.showwarning("Wrong password", "Password entered is wrong")


class Dashboard:

    def __init__(self, frame, input):
        self.frame = frame
        self.user = input
        self.main = Frame(self.frame, width=800, height=720)
        self.main.pack(side=TOP)

        self.heading1 = Label(self.main, text="Welcome " + self.user, fg='steelblue', font=('arial 40 bold'))

        self.heading1.place(x=150, y=50)
        self.heading = Label(self.main, text="Dashboard", fg='steelblue', font=('arial 40 bold'))
        self.heading.place(x=150, y=0)
        self.create1 = Button(self.main, text="Create Account", width=12, height=1, bg='steelblue',
                              command=self.create_acc)
        self.create1.place(x=350, y=250)
        self.withdraw = Button(self.main, text="Withdraw", width=12, height=1, bg='steelblue', command=self.withdraw)
        self.withdraw.place(x=350, y=350)
        self.check_bal = Button(self.main, text="Check balance", width=12, height=1, bg='steelblue',
                                command=self.check_bal)
        self.check_bal.place(x=350, y=450)
        self.deposit = Button(self.main, text="Deposit", width=12, height=1, bg='steelblue', command=self.deposit)
        self.deposit.place(x=550, y=250)
        self.transfer_mon = Button(self.main, text="Transfer Money", width=12, height=1, bg='steelblue',
                                   command=self.transfer_mon)
        self.transfer_mon.place(x=550, y=350)
        self.principle = Button(self.main, text="Principle of bank", width=12, height=1, bg='steelblue')
        self.principle.place(x=550, y=450)
        self.interest = Button(self.main, text="Interest", width=12, height=1, bg='steelblue',command=self.interest)
        self.interest.place(x=350, y=550)
        self.logout = Button(self.main, text="Logout", width=12, height=1, bg='steelblue', command=self.logout)
        self.logout.place(x=650, y=650)

    def create_acc(self):
        self.main.destroy()
        Create(root, self.user)

    def withdraw(self):
        self.main.destroy()
        Withdraw(root, self.user)

    def deposit(self):
        self.main.destroy()
        Deposit(root, self.user)

    def transfer_mon(self):
        self.main.destroy()
        Transfer(root, self.user)

    def check_bal(self):
        self.main.destroy()
        Check(root, self.user)

    def logout(self):
        self.main.destroy()
        Application(root)
    def interest(self):
        self.main.destroy()
        Interest(root,self.user)


class Create:

    def __init__(self, master, user):
        self.master = master
        self.input = ""
        self.input2 = ""
        self.random_str = ""
        self.user = user
        self.main = Frame(master, width=800, height=720)
        self.main.pack(side=TOP)

        self.heading = Label(self.main, text="Create Account", fg='steelblue', font=('arial 40 bold'))
        self.heading.place(x=150, y=0)

        self.name = Label(self.main, text="Name", font=('arial 18 bold'))
        self.name.place(x=0, y=60)

        self.namenet = Entry(self.main, width=30)
        self.namenet.place(x=280, y=62)

        self.name1 = Label(self.main, text="Money deposited", font=('arial 18 bold'))
        self.name1.place(x=0, y=100)

        self.namenet1 = Entry(self.main, width=30)
        self.namenet1.place(x=280, y=102)

        self.search = Button(self.main, text="Create Account", width=12, height=1, bg='steelblue',
                             command=self.create_acc)
        self.search.place(x=350, y=150)
        self.back = Button(self.main, text="Dashboard", width=12, height=1, bg='steelblue', command=self.back)
        self.back.place(x=350, y=250)

    def create_acc(self):
        self.input = self.namenet.get()
        self.input2 = self.namenet1.get()
        self.acc_no()
        sql = "INSERT INTO bank2 values ('%s','%s','%s')" % (self.input, self.input2, self.random_str)
        c.execute(sql)
        db.commit()

        tkinter.messagebox.showinfo("Account Number", "Account Number generated is " + self.random_str)
        self.random_str = ""

    def acc_no(self):
        digits = [i for i in range(0, 10)]

        for i in range(6):
            index = math.floor(random.random() * 10)

            self.random_str += str(digits[index])

    def back(self):
        self.main.destroy()
        Dashboard(root, self.user)


class Withdraw:

    def __init__(self, master, user):
        self.master = master
        self.input = ""
        self.input1 = ""
        self.acc_no = ""
        self.money = ""
        self.user = user
        self.main = Frame(master, width=800, height=720)
        self.main.pack(side=TOP)

        self.heading = Label(self.main, text="Withdraw", fg='steelblue', font=('arial 40 bold'))
        self.heading.place(x=150, y=0)

        self.name = Label(self.main, text="Account Number", font=('arial 18 bold'))
        self.name.place(x=0, y=60)

        self.namenet = Entry(self.main, width=30)
        self.namenet.place(x=280, y=62)

        self.name1 = Label(self.main, text="Withdraw Amount", font=('arial 18 bold'))
        self.name1.place(x=0, y=100)

        self.namenet1 = Entry(self.main, width=30)
        self.namenet1.place(x=280, y=102)

        self.search = Button(self.main, text="Withdraw", width=12, height=1, bg='steelblue', command=self.withdraw)
        self.search.place(x=350, y=150)
        self.back = Button(self.main, text="Dashboard", width=12, height=1, bg='steelblue', command=self.back)
        self.back.place(x=350, y=250)

    def back(self):
        self.main.destroy()
        Dashboard(root, self.user)

    def withdraw(self):
        self.input = self.namenet.get()
        self.input1 = self.namenet1.get()
        sql = "SELECT * FROM bank2 WHERE acc_no='%s'" % self.input
        c.execute(sql)
        self.res = c.fetchall()
        for self.row in self.res:
            self.acc_no = self.row[2]
            self.money = self.row[1]
        self.money = int(self.money) - int(self.input1)

        sql = "UPDATE bank2 SET money ='%s' WHERE acc_no='%s'" % (self.money, self.acc_no)
        c.execute(sql)
        db.commit()


class Deposit:

    def __init__(self, master, user):
        self.master = master
        self.input = ""
        self.input1 = ""
        self.acc_no = ""
        self.money = ""
        self.user = user
        self.main = Frame(master, width=800, height=720)
        self.main.pack(side=TOP)

        self.heading = Label(self.main, text="Deposit", fg='steelblue', font=('arial 40 bold'))
        self.heading.place(x=150, y=0)

        self.name = Label(self.main, text="Account Number", font=('arial 18 bold'))
        self.name.place(x=0, y=60)

        self.namenet = Entry(self.main, width=30)
        self.namenet.place(x=280, y=62)

        self.name1 = Label(self.main, text="Deposit Money", font=('arial 18 bold'))
        self.name1.place(x=0, y=100)

        self.namenet1 = Entry(self.main, width=30)
        self.namenet1.place(x=280, y=102)

        self.search = Button(self.main, text="Deposit", width=12, height=1, bg='steelblue', command=self.withdraw)
        self.search.place(x=350, y=150)
        self.back = Button(self.main, text="Dashboard", width=12, height=1, bg='steelblue', command=self.back)
        self.back.place(x=350, y=250)

    def back(self):
        self.main.destroy()
        Dashboard(root, self.user)

    def withdraw(self):
        self.input = self.namenet.get()
        self.input1 = int(self.namenet1.get())
        sql = "SELECT * FROM bank2 WHERE acc_no='%s'" % self.input
        c.execute(sql)
        self.res = c.fetchall()
        for self.row in self.res:
            self.acc_no = self.row[2]
            self.money = self.row[1]
        self.money = self.money + self.input1
        sql = "UPDATE bank2 SET money ='%s' WHERE acc_no ='%s'" % (self.money, self.acc_no)
        c.execute(sql)
        db.commit()


class Transfer:

    def __init__(self, master, user):
        self.master = master
        self.input = ""
        self.input1 = ""
        self.input2 = ""
        self.money1 = ""
        self.money2 = ""
        self.user = user

        self.main = Frame(master, width=800, height=720)
        self.main.pack(side=TOP)

        self.heading = Label(self.main, text="Transfer Money", fg='steelblue', font=('arial 40 bold'))
        self.heading.place(x=150, y=0)

        self.name = Label(self.main, text="From Account Number", font=('arial 18 bold'))
        self.name.place(x=0, y=60)
        self.name2 = Label(self.main, text="To Account Number", font=('arial 18 bold'))
        self.name2.place(x=0, y=100)

        self.namenet1 = Entry(self.main, width=30)
        self.namenet1.place(x=280, y=112)

        self.namenet = Entry(self.main, width=30)
        self.namenet.place(x=280, y=62)

        self.name1 = Label(self.main, text="Money to be sent", font=('arial 18 bold'))
        self.name1.place(x=0, y=150)

        self.namenet2 = Entry(self.main, width=30)
        self.namenet2.place(x=280, y=152)
        self.search = Button(self.main, text="Transfer Money", width=12, height=1, bg='steelblue',
                             command=self.transfer)
        self.search.place(x=350, y=200)

        self.back = Button(self.main, text="Dashboard", width=12, height=1, bg='steelblue', command=self.back)
        self.back.place(x=350, y=250)

    def back(self):
        self.main.destroy()
        Dashboard(root, self.user)

    def transfer(self):
        self.input = self.namenet.get()

        self.input1 = self.namenet1.get()
        self.input2 = int(self.namenet2.get())

        sql = "SELECT * FROM bank2 WHERE acc_no='%s'" % (self.input)
        c.execute(sql)
        self.res = c.fetchall()

        for self.row in self.res:
            self.money1 = self.row[1]
        print(self.money1)
        sql = "SELECT * FROM bank2 WHERE acc_no='%s'" % (self.input1)
        c.execute(sql)
        self.res1 = c.fetchall()
        for self.row1 in self.res1:
            self.money2 = self.row1[1]

        self.money1 = self.money1 - self.input2

        self.money2 = self.money2 + self.input2
        sql = "UPDATE bank2 SET money ='%s' WHERE acc_no='%s'" % (self.money1, self.input)
        c.execute(sql)
        sql = "UPDATE bank2 SET money ='%s' WHERE acc_no='%s'" % (self.money2, self.input1)
        c.execute(sql)
        db.commit()


class Check:

    def __init__(self, master, user):
        self.master = master
        self.input = ""

        self.money = ""
        self.user = user

        self.main = Frame(master, width=800, height=720)
        self.main.pack(side=TOP)

        self.heading = Label(self.main, text="Check Balance", fg='steelblue', font=('arial 40 bold'))
        self.heading.place(x=150, y=0)

        self.name = Label(self.main, text="Account Number", font=('arial 18 bold'))
        self.name.place(x=0, y=60)

        self.namenet = Entry(self.main, width=30)
        self.namenet.place(x=280, y=62)
        self.name1 = Label(self.main, text="Balance is", font=('arial 18 bold'))
        self.name1.place(x=350, y=100)

        self.search = Button(self.main, text="Check Balance", width=12, height=1, bg='steelblue', command=self.check)
        self.search.place(x=350, y=150)
        self.back = Button(self.main, text="Dashboard", width=12, height=1, bg='steelblue', command=self.back)
        self.back.place(x=340, y=250)

    def back(self):
        self.main.destroy()
        Dashboard(root, self.user)

    def check(self):
        self.input = self.namenet.get()
        sql = "SELECT * FROM bank2 WHERE acc_no='%s'" % self.input
        c.execute(sql)
        self.res = c.fetchall()
        for self.row in self.res:
            self.money = self.row[1]
        self.name1.destroy()
        self.name1 = Label(self.main, text="Balance is " + str(self.money), font=('arial 18 bold'))
        self.name1.place(x=340, y=100)
class Interest:
    def __init__(self, master,user):
        self.master = master
        self.input = ""
        self.user=user
        self.money = ""



        self.main = Frame(master, width=800, height=720)
        self.main.pack(side=TOP)

        self.heading = Label(self.main, text="Interest", fg='steelblue', font=('arial 40 bold'))
        self.heading.place(x=150, y=0)

        self.name = Label(self.main, text="Account Number", font=('arial 18 bold'))
        self.name.place(x=0, y=60)

        self.namenet = Entry(self.main, width=30)
        self.namenet.place(x=280, y=62)
        self.name1 = Label(self.main, text="Interest at 5% is", font=('arial 18 bold'))
        self.name1.place(x=350, y=100)

        self.search = Button(self.main, text="Calculate Interest", width=12, height=1, bg='steelblue', command=self.check)
        self.search.place(x=350, y=150)
        self.back = Button(self.main, text="Dashboard", width=12, height=1, bg='steelblue', command=self.back)
        self.back.place(x=340, y=250)

    def back(self):
        self.main.destroy()
        Dashboard(root, self.user)

    def check(self):
        self.input = self.namenet.get()
        sql = "SELECT * FROM bank2 WHERE acc_no='%s'" % self.input
        c.execute(sql)
        self.res = c.fetchall()
        for self.row in self.res:
            self.money = self.row[1]
        self.money=self.money*5/100

        self.name1.destroy()
        self.name1 = Label(self.main, text="Interest at 5% is " + str(self.money), font=('arial 18 bold'))
        self.name1.place(x=340, y=100)



root = Tk()

b = Application(root)
root.geometry("1200x720+0+0")

root.mainloop()
