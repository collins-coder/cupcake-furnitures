from flask import Blueprint
from flask import request
from flask import jsonify
from flask import current_app

from werkzeug.utils import secure_filename

import os
import uuid

product_bp = Blueprint(
    "products",
    __name__
)

UPLOAD_FOLDER = "uploads"

# GET PRODUCTS
@product_bp.route(
    "/api/products",
    methods=["GET"]
)
def get_products():

    cursor = (
        current_app.mysql
        .connection
        .cursor()
    )

    cursor.execute(
        """
        SELECT * FROM products
        ORDER BY id DESC
        """
    )

    products = cursor.fetchall()

    result = []

    for product in products:

        result.append({
            "id": product[0],
            "title": product[1],
            "description": product[2],
            "price": float(product[3]),
            "oldPrice": float(product[4]) if product[4] else None,
            "discount": product[5],
            "category": product[6],
            "image": product[7],
        })

    cursor.close()

    return jsonify(result)

# ADD PRODUCT
@product_bp.route(
    "/api/products",
    methods=["POST"]
)
def add_product():

    title = request.form.get("title")

    description = request.form.get(
        "description"
    )

    price = request.form.get("price")

    oldPrice = request.form.get(
        "oldPrice"
    )

    discount = request.form.get(
        "discount"
    )

    category = request.form.get(
        "category"
    )

    image = request.files.get("image")

    image_filename = ""

    if image:

        filename = secure_filename(
            image.filename
        )

        unique_name = (
            str(uuid.uuid4())
            + "_"
            + filename
        )

        image_path = os.path.join(
            UPLOAD_FOLDER,
            unique_name
        )

        image.save(image_path)

        image_filename = unique_name

    cursor = (
        current_app.mysql
        .connection
        .cursor()
    )

    cursor.execute(
        """
        INSERT INTO products
        (
            title,
            description,
            price,
            oldPrice,
            discount,
            category,
            image
        )

        VALUES
        (%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            title,
            description,
            price,
            oldPrice,
            discount,
            category,
            image_filename
        )
    )

    current_app.mysql.connection.commit()

    cursor.close()

    return jsonify({
        "message":
        "Product added successfully"
    })

# DELETE PRODUCT
@product_bp.route(
    "/api/products/<int:id>",
    methods=["DELETE"]
)
def delete_product(id):

    cursor = (
        current_app.mysql
        .connection
        .cursor()
    )

    cursor.execute(
        """
        DELETE FROM products
        WHERE id=%s
        """,
        (id,)
    )

    current_app.mysql.connection.commit()

    cursor.close()

    return jsonify({
        "message":
        "Product deleted"
    })