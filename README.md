# Product API Client

[Python](https://www.python.org/) [Status: Completed]

**Product API Client is a Python CLI application for managing product data through a REST API.**

The application provides a terminal-based interface for working with product data, including retrieving, searching, creating, updating, and deleting products.

## What it can do

- Fetch all products
- Search products by keyword
- View product details by ID
- Create new products
- Update existing products
- Delete products
- Handle API and network errors
- Display colored terminal output
- Log application errors
- Run automated API tests

## How it works

The application separates user interaction and API communication into different modules.

The CLI handles user input and displays results, while the API layer manages requests, responses, and error handling.

```
User Input
    ↓
CLI Interface
    ↓
API Client
    ↓
REST API
    ↓
Response Processing
    ↓
Terminal Output
```

## Project Structure

```
product-api-client/
│
├── src/
│   ├── api.py          # REST API communication layer
│   ├── cli.py          # Command-line interface
│   └── main.py         # Application entry point
│
├── tests/
│   └── test_api.py     # API unit tests
│
├── requirements.txt
├── README.md
└── .gitignore
```

The project is organized into separate modules to keep API operations, user interaction, and testing responsibilities independent.

## Built With

- **Python**
- **Requests**
- **Pytest**
- **Colorama**
- **DummyJSON REST API**
- **Python Logging**

## Example Output

```
========== PRODUCT API CLIENT ==========

1. List products
2. Search products
3. View product
4. Add product
5. Update product
6. Delete product
7. Exit


========= SEARCH RESULTS =========

-------------------
ID: 81
NAME: Lenovo Yoga 920
PRICE: 1099.99

-------------------
ID: 159
NAME: iPad Mini 2021 Starlight
PRICE: 499.99
```

*Results depend on the selected search term and API data.*

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/MohammadAminHasani/product-api-client.git

cd product-api-client
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python src/main.py
```

## Testing

Run the test suite:

```bash
python -m pytest
```

Example output:

```
6 passed
```

## Project Status

**Completed**

Product API Client is complete within its current CLI scope.

The project was built to practice working with REST APIs, CRUD operations, Python application structure, error handling, logging, and automated testing.

## License

MIT License

## Author

**MohammadAmin**