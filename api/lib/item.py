from . import storage
from . import ml_api
import logging


logger = logging.getLogger()


def get(item_id):
    test_result = {
        'foo': 'bar'
    }
    if item_id == 'test':
        return test_result

    item = storage.get(item_id)
    if item is None:
        logger.debug('Miss!')
        item = ml_api.get(item_id)
        storage.store(item_id, item)
        item = storage.get(item_id)
    else:
        logger.debug('Hit!')

    result = {'item': item}
    return result
