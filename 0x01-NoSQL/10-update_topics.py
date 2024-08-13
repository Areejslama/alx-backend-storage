#!/usr/bin/env python3
"""this script to change topics"""


def update_topics(mongo_collection, name, topics):
    """define the function"""
    result = mongo_collection.update_many(
            {"name" : name},
            {"$set": {"topics" : topics}}
)
    return result
