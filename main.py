from flask import Flask, jsonify, request

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
    return jsonify({'products' : products})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    final_product = [product for product in products if product['name'] == product_name]

    if (len(final_product)) > 0 :
        return jsonify({'product' : final_product[0]})
    else:
        return jsonify({'message':'Product Not Found'})

@app.route('/products', methods=['POST'])
def addProduct():
    new_prodcut = {'name': request.json['name'], 'price':request.json['price']}
    products.append(new_prodcut)
    return jsonify({'message': 'Producto Recibido' })

if __name__ == '__main__':
    app.run(debug=True, port=4000)
