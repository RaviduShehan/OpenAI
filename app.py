from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)
OPENAI_API_KEY = "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"
# Set up OpenAI API credentials
openai.api_key = OPENAI_API_KEY

# Define the home page
@app.route('/')
def home():
    return render_template('home.html')

# Define the chat page
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        prompt = request.form['prompt']
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        message = response.choices[0].text.strip()
        return render_template('chat.html', message=message, prompt=prompt)
    else:
        return render_template('chat.html')

# Define the edit page
@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        text = request.form['text']
        response = openai.Completion.create(
            engine="davinci",
            prompt=f"\"\"\"python\n{text}\n\"\"\"",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        code = response.choices[0].text.strip()
        return render_template('edit.html', code=code, text=text)
    else:
        return render_template('edit.html')

# Define the completion page
@app.route('/completion', methods=['GET', 'POST'])
def completion():
    if request.method == 'POST':
        prompt = request.form['prompt']
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        suggestion = response.choices[0].text.strip()
        return render_template('completion.html', suggestion=suggestion, prompt=prompt)
    else:
        return render_template('completion.html')

if __name__ == '__main__':
    app.run(debug=True)
