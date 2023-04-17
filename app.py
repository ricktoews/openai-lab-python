from flask import Flask, request
from modules.chat_api import chat_prompt

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/chat', methods=['POST'])
def chat():
    prompt = request.json['prompt']
    return chat_prompt(prompt)

if __name__ == '__main__':
    app.run(debug=True)

