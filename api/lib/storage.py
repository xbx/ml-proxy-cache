import redis

r = redis.StrictRedis(host='redis', port=6379, db=0)


def _make_redis_id(item_id):
    return 'item:' + item_id


def get(item_id):
    id_ = _make_redis_id(item_id)
    item = r.get(id_)
    if item is not None:
        return item.decode('utf-8')
    else:
        return None


def store(item_id, item):
    r.set(_make_redis_id(item_id), item)
