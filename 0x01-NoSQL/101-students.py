#!/usr/bin/env python3
"""define function"""


def top_students(mongo_collection, top_n=5):
    """Retrieve and sort the top N students by average score in descending order."""
    result = mongo_collection.find({}).sort("averageScore", -1).limit(top_n)
    return result
