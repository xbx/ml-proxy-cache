import requests
import logging

logger = logging.getLogger()

ML_API_URL = 'https://api.mercadolibre.com/'
ML_API_URL_ITEMS = ML_API_URL + 'items/'

keys_to_keep = ['id', 'title', 'category_id', 'price', 'start_time', 'stop_time']


def get(item_id):
    logger.debug('ml_api: Getting item: ' + item_id)
    r = requests.get(ML_API_URL_ITEMS + item_id)
    if r.status_code == 200:
        item_dict = r.json()
        # Se filtran las key que solo necesitamos:
        item = {key: item_dict[key] for key in keys_to_keep}
        return item
    elif r.status_code == 404:
        logger.warn('Item %s not found in ML. Status 404' % item_id)
        return None
    elif r.status_code >= 500:
        logger.warn('Error received when getting item %s. Status %s' % (item_id, r.status_code))
