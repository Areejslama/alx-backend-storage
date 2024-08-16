#!/usr/bin/env python3
"""this script to define redis"""
import redis
from typing import Union, Callable, Any, Optional
from uuid import uuid4
from functools import wraps


def count_calls(method: Optional[Callable]) -> Callable:
        """define decorator"""
        @wraps(method)
        def wrapper(self, *args, **kwargs ):
            """define function"""
            key = f"{method.__name__}_calls"
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper

class Cache:
    """define class"""
    def __init__(self):
        """define init"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the data in Redis and return a unique key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], Any]] = None) -> Any:
        """Retrieve data from Redis and optionally apply a transformation"""
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve data as a string from Redis"""
        data = self.get(key, lambda d: d.decode("utf-8"))
        return data

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve data as an integer from Redis"""
        data = self.get(key, int)
        return data
