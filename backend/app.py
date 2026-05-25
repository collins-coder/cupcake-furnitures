from flask import Flask
from flask_cors import CORS
from flask_mysqldb import MySQL

from routes.product_routes import product_bp

app = Flask(__name__)

CORS(app)

# DATABASE CONFIG
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "cupcake"

mysql = MySQL(app)

# REGISTER ROUTES
app.register_blueprint(product_bp)

@app.route("/")
def home():
    return {
        "message": "Cupcake Furnitures API Running"
    }

if __name__ == "__main__":
    app.run(debug=True)