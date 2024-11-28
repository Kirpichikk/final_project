import json
from redis import Redis

class RedisCache:
    def __init__(self, config: dict):
        self.config = config
        self.conn = self._connect()

    def _connect(self):
        conn = Redis(**self.config)
        return conn

    def reconnect_if_need(self):
        try:
            self.conn.ping()
        except:
            self.conn = self._connect()

    def set(self, key, value):
        self.conn.set(key, value)

    def get(self,key):
        return self.conn.get(key)

    def add_list(self,key, value):
        self.conn.rpush(key,value)

    def get_list(self,key):
        return self.conn.lrange(key, 0, -1)

    def create_hset(self, key, field, value):
        self.conn.hset(key, field, value)

    def get_hset(self,key, field):
        return self.conn.hget(key, field)

    def get_hsetall(self,key):
        return self.conn.hgetall(key)

    def hdel(self, key, field):
        self.conn.hdel(key, field)

    def clean(self):
        self.conn.flushall()
