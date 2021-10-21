import random

from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__,
                   url_prefix='/api',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/api')

jokes = []
joke_list = [
    "Q: What is a snake's favorite subject at school? A: Hisssstory.",
    "Q: What do other plants do when one of their plant friends is sad? A: Photosympathize.",
    "Q: What's the derivative of Amazon with respect to cost of shipping? A: Amazon Prime!",
    "Q: What did Cinderella say while reading a biology textbook? A: 'I hate mitosis.'",
    "Q: Was General Washington a handsome man? A: Yes, he was George-eous!!",
    "Q: What did one ion say to another? A: I’ve got my ion you.",
    "Q: What dance was very popular in 1776? A: Indepen-dance!",
    "Q: What is blood’s message to the world? A: B positive.",
    "Q: What did Al Gore play on his guitar? A: An Algorithm",
    "Never take a victory for Grant-ed.",
    "I wish I was adenine... Then I could get paired with U.",
    "He He He. Who knew helium could be so funny?",
    "I thought about being a historian, but I couldn’t see a future in it.",
    "Q: Why do you rarely find mathematicians spending time at the beach? A: They have sine and cosine to get a tan "
    "and don't need the sun!",
    "Q: What do you call a fish with no eyes? A: A fsh.",
    "Q: Why did the white bear dissolve in water? A: Because it was polar.",
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