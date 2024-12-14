from flask import Flask, render_template, jsonify
import requests
from googletrans import Translator

app = Flask(__name__)

@app.route('/')
def index():
    # Отображение HTML-страницы
    return render_template('index.html')

@app.route('/api/get-quote', methods=['GET'])
def get_quote():
    try:
        # Запрос к API для получения случайной цитаты
        response = requests.get('https://zenquotes.io/api/random')
        if response.status_code == 200:
            data = response.json()
            quote = data[0]["q"]  # Текст цитаты
            author = data[0]["a"]  # Автор цитаты

            # Перевод цитаты и автора на русский
            translator = Translator()
            translated_quote = translator.translate(quote, src='en', dest='ru').text
            translated_author = translator.translate(author, src='en', dest='ru').text

            # Возвращаем переведенные данные в формате JSON
            return jsonify({
                "quote": translated_quote,
                "author": translated_author
            })
        else:
            return jsonify({"error": "Failed to fetch quote from API"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
