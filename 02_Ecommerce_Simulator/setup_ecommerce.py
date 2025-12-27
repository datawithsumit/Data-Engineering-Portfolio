import datetime
import time
import sqlite3
import random

cities = ["Mumbai", "Delhi", "Bangalore", "Pune", "Chennai"]
categories = ["Electronics", "Books", "Clothing", "Home"]
products = {
    "iPhone 15": 70000,
    "Macbook Air": 90000,
    "Harry Potter": 500,
    "T-Shirt": 800,
    "Smart Watch": 3000
}

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

sql = """
CREATE TABLE IF NOT EXISTS orders(
order_id TEXT PRIMARY KEY,
timestamp TEXT,
city TEXT,
product_name TEXT,
category TEXT,
price INTEGER,
quantity INTEGER
)
"""
cursor.execute(sql)
conn.commit()
conn.close()

print("--- ECOMMERCE SIMULATOR STARTED ---")
while True:
    city = random.choice(cities)
    product = random.choice(list(products.keys()))
    category = random.choice(categories)
    price = products[product]
    quantity = random.randint(1,5)
    oid = "ORD-" + str(random.randint(1000,9999))
    now = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")

    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()

    sql = """INSERT INTO ORDERS (
    order_id, timestamp, city, product_name, category, price, quantity
    )
    VALUES (?,?,?,?,?,?,?)
    """
    cursor.execute(sql,(oid,now,city,product,category,price,quantity))
    conn.commit()
    conn.close()

    total_bill = price*quantity
    print(f"{now} NEW ORDER {oid}:{quantity} x {product} from {city}, Total_price = ₹{total_bill}")

    time.sleep(2)
