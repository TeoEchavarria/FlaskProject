from flask import Flask

app = Flask(__name__)

#importar productos
from products import products

@app.route('/')
def hello():
    return 'Hello World Flask'

@app.route('/ping')
def ping():
    return products


if __name__ == '__main__':
    app.run(debug=True, port=4000)
