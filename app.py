from flask  import Flask, jsonify, request
import src.middleware.connection as connection
from src.handlers.rice_products import rice_products

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/bcg/v1/login', methods=['POST'])
def login():
    auth = request.authorization

    if auth and auth.password == 'password':
        return ''
    else:
        return 'could not verify!', 401

@app.route('/bcg/v1/rice-products', methods=['GET'])
def handler_rice_products():
    respone = rice_products()
    return respone


@app.route('/bcg/v1/TEST_mySQL', methods=['GET'])
def test():
    code = request.args.get('code')
    try:
        result = connection.query_database("""SELECT * from `rice_amphoe` where `P_NAME_T` = '{}'""".format(code))
        return jsonify(result), 200
    except:
        return ''

if __name__ == '__main__':
    app.run(debug=True)