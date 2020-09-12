from tkinter import *
import tkinter.messagebox as msg
from tkinter.ttk import Treeview, Style
import Database
import Home
import pandas as pd
from PIL import ImageTk,Image
import Check_Products_Quantity
import Check_Sales_Products
import Sales_Products_Records
import Check_Profit_Loss_GUI
import Check_Amount_Details
import Add_Customer
import Customer_Records

class show:
    def __init__(self):
        self.window=Tk()
        self.window.title("Show | All Products")
        self.window.iconbitmap('shop.ico')
        self.window.geometry("1365x700+10+10")
        self.window.maxsize(1365,700)
        self.window.minsize(1365,700)
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
        self.l1=Label(self.window,text="**Products Details**",font="Courier 25 bold",bg="black",fg="white",width=61)
        self.l1.place(x=82,y=20)

        self.l1 = Label(self.window, text="Developed by : Muhammad Talha | NTU", font="Courier 10 bold")
        self.l1.place(x=530, y=610)

        self.l1 = Label(self.window, text="Enter Product Name:", font="courier 16 bold",bg="blue",fg="white")
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
        self.tr=Treeview(self.window,columns=('A','B','C','D','E','F','G','H'),selectmode="extended",style='mystyle.Treeview')
        # heading key+text
        self.tr.heading("#0", text="Sr.No")
        self.tr.column("#0", minwidth=0, width=85, stretch=NO)

        self.tr.heading("#1",text="Product Name")
        self.tr.column("#1",minwidth=0,width=160,stretch=NO)

        self.tr.heading("#2", text="Product Catagory")
        self.tr.column("#2", minwidth=0, width=200, stretch=NO)

        self.tr.heading("#3", text="Total Quantity")
        self.tr.column("#3", minwidth=0, width=175, stretch=NO)

        self.tr.heading("#4", text="Purchase Price")
        self.tr.column("#4", minwidth=0, width=175, stretch=NO)

        self.tr.heading("#5", text="Sales Price")
        self.tr.column("#5", minwidth=0, width=160, stretch=NO)

        self.tr.heading("#6", text="Update")
        self.tr.column("#6", minwidth=0, width=85, stretch=NO)

        self.tr.heading("#7", text="Delete")
        self.tr.column("#7", minwidth=0, width=85, stretch=NO)

        self.tr.heading("#8", text="Sales")
        self.tr.column("#8", minwidth=0, width=100, stretch=NO)
        j=1
        for i in Database.show_product_details():
            self.tr.insert('',index=j,tags=i[0],text=j,values=(i[1],i[2],i[3],i[4],i[5],"UPDATE","DELETE","SALES"))
            j+=1

        self.Entry_reg.bind('<KeyRelease>', self.remove)
        self.tr.bind('<Double-Button-1>',self.action)


        self.sb = Scrollbar(self.tr)
        self.sb.place(x=1205,y=2,height=452,width=22,bordermode=OUTSIDE)
        self.sb.config(command=self.tr.yview)
        self.tr.config(yscrollcommand=self.sb.set)
        self.tr.place(x=85,y=150)
        self.tr.tag_configure('data', background='black')

        # to excel file
        self.b1 = Button(self.window, text="Save to Excel", font="Times 12 bold",bg="blue",fg="white",width=20,
        )
        self.b1.place(x=1122, y=610)
        self.b1.bind('<Button-1>', self.excel)


        self.window.mainloop()
    def action(self,event):
        fcs=self.tr.focus()
        col=self.tr.identify_column(event.x)
        x=self.tr.item(fcs).get('values')
        text=x[1]
        data=(
            text,
        )
        if col=="#7":
            res=msg.askyesno("Message!","Do you want to delete this product?")
            if res:
                d=Database.delete_details(data)
                if d:
                    msg.showinfo("Deleted","Your product has been deleted successfully!!!")
                    self.window.destroy()
                    x=show()
                    x.add_background()
                    x.add_table()
                else:
                    self.window.destroy()
                    x=show()
                    x.add_table()
        elif col=="#6":
            x=Home.data(self.tr.item(fcs))
            x.add_frame()
        elif col=="#8":
            x = Sales_Products_Records.data(self.tr.item(fcs))
            x.add_frame()


    def remove(self,event):
        for row in self.tr.get_children():
            self.tr.delete(row)
        j = 1
        for i in Database.show_product_details():
            self.tr.insert('', index=j, text=j, values=(i[1], i[2], i[3], i[4], i[5], "UPDATE", "DELETE", "SALES"))
            j += 1

    def search_product(self,event):
        try:
            data = (self.Entry_reg.get(),)
            if self.Entry_reg.get() == "":
                msg.showwarning("Message ! ", "please insert product name !")
            else:
                j = 1
                D = Database.search_details(data)
                if D:
                    for row in self.tr.get_children():
                        self.tr.delete(row)
                    self.Entry_reg.delete(0, END)
                    for i in D:
                        self.tr.insert('', index=j, text=j, values=(i[1],i[2],i[3],i[4],i[5],"UPDATE","DELETE","SALES"))
                        j += 1
                else:
                    msg.showwarning("Message!", "No result Found!")

        except:
            msg.showwarning("Error!", "Something went wrong! please contact with developer !!!")
    def excel(self,event):
        try:
            x=Database.show_product_details()
            p_name=[]
            p_catagory=[]
            p_quantity=[]
            p_purchase_price=[]
            p_sales_price=[]
            for i in range(len(x)):
                z=x.__getitem__(i)
                p_name.append(z[1])
                p_catagory.append(z[2])
                p_quantity.append(z[3])
                p_purchase_price.append(z[4])
                p_sales_price.append(z[5])

            products = pd.DataFrame({
                "Product Name": p_name,
                "Product Catagory":p_catagory,
                "Total Quantity":p_quantity,
                "Purchase Price":p_purchase_price,
                "Sales Price":p_sales_price
            })

            with pd.ExcelWriter("Excel Files/All_Products.xlsx") as writer:
                products.to_excel(writer, sheet_name="All_Products", index=False)
            msg.showinfo("Message ! ", "Your data has been inserted Susccessfully !")
        except:
            msg.showwarning("Message!","Something Went Wrong!please contact with developer!!!")


    def add_products(self):
        self.window.destroy()
        home = Home.data()
        home.add_background()
        home.add_frame()

    def sales_products(self):
        pass
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

    def check_amount(self):
        self.window.destroy()
        showP = Check_Amount_Details.show()
        showP.add_background()
        showP.add_table()


if __name__ == '__main__':
    x=show()
    x.add_background()
    x.add_table()