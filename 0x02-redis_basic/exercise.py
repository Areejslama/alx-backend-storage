#!/usr/bin/env python3
"""this script to define redis"""
import redis
from typing import Union, Callable
from uuid import uuid4

class Cache:
    """define class"""
    def __init__(self):
        """define init"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """define store method"""
        key = str(uuid4())
        self._redis.set(key, data)

        return key
    
    def get(self, Key: str, fn: [Callable]):
        """define get method"""
        data = self._redis.set(key)
        if data is not None:
            fn(data)
        return data
    
    def get_str(self, key: str):
        """define get function"""
        val =  self._redis.get(key, lambda d: d.decode("utf-8"))
        return val

    def get_int(self):
        data = self.__redis.get(key, int)
        return data
