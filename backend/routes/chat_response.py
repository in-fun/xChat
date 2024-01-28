
from flask import Blueprint, jsonify, make_response, request
from bot import load_bot


chat_response_bp = Blueprint("chat_response", __name__)


# Chat Response for user query
@chat_response_bp.route("/api/get_answer", methods=["POST"])
def get_answer():
    try:
        data = request.get_json()
        query = data.get("query")
        bot_name = data.get("name")

        chat_bot = load_bot(bot_name)
        if chat_bot is None:
            return make_response(jsonify({"error": f"Bot {bot_name} not found"}), 404)

        response = chat_bot.chat(query)
        return make_response(jsonify({"response": response}), 200)

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 400)
