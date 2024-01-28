import yaml
from models import Bot


from embedchain import App
from flask import json


from functools import lru_cache


@lru_cache(maxsize=32)
def load_bot(slug: str):
    # select by unique key slug
    bot = Bot.query.filter_by(slug=slug).first()
    if bot is None:
        return None
    else:
        # load the config as yaml
        data = yaml.safe_load(bot.config)
        return App.from_config(config=data)
