#!/usr/bin/env python3
"""define function"""


def top_students(mongo_collection):
    """function"""
    result = mongo_collection.find({"averageScores" : "averageScore"})
    return result
