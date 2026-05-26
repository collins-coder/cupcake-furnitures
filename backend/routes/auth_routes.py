from flask import Blueprint, request, jsonify
import jwt
import datetime

auth_bp = Blueprint("auth", __name__)

SECRET_KEY = "cupcake_secret_key"

@auth_bp.route("/api/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username == "admin" and password == "12345":

        token = jwt.encode(
            {
                "username": username,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=5)
            },
            SECRET_KEY,
            algorithm="HS256"
        )

        return jsonify({
            "message": "Login successful",
            "token": token
        })

    return jsonify({
        "message": "Invalid credentials"
    }), 401