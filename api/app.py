from flask import Flask, jsonify
from flasgger import Swagger
from lib import storage, ml_api
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging_handler = logging.StreamHandler()
logger.addHandler(logging_handler)

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
        return jsonify(test_result)

    item = storage.get(item_id)
    if item is None:
        logger.debug('Miss!')
        item = ml_api.get(item_id)
        storage.store(item_id, item)
        item = storage.get(item_id)
    else:
        logger.debug('Hit!')

    result = {'item': item}

    return jsonify(result)

app.run(debug=True, host="0.0.0.0", port=8080)
