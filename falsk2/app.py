from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('layout.html')

@app.route('/result', methods=['GET'])
def result():
    number = request.args.get('number', None)

    if number is None:
        return "Error: No number provided. <a href='/'>Go back</a>"

    try:
        number = int(number)
        if number % 2 == 0:
            result_text = "Even number"
        else:
            result_text = "Odd number"
    except ValueError:
        result_text = "Not an integer"

    return render_template('result.html', result=result_text)

if __name__ == '__main__':
    app.run(debug=True)
