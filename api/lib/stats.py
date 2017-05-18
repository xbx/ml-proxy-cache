from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError
import logging

ES_HOST = 'elasticsearch'
INDEX_NAME = 'ml-proxy-api-stats'

es = Elasticsearch(host=ES_HOST)
logger = logging.getLogger()

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}


def put(**kwargs):
    res = es.index(index=INDEX_NAME, doc_type='stat', body=kwargs)
    logger.debug(res['created'])


def get():
    try:
        #stat = es.get(index=INDEX_NAME, doc_type="stat", id='AVwZ5IjzZVLpAlvalMIB')['_source']
        result = es.search(
            index=INDEX_NAME,
            body={
              "aggs" : {
                    "avg_response_time": {"avg": {"field": "response_time"}},
                    "avg_response_time_api_calls": {"avg": {"field": "response_time_api_calls"}}
              }
            }
        )
        return {
            "avg_response_time": result['aggregations']['avg_response_time']['value'],
            "avg_response_time_api_calls": result['aggregations']['avg_response_time_api_calls']['value']
        }
    except NotFoundError as ex:
        logger.error('Error getting stats: %s' % str(ex))

    return None
