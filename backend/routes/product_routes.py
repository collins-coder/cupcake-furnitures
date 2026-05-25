from flask import Blueprint, jsonify

product_bp = Blueprint("products", __name__)

@product_bp.route("/api/products", methods=["GET"])
def get_products():

    sample_products = [
        {
            "id": 1,
            "title": "Modern Sofa",
            "price": 45000,
            "image": "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85"
        },
        {
            "id": 2,
            "title": "Wooden Dining Table",
            "price": 65000,
            "image": "https://images.unsplash.com/photo-1524758631624-e2822e304c36"
        }
    ]

    return jsonify(sample_products)