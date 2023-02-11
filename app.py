from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests

app = Flask(__name__)
# add database
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coupons.sqlite3'


# DISCORD STUFF


#initializing the database
db = SQLAlchemy(app)

# creating the model
class coupons(db.Model):
   id = db.Column('coupon_id', db.Integer, primary_key = True)
   name = db.Column(db.String(50), nullable=False)
   desc = db.Column(db.String(100), nullable=False)  
   img = db.Column(db.String(200), nullable=False)
   amount = db.Column(db.Integer, nullable=False)

def __repr__(self):
    return '<Name %r>' % self.name

TEMPLATES_AUTO_RELOAD = True

@app.route('/', methods=['GET', 'POST'])
def hello():
    coupon_kiss = coupons.query.get(1)
    coupon_movie = coupons.query.get(2)
    coupon_game = coupons.query.get(3)
    coupon_break = coupons.query.get(4)
    coupon_secret = coupons.query.get(5)

    return render_template('index.html',
        coupon_kiss=coupon_kiss, 
        coupon_movie=coupon_movie,
        coupon_game=coupon_game,
        coupon_break=coupon_break,
        coupon_secret=coupon_secret)

@app.route('/subtract', methods=['POST'])
def subtract():
    coupon_kiss = coupons.query.get(1)
    coupon_movie = coupons.query.get(2)
    coupon_game = coupons.query.get(3)
    coupon_break = coupons.query.get(4)
    coupon_secret = coupons.query.get(5)

    if request.method == 'POST':
        # Print the form data to the console
        for key, value in request.form.items():
            if key == "kiss":
                if coupon_kiss.amount > 0:
                    coupon_kiss.amount = coupon_kiss.amount - 1
                return redirect('/kiss')
            if key == "secret":
                if coupon_secret.amount > 0:
                    coupon_secret.amount = coupon_secret.amount - 1
                db.session.commit()
                return redirect('/secret')

@app.route('/kiss')
def discordBot():
    url = 'https://discordapp.com/api/webhooks/1073052116865781881/swJ7VhBi9rwg8sMYYRkNUhL7HetoXqnHmnwWMUMj2CpoDC7cFX2i8ZsG87beLispDv1u'

    data = {
        "username": 'CouponCupid',
        "content": "<@261345972242612226>",
        "embeds": [{
            "title": "KISS",
        }]
    }
    x = requests.post(url, json=data)
    print(x)

    # return render_template('testing_page.html')
    return redirect('/')