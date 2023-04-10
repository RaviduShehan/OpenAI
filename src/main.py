from flask import Flask, request, render_template
import requests

app = Flask(__name__)
# URLs for the microservices
CHAT_SERVICE_URL = "http://localhost:5001/chat"
COMPLETION_SERVICE_URL = "http://localhost:5002/completion"
EDIT_SERVICE_URL = "http://localhost:5003/edit"
IMAGE_SERVICE_URL = "http://localhost:5004/image"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/chat')
def chat():
    print('Connecting to chat service...')
    prompt = request.args.get('prompt')
    response = requests.get(f"{CHAT_SERVICE_URL}?prompt={prompt}")
    print('Chat service URL:', CHAT_SERVICE_URL)
    response = response.json()['response']
    # return render_template('chat.html', prompt=prompt, )
    return response

@app.route('/completion')
def completion():
    prompt = request.args.get('prompt')
    response = requests.get(f"{COMPLETION_SERVICE_URL}?prompt={prompt}")
    res = response.json()['response']
    return res
    # return render_template('completion.html', prompt=prompt, response=response.json()['response'])

@app.route('/edit')
def edit():
    prompt = request.args.get('prompt')
    response = requests.get(f"{EDIT_SERVICE_URL}?prompt={prompt}")
    # return render_template('edit.html', prompt=prompt, response=response.json()['response'])
    res = response.json()['response']
    return res

@app.route('/image')
def image():
    print('Connecting to image service...')
    prompt = request.args.get('prompt')
    response = requests.get(f"{IMAGE_SERVICE_URL}?prompt={prompt}")
    print('Image service URL:', IMAGE_SERVICE_URL)
    response = response.json()['response']
    # return render_template('image.html', prompt=prompt, response=response)
    return response

if __name__ == '__main__':
    app.run(debug=True)
