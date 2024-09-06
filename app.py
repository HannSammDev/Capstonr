from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate_expression():
    expression = request.form['expression']
    try:
        result = str(eval(expression))
    except:
        result = 'Error'
    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
