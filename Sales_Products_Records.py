from tkinter import *
import tkinter.messagebox as msg
import Database
import time
import Showing_Records
# import Searching_Records
import pandas as pd
from PIL import ImageTk, Image
import Check_Profit_Loss_GUI


class data:
    count = []
    def __init__(self, Data=''):
        self.Data = Data
        # print("This is Paramter",self.Data)
        self.window = Tk()
        self.window.geometry("1365x700+0+0")
        self.window.iconbitmap('shop.ico')
        self.window.maxsize(1365, 700)
        self.window.minsize(1365, 700)
        self.window.title("Different Products | Shop")

    def add_background(self):
        self.image = Image.open("images/back.jpg")
        self.image = self.image.resize((1365, 700), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.image)
        self.li = Label(image=self.img, text="TALHA")
        self.li.image = self.img
        self.li.pack()

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
            pass
        else:
            self.l1 = Label(self.window, text="**Sales Products**", font="Courier 25 bold", bg="black", fg="white",
                            width=29)
            self.l1.place(x=330, y=55)

            self.l1 = Label(self.window, text="Developed by : Muhammad Talha | NTU", font="Courier 10 bold")
            self.l1.place(x=480, y=550)

            # enter product quantity
            self.l6 = Label(self.window, text="Enter Quantity:", font="courier 12 bold", bg="blue", fg="white")
            self.l6.place(x=330, y=400)
            self.entry6 = Entry(self.window, borderwidth=3, relief=SUNKEN, font="courier 12 bold",
                                width=12, textvariable=self.sales_quantity)
            self.entry6.place(x=500, y=400)

            # enter product price
            self.l7 = Label(self.window, text="price per product:", font="courier 12 bold", bg="blue", fg="white")
            self.l7.place(x=640, y=400)
            self.entry7 = Entry(self.window, borderwidth=3, relief=SUNKEN, font="courier 12 bold",
                                width=12, textvariable=self.price_per_product)
            self.entry7.place(x=840, y=400)

            # slaes_price
            self.l8 = Label(self.window, text="Sales Price:", font="courier 17 bold", bg="blue", fg="white")
            self.l8.place(x=330, y=450)
            self.entry8 = Entry(self.window, borderwidth=3, relief=SUNKEN, font="courier 16 bold",
                                width=25, textvariable=self.set_sales_price)
            self.entry8.place(x=580, y=450)

            # calculate price
            self.btn5 = Button(self.window, text="calculate", borderwidth=3, relief=GROOVE, font="courier 12 bold",
                               bg="blue", fg="white", command=self.caculate)
            self.btn5.place(x=980, y=400)

            self.entry6.bind('<KeyRelease>', self.remove)
            self.entry7.bind('<KeyRelease>', self.remove)

            # focus set on next entry widget
            def go_to_next_entry(event, entry_list, this_index):
                next_index = (this_index + 1) % len(entry_list)
                entry_list[next_index].focus_set()

            entries = [child for child in self.window.winfo_children() if isinstance(child, Entry)]
            for idx, entry in enumerate(entries):
                entry.bind('<Return>', lambda e, idx=idx: go_to_next_entry(e, entries, idx))

        # product name
        self.l1 = Label(self.window, text="Product Name:", font="courier 17 bold", bg="blue", fg="white")
        self.l1.place(x=330, y=150)
        self.entry1 = Entry(self.window, borderwidth=3, relief=SUNKEN, font="courier 16 bold",
                            width=25, textvariable=self.p_name)
        self.entry1.place(x=580, y=150)

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
        self.entry3.delete(0, END)

        # product purchase price
        self.l4 = Label(self.window, text="Purchase Price:", font="courier 17 bold", bg="blue", fg="white")
        self.l4.place(x=330, y=300)
        self.entry4 = Entry(self.window, borderwidth=3, relief=SUNKEN, font="courier 16 bold",
                            width=25, textvariable=self.p_purchase_price)
        self.entry4.place(x=580, y=300)
        self.entry4.delete(0, END)

        # product sales price
        self.l5 = Label(self.window, text="Sales Price:", font="courier 17 bold", bg="blue", fg="white")
        self.l5.place(x=330, y=350)
        self.entry5 = Entry(self.window, borderwidth=3, relief=SUNKEN, font="courier 16 bold",
                            width=25, textvariable=self.p_sales_price)
        self.entry5.place(x=580, y=350)
        self.entry5.delete(0, END)

        # add product button
        if self.Data == '':
            pass

        else:
            up = dict(self.Data).get('values')
            self.entry1.insert(0, up[0])
            self.entry2.insert(0, up[1])
            self.entry3.insert(0, up[2])
            self.entry4.insert(0, up[3])
            self.entry5.insert(0, up[4])
            self.btn1 = Button(self.window, text="Sales Product", borderwidth=3, relief=GROOVE, font="courier 15 bold",
                               bg="blue", fg="white", padx=205, command=self.sales_product)
            self.btn1.place(x=325, y=500)
        self.window.mainloop()


    def sales_product(self):
        x = dict(self.Data).get('values')
        text = x[1]
        # print(text)
        data = (self.entry1.get(), self.entry2.get(), self.entry6.get(), self.entry7.get(), self.entry8.get(),)

        # print(data)
        if self.entry6.get() == "" and self.entry7.get() == "" and self.entry8.get() == "":
            msg.showerror("Error","please insert data !!!")
        elif self.entry6.get() == "":
            msg.showerror("Error","please enter a quantity!!")
        elif self.entry7.get() == "":
            msg.showerror("Error","please enter a price per product!!")
        elif self.entry8.get() == "":
            msg.showerror("Error","please enter a sales price!!")
        elif self.entry6.get() or self.entry7.get() or self.entry8.get():
            try:
                int(self.entry6.get())
                float(self.entry7.get())
                float(self.entry8.get())
            except ValueError:
                msg.showwarning("Message ! ", "please insert quantity , price per product and sales price in valid format !")
            else:
                if self.entry3.get() <= '0':
                    msg.showinfo("Remaining Quantity",f"Quantity for this product {self.entry3.get()} ! please add quantity for this product!!!")
                    # time.sleep(1)
                    # self.window.destroy()
                elif eval(self.entry6.get()) > eval(self.entry3.get()):
                    msg.showinfo("Quantity",
                                 f"Only {self.entry3.get()} quantity for this product  ! please add right quantity for this product!!!")
                    # time.sleep(1)
                    # self.window.destroy()

                else:
                    # updated quantity in products table
                    q1 = self.entry3.get()
                    q2 = self.entry6.get()
                    res = eval(q1) - eval(q2)
                    update_quantity = (res, text)

                    # updated sales product in products table
                    s1 = self.entry5.get()
                    s2 = self.entry8.get()
                    res1 = eval(s1) + eval(s2)
                    update_sales_quantity = (res1, text)

                    res = Database.insert_sales_products(data)
                    print(res)
                    if res:
                        updated_success = Database.update_quantity_details(update_quantity)
                        updated_sales_price_success = Database.update_sales_price_details(update_sales_quantity)

                        msg.showinfo('Sales Product!', "Your sales product record has been added successfully !!!")
                        time.sleep(1)
                        self.window.destroy()
                    else:
                        msg.showinfo("ERROR ! ", "Something went wrong! please contact with developer!!!")
    def caculate(self):
        if self.entry6.get() == "" and self.entry7.get() == "":
            msg.showerror("Error","please insert data in required fileds!!!")
        elif self.entry6.get() == "":
            msg.showerror("Error","please enter a quantity!!")
        elif self.entry7.get() == "":
            msg.showerror("Error","please enter a price per product!!")
        else:
            a = self.entry6.get()
            b = self.entry7.get()
            res = eval(a) * eval(b)
            self.entry8.insert(0,str(res))
    def remove(self,event):
        self.entry8.delete(0,END)

    def check_profit_loss(self):
        self.window.destroy()
        showP = Check_Profit_Loss_GUI.show()
        showP.add_background()
        showP.add_table()


if __name__ == '__main__':
    x = data()
    x.add_background()
    x.add_frame()

