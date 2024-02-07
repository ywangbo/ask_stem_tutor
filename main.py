from flask import Flask, render_template, request
import askAI

app = Flask(__name__)
app.config['SECRET_KEY'] = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_question = request.form['user_question']
    response_paragraph = askAI.ask_a_question(user_question)
    return render_template('index.html', response_paragraph=response_paragraph)