from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "SomeSecretKey"

debug = DebugToolbarExtension(app)

@app.route("/")
def form_input():
    """Makes forms for user input"""

    prompts = story.prompts
    return render_template("questions.html", prompts = prompts)

@app.route("/story")
def show_story():
    """Shows the story from the user imputs"""
    text = story.generate(request.args)

    return render_template("story.html", text=text)
