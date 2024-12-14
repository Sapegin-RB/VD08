from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Отображение HTML-страницы

@app.route('/api/get-quote', methods=['GET'])
def get_quote():
    try:
        response = requests.get('https://zenquotes.io/api/random')
        if response.status_code == 200:
            data = response.json()
            return jsonify({
                "quote": data[0]["q"],
                "author": data[0]["a"]
            })
        else:
            return jsonify({"error": "Failed to fetch quote from API"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
