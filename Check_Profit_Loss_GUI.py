from tkinter import *
import tkinter.messagebox as msg
from tkinter.ttk import Treeview, Style
import Database
import Home
import pandas as pd
from PIL import ImageTk,Image
import Sales_Products_Records
import Showing_Records
import Check_Products_Quantity
import datetime
from math import fabs
import Check_Sales_Products
import Check_Amount_Details
import Add_Customer
import Customer_Records

class show:
    def __init__(self):
        self.window=Tk()
        self.window.title("Show | Profit Loss")
        self.window.iconbitmap('shop.ico')
        self.window.geometry("1365x670+0+0")
        self.window.maxsize(1365,670)
        self.window.minsize(1365,670)
        # self.window.resizable(width=False,height=False)
    def add_background(self):
        self.image = Image.open("images/back.jpg")
        self.image = self.image.resize((1365, 700), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.image)
        self.li = Label(image = self.img, text="TALHA")
        self.li.image = self.img
        self.li.pack()
        self.Menubar()

    def Menubar(self):
        self.menubar = Menu()
        self.menuitems_add = Menu(self.menubar, tearoff=0,bg="blue",fg="white")
        self.menuitems_add.add_command(label="Add Products", command=self.add_products)
        # self.menuitems.add_separator()

        self.menuitems_sales = Menu(self.menubar, tearoff=0,bg="blue",fg="white")
        self.menuitems_sales.add_command(label="Sale Products", command=self.sales_products)

        self.menuitems_customer = Menu(self.menubar, tearoff=0, bg="blue", fg="white")
        self.menuitems_customer.add_command(label="Add Customer", command=self.add_customer)
        self.menuitems_customer.add_command(label="Show Customer Records", command=self.customer_record)


        self.menuitems_reports = Menu(self.menubar, tearoff=0, bg="blue", fg="white")
        self.menuitems_reports.add_command(label="Check Products Quantity", command=self.check_products_quantity)
        self.menuitems_reports.add_command(label="Check Profit/Loss", command=self.check_profit_loss)
        self.menuitems_reports.add_command(label="Check Sales Products", command=self.check_products_sales)
        self.menuitems_reports.add_command(label="Check Sent Amount Details", command=self.check_amount)

        self.menubar.add_cascade(label="Add Products", menu=self.menuitems_add)
        self.menubar.add_cascade(label="Sales Products", menu=self.menuitems_sales)
        self.menubar.add_cascade(label="Customer", menu=self.menuitems_customer)
        self.menubar.add_cascade(label="Reports", menu=self.menuitems_reports)
        self.menubar.add_cascade(label="Exit", command=quit)
        self.window.config(menu=self.menubar)

    def add_table(self):
        self.l1=Label(self.window,text="**Profit/Loss Details**",font="Courier 25 bold",bg="black",fg="white",width=61)
        self.l1.place(x=82,y=20)

        self.l1 = Label(self.window, text="Developed by : Muhammad Talha | NTU", font="Courier 10 bold")
        self.l1.place(x=470, y=610)

        # now date
        now = datetime.datetime.today().strftime('%Y-%m-%d')
        # previous date
        prev = datetime.datetime.today() - datetime.timedelta(days=1)
        prev = prev.strftime("%Y-%m-%d")

        # total profit
        date = Database.show_sales_date_details()
        total_sales_today = 0
        total_sales_prev = 0
        profit = 0
        loss = 0
        for i in range(0, len(date)):
            if f"{date[i][1]}" == f"{now}":
                total_sales_today = total_sales_today + date[i][0]

            if f"{date[i][1]}" == f"{prev}":
                total_sales_prev = total_sales_prev + date[i][0]

        if total_sales_today < total_sales_prev:
            loss_sales = total_sales_today - total_sales_prev
            loss = loss + loss_sales
            profit = 0
        if total_sales_today == total_sales_prev:
            loss = 0
            profit = 0
        if total_sales_today > total_sales_prev:
            profit_sales = total_sales_today - total_sales_prev
            profit = profit + profit_sales
            loss = 0


        self.l2 = Label(self.window, text="Total Sales Yesterday:", font="courier 25 bold", bg="blue", fg="white")
        self.l2.place(x=300, y=170)
        self.l2 = Label(self.window, text=total_sales_prev, font="courier 25 bold", bg="black", fg="white")
        self.l2.place(x=760, y=170)

        self.l3 = Label(self.window, text="Total Sales Today:", font="courier 25 bold", bg="blue", fg="white")
        self.l3.place(x=300, y=220)
        self.l3 = Label(self.window, text=total_sales_today, font="courier 25 bold", bg="black", fg="white")
        self.l3.place(x=760, y=220)

        self.l3 = Label(self.window, text="Profit:", font="courier 25 bold", bg="blue", fg="white")
        self.l3.place(x=300, y=270)
        self.l3 = Label(self.window, text=profit, font="courier 25 bold", bg="black", fg="white")
        self.l3.place(x=760, y=270)

        self.l3 = Label(self.window, text="Loss:", font="courier 25 bold", bg="blue", fg="white")
        self.l3.place(x=300, y=320)
        self.l3 = Label(self.window, text=fabs(loss), font="courier 25 bold", bg="black", fg="white")
        self.l3.place(x=760, y=320)

        self.extras = StringVar()

        self.l1 = Label(self.window, text="Enter today spent money :", font="courier 17 bold", bg="blue", fg="white")
        self.l1.place(x=300, y=450)
        self.entry1 = Entry(self.window, borderwidth=3, relief=SUNKEN, font="courier 16 bold",
                            width=15, textvariable=self.extras)
        self.entry1.place(x=700, y=450)
        self.entry1.focus_set()
        self.btn1 = Button(self.window, text="ADD", borderwidth=3, relief=GROOVE, font="courier 12 bold",
                           bg="blue", fg="white",padx=12, command=self.add_product)
        self.btn1.place(x=920, y=450)





        self.window.mainloop()


    def add_products(self):
        self.window.destroy()
        home = Home.data()
        home.add_background()
        home.add_frame()

    def sales_products(self):
        self.window.destroy()
        showP = Showing_Records.show()
        showP.add_background()
        showP.add_table()
    def check_products_quantity(self):
        self.window.destroy()
        showP = Check_Products_Quantity.show()
        showP.add_background()
        showP.add_table()
    def check_products_sales(self):
        self.window.destroy()
        showP = Check_Sales_Products.show()
        showP.add_background()
        showP.add_table()
    def check_profit_loss(self):
        pass

    def check_amount(self):
        self.window.destroy()
        showP = Check_Amount_Details.show()
        showP.add_background()
        showP.add_table()
    def add_customer(self):
        self.window.destroy()
        home = Add_Customer.data()
        home.add_background()
        home.add_frame()
    def customer_record(self):
        self.window.destroy()
        showP = Customer_Records.show()
        showP.add_background()
        showP.add_table()

    def add_product(self):
        if self.extras.get() == "":
            msg.showwarning("Message ! ", "please insert spent money!")
        elif self.entry1.get():
            try:
                int(self.entry1.get())
            except ValueError:
                msg.showwarning("Message ! ","please insert spent money in valid format !")
            else:
                # now date
                now = datetime.datetime.today().strftime('%Y-%m-%d')
                # previous date
                prev = datetime.datetime.today() - datetime.timedelta(days=1)
                prev = prev.strftime("%Y-%m-%d")

                # total profit
                date = Database.show_sales_date_details()
                total_sales_today = 0
                total_sales_prev = 0
                profit = 0
                loss = 0
                for i in range(0, len(date)):
                    if f"{date[i][1]}" == f"{now}":
                        total_sales_today = total_sales_today + date[i][0]

                    if f"{date[i][1]}" == f"{prev}":
                        total_sales_prev = total_sales_prev + date[i][0]

                if total_sales_today < total_sales_prev:
                    loss_sales = total_sales_today - total_sales_prev
                    loss = loss + loss_sales
                    profit = 0
                if total_sales_today == total_sales_prev:
                    loss = 0
                    profit = 0
                if total_sales_today > total_sales_prev:
                    profit_sales = total_sales_today - total_sales_prev
                    profit = profit + profit_sales
                    loss = 0

                total_sales_today = total_sales_today - eval(self.entry1.get())


                self.l3 = Label(self.window, text="Total Sales after adding spent Money:", font="courier 25 bold", bg="blue", fg="white")
                self.l3.place(x=300, y=220)
                self.l3 = Label(self.window, text=total_sales_today, font="courier 25 bold", bg="black", fg="white")
                self.l3.place(x=1050, y=220)
                msg.showwarning("Message ! ", "Your spent money has been inserted successfully!")
                self.entry1.delete(0,END)






if __name__ == '__main__':
    x=show()
    x.add_background()
    x.add_table()