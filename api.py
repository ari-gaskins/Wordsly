from flask import Flask, render_template
from random import choice

app = Flask(__name__)

@app.route('/wordsly')
def wordsly():
    return render_template('index.html')

def generate_word():
    filename = 'five_letter_words.txt'
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        random_word = choice(lines)
        file.close()

    return random_word
