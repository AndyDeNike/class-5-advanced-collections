from data import products_string

def transform_products_to_list(products_string):
    split_products = products_string.split('\n')
    products_list = []
    for product_line in split_products:
        if product_line: #if product is True .....   if product != ''
            product = product_line.split(',')
            products_list.append(product)
    return products_list
    
transform_products_to_list(products_string)