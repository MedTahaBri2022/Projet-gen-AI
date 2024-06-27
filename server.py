from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

app = Flask(__name__)

# Charger le modèle LLaMA depuis Hugging Face
model_name = "daryl149/llama-2-70b-chat-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    input_text = data['input_text']
    
    # Prétraitement avec le tokenizer
    inputs = tokenizer(input_text, return_tensors="pt")
    
    # Génération de la réponse
    with torch.no_grad():
        outputs = model.generate(**inputs)
    
    # Décodage de la réponse générée
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return jsonify({'response': generated_text})

if __name__ == '__main__':
    app.run(debug=True)