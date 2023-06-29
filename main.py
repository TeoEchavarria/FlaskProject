from flask import Flask, jsonify

app = Flask(__name__)

#importar productos
from products import products

@app.route('/')
def hello():
    return 'Hello World Flask'

@app.route('/ping')
def ping():
    return jsonify({"message":"pong"})

@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify(products)

@app.route('/productsPropiedades', methods=['GET'])
def getProductsPropiedades():
    return jsonify({'products' : products})


if __name__ == '__main__':
    app.run(debug=True, port=4000)
