# chatbot.py
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
from flask import Flask, request, render_template

# Initialize GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Flask app initialization
app = Flask(__name__)

# Function to generate response using GPT-2
def generate_response(input_text):
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    output = model.generate(input_ids, max_length=120, num_return_sequences=1, no_repeat_ngram_size=2, early_stopping=True)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response


# Route for home page
@app.route('/')
def home():
    return render_template('index.html', response=None)

# Route for chat endpoint
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']
    response = generate_response(user_input)
    return render_template('index.html', response=response)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
