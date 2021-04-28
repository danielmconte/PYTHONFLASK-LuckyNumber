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


