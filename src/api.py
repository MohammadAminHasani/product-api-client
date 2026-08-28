import requests
import logging


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

BASE_URL = 'https://dummyjson.com'
TIMEOUT = 10

def get_products() -> dict | None:

    try:
        response = requests.get(f"{BASE_URL}/products" , timeout=TIMEOUT)

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as error:

        logger.error('GET Error: %s' , error)

        return None
    
def add_product(product: dict)-> dict | None:
    try:
        url = f"{BASE_URL}/products/add"

        response = requests.post(url,json=product,timeout=TIMEOUT)

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as error:

        logger.error('POST Error : %s', error)

        return None

def update_product(product_id: int,update_data: dict)-> dict | None:

    try:
        url=(f"{BASE_URL}/products/{product_id}")

        response = requests.put(url , json=update_data, timeout=TIMEOUT)

        response.raise_for_status()

        return response.json()
    
    except requests.exceptions.RequestException as error:

        logger.error("PUT Error : %s" , error)

        return None

def delete_product(product_id: int)-> dict | None:
    try:

        url=(f"{BASE_URL}/products/{product_id}")

        response = requests.delete(url, timeout=TIMEOUT)

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as error:
        
        logger.error("DELETE Error: %s" , error)

        return None