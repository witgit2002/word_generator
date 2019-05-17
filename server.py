from flask import Flask
app = Flask(__name__)
from flask import request
from flask import jsonify
from word_generator import WordGenerator

word_generator = WordGenerator()

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/row_placements/")
def row_placements():
    letters = request.args.get('letters')
    if letters == None:
        letters = ""
    word_len = request.args.get('word_len')
    if word_len == None or len(word_len) == 0:
        word_len = len(letters)
    word_mask = request.args.get('word_mask')
    if word_mask == None:
        word_mask = ""
    return jsonify(word_generator.getAllPlacements(letters, int(word_len), word_mask))

@app.route("/words_unfiltered/")
def words_unfiltered():
    letters = request.args.get('letters')
    print("letters ", letters)
    if letters == None:
        letters = ""
    word_len = request.args.get('word_len')
    print("word_len ", word_len)
    if word_len == None or len(word_len) == 0:
        word_len = len(letters)
    word_mask = request.args.get('word_mask')
    print("word_mask ", word_mask)
    if word_mask == None:
        word_mask = ""
    all_placements = word_generator.getAllPlacements(letters, int(word_len), word_mask)
    return jsonify(word_generator.checkDictionary(all_placements, "words.txt", int(word_len)))

@app.route("/check_dictionary/")
def check_dictionary():
    letters = request.args.get('letters')
    return jsonify(word_generator.checkDictionary([letters], "words.txt", len(letters)))

