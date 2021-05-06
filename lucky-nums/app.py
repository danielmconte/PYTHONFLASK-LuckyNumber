from flask import Flask, jsonify, render_template, redirect, request
from models import db, connect_db, Response
from forms import InfoForm
import requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///lucky_num_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)

@app.route("/")
def homepage():
    """Show homepage."""

    return redirect('/api/get-lucky-num')

@app.route("/api/get-lucky-num", methods=['GET', 'POST'])
def create_response():

    form = InfoForm()
    
    if form.validate_on_submit():
        name = form.name.data 
        email = form.email.data
        year = form.year.data
        color = form.color.data
        num_fact = requests.get('http://numbersapi.com/random?min=1&max=100')
        year_fact = requests.get(f'http://numbersapi.com/{year}/year')
        
        print(year_fact)
        # data1 = num_fact.request.json 
        # data2 = year_fact.request.json
        
    # data = request.json
        new_response = Response(
                        name=name,
                        email=email,
                        year=year,
                        color=color
                        )
    
    # # a_response = jsonify(response=new_response.serialize())
    

    
    # num_fact = requests.get('http://numbersapi.com/random?min=1&max=100')
    # year_fact = requests.get(f'http://numbersapi.com/{new_response.year}/year')


    # response = {
    #     "num": {
    #         "fact": f'{num_fact.text}'
    #     },
    #     "year": {
    #         "fact": f'{year_fact.text}',
    #         "year": f'{new_response.year}'
    #     }
    # }

        response = {
            "num": {
                "fact": f'{num_fact.text}'
            },
            "year": {
                "fact": f'{year_fact.text}'
            }
        }

       
    
        db.session.add(new_response)
        db.session.commit()      
        return response
    else:
        return render_template("form.html", form=form)

   
   
    # This works for db
    # db.session.add(new_response)
    # db.session.commit()  
    # return (jsonify(response=new_response.serialize()), 201)


