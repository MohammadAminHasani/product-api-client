from unittest.mock import patch, Mock
import requests
from src.api import get_products, add_product, update_product, delete_product


@patch("src.api.requests.get")
def test_get_products_success(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {"products": [{"id": 1, "title": "Phone"}]}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = get_products()
    assert result["products"][0]["title"] == "Phone"


@patch("src.api.requests.get")
def test_get_products_network_error(mock_get):
    mock_get.side_effect = requests.exceptions.ConnectionError("no internet")
    result = get_products()
    assert result is None


@patch("src.api.requests.post")
def test_add_product_success(mock_post):
    mock_response = Mock()
    mock_response.json.return_value = {"id": 101, "title": "Gaming Controller"}
    mock_response.raise_for_status.return_value = None
    mock_post.return_value = mock_response

    result = add_product({"title": "Gaming Controller", "price": 80})
    assert result["id"] == 101


@patch("src.api.requests.put")
def test_update_product_success(mock_put):
    mock_response = Mock()
    mock_response.json.return_value = {"id": 1, "price": 330}
    mock_response.raise_for_status.return_value = None
    mock_put.return_value = mock_response

    result = update_product(1, {"price": 330})
    assert result["price"] == 330


@patch("src.api.requests.delete")
def test_delete_product_bad_status(mock_delete):
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404")
    mock_delete.return_value = mock_response

    result = delete_product(9999)
    assert result is None