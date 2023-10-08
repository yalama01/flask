from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        number = request.form.get('number')
    else:
        number = request.args.get('number')

    result_text = ""

    if number is not None:
        try:
            number = int(number)
            if number % 2 == 0:
                result_text = "Even number"
            else:
                result_text = "Odd number"
        except ValueError:
            result_text = "Not an integer"

    return render_template('layout.html', result=result_text)

if __name__ == '__main__':
    app.run(debug=True)
