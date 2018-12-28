from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import dbSetup
import json
from pprint import pprint

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'xcjytebjby6 yycefgjydtvh b'
db = SQLAlchemy(app)
dbSetup.setup()
import dbModel

@app.route('/')
def list():
    productList = dbModel.Product.query.all()
    # prod1 = dbModel.Product(name = 'Apaszka Londyn',currentPrice = '119.90 zł', originalPrice='159.90 zł')
    # db.session.add(prod1)
    # prod2 = dbModel.Product(name = 'Apaszka Paryż',currentPrice = '119.90 zł', originalPrice='159.90 zł')
    # db.session.add(prod2)
    # prod3 = dbModel.Product(name = 'Apaszka Tokyo',currentPrice = '119.90 zł', originalPrice='159.90 zł')
    # db.session.add(prod3)
    # db.session.commit()
    # print(productList)
    return render_template('index.html', productList=productList)

@app.route('/login')
def login():
    return render_template('index.html')

def updateDB():
    return 0

if __name__ == '__main__':
    updateDB()
    app.run(debug=True)
