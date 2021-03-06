from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)



@app.get('/')
def display_instructions():
    """Displays survey instructions and start button"""
    title = survey.title
    instructions = survey.instructions
    
    return render_template("survey_start.html", title=title, instructions=instructions)

@app.post('/begin')
def start_survey():
    """Redirects to first question"""

    session["responses"] = []

    return redirect(f'/questions/{len(session["responses"])}')

@app.get('/questions/<num>')
def show_question(num):
    """Generate survey question"""
    if len(session["responses"]) == num:
        question = survey.questions[int(num)]
        return render_template("question.html", question=question)
    else:
        return redirect(f'/questions/{len(session["responses"]) + 1}')

    
    

@app.post('/answer')
def save_answer_and_next_question():
    """capture the answer of question and send user to new question"""
    
    answer = request.form['answer']
    responses = session["responses"]
    responses.append(answer)
    session["responses"] = responses
    

    if len(responses) < len(survey.questions):
        return redirect(f'/questions/{len(responses)}')
    else:
        responses.clear()
        return render_template('completion.html')
