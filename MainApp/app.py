from flask import Flask, request, render_template
import requests

app = Flask(__name__, template_folder="templates")

# URLs for the microservices
CHAT_SERVICE_URL = "http://localhost:5001/chat"
COMPLETION_SERVICE_URL = "http://localhost:5002/completion"
EDIT_SERVICE_URL = "http://localhost:5003/edit"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/chat')
def chat():
    prompt = request.args.get('prompt')
    response = requests.get(f"{CHAT_SERVICE_URL}?prompt={prompt}")
    return render_template('chat.html', prompt=prompt, response=response.json()['response'])

@app.route('/completion')
def completion():
    prompt = request.args.get('prompt')
    response = requests.get(f"{COMPLETION_SERVICE_URL}?prompt={prompt}")
    return render_template('completion.html', prompt=prompt, response=response.json()['response'])

@app.route('/edit')
def edit():
    prompt = request.args.get('prompt')
    response = requests.get(f"{EDIT_SERVICE_URL}?prompt={prompt}")
    return render_template('edit.html', prompt=prompt, response=response.json()['response'])

if __name__ == '__main__':
    app.run(debug=True)
