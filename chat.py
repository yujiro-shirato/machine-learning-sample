from flask import Flask, render_template, request, jsonify
import logic
import poke
import openai_api

app = Flask(__name__)

chat_messages = []

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form.get('message')

    if user_message:
        # メッセージの前に "user:" を付けて保存
        formatted_user_message = f'user: {user_message}'
        chat_messages.append(formatted_user_message)

        # Botからの応答を生成
        # bot_response = poke.get_pokemon_info(user_message)
        bot_response = openai_api.generate_text(user_message)
        formatted_bot_response = f'bot: {bot_response}'
        chat_messages.append(formatted_bot_response)

        return jsonify({'status': 'success', 'bot_response': bot_response})
    else:
        return jsonify({'status': 'error', 'message': 'Invalid message'})

@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify({'messages': chat_messages})

if __name__ == '__main__':
    app.run(debug=True)
