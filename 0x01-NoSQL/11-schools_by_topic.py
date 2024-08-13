#!/usr/bin/env python3
"""this script to find topic"""


def schools_by_topic(mongo_collection, topic):
    """define the function"""
    result = mongo_collection.find({"topics" : topic})
    return list(result)
