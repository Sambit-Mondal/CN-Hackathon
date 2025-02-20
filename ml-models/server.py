from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import pymongo
from dotenv import load_dotenv
from chatbot import get_bot_response  # Import chatbot function

# Load environment variables
load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Connect to MongoDB
mongo_client = pymongo.MongoClient(MONGODB_URI)
db = mongo_client[DB_NAME] # Replace with your actual database name
inventory_collection = db[COLLECTION_NAME]  # Replace with your actual collection name

@app.route('/chat', methods=['POST'])
def chat():
    """
    API endpoint to receive user messages, fetch inventory data, 
    and return chatbot responses.
    """
    try:
        data = request.get_json()
        user_message = data.get("message", "")
        low_threshold = 10  # Example threshold for low stock
        excess_threshold = 100  # Example threshold for excess stock

        # Get chatbot response
        bot_response = get_bot_response(user_message, low_threshold, excess_threshold)

        return jsonify({"response": bot_response})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal server error"}), 500


@app.route('/inventory', methods=['GET'])
def get_inventory():
    """Fetch inventory data from MongoDB and return JSON."""
    try:
        inventory_data = list(inventory_collection.find({}, {"_id": 0}))  # Exclude MongoDB _id
        return jsonify(inventory_data)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)