#!/usr/bin/env python3
"""Define function"""


def top_students(mongo_collection):
    """Retrieve and sort the top average score in descending order."""
    pipeline = [
        {
            '$project': {
                '_id': 1,
                'name': 1,
                'averageScore': {
                    '$avg': '$topics.score'
                }
            }
        },
        {
            '$sort': {'averageScore': -1}
        },
    ]
    result = mongo_collection.aggregate(pipeline)
    return result

