import logging
from logging.handlers import RotatingFileHandler
from dataclasses import dataclass
from flask import Flask, jsonify, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
import requests
from producer import publish

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@flask_db/main'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

# Create a logger instance for the Flask app
logger = logging.getLogger(__name__)

# Configure the logger
def configure_logger():
    # Set the log level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)
    logger.setLevel(logging.DEBUG)

    # Create a rotating file handler to manage log files
    log_file = "app.log"
    max_bytes = 1024 * 1024  # 1 MB
    backup_count = 3  # Number of backup log files to keep
    file_handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)

    # Define the log format
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

# Call the configure_logger function to set up the logger
configure_logger()

db = SQLAlchemy(app)

@dataclass
class Product(db.Model):
    id: int
    title: str
    image: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, primary_key=True)

    __table_args__ = (
        UniqueConstraint('user_id', 'product_id', name='user_product_unique'),
    )

@app.route('/api/products')
def index():
    logger.info('Request made to /api/products')
    return jsonify(Product.query.all())

@app.route('/api/products/<int:id>/like', methods=['POST'])
def like(id):
    req = requests.get('http://django:8000/api/user')
    logger.info(f'Received response from Django API: {req.text}')
    json = req.json()
    logger.debug(f'Parsed JSON data from response: {json}')
    
    try:
        productUser = ProductUser(user_id=json['id'], product_id=id)
        db.session.add(productUser)
        db.session.commit()
        publish('product_liked', id)
    except:
        logger.error('An error occurred while processing the request.', exc_info=True)
        abort(400, 'You already liked this product')

    logger.info(f'Product liked by user: {json["id"]}, Product ID: {id}')
    return jsonify({
        'message': 'success'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')