from flask import Flask, render_template, request, jsonify
from your_existing_app import process_input  # Import your existing application's main function

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        output = process_input(user_input)  # Call your existing application's function
        return jsonify({'output': output})
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)