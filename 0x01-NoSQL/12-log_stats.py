#!/usr/bin/env python3
"""Define function to count stats"""
from pymongo import MongoClient

def count_stats():
    """Fetch and print statistics about Nginx logs"""
    client = MongoClient("mongodb://localhost:27017/")
    db = client.logs
    collection = db.nginx

    total = collection.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    stats = {method: collection.count_documents({"method": method}) for method in methods}
    get_count = collection.count_documents({"method": "GET", "path": "/status"})

    print(f"{total} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {stats[method]}")
    print(f"{get_count} status check")

if __name__ == "__main__":
    count_stats()
