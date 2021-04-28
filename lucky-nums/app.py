from flask import Flask, jsonify, render_template, request
from models import db, connect_db, Response
import requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///lucky_num_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)

@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")

# @app.route("/api/get-lucky-num", methods=['POST'])
# def create_response():
#     new_response = Response(
#                     name=request.json['name'],
#                     email=request.json['name'],
#                     year=request.json['year'],
#                     color=request.json['color']
#                     )
#     response_json = new_response.serialize()
#     db.session.add(response_json)
#     db.session.commit() 
#     return ("It's all there", 201)

@app.route("/response")
def new_response():
    response = {
    "errors": {
        "color": [
        "Invalid value, must be one of: red, green, orange, blue."
        ],
        "name": [
        "This field is required."
        ]
    }
    }

    return jsonify(response); 

@app.route("/api/get-lucky-num", methods=['POST'])
def get_num(): 
    name = request.form['name']
    email = request.form['email']
    year = request.form['year']
    color = request.form['color']

    num_fact = requests.get('http://numbersapi.com/random?min=1&max=100')
    year_fact = requests.get(f'http://numbersapi.com/{year}/year')
    print()
    # obj = jsonify(name=name, email=email, year=year, color=color, num_fact=num_fact, year_fact=year_fact)
    response = {
        "num": {
            "fact": num_fact,
            "num": 25
        },
        "year": {
            "fact": year_fact,
            "year": year
        }
    }
    return jsonify(response)


# @app.route("/api/get-lucky-num", methods=['POST'])
# def get_num(): 

#     name = form.name.data   
#     email = form.email.data
#     year = form.year.data
#     color = form.color.data

#     num_fact = requests.get('http://numbersapi.com/random?min=1&max=100')
#     year_fact = requests.get(f'http://numbersapi.com/{year}/year')

#     obj = jsonify(name=name, email=email, year=year, color=color, num_fact=num_fact, year_fact=year_fact)

#     return obj 