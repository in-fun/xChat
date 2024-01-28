from flask import Blueprint, jsonify, make_response, request
from bot import load_bot


sources_bp = Blueprint("sources", __name__)


# API route to add data sources
@sources_bp.route("/api/add_sources", methods=["POST"])
def add_sources():
    try:
        bot_slug = request.json.get("bot")
        data_type = request.json.get("type")
        value = request.json.get("value")
        chat_bot = load_bot(bot_slug)
        chat_bot.add(value, data_type=data_type)
        return make_response(jsonify(message="Sources added successfully"), 200)
    except Exception as e:
        return make_response(jsonify(message=f"Error adding sources: {str(e)}"), 400)
