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

@app.route("/api/get-lucky-num", methods=['POST'])
def create_response():
    # if not 'color' in request.form:
    #     response = {
    #         "Must have name, email, year and color"
    #     }
    #     return response
    
    # else:
        
    data = request.json
    new_response = Response(
                    name=data['name'],
                    email=data['email'],
                    year=data['year'],
                    color=data['color']
                    )
    
    a_response = jsonify(response=new_response.serialize())
    

    
    num_fact = requests.get('http://numbersapi.com/random?min=1&max=100')
    year_fact = requests.get(f'http://numbersapi.com/{new_response.year}/year')


    response = {
        "num": {
            "fact": f'{num_fact.text}'
        },
        "year": {
            "fact": f'{year_fact.text}',
            "year": f'{new_response.year}'
        }
    }
    
    return response

   
   
    # This works for db
    # db.session.add(new_response)
    # db.session.commit()  
    # return (jsonify(response=new_response.serialize()), 201)




# @app.route("/response")
# def new_response():
#     response = {
#     "errors": {
#         "color": [
#         "Invalid value, must be one of: red, green, orange, blue."
#         ],
#         "name": [
#         "This field is required."
#         ]
#     }
#     }

#     return jsonify(response); 

# @app.route("/api/get-lucky-num", methods=['POST'])
# def get_num(): 
#     name = request.form['name']
#     email = request.form['email']
#     year = request.form['year']
#     color = request.form['color']

#     num_fact = requests.get('http://numbersapi.com/random?min=1&max=100')
#     year_fact = requests.get(f'http://numbersapi.com/{year}/year')
#     print()
#     # obj = jsonify(name=name, email=email, year=year, color=color, num_fact=num_fact, year_fact=year_fact)
#     response = {
#         "num": {
#             "fact": num_fact,
#             "num": 25
#         },
#         "year": {
#             "fact": year_fact,
#             "year": year
#         }
#     }
#     return jsonify(response)


