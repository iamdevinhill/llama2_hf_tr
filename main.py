from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Initialize the pipeline
pipe = pipeline("text-generation", model="meta-llama/Llama-2-7b-chat-hf", use_auth_token="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")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json['userInput']
    response = pipe(user_input, max_length=100, num_return_sequences=1)[0]["generated_text"]
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)

