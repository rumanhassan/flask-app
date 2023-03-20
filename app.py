from flask import Flask, render_template, logging, request, jsonify, url_for

app = Flask(__name__)

employees = [
    {'id': 1, 'name': 'Alex', 'org': 'CIBU', 'position': 'Sr. Engineer' },
    {'id': 2, 'name': 'Carey', 'org': 'CIBU', 'position': 'Staff Engineer' },
    {'id': 3, 'name': 'Bob', 'org': 'Cloud', 'position': 'General Manager' },
    {'id': 4, 'name': 'David', 'org': 'Marketing', 'position': 'Sales person' },
    {'id': 5, 'name': 'Sam', 'org': 'Marketing', 'position': 'Marketing Manager' }
]

navbarLinks = [
        {'label': 'Home', 'endpoint': '/'},
        {'label': 'First Section', 'endpoint': '/firstsection'},
        {'label': 'Second Section', 'endpoint': '/secondsection'},
        {'label': 'Contact', 'endpoint': '/contact'}
]

@app.route("/")
def home():
    return render_template("index.html", navbarLinks=navbarLinks, activeIndex=1)

@app.route("/firstsection")
def firstsection():
    return render_template("firstsection.html", navbarLinks=navbarLinks, activeIndex=2)

@app.route("/secondsection")
def secondsection():
    return render_template("secondsection.html", navbarLinks=navbarLinks, activeIndex=3, employees=employees)

@app.route("/contact")
def contact():
    return render_template("contact.html", navbarLinks=navbarLinks, activeIndex=4)

@app.route("/submit", methods=['POST'])
def submit():
    print('Infoo---', request.form)
    # Return a JSON response indicating success
    response = {'status': 'success', 'message': 'Form submitted successfully!'}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)