from flask import Blueprint, jsonify, make_response, request
from models import APIKey, Bot, db

dashboard_bp = Blueprint("dashboard", __name__)

# read default config from path "config.yaml" as plain string
default_config = open("config.yaml").read()


# Set Open AI Key
@dashboard_bp.route("/api/set_key", methods=["POST"])
def set_key():
    data = request.get_json()
    api_key = data["openAIKey"]
    existing_key = APIKey.query.first()
    if existing_key:
        existing_key.key = api_key
    else:
        new_key = APIKey(key=api_key)
        db.session.add(new_key)
    db.session.commit()
    return make_response(jsonify(message="API key saved successfully"), 200)


# Check OpenAI Key
@dashboard_bp.route("/api/check_key", methods=["GET"])
def check_key():
    existing_key = APIKey.query.first()
    if existing_key:
        return make_response(jsonify(status="ok", message="OpenAI Key exists"), 200)
    else:
        return make_response(
            jsonify(status="fail", message="No OpenAI Key present"), 200
        )


# Create a bot
@dashboard_bp.route("/api/create_bot", methods=["POST"])
def create_bot():
    data = request.get_json()
    name = data["name"]
    slug = name.lower().replace(" ", "_")
    # get bot config text from request payload, or default config
    config = data.get("config", default_config)
    existing_bot = Bot.query.filter_by(slug=slug).first()
    if existing_bot:
        return (make_response(jsonify(message="Bot already exists"), 400),)
    new_bot = Bot(name=name, slug=slug, config=config)
    db.session.add(new_bot)
    db.session.commit()
    return make_response(jsonify(message="Bot created successfully"), 200)


# Delete a bot
@dashboard_bp.route("/api/delete_bot", methods=["POST"])
def delete_bot():
    data = request.get_json()
    slug = data.get("slug")
    bot = Bot.query.filter_by(slug=slug).first()
    if bot:
        db.session.delete(bot)
        db.session.commit()
        return make_response(jsonify(message="Bot deleted successfully"), 200)
    return make_response(jsonify(message="Bot not found"), 400)


# Get the list of bots
@dashboard_bp.route("/api/get_bots", methods=["GET"])
def get_bots():
    bots = Bot.query.all()
    bot_list = []
    for bot in bots:
        bot_list.append({"name": bot.name, "slug": bot.slug, "config": bot.config})
    return jsonify(bot_list)
