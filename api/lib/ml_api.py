import requests
import logging

logger = logging.getLogger()

ML_API_URL = 'https://api.mercadolibre.com/'
ML_API_URL_ITEMS = ML_API_URL + 'items/'

item_keys_to_keep = ['id', 'title', 'category_id', 'price', 'start_time', 'stop_time']
child_keys_to_keep = ['id', 'stop_time']


def get(item_id):
    item = get_item(item_id)
    if item is not None:
        children = get_children(item_id)
        item['children'] = children

    return item


def get_item(item_id):
    logger.debug('ml_api: Getting item: ' + item_id)
    r = requests.get(ML_API_URL_ITEMS + item_id)
    if r.status_code == 200:
        item_dict = r.json()
        # Se filtran las key que solo necesitamos:
        item = {key: item_dict[key] for key in item_keys_to_keep}
        return item
    elif r.status_code == 404:
        logger.warn('Item %s not found in ML. Status 404' % item_id)
    elif r.status_code >= 500:
        logger.warn('Error received when getting item %s. Status %s' % (item_id, r.status_code))

    return None

def get_children(item_id):
    logger.debug('ml_api: Getting item children: ' + item_id)
    r = requests.get(ML_API_URL_ITEMS + item_id + '/children')
    if r.status_code == 200:
        children_list = r.json()
        children_parsed = []
        for child_original in children_list:
            # Se filtran las key que solo necesitamos:
            child = {key: child_original[key] for key in child_keys_to_keep}
            children_parsed.append(child)
        return children_parsed
    elif r.status_code == 404:
        logger.warn('Item %s not found in ML. Status 404' % item_id)
    elif r.status_code >= 500:
        logger.warn('Error received when getting item %s. Status %s' % (item_id, r.status_code))

    return None
