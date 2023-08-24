from flask import Flask, request, jsonify
from concurrent.futures import ThreadPoolExecutor
from transformers import MarianMTModel, MarianTokenizer
import time

app = Flask(__name__)

# Load the pretrained model and tokenizer
model_name = "Helsinki-NLP/opus-mt-ko-en"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

executor = ThreadPoolExecutor()

def translate_text(text):
    start_time = time.time()
    
    inputs = tokenizer(text, return_tensors="pt", padding="max_length", truncation=True)
    translation = model.generate(**inputs)
    translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    return translated_text, elapsed_time

import psutil
import os

def get_memory_usage():
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    memory_usage = memory_info.rss / (1024 * 1024)  # Convert bytes to megabytes
    return memory_usage

@app.route('/translate', methods=['POST'])
def handle_translation():
    try:
        memory_before = get_memory_usage()
        data = request.json
        text = data['text']
        future = executor.submit(translate_text, text)
        memory_after = get_memory_usage()
        memory_used = memory_after - memory_before
        print(f"Memory used: {memory_used:.2f} MB")
        return jsonify({'status': 'processing', 'future_id': id(future),'text':translate_text(text)})

    except Exception as e:
        return jsonify({'error': str(e)})
    

    
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
