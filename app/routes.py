from app import app
from flask import render_template

@app.route('/')
def homePage():
    indexCopy1 = 'This is all placeholder text! Currently learning to pass python data through html via flask + jinja. This will all be beautified later down the road.'
    return render_template('index.html', indexCopy1 = indexCopy1)

@app.route('/top5')
def top5Page():
    food = ['Sushi', 'Chicken Tikka', 'Pho', 'Ramen', 'Korean BBQ']
    top5Copy1 = 'Below is a list of my favorite foods!'
    return render_template('top5.html', my_food = food, top5Copy1 = top5Copy1)
