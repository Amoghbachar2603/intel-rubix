# app.py (example)

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed='*')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/ask', methods=['POST'])
def ask_llm():
    question = request.json['question']
    
    response = mistralai.generate_text(question)

    return jsonify({'response': response})

@socketio.on('connect')
def handle_connect():
    print('User connected!')

@socketio.on('message')
def handle_message(data):
    question = data['message']
    # Send the question to the LLM through API
    response = ask_llm(question)
    # Emit the LLM's response back to the user
    emit('response', response)

if __name__ == '__main__':
    socketio.run(app, debug=True)

