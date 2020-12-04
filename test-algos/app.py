from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail
from chatbot import bot
import os

# --------------------------------------

# GUI + website
app = Flask(__name__)
# switches from deployment to development sever
ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    # database config is 'postgresql://username:password@serveradress/servername
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'postgresql://postgres:postgres@localhost/feedback_chatbot'

else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# --------------------------------------


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    emotion = db.Column(db.String(200))
    comments = db.Column(db.Text())

    def __init__(self, customer, emotion, comments):
        self.customer = customer
        self.emotion = emotion
        self.comments = comments


# --------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# --------------------------------------

@app.route("/get")
def get_bot_response():
    usertext = request.args.get('msg')
    return str(bot.get_response(usertext))


# --------------------------------------

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        emotion = request.form['emotion']
        comments = request.form['comments']
        if customer == '' or emotion == '':
            return render_template('index.html', message='Por favor preencha todos os campos')

        # if the customer's name is not on database, it will add its feedback to it
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer, emotion, comments)
            db.session.add(data)
            db.session.commit()
            send_mail(customer, emotion, comments)
            return render_template('success.html')
        return render_template('index.html', message='Você já mandou seu feedback')


if __name__ == "__main__":
    app.run()
# --------------------------------------
