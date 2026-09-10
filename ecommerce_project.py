import mysql.connector
import random
from datetime import date, timedelta
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Your_password,
    database="ecommerce_analytics"
    )
cursor=conn.cursor()
print("connected successfully!")


first_names = [
     "Rahul", "Priya", "Arjun", "Sneha", "Kiran",
     "Anjali", "Vikram", "Meena", "Rohit", "Divya",
     "Sai", "Lakshmi", "Harsha", "Keerthi", "Nikhil",
     "Shreya", "Rakesh", "Deepika", "Vamsi", "Tejas"
 ]

last_names = [
     "Sharma", "Reddy", "Kumar", "Rao", "Patel",
     "Singh", "Das", "Nair", "Verma", "Gupta"
 ]

cities = [
     ("Hyderabad", "Telangana"),
     ("Vijayawada", "Andhra Pradesh"),
     ("Bengaluru", "Karnataka"),
     ("Chennai", "Tamil Nadu"),
     ("Mumbai", "Maharashtra"),
     ("Pune", "Maharashtra"),
     ("Kochi", "Kerala"),
     ("Delhi", "Delhi")
 ]

customer_query = """
INSERT INTO customers
 (customer_id, customer_name, gender, age, city, state, signup_date)
VALUES (%s, %s, %s, %s, %s, %s, %s)
 """

customers = []

start_date = date(2024, 1, 1)

for customer_id in range(1, 1001):

     city, state = random.choice(cities)

     customers.append((
         customer_id,
         random.choice(first_names) + " " + random.choice(last_names),
         random.choice(["Male", "Female"]),
         random.randint(18, 60),
         city,
         state,
         start_date + timedelta(days=random.randint(0, 730))
     ))

cursor.executemany(customer_query, customers)

conn.commit()

print("1000 Customers Inserted Successfully!")






product_data = [
    ("Laptop", "Electronics", "Computers", 65000),
    ("Mobile", "Electronics", "Mobiles", 25000),
    ("Smart TV", "Electronics", "Television", 45000),
    ("Headphones", "Electronics", "Accessories", 3500),
    ("Camera", "Electronics", "Cameras", 50000),

    ("Running Shoes", "Fashion", "Footwear", 4500),
    ("Casual Shirt", "Fashion", "Clothing", 1800),
    ("Jeans", "Fashion", "Clothing", 2500),
    ("Backpack", "Fashion", "Bags", 2200),
    ("Smart Watch", "Fashion", "Watches", 6500),

    ("Office Chair", "Furniture", "Chairs", 8500),
    ("Study Table", "Furniture", "Tables", 12000),
    ("Bookshelf", "Furniture", "Storage", 9500),
    ("Sofa", "Furniture", "Sofas", 28000),
    ("Bed Frame", "Furniture", "Beds", 22000),

    ("Coffee Maker", "Home Appliances", "Kitchen", 5500),
    ("Mixer Grinder", "Home Appliances", "Kitchen", 4200),
    ("Vacuum Cleaner", "Home Appliances", "Cleaning", 9000),
    ("Air Cooler", "Home Appliances", "Cooling", 11000),
    ("Air Fryer", "Home Appliances", "Kitchen", 6500)
]
query = """
INSERT INTO products
(product_id, product_name, category, sub_category, price)
VALUES (%s, %s, %s, %s, %s)
"""

products = []

product_id = 1

for product, category, sub_category, price in product_data:

    for i in range(10):

        products.append((
            product_id,
            product + " " + str(i + 1),
            category,
            sub_category,
            price))
        product_id += 1

cursor.executemany(query, products)

conn.commit()

print("200 Products Inserted Successfully!")





order_query = """ 
INSERT INTO orders 
 (order_id, customer_id, product_id, order_date, 
 quantity, discount, payment_method, status) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s) 
 """ 
 
orders = [] 
start_order_date = date(2024, 1, 1) 
 
for order_id in range(21, 10001): 
 
     customer_id = random.randint(1, 1000) 
     product_id = random.randint(1, 200) 
 
     order_date = start_order_date + timedelta( 
         days=random.randint(0, 730) 
     ) 
 
     quantity = random.randint(1, 5) 
 
     discount = random.choice([0, 5, 10, 15, 20]) 
 
     payment_method = random.choice([ 
         "UPI", 
         "Card", 
         "Cash", 
         "Net Banking", 
         "Wallet" 
     ]) 
 
     status = random.choices( 
         ["Delivered", "Cancelled"], 
         weights=[93, 7] 
     )[0] 
 
     orders.append(( 
         order_id, 
         customer_id, 
         product_id, 
         order_date, 
         quantity, 
         discount, 
         payment_method, 
         status 
     )) 
 
cursor.executemany(order_query, orders) 
 
conn.commit() 
 
print("10000 Orders Inserted Successfully!")





return_query = """ 
INSERT INTO returns 
 (return_id, order_id, return_date, reason) 
VALUES (%s, %s, %s, %s) 
 """ 
 
returns = [] 
 
return_reasons = [ 
     "Size issue", 
     "Product damaged", 
     "Wrong product", 
     "Not satisfied", 
     "Late delivery", 
     "Quality issue" 
 ] 
 
   
cursor.execute(""" 
SELECT order_id, order_date 
 FROM orders 
WHERE status = 'Delivered' 
 """) 
 
delivered_orders = cursor.fetchall() 
 
selected_orders = random.sample( 
     delivered_orders, 
     500 
) 
 
for return_id, (order_id, order_date) in enumerate( 
     selected_orders, start=1 
 ): 
 
     return_date = order_date + timedelta( 
         days=random.randint(3, 30) 
     ) 
 
     reason = random.choice(return_reasons) 
 
     returns.append(( 
         return_id, 
         order_id, 
         return_date, 
         reason 
     )) 
 
cursor.executemany(return_query, returns) 
 
conn.commit() 
 
print("500 Returns Inserted Successfully!")


cursor.close()
conn.close()

print("FULL DATASET CREATED SUCCESSFULLY!")
