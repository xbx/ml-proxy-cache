from . import storage, ml_api, stats, timer
import logging


logger = logging.getLogger()


def get(item_id):
    response_time_api_calls = lambda: 0
    status_code = 200
    was_hit = 1

    with timer.elapsed_timer() as response_time:
        item = storage.get(item_id)
        if item is None:
            was_hit = 0
            logger.debug('Miss!')
            with timer.elapsed_timer() as response_time_api_calls:
                item = ml_api.get(item_id)
            storage.store(item_id, item)
            item = storage.get(item_id)
        else:
            logger.debug('Hit!')

        result = {'item': item}

    if item is None:
        status_code=404

    stats.put(status_code=status_code,
              response_time_api_calls=response_time_api_calls(),
              response_time=response_time(),
              hit=was_hit
              )
    return result
