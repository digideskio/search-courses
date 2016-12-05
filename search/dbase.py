# -*- coding: utf-8 -*-

import redis
import json
from pymongo import MongoClient
from urlparse import urlparse
from search import settings

class MongoBase():
    def __init__(self):
        self.host = settings.PALOMA_DB_HOST
        self.port = settings.PALOMA_DB_PORT
        self.name = settings.PALOMA_DB_NAME
        client = MongoClient(self.host, int(self.port))
        dbname = client[self.name]
        self.db = dbname['language_ingles']

    def get(self, key):
        num_courses = self.db.count({"url": key})
        if num_courses > 0:
            return True
        return False

class DataBase():
    def __init__(self):
        self.host = urlparse(settings.REDIS_HOST)
        self.client = redis.StrictRedis(
            host=self.host.hostname,
            port=self.host.port,
            password=settings.REDIS_PWD
        )
        self.HASH = 'courses'
        self.HASH_BLACK = 'black_list'
        self.db_paloma = MongoBase()

    def check_db_paloma(self, key):
        return self.db_paloma.get(key)

    def save_black(self, address):
        if not self.client.hexists(self.HASH_BLACK, str(address)):
            self.client.hset(self.HASH_BLACK, str(address), 1)

    def get_black(self, address):
        try:
            if not self.client.hexists(self.HASH_BLACK, str(address)):
                raise KeyError('Invalid')
            return self.client.hget(self.HASH_BLACK, str(address))
        except Exception:
            raise Exception

    def check_black_list(self, address):
        return self.client.hexists(self.HASH_BLACK, str(address))

    def save(self, items):
        for item in items:
            self._save(
                item.get('title').encode("utf-8"),
                item.get('formattedUrl')
            )

    def _save(self, name, address):
        try:
            if not self.client.hexists(self.HASH, str(name)) and not self.check_db_paloma(address) and \
               not self.check_black_list(address):
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

    def remove(self, key):
        try:
            if not self.client.hexists(self.HASH, str(key)):
                raise KeyError('Invalid')
            self.client.hdel(self.HASH, str(key))
        except Exception:
            raise Exception

    def get_all(self):
        try:
            return self.client.hscan_iter(self.HASH)
        except Exception:
            raise Exception

