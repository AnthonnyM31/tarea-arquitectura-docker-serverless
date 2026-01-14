from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    # Obtenemos el parámetro 'name' de la URL
    name = request.args.get('name', 'Usuario')
    return jsonify({"message": f"Hola {name} desde Docker"})

if __name__ == '__main__':
    # Ejecutamos en el puerto 5000, accesible externamente
    app.run(host='0.0.0.0', port=5000)