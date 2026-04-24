from flask import Flask, render_template
from brain import *
import random


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/story/<adjective>/<noun>/<animal>/<verb>/<name>/<number>')
def story(adjective, noun, animal, verb, name, number):
    story_text = random.choice(mad_templates).replace('{adjective}', adjective).replace('{noun}', noun).replace('{animal}', animal).replace('{verb}', verb).replace('{name}', name.title()).replace('{number}', number)
    print(story)
    return render_template('story.html', story=story_text)





if __name__ == '__main__':
    app.run(debug=True)
