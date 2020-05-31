import redis
import json


class RedisOperations(object):
    def __init__(self, **redis_kwargs):
        host = "18.217.30.68"
        password = "6zl/pAH1cTWPIc2kx8jtlMoGHihHdEU9TW/PYpkOhnhyG1Zr9jundYzqjKXCgtO14yUkCrkheYutFxOh"
        self.db = redis.Redis(host=host, password=password, port=6379)
        self.pipe = self.db.pipeline()

    def put(self, name, item):
        item = json.dumps(item)
        self.db.sadd(name, item)

    def get(self, name):
        result = self.db.spop(name)
        return json.loads(result)
