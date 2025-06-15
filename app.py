from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    print("Iniciando servidor Flask en http://localhost:8081...")
    app.run(host='0.0.0.0', port=8081, debug=True)