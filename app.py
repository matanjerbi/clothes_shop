from flask import Flask, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from config.sql_config import get_db
from models.users import insert_user, check_if_email_exsist
from rabbit.basic_rabbit import publish_to_queue

app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome to the User Signup API!'


@app.route('/signup', methods=['POST'])
def signup():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 400

    data = request.get_json()

    # בדיקת שדות חובה
    if not all(key in data for key in ['email', 'name']):
        return jsonify({"error": "Missing required fields: email and name"}), 400

    db = next(get_db())
    result = insert_user(db, data)

    if result.get('error'):
        return jsonify(result), 400
    return jsonify(result), 201


@app.route('/buy', methods=['POST'])
def buy_clothes():
    # בדיקת תקינות הבקשה
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 400

    data = request.get_json()
    if not all(key in data for key in ['email', 'items', 'shipping_address']):
        return jsonify({"error": "Missing required fields"}), 400

    # בדיקה אם המשתמש קיים
    db = next(get_db())
    user = check_if_email_exsist(db, data['email'])
    if not user:
        return jsonify({"error": "User not found"}), 404

    try:
        # שליחה לכל התורים
        queues_data = {
            'update_inventory': {'items': data['items']},
            'save_purchase': {'user_id': user.id, 'items': data['items']},
            'create_shipping': {'user_id': user.id, 'address': data['shipping_address']},
            'send_email': {'email': data['email'], 'items': data['items']}
        }

        # שליחת ההודעות לכל התורים
        for queue, message in queues_data.items():
            publish_to_queue(queue, message)

        return jsonify({"success": "Order processed"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)