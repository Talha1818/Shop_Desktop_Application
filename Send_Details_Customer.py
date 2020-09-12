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
        self.c_name = StringVar()
        self.p_detail = StringVar()
        self.c_amount = StringVar()
        self.r_amount = StringVar()
        self.s_amount = StringVar()
        self.sent_amount = StringVar()
        self.sales_quantity = StringVar()
        self.set_sales_price = StringVar()
        self.price_per_product = StringVar()

        if self.Data == '':
            pass
        else:
            self.l1 = Label(self.window, text="**Send Amount**", font="Courier 25 bold", bg="black", fg="white",
                            width=29)
            self.l1.place(x=330, y=55)

            self.l1 = Label(self.window, text="Developed by : Muhammad Talha | NTU", font="Courier 10 bold")
            self.l1.place(x=480, y=550)

            # enter product quantity
            self.l6 = Label(self.window, text="Enter Amount:", font="courier 12 bold", bg="blue", fg="white")
            self.l6.place(x=330, y=400)
            self.entry6 = Entry(self.window, borderwidth=3, relief=SUNKEN, font="courier 12 bold",
                                width=12, textvariable=self.sent_amount)
            self.entry6.place(x=500, y=400)

            # calculate price
            # self.btn5 = Button(self.window, text="send", borderwidth=3, relief=GROOVE, font="courier 12 bold",
            #                    bg="blue", fg="white", command=self.caculate)
            # self.btn5.place(x=980, y=400)


            # focus set on next entry widget
            def go_to_next_entry(event, entry_list, this_index):
                next_index = (this_index + 1) % len(entry_list)
                entry_list[next_index].focus_set()

            entries = [child for child in self.window.winfo_children() if isinstance(child, Entry)]
            for idx, entry in enumerate(entries):
                entry.bind('<Return>', lambda e, idx=idx: go_to_next_entry(e, entries, idx))

        # product name
        self.l1 = Label(self.window, text="Customer Name:", font="courier 17 bold", bg="blue", fg="white")
        self.l1.place(x=330, y=150)
        self.entry1 = Entry(self.window, borderwidth=3, relief=SUNKEN, font="courier 16 bold",
                            width=25, textvariable=self.c_name)
        self.entry1.place(x=580, y=150)

        # product catagory
        self.l2 = Label(self.window, text="Product Details:", font="courier 17 bold", bg="blue", fg="white")
        self.l2.place(x=330, y=200)
        self.entry2 = Entry(self.window, borderwidth=3, relief=SUNKEN, font="courier 16 bold",
                            width=25, textvariable=self.p_detail)
        self.entry2.place(x=580, y=200)

        # product quantity
        self.l3 = Label(self.window, text="Total Amount:", font="courier 17 bold", bg="blue", fg="white")
        self.l3.place(x=330, y=250)
        self.entry3 = Entry(self.window, borderwidth=3, relief=SUNKEN, font="courier 16 bold",
                            width=25, textvariable=self.c_amount)
        self.entry3.place(x=580, y=250)
        self.entry3.delete(0, END)

        # product sales price
        self.l4 = Label(self.window, text="Remaining Amount", font="courier 17 bold", bg="blue", fg="white")
        self.l4.place(x=330, y=350)
        self.entry4 = Entry(self.window, borderwidth=3, relief=SUNKEN, font="courier 16 bold",
                            width=25, textvariable=self.r_amount)
        self.entry4.place(x=580, y=350)

        # product purchase price
        self.l5 = Label(self.window, text="Sent Amount:", font="courier 17 bold", bg="blue", fg="white")
        self.l5.place(x=330, y=300)
        self.entry5 = Entry(self.window, borderwidth=3, relief=SUNKEN, font="courier 16 bold",
                            width=25, textvariable=self.s_amount)
        self.entry5.place(x=580, y=300)

        self.entry1.focus_set()

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
            self.btn1 = Button(self.window, text="Send Amount", borderwidth=3, relief=GROOVE, font="courier 15 bold",
                               bg="blue", fg="white", padx=205, command=self.sales_product)
            self.btn1.place(x=325, y=500)
        self.window.mainloop()


    def sales_product(self):
        x = dict(self.Data).get('values')
        text = x[1]
        # print(text)
        data = (self.entry1.get(), self.entry2.get(), self.entry6.get(),)

        # print(data)
        if self.entry6.get() =="":
            msg.showwarning("Message ! ", "please insert sent amount!!!")
        elif self.entry6.get():
            try:
                float(self.entry6.get())
            except ValueError:
                msg.showwarning("Message ! ", "please insert amount in valid format !")
            else:
                    # updated quantity in products table
                    q1 = self.entry3.get()
                    q2 = self.entry6.get()
                    res = eval(q1) - eval(q2)
                    update_rem_amount = (res, text)

                    # updated sales product in products table
                    # s1 = self.entry5.get()
                    # s2 = self.entry8.get()
                    # res1 = eval(s1) + eval(s2)
                    update_sent_amount = (self.entry6.get(), text)

                    res = Database.insert_sent_amount(data)
                    print(res)
                    if res:
                        updated_success = Database.update_rem_amount_details(update_rem_amount)
                        updated_sales_price_success = Database.update_sent_amount_details(update_sent_amount)

                        msg.showinfo('Sales Product!', "Your Amount record has been added successfully !!!")
                        time.sleep(1)
                        self.window.destroy()
                    else:
                        msg.showinfo("ERROR ! ", "Something went wrong! please contact with developer!!!")

    def check_profit_loss(self):
        self.window.destroy()
        showP = Check_Profit_Loss_GUI.show()
        showP.add_background()
        showP.add_table()


if __name__ == '__main__':
    x = data()
    x.add_background()
    x.add_frame()

