# Import necessary modules
from flask import Flask, render_template, request, jsonify
from transformers import pipeline

# Create a Flask web application
app = Flask(__name__)

# Initialize a text generation pipeline using the Hugging Face Transformers library
# This pipeline will use the "meta-llama/Llama-2-7b-chat-hf" model for text generation
# It also provides an authentication token for model access
pipe = pipeline("text-generation", model="meta-llama/Llama-2-7b-chat-hf", use_auth_token="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")

# Define a route for the root URL ('/') that renders an HTML template
@app.route('/')
def index():
    return render_template('index.html')

# Define a route for handling POST requests to '/get_response'
@app.route('/get_response', methods=['POST'])
def get_response():
    # Get user input data from the POST request's JSON payload
    user_input = request.json['userInput']
    
    # Generate a text response using the initialized pipeline
    # The generated response will have a maximum length of 100 characters
    # Only one sequence (response) will be generated
    response = pipe(user_input, max_length=100, num_return_sequences=1)[0]["generated_text"]
    
    # Return the generated response as JSON
    return jsonify({'response': response})

# Start the Flask application only if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
