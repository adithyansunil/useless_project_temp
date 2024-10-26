from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)
CORS(app)

# Load the model and tokenizer from Hugging Face
model_name = "gpt2"  # Or use another model like "gpt-3.5-turbo" if available
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"response": "Please enter a valid message."}), 400
    
    # Tokenize and generate response
    input_ids = tokenizer.encode(user_input, return_tensors="pt")
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    
    # Return the response as JSON
    return jsonify({"response": response})

if __name__ == '_main_':
    app.run(debug=True, port=5000)