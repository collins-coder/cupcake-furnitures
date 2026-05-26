from flask import Flask
from flask_cors import CORS
from flask import send_from_directory

from flask_mysqldb import MySQL

from routes.product_routes import product_bp
from routes.auth_routes import auth_bp

app = Flask(__name__)

CORS(app)

# MYSQL CONFIG
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Rugutson-3"
app.config["MYSQL_DB"] = "cupcake_furnitures"

# UPLOADS
app.config["UPLOAD_FOLDER"] = "uploads"

# MYSQL INIT
mysql = MySQL(app)

# MAKE MYSQL AVAILABLE
app.mysql = mysql

# REGISTER ROUTES
app.register_blueprint(product_bp)
app.register_blueprint(auth_bp)

# SERVE IMAGES
@app.route("/uploads/<filename>")
def uploaded_file(filename):

    return send_from_directory(
        app.config["UPLOAD_FOLDER"],
        filename
    )

@app.route("/")
def home():

    return {
        "message":
        "Cupcake Furnitures API Running"
    }

if __name__ == "__main__":
    app.run(debug=True)