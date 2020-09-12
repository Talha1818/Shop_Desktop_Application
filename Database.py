import mysql.connector as mc
conn_bds=mc.connect(user="root",password="",host="localhost",database="stationary")
cursor_bds=conn_bds.cursor()

def product_insert(tup):
    try:
        cursor_bds.execute("insert into products(product_name,product_catagory,quantity,purchase_price,sales_price) values(%s,%s,%s,%s,%s)",tup)
        conn_bds.commit()
        return True
    except:
        return False

def insert_sales_products(tup):
    try:
        cursor_bds.execute("insert into sales_products(product_name,product_catagory,quantity,price_per_product,sales_price) values(%s,%s,%s,%s,%s)",tup)
        conn_bds.commit()
        return True
    except:
        return False

def show_product_details():
    cursor_bds.execute("select * from products")
    return cursor_bds.fetchall()

def show_sales_details():
    cursor_bds.execute("select * from sales_products")
    return cursor_bds.fetchall()


def delete_details(tup):
    cursor_bds.execute("delete from products where product_catagory=%s", tup)
    conn_bds.commit()
    return True

def update_details(tup):
    cursor_bds.execute("update products set product_name=%s,product_catagory=%s,quantity=%s,purchase_price=%s,sales_price=%s where product_catagory=%s",tup)
    conn_bds.commit()
    return True

def update_quantity_details(tup):
    cursor_bds.execute("update products set quantity=%s where product_catagory=%s",tup)
    conn_bds.commit()
    return True

def update_sales_price_details(tup):
    cursor_bds.execute("update products set sales_price=%s where product_catagory=%s",tup)
    conn_bds.commit()
    return True

def search_details(tup):
    cursor_bds.execute("select * from products where  product_name=%s",tup)
    return cursor_bds.fetchall()

def search_details_sales_table(tup):
    cursor_bds.execute("select * from sales_products where  product_name=%s",tup)
    return cursor_bds.fetchall()

def show_sales_date_details():
    cursor_bds.execute("select sales_price,date from sales_products")
    return cursor_bds.fetchall()

def profit_loss_insert(tup):
    try:
        cursor_bds.execute("insert into profit_loss(sales_price,date,profit,loss) values(%s,%s,%s,%s)",tup)
        conn_bds.commit()
        return True
    except:
        return False

def show_profit_loss_details():
    cursor_bds.execute("select * from profit_loss")
    return cursor_bds.fetchall()

def insert_full_day_sales_products(tup):
    try:
        cursor_bds.execute("insert into full_day_sales(total_sales) values(%s)",tup)
        conn_bds.commit()
        return True
    except:
        return False


def search_details_amount_table(tup):
    cursor_bds.execute("select * from sent_amount where customer_name=%s",tup)
    return cursor_bds.fetchall()


def show_sales_today_details(tup):
    cursor_bds.execute("select total_sales from full_day_sales where date = %s",tup)
    return cursor_bds.fetchone()

def customer_insert(tup):
    try:
        cursor_bds.execute("insert into customer(customer_name,product_detail,total_amount) values(%s,%s,%s)",tup)
        conn_bds.commit()
        return True
    except:
        return False

def show_customer_details():
    cursor_bds.execute("select * from customer")
    return cursor_bds.fetchall()
def delete_customer_details(tup):
    cursor_bds.execute("delete from customer where product_detail=%s", tup)
    conn_bds.commit()
    return True

def update_customer_details(tup):
    cursor_bds.execute("update customer set customer_name=%s,product_detail=%s,total_amount=%s,sent_amount=%s,remaining_amount=%s where product_detail=%s",tup)
    conn_bds.commit()
    return True

def insert_sent_amount(tup):
    try:
        cursor_bds.execute("insert into sent_amount(customer_name,product_detail,s_amount) values(%s,%s,%s)",tup)
        conn_bds.commit()
        return True
    except:
        return False

def update_rem_amount_details(tup):
    cursor_bds.execute("update customer set remaining_amount=%s where product_detail=%s",tup)
    conn_bds.commit()
    return True

def update_sent_amount_details(tup):
    cursor_bds.execute("update customer set sent_amount=%s where product_detail=%s",tup)
    conn_bds.commit()
    return True

def show_amount_details():
    cursor_bds.execute("select * from sent_amount")
    return cursor_bds.fetchall()

def search_customer_details(tup):
    cursor_bds.execute("select * from customer where  customer_name=%s",tup)
    return cursor_bds.fetchall()
# def search_details_bg(tup):
#     cursor_bds.execute("select * from bds where  bloodGroup=%s",tup)
#     return cursor_bds.fetchall()

# def get_name():
#     cursor_bds.execute("select quantity from products")
#     return cursor_bds.fetchone()
#
#
# def get_regno():
#     cursor_bds.execute("select RegNo from bds")
#     return cursor_bds.fetchall()
