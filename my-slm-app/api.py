from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

print("Loading AI Model...")
generator = pipeline("text-generation", model="sshleifer/tiny-gpt2")
print("AI Model Ready!")

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')
    
    output = generator(prompt, max_new_tokens=50, do_sample=True)
    generated_text = output[0]['generated_text']
    
    return jsonify({"response": generated_text})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
