#!/usr/bin/env python3
"""this script to define redis"""
import redis
from typing import Union, Callable, Any, Optional
from uuid import uuid4
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """define decorator"""
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """define function"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """define the function"""
    @wraps(method)
    def wrapper(self, *args, **kwds):
        key = method.__qualname__
        l_input = key + ":inputs"
        l_output = key + ":outputs"
        data = str(args)
        self._redis.rpush(l_input, data)
        m = method(self, *args, **kwds)
        self._redis.rpush(l_output, str(m))
        return m
    return wrapper


class Cache:
    """define class"""
    def __init__(self):
        """define init"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the data in Redis and return a unique key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable[[bytes], Any]] = None) -> Any:
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

    def replay(func: callable):
        """define function"""
        key = func.__qualname__
        data1 = self.__redis.lrange(f"{key}:inputs", 0, -1)
        data2 = self.__redis.lrange(f"{key}:outputs", 0, -1)
        print("{} was called {} times:".format
              (key, len(data1)))
        for k, v in zip(data1, data2):
            val = '{}(*{}) -> {}'.format(
                    key,
                    k.decode('utf-8'),
                    v.decode('utf-8')
                    )
            print(val)
