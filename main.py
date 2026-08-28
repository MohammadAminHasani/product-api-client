from src.api import (
    get_products,
    add_product,
    update_product,
    delete_product
)

def main():
    products = get_products()
    
    print("\n========== PRODUCTS ==========")
    
    
    if products:
    
        for product in products['products']:
            print("----------------")
            print("ID: ",product['id'])
            print("NAME: ",product['title'])
            print("PRICE: ",product['price'])
            print("Discount: ",product['discountPercentage'])
    
    else:
        print('No Products Found')
    
    
    new_product = {
        'title':'Gaming Controller',
        'price':80,
        'stock': 50
    }
    
    added = add_product(new_product)
    
    
    print("\n========== ADDED PRODUCT ==========")
    
    if added:
    
        print("ID: ",added['id'])
        print("NAME: ",added['title'])
        print('PRICE: ',added['price'])
    
    else:
    
        print('Failed To Add Product')
    
    updated = update_product(
        1,
        {
            'price':330
        }
    )
    
    print("\n========== UPDATED ==========")
    
    if updated:
    
        print("ID: ",updated['id'])
        print("NAME: ",updated['title'])
        print('PRICE: ',updated['price'])
    
    else:
    
        print('Failed To Update Product')
    
    deleted = delete_product(1)
    
    print("\n========== DELETED ==========")
    
    if deleted:
    
        print("ID: ",deleted['id'])
        print("NAME: ",deleted['title'])
        print("Deleted:", deleted["isDeleted"])
    
    else:
    
        print('Failed To Delete Product')

if __name__ == '__main__':
    main()