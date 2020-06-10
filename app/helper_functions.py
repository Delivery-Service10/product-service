from models import Product
import uuid


def populate_product(data):
    new_product = Product(public_id=str(uuid.uuid4()),
                          name=data['name'],
                          brand=data['brand'],
                          size=data['size'],
                          description=data['description'],
                          category=data['category'],
                          )
    return new_product


def allocate_data(product):
    product_data = {'public_id': product.public_id,
                    'name': product.name,
                    'brand': product.brand,
                    'size': product.size,
                    'category': product.category,
                    'description': product.description,
                    }
    return product_data


def combine_results(products):
    output = []
    for product in products:
        product_data = allocate_data(product)
        output.append(product_data)
    return output
