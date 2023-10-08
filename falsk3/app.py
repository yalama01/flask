from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Global dictionary to store registrations (name: organization)
user_registrations = {}

# List of valid organizations
valid_organizations = ['Organization A', 'Organization B', 'Organization C', 'Organization D', 'Organization E']

@app.route('/')
def index():
    return render_template('index.html', organizations=valid_organizations)

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    organization = request.form.get('organization')

    if not name or not organization:
        return "Error: Both name and organization are required. <a href='/'>Go back</a>"

    if organization not in valid_organizations:
        return "Error: Invalid organization selected. <a href='/'>Go back</a>"

    user_registrations[name] = organization

    return redirect(url_for('registrations'))

@app.route('/registrations')
def registrations():
    return render_template('registrations.html', registrations=user_registrations)

if __name__ == '__main__':
    app.run(debug=True)
