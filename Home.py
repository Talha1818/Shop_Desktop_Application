from tkinter import *
import tkinter.messagebox as msg
import Database
import time
import Showing_Records
# import Searching_Records
import pandas as pd
from PIL import ImageTk,Image
import Check_Products_Quantity
import Check_Sales_Products
import Check_Profit_Loss_GUI
import Check_Amount_Details
import Add_Customer
import Customer_Records

class data:
    def __init__(self, Data='') :
        self.Data = Data
        # print("This is Paramter",self.Data)
        self.window=Tk()
        self.window.geometry("1365x700+0+0")
        self.window.iconbitmap('shop.ico')
        self.window.maxsize(1365,700)
        self.window.minsize(1365,700)
        self.window.title("Different Products | Shop")

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

        self.menuitems_sales = Menu(self.menubar, tearoff=0,bg="blue",fg="white")
        self.menuitems_sales.add_command(label="Sale Products", command=self.sales_products)

        self.menuitems_customer = Menu(self.menubar, tearoff=0, bg="blue", fg="white")
        self.menuitems_customer.add_command(label="Add Customer", command=self.add_customer)
        self.menuitems_customer.add_command(label="Show Customer Records", command=self.customer_record)

        self.menuitems_reports = Menu(self.menubar, tearoff=0, bg="blue", fg="white")
        self.menuitems_reports.add_command(label="Check Products Quantity", command=self.check_products_quantity)
        self.menuitems_reports.add_command(label="Check Sales Products", command=self.check_products_sales)
        self.menuitems_reports.add_command(label="Check Profit/Loss", command=self.check_profit_loss)
        self.menuitems_reports.add_command(label="Check Sent Amount Details", command=self.check_amount)

        self.menubar.add_cascade(label="Add Products", menu=self.menuitems_add)
        self.menubar.add_cascade(label="Sales Products", menu=self.menuitems_sales)
        self.menubar.add_cascade(label="Customer", menu=self.menuitems_customer)
        self.menubar.add_cascade(label="Reports", menu=self.menuitems_reports)
        self.menubar.add_cascade(label="Exit", command=quit)
        self.window.config(menu=self.menubar)

    def add_frame(self):
        self.p_name = StringVar()
        self.p_catagory = StringVar()
        self.p_qunatity = StringVar()
        self.p_purchase_price = StringVar()
        self.p_sales_price = StringVar()
        self.sales_quantity = StringVar()
        self.set_sales_price = StringVar()
        self.price_per_product = StringVar()

        if self.Data == '':
            self.l1 = Label(self.window, text="**Adding Products**", font="Courier 25 bold", bg="black", fg="white",
                            width=29)
            self.l1.place(x=330, y=55)

            self.l1 = Label(self.window, text="Developed by : Muhammad Talha | NTU", font="Courier 10 bold")
            self.l1.place(x=480, y=465)
        else:
            self.l1 = Label(self.window, text="**Updating Products**", font="Courier 25 bold", bg="black", fg="white",
                            width=29)
            self.l1.place(x=330, y=55)

            self.l1 = Label(self.window, text="Developed by : Muhammad Talha | NTU", font="Courier 10 bold")
            self.l1.place(x=480, y=450)

            # product sales price
            self.l5 = Label(self.window, text="Sales Price:", font="courier 17 bold", bg="blue", fg="white")
            self.l5.place(x=330, y=350)
            self.entry5 = Entry(self.window, borderwidth=3, relief=SUNKEN, font="courier 16 bold",
                                width=25, textvariable=self.p_sales_price)
            self.entry5.place(x=580, y=350)


        # product name
        self.l1 = Label(self.window, text="Product Name:", font="courier 17 bold", bg="blue",fg="white")
        self.l1.place(x=330,y=150)
        self.entry1=Entry(self.window,borderwidth=3,relief=SUNKEN, font="courier 16 bold",
                         width=25,textvariable=self.p_name)
        self.entry1.place(x=580,y=150)

        # product catagory
        self.l2 = Label(self.window, text="Product Catagory:", font="courier 17 bold", bg="blue", fg="white")
        self.l2.place(x=330, y=200)
        self.entry2 = Entry(self.window, borderwidth=3, relief=SUNKEN, font="courier 16 bold",
                            width=25, textvariable=self.p_catagory)
        self.entry2.place(x=580, y=200)
        
        # product quantity
        self.l3 = Label(self.window, text="Product Quantity:", font="courier 17 bold", bg="blue", fg="white")
        self.l3.place(x=330, y=250)
        self.entry3 = Entry(self.window, borderwidth=3, relief=SUNKEN, font="courier 16 bold",
                            width=25, textvariable=self.p_qunatity)
        self.entry3.place(x=580, y=250)
        self.entry3.delete(0,END)

        # product purchase price
        self.l4 = Label(self.window, text="Purchase Price:", font="courier 17 bold", bg="blue", fg="white")
        self.l4.place(x=330, y=300)
        self.entry4 = Entry(self.window, borderwidth=3, relief=SUNKEN, font="courier 16 bold",
                            width=25, textvariable=self.p_purchase_price)
        self.entry4.place(x=580, y=300)
        self.entry4.delete(0, END)

        self.entry1.focus_set()

        # focus set on next entry widget
        def go_to_next_entry(event, entry_list, this_index):
            next_index = (this_index + 1) % len(entry_list)
            entry_list[next_index].focus_set()

        entries = [child for child in self.window.winfo_children() if isinstance(child, Entry)]
        for idx, entry in enumerate(entries):
            entry.bind('<Return>', lambda e, idx=idx: go_to_next_entry(e, entries, idx))

        # add product button
        if self.Data == '':
            self.btn1 = Button(self.window, text="Add Product", borderwidth=3, relief=GROOVE, font="courier 17 bold", bg="blue",fg="white",padx=205,command=self.add_product)
            self.btn1.place(x=330,y=400)

        else:
            up = dict(self.Data).get('values')
            self.entry1.insert(0,up[0])
            self.entry2.insert(0,up[1])
            self.entry3.insert(0,up[2])
            self.entry4.insert(0,up[3])
            self.entry5.insert(0,up[4])
            self.btn1 = Button(self.window, text="Update Product", borderwidth=3, relief=GROOVE, font="courier 15 bold",
                               bg="blue", fg="white", padx=205, command=self.update_product)
            self.btn1.place(x=325, y=400)

        self.window.mainloop()

    def add_product(self):
        data = (self.p_name.get(), self.p_catagory.get(), self.p_qunatity.get(), self.p_purchase_price.get(),self.p_sales_price.get())

        if self.p_name.get() == "" and self.p_catagory.get() == "" and self.p_qunatity.get() == "" and self.p_purchase_price.get() == "":
            msg.showwarning("Message ! ", "please insert data !")
        elif self.p_name.get() == "":
            msg.showwarning("Message ! ", "please insert product name!")
        elif self.p_name.get().isdigit():
            msg.showwarning("Message ! ", "Number not allowed in product name!")
        elif len(self.p_name.get()) <= 2:
            msg.showwarning("Message ! ", "Enter valid product name!")

        elif self.p_catagory.get() == "":
            msg.showwarning("Message!", "please insert product catagory!")
        elif self.p_catagory.get().isdigit():
            msg.showwarning("Message ! ", "Number not allowed in product catagory!")

        elif self.p_qunatity.get() == "":
            msg.showwarning("Message!", "please insert a product qunatity!")

        elif self.p_purchase_price.get()=="":
            msg.showwarning("Message!", "please insert a purchase price!")

        elif self.p_qunatity.get() or self.p_purchase_price.get():
            try:
                int(self.p_qunatity.get())
                float(self.p_purchase_price.get())
            except ValueError:
                msg.showwarning("Message ! ", "please insert quantity , purchase price in valid format !")
            else:
                res = Database.product_insert(data)
                if res:
                    msg.showinfo('Adding Product!', "Product added successfully !!!")
                    self.entry1.delete(0, END)
                    self.entry2.delete(0, END)
                    self.entry3.delete(0, END)
                    self.entry4.delete(0, END)
                    # self.entry5.delete(0, END)
                    self.entry1.focus_set()
                else:
                    msg.showwarning("Error!", "Something went wrong, please contact with developer!!!")


    def update_product(self):
        x = dict(self.Data).get('values')
        text = x[1]
        # print(text)
        data = (self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get(),self.entry5.get(), text)
        # print(data)
        res = Database.update_details(data)
        # print(res)

        if res:
            msg.showinfo("Message ! ", "Your product has been updated successfully !!!")
            time.sleep(1)
            self.window.destroy()
        else:
            msg.showinfo("ERROR ! ", "Something went wrong! please contact with developer!!!")

    def add_products(self):
        pass

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
        self.window.destroy()
        showP = Check_Profit_Loss_GUI.show()
        showP.add_background()
        showP.add_table()

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



if __name__ == '__main__':
    x=data()
    x.add_background()
    x.add_frame()

