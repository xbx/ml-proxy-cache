from datetime import datetime
from elasticsearch import Elasticsearch
import logging

es = Elasticsearch(host='elastic')
logger = logging.getLogger()

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}


def put(**kwargs):
    res = es.index(index="api-stats", doc_type='stat', body=kwargs)
    logger.debug(res['created'])
