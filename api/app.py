from flask import Flask, jsonify
from flasgger import Swagger
from lib import item

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
    result = item.get(item_id)

    return jsonify(result)

app.run(debug=True, host="0.0.0.0", port=8080)
