from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []


@app.get('/')
def display_instructions():
    title = survey.title
    instructions = survey.instructions
    return render_template("survey_start.html", title=title, instructions=instructions)

@app.post('/begin')
def start_survey():

    return redirect('/questions/0')

@app.get('/questions/0')
def show_question():

    return render_template("question.html")
