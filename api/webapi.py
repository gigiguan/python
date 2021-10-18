import random

from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__,
                   url_prefix='/api',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/api')

jokes = []
joke_list = [
    "Q: What is a snake's favorite subject at school? A: Hisssstory."
    "Q: Was General Washington a handsome man? A: Yes, he was George-eous!!",
    "Q: What dance was very popular in 1776? A: Indepen-dance!",
    "Never take a victory for Grant-ed.",
    "I thought about being a historian, but I couldn’t see a future in it.",
    "Q: What is the most popular college during election season? A: The Electoral College.",
    "Q: What’s red, white and blue? A: Our flag, of course. And a sad candy cane!",
    "Q: What was Thomas Jefferson’s favorite dessert? A: Monti jello."
]


def _find_next_id():
    return max(jokes["id"] for joke in jokes) + 1


def _init_jokes():
    id = 1
    for joke in joke_list:
        jokes.append({"id": id, "joke": joke, "haha": 0, "boohoo": 0})
        id += 1


@api_bp.route('/joke')
def get_joke():
    if len(jokes) == 0:
        _init_jokes()
    return jsonify(random.choice(jokes))


@api_bp.route('/jokes')
def get_jokes():
    if len(jokes) == 0:
        _init_jokes()
    return jsonify(jokes)


if __name__ == "__main__":
    print(random.choice(joke_list))