# Product API Client

A lightweight Python client for the [DummyJSON](https://dummyjson.com) Products API.
Wraps the four core REST operations (list, create, update, delete) behind typed,
tested functions with proper error handling — no raw `requests` calls scattered
through the app code.

## Features

- **Typed interface** — every function has type hints and a docstring
- **Centralized error handling** — network failures and bad HTTP status codes
  (4xx/5xx) are both caught via `raise_for_status()`, logged, and turned into a
  clean `None` return instead of an unhandled exception
- **Request timeouts** — no call can hang indefinitely
- **Unit tested** — all four functions are covered with mocked requests, so the
  test suite runs instantly and requires no network access or live API

## Project Structure

```
product-api-client/
├── main.py              # Demo script: list, add, update, delete a product
├── src/
│   └── api.py            # API client functions
├── tests/
│   └── test_api.py       # Unit tests (mocked, no network calls)
├── requirements.txt
└── .gitignore
```

## Setup

```bash
git clone <your-repo-url>
cd product-api-client
pip install -r requirements.txt
```

## Usage

Run the demo script:

```bash
python main.py
```

This will fetch all products, add a new one, update an existing one, and delete
one — printing the result of each step.

Or import the client into your own code:

```python
from src.api import get_products, add_product

data = get_products()
if data:
    for product in data["products"]:
        print(product["title"], product["price"])

new_item = add_product({"title": "Gaming Controller", "price": 80, "stock": 50})
```

## Running Tests

```bash
pytest tests/ -v
```

All API calls are mocked (`unittest.mock.patch`), so tests run without hitting
the real API and pass consistently regardless of network conditions.

## Error Handling

Every function returns `dict | None`:
- Returns the parsed JSON response on success (2xx status)
- Returns `None` and logs the error on network failure or a non-2xx response

This keeps error handling out of calling code — check for `None`, nothing else.

## Notes

DummyJSON is a public sandbox/mock API. Write operations (`add`, `update`,
`delete`) are simulated by the server and are **not actually persisted** —
running the demo repeatedly will not accumulate real data.

## License

MIT

## Author

MohammadAmin