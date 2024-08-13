#!/usr/bin/env python3
"""this script to insert document"""


def insert_school(mongo_collection, **kwargs):
    """drfine the function"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
