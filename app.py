from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# add database
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coupons.sqlite3'

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

    if request.method == 'POST':
        # Print the form data to the console
        for key, value in request.form.items():
            if key == "kiss":
                coupon_kiss.amount = coupon_kiss.amount - 1;
                db.session.commit()

    return render_template('index.html',
        coupon_kiss=coupon_kiss, 
        coupon_movie=coupon_movie,
        coupon_game=coupon_game,
        coupon_break=coupon_break)

@app.route('/subtract', methods=['POST'])
def subtract():
    coupon_kiss = coupons.query.get(1)
    coupon_movie = coupons.query.get(2)
    coupon_game = coupons.query.get(3)
    coupon_break = coupons.query.get(4)

    if request.method == 'POST':
        # Print the form data to the console
        for key, value in request.form.items():
            if key == "kiss":
                coupon_kiss.amount = coupon_kiss.amount - 1;

                db.session.commit()
                return redirect('/')