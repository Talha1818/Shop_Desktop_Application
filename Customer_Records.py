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
import Add_Customer
import Send_Details_Customer
import Check_Amount_Details
import Showing_Records

class show:
    def __init__(self):
        self.window=Tk()
        self.window.title("Show | All Customer")
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
        self.l1=Label(self.window,text="**Customer Details**",font="Courier 25 bold",bg="black",fg="white",width=61)
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
        self.tr=Treeview(self.window,columns=('A','B','C','D','E','F','G','H','I'),selectmode="extended",style='mystyle.Treeview')
        # heading key+text
        self.tr.heading("#0", text="sr#")
        self.tr.column("#0", minwidth=0, width=40, stretch=NO)

        self.tr.heading("#1",text="Customer Name")
        self.tr.column("#1",minwidth=0,width=160,stretch=NO)

        self.tr.heading("#2", text="Product Detail")
        self.tr.column("#2", minwidth=0, width=200, stretch=NO)

        self.tr.heading("#3", text="Total Amount")
        self.tr.column("#3", minwidth=0, width=175, stretch=NO)

        self.tr.heading("#4", text="Sent Amount")
        self.tr.column("#4", minwidth=0, width=160, stretch=NO)

        self.tr.heading("#5", text="Rem Amount")
        self.tr.column("#5", minwidth=0, width=160, stretch=NO)

        self.tr.heading("#6", text="Datetime")
        self.tr.column("#6", minwidth=0, width=170, stretch=NO)

        self.tr.heading("#7", text="Update")
        self.tr.column("#7", minwidth=0, width=85, stretch=NO)

        self.tr.heading("#8", text="Delete")
        self.tr.column("#8", minwidth=0, width=85, stretch=NO)

        self.tr.heading("#9", text="Send")
        self.tr.column("#9", minwidth=0, width=85, stretch=NO)
        j=1
        for i in Database.show_customer_details():
            self.tr.insert('',index=j,tags=i[0],text=j,values=(i[1],i[2],i[3],i[4],i[5],i[6],"UPDATE","DELETE","SEND"))
            j+=1

        self.Entry_reg.bind('<KeyRelease>', self.remove)
        self.tr.bind('<Double-Button-1>',self.action)


        self.sb = Scrollbar(self.tr)
        self.sb.place(x=1300,y=2,height=452,width=22,bordermode=OUTSIDE)
        self.sb.config(command=self.tr.yview)
        self.tr.config(yscrollcommand=self.sb.set)
        self.tr.place(x=30,y=150)
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
        if col=="#8":
            res=msg.askyesno("Message!","Do you want to delete this product?")
            if res:
                d=Database.delete_customer_details(data)
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
        elif col=="#7":
            x=Add_Customer.data(self.tr.item(fcs))
            x.add_frame()
        elif col=="#9":
            x = Send_Details_Customer.data(self.tr.item(fcs))
            x.add_frame()


    def remove(self,event):
        for row in self.tr.get_children():
            self.tr.delete(row)
        j = 1
        for i in Database.show_customer_details():
            self.tr.insert('', index=j, text=j, values=(i[1], i[2], i[3], i[4], i[5],i[6], "UPDATE", "DELETE", "SEND"))
            j += 1

    def search_product(self,event):
        try:
            data = (self.Entry_reg.get(),)
            if self.Entry_reg.get() == "":
                msg.showwarning("Message ! ", "please insert customer name !")
            else:
                j = 1
                D = Database.search_customer_details(data)
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
            x=Database.show_customer_details()
            c_name=[]
            p_detail=[]
            t_amount=[]
            s_amount=[]
            r_amount=[]
            for i in range(len(x)):
                z=x.__getitem__(i)
                c_name.append(z[1])
                p_detail.append(z[2])
                t_amount.append(z[3])
                s_amount.append(z[4])
                r_amount.append(z[5])

            products = pd.DataFrame({
                "Customer Name": c_name,
                "Product Detail":p_detail,
                "Total Amount":t_amount,
                "Sent Amount":s_amount,
                "Remaining Amount":r_amount
            })

            with pd.ExcelWriter("Excel Files/All_Customer_Details.xlsx") as writer:
                products.to_excel(writer, sheet_name="All_Customer_Details", index=False)
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
        self.window.destroy()
        showP = Check_Sales_Products.show()
        showP.add_background()
        showP.add_table()

    def check_amount(self):
        self.window.destroy()
        showP = Check_Amount_Details.show()
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
        pass


if __name__ == '__main__':
    x=show()
    x.add_background()
    x.add_table()