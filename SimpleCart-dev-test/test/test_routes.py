import json

from .settings import DEFAULT_PRICE

def test_product_detail_api(client):
    id = 3
    response = client.get(f"/api/products/{id}")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert id == data.get('id')
    assert DEFAULT_PRICE * id


def test_product_api(client):
    response = client.get("/api/products")
    assert response.status_code == 200

# post new cart
def test_post_cart(client):
    data=   {
            "coupon_code": "string",
            "shipping_fee": 0,
            "cart_items": [
                {
                    "product_id": 0,
                    "qty": 0
                }
              ]
            }
    response = client.get(f"/api/cart", json=data)
    assert response.status_code == 200


