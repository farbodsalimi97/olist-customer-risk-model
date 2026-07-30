import pandas as pd

orders = pd.read_csv("olist_orders_dataset.csv")
order_items = pd.read_csv( "olist_order_items_dataset.csv")
customers = pd.read_csv( "olist_customers_dataset.csv")
products = pd.read_csv( "olist_products_dataset.csv")
payments = pd.read_csv("olist_order_payments_dataset.csv")
reviews = pd.read_csv( "olist_order_reviews_dataset.csv")
sellers = pd.read_csv( "olist_sellers_dataset.csv")
category_translation = pd.read_csv("product_category_name_translation.csv")
