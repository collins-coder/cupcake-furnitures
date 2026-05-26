from flask import (
    Blueprint,
    request,
    jsonify,
    current_app
)

from flask_mail import (
    Mail,
    Message
)

contact_bp = Blueprint(
    "contact_bp",
    __name__
)

mail = Mail()

@contact_bp.route(
    "/api/contact",
    methods=["POST"]
)
def send_contact_message():

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    try:

        msg = Message(
            subject=f"New Message From {name}",

            sender=current_app.config[
                "MAIL_USERNAME"
            ],

            recipients=[
                current_app.config[
                    "MAIL_USERNAME"
                ]
            ]
        )

        msg.body = f"""
NEW CONTACT MESSAGE

Name:
{name}

Email:
{email}

Message:
{message}
"""

        mail.init_app(
            current_app
        )

        mail.send(msg)

        return jsonify({
            "message":
            "Message sent successfully"
        }), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500