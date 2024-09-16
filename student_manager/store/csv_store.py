import csv
import os

file = "student_manager\store\students.csv"

def load_data() -> dict:
    if os.path.exists(file):
        file_instance = open(file, encoding='utf8')
        csv_reader = csv.DictReader(file_instance)

        result = {}
        for row in csv_reader:
            name = row.get("Name")
            result[name] = row
        # print(result)

        return result

def save_data(student_data: dict):
    file_instance = open(file, 'w', encoding='utf8')

    if len(student_data) > 0:
        rows = list(student_data.values())
        csv_writer = csv.DictWriter(file_instance, fieldnames=rows[0].keys())
        csv_writer.writeheader()
        csv_writer.writerows(rows)

    file_instance.close()

  