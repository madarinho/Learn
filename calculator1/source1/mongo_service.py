import os
import pymongo
from pymongo import MongoClient
from calculator1.source1.calculation import Calculation


class MongoSerivce:
    def __init__(self):
        self.cluster_madar = pymongo.MongoClient(os.environ["MDB_URL"])
        self.db_calculator = self.cluster_madar["calculator"]
        self.collection_calculations = self.db_calculator["calculations"]

    def insert(self, raw_calculation):
        calculation = Calculation(raw_calculation)
        self.collection_calculations.insert_one(calculation.__dict__)

    def find_by_number(self, number):
        query = { "raw": { "$regex": f'([^0-9]|^){number}([^0-9]|$)' } }
        result = self.collection_calculations.find_one(query)
        return result['raw']