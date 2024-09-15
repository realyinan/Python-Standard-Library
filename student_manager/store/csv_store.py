import csv
import os

def load_data() -> dict:
    file = "./students.csv"

    if os.path.exists(file):
        file_instance = open(file, encoding='utf8')
        csv_reader = csv.DictReader(file_instance)

        result = {}
        for row in csv_reader:
            name = row.get("name")
            result[name] = row

        return result

def save_data(data: dict):
    pass

