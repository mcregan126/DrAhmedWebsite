import os
from flask import Flask, render_template, request
from helpers import calculate_length 

os.environ['FLASK_ENV'] = 'development'


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/api')
def api():
    return render_template('api.html')

@app.route('/models', methods=['GET', 'POST'])
def models():
    length = None
    if request.method == 'POST':
        user_input = request.form.get('user_input', '')
        length = calculate_length(user_input)
    return render_template('models.html', length=length)

@app.route('/data')
def data():
    return render_template('data.html')

if __name__ == '__main__':
    app.run(debug=True)


