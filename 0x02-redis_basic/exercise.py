#!/usr/bin/env python3
"""this script to define redis"""
import redis
from typing import Any
from uuid import uuid4

class Cache:
    """define class"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        key = str(uuid4())
        self._redis.set(key, data)
        
        return key
