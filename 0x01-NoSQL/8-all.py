#!/usr/bin/env python3
"""this script list documents"""
def list_all(mongo_collection):
    """Check if mongo_collection is None"""
    return [doc for doc in mongo_collection.find()]
