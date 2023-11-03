from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

from gpt_wrapper import RAG

app = Flask(__name__)
CORS(app)

@app.route('/check', methods=['POST'])
def check():
    if request.method.lower() == 'get':
        return "Method Not Allowed. Please use POST API calls"
    req = request.get_json()
    api_key = request.headers.get('x-api-key')
    if not api_key:
        return jsonify({'error': 'x-api-key header is required. Please set it to your OpenAI API key.'})
    compliance_url = req.get('compliance_url')
    if not compliance_url:
        return jsonify({'error': 'compliance_url is required'})
    url_to_check = req.get('url_to_check')
    if not url_to_check:
        return jsonify({'error': 'url_to_check is required'})
    try:
        rag = RAG()
        rag.initialize(compliance_url, url_to_check, api_key)
        response = rag.run()
        return {
            'response': response
        }
    except Exception as e:
        return {
            'error': str(e)
        }
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002, debug=True)