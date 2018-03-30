from step_1 import transform_products_to_list
from data import products_string
from pprint import pprint

def group_products_by_customer_and_invoice(products_string):
    products_list = transform_products_to_list(products_string)
    customers = {}
    for product in products_list:
        invoice_id = product[0]
        customer_id = product[-2]
        customers.setdefault(customer_id, {})
        customers[customer_id].setdefault(invoice_id, [])
        customers[customer_id][invoice_id].append(product)
    return customers
    
customers = group_products_by_customer_and_invoice(products_string)
pprint(customers)
customer_id = customers['12583']


print(customers['12583']['536370'][0][2])