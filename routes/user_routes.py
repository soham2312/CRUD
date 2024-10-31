from flask import Blueprint, request, jsonify
from models import User
from db import Database
from bson.json_util import dumps
import json

user = Blueprint('user', __name__)
db = Database()

@user.post("/user")
def insert_user():
    try:
        content = request.get_json()
        if not content:
            return jsonify({"message": "No data provided"}), 400
        
        user_data = User.create_user(content)
        result = db.user.insert_one(user_data)
        
        if not result.inserted_id:
            return jsonify({"message": "Failed to insert"}), 500
        
        return jsonify({
            "message": "Success",
            "data": {"id": result.inserted_id}
        }), 201
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

@user.get("/user/<user_id>")
def get_user(user_id):
    try:
        user = db.user.find_one({"_id": user_id})
        if not user:
            return jsonify({"message": "User not found"}), 404
        
        return jsonify({
            "data": json.loads(dumps(user))
        }), 200
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

@user.delete("/user/<user_id>")
def delete_user(user_id):
    try:
        result = db.user.delete_one({"_id": user_id})
        
        if not result.deleted_count:
            return jsonify({"message": "User not found"}), 404
        
        return jsonify({"message": "Delete success"}), 200
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

@user.put("/user/<user_id>")
def update_user(user_id):
    try:
        content = request.get_json()
        if not content:
            return jsonify({"message": "No data provided"}), 400
        
        update_data = User.update_user(content)
        result = db.user.update_one(
            {"_id": user_id},
            {"$set": update_data}
        )

        if not result.matched_count:
            return jsonify({"message": "User not found"}), 404
        
        if not result.modified_count:
            return jsonify({"message": "No changes applied"}), 200
        
        return jsonify({"message": "Update success"}), 200
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

@user.get("/users")
def get_users():
    try:
        users = list(db.user.find({}))
        return jsonify({
            "data": json.loads(dumps(users))
        }), 200
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500