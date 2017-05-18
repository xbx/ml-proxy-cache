from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route('/items/<item_id>/')
def items(item_id):
    """Endpoint returning the item information
    ---
    parameters:
      - name: item_id
        in: path
        type: string
        required: true
    definitions:
      Item:
        type: object
        properties:
          id:
            type: string
    responses:
      200:
        description: The ML item information.
        schema:
          $ref: '#/definitions/Item'
    """
    test_result = {
        'foo': 'bar'
    }
    if item_id == 'test':
        result = test_result
    else:
        result = test_result

    return jsonify(result)

app.run(debug=True, host="0.0.0.0", port=8080)