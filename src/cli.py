from src.api import (
    get_products,
    get_product,
    add_product,
    update_product,
    delete_product,
    search_products
)

from colorama import Fore, Style, init

init()


def show_menu():
    print(
        Fore.CYAN +
        """
========== PRODUCT API CLIENT ==========

1. List products
2. Search products
3. View product
4. Add product
5. Update product
6. Delete product
7. Exit

""" +
        Style.RESET_ALL
    )


def list_products():
    products = get_products()

    print(Fore.CYAN + "\n========= PRODUCTS ==========" + Style.RESET_ALL)

    if products:
        for product in products['products']:
            print(Fore.YELLOW + "-------------------" + Style.RESET_ALL)
            print("ID:", product['id'])
            print("NAME:", product['title'])
            print("PRICE:", product['price'])
            print("DISCOUNT:", product['discountPercentage'])

    else:
        print(Fore.RED + "No Products Found" + Style.RESET_ALL)

def search_product():
    query = input("Search product: ")

    result = search_products(query)

    print(Fore.CYAN + "\n========= SEARCH RESULTS =========" + Style.RESET_ALL)

    if result and result["products"]:
        for product in result["products"]:
            print(Fore.YELLOW + "-------------------" + Style.RESET_ALL)
            print("ID:", product["id"])
            print("NAME:", product["title"])
            print("PRICE:", product["price"])

    else:
        print(Fore.RED + "No products found" + Style.RESET_ALL)


def view_product():
    product_id = input("Enter product ID: ")

    try:
        product_id = int(product_id)

    except ValueError:
        print(Fore.RED + "Invalid ID" + Style.RESET_ALL)
        return

    product = get_product(product_id)

    print(Fore.CYAN + "\n========= PRODUCT =========" + Style.RESET_ALL)

    if product:
        print("ID:", product['id'])
        print("NAME:", product['title'])
        print("PRICE:", product['price'])

    else:
        print(Fore.RED + "Product not found" + Style.RESET_ALL)


def create_product():
    print(Fore.CYAN + "\n======= ADD PRODUCT =======" + Style.RESET_ALL)

    title = input("Product name: ")

    try:
        price = float(input("Price: "))
        stock = float(input("Stock: "))

    except ValueError:
        print(Fore.RED + "Invalid price or stock" + Style.RESET_ALL)
        return

    product = {
        "title": title,
        "price": price,
        "stock": stock
    }

    result = add_product(product)

    if result:
        print(Fore.GREEN + "\n✓ Product created!" + Style.RESET_ALL)
        print("ID:", result["id"])
        print("NAME:", result["title"])
        print("PRICE:", result["price"])

    else:
        print(Fore.RED + "✗ Failed to create product" + Style.RESET_ALL)


def edit_product():
    print(Fore.CYAN + "\n========== UPDATE PRODUCT ==========" + Style.RESET_ALL)

    try:
        product_id = int(input("Product ID: "))
        price = float(input("New price: "))

    except ValueError:
        print(Fore.RED + "Invalid input" + Style.RESET_ALL)
        return

    result = update_product(product_id, {"price": price})

    if result:
        print(Fore.GREEN + "\n✓ Product updated!" + Style.RESET_ALL)
        print("ID:", result["id"])
        print("NAME:", result["title"])
        print("PRICE:", result["price"])

    else:
        print(Fore.RED + "✗ Failed to update product" + Style.RESET_ALL)


def remove_product():
    print(Fore.CYAN + "\n========== DELETE PRODUCT ==========" + Style.RESET_ALL)

    try:
        product_id = int(input("Product ID: "))

    except ValueError:
        print(Fore.RED + "Invalid ID" + Style.RESET_ALL)
        return

    result = delete_product(product_id)

    if result:
        print(Fore.GREEN + "\n✓ Product deleted!" + Style.RESET_ALL)
        print("ID:", result["id"])
        print("NAME:", result["title"])
        print("Deleted:", result["isDeleted"])

    else:
        print(Fore.RED + "✗ Failed to delete product" + Style.RESET_ALL)


def run_cli():
    while True:
        show_menu()

        choice = input(Fore.MAGENTA + "Choose: " + Style.RESET_ALL)

        if choice == '1':
            list_products()

        elif choice == '2':
            search_product()

        elif choice == '3':
            view_product()

        elif choice == '4':
            create_product()

        elif choice == '5':
            edit_product()

        elif choice == '6':
            remove_product()

        elif choice == '7':
            print(Fore.GREEN + "Goodbye!" + Style.RESET_ALL)
            break

        else:
            print(Fore.YELLOW + "Invalid choice" + Style.RESET_ALL)