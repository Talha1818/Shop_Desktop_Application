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
import Check_Profit_Loss_GUI
import Add_Customer
import Customer_Records

class show:
    def __init__(self):
        self.window=Tk()
        self.window.title("Show | Amount Details")
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
        self.l1=Label(self.window,text="**Sent Amount Details**",font="Courier 25 bold",bg="black",fg="white",width=61)
        self.l1.place(x=82,y=20)

        self.l1 = Label(self.window, text="Developed by : Muhammad Talha | NTU", font="Courier 10 bold")
        self.l1.place(x=470, y=610)

        self.l1 = Label(self.window, text="Enter Customer Name:", font="courier 16 bold",bg="blue",fg="white")
        self.l1.place(x=280, y=90)

        self.Entry_reg = Entry(self.window, font="courior 14 bold")
        self.Entry_reg.place(x=550, y=90, height=30)

        self.b1 = Button(self.window, text="Search", font="Times 13 bold",fg="white",bg="blue",width=10)
        self.b1.place(x=790, y=90)
        self.b1.bind('<Button-1>', self.search_product)


        # for Style Table
        style = Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                        font=('courier 12 bold'),rowheight=43)  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Times 15 bold'),foreground="black")  # Modify the font of the headings
        # style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders
        # import TreeViewe
        self.tr=Treeview(self.window,columns=('A','B','C','D'),selectmode="extended",style='mystyle.Treeview')
        # heading key+text
        self.tr.heading("#0", text="Sr.No")
        self.tr.column("#0", minwidth=0, width=85, stretch=NO)

        self.tr.heading("#1",text="Customer Name")
        self.tr.column("#1",minwidth=0,width=160,stretch=NO)

        self.tr.heading("#2", text="Product Detail")
        self.tr.column("#2", minwidth=0, width=200, stretch=NO)

        self.tr.heading("#3", text="Sent Amount")
        self.tr.column("#3", minwidth=0, width=175, stretch=NO)

        self.tr.heading("#4", text="Datetime")
        self.tr.column("#4", minwidth=0, width=250, stretch=NO)

        j=1
        for i in Database.show_amount_details():
            self.tr.insert('',index=j,text=j,values=(i[1],i[2],i[3],i[4]))
            j+=1

        self.Entry_reg.bind('<KeyRelease>', self.remove)

        self.sb = Scrollbar(self.tr)
        self.sb.place(x=850,y=2,height=452,width=22,bordermode=OUTSIDE)
        self.sb.config(command=self.tr.yview)
        self.tr.config(yscrollcommand=self.sb.set)
        self.tr.place(x=170,y=150)

        # to excel file
        self.b1 = Button(self.window, text="Save to Excel", font="Times 12 bold",bg="blue",fg="white",width=20,
        )
        self.b1.place(x=938, y=610)
        self.b1.bind('<Button-1>', self.excel)


        self.window.mainloop()


    def remove(self,event):
        for row in self.tr.get_children():
            self.tr.delete(row)
        j = 1
        for i in Database.show_amount_details():
            self.tr.insert('', index=j, text=j, values=(i[1], i[2], i[3], i[4]))
            j += 1

    def search_product(self,event):
        try:
            data = (self.Entry_reg.get(),)
            if self.Entry_reg.get() == "":
                msg.showwarning("Message ! ", "please insert customer name !")
            else:
                j = 1
                D = Database.search_details_amount_table(data)
                if D:
                    for row in self.tr.get_children():
                        self.tr.delete(row)
                    self.Entry_reg.delete(0, END)
                    for i in D:
                        self.tr.insert('', index=j, text=j, values=(i[1],i[2],i[3],i[4]))
                        j += 1
                else:
                    msg.showwarning("Message!", "No result Found!")

        except:
            msg.showwarning("Error!", "Something went wrong! please contact with developer !!!")
    def excel(self,event):
        try:
            x=Database.show_amount_details()
            c_name=[]
            p_detail=[]
            sent_amount=[]
            # date=[]
            for i in range(len(x)):
                z=x.__getitem__(i)
                c_name.append(z[1])
                p_detail.append(z[2])
                sent_amount.append(z[3])
                # date.append(z[4])

            products = pd.DataFrame({
                "Customer Name": c_name,
                "Product Detail":p_detail,
                "Sent Amount":sent_amount,
                # "Date":date,
            })

            with pd.ExcelWriter("Excel Files/Sent_Amount_Records.xlsx") as writer:
                products.to_excel(writer, sheet_name="Sales_Products", index=False)
            msg.showinfo("Message ! ", "Your data has been inserted Susccessfully !")
        except:
            msg.showwarning("Message!","Something Went Wrong!please contact with developer!!!")

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
        pass
    def check_profit_loss(self):
        self.window.destroy()
        showP = Check_Profit_Loss_GUI.show()
        showP.add_background()
        showP.add_table()
    def check_amount(self):
         pass
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
    x=show()
    x.add_background()
    x.add_table()