import redis
import json
from urlparse import urlparse
from search import settings

class DataBase():
    def __init__(self):
        self.host = urlparse(settings.REDIS_HOST)
        self.client = redis.StrictRedis(
            host=self.host.hostname,
            port=self.host.port,
            password=settings.REDIS_PWD
        )
        self.HASH = 'courses'

    def save(self, items):
        for item in items:
            print "save"
            self._save(
                item.get('title'),
                item.get('formattedUrl')
            )

    def _save(self, name, address):
        try:
            if not self.client.hexists(self.HASH, str(name)):
                self.client.hset(self.HASH, str(name), str(address))
        except Exception as Error:
            print "Dont save because %s" % Error

    def get(self, key):
        try:
            if not self.client.hexists(self.HASH, str(key)):
                raise KeyError('Invalid')
            return self.client.hget(self.HASH, str(key))
        except Exception:
            raise Exception

