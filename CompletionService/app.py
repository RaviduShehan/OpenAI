from flask import Flask, request, jsonify
import openai_secret_manager
import openai

app = Flask(__name__)

# Load OpenAI API key
secrets = openai_secret_manager.get_secret("openai", path="config/secrets.json")
openai.api_key = secrets["api_key"]

@app.route('/completion')
def completion():
    prompt = request.args.get('prompt')
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5
    )
    return jsonify({'response': response.choices[0].text.strip()})
