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
    """Displays survey instructions and start button"""
    title = survey.title
    instructions = survey.instructions

    return render_template("survey_start.html", title=title, instructions=instructions)

@app.post('/begin')
def start_survey():
    """Redirects to first question"""

    return redirect('/questions/0')

@app.get('/questions/<num>')
def show_question(num):
    """Generate survey question"""

    # var = request.args[]
    question_data = survey.questions[int(num)]
    # choices = survey.questions[int(num)].choices

    return render_template("question.html", question_data=question_data)
    # return render_template("question.html", question=question, choices=choices)
