def process_list(student_data: dict):
    records = list(student_data.values())
    records.sort(key=lambda a: a.get("Name"))

    for record in records:     
        print(record.get("Name"))
        print(f'Chinese score: {record.get("Chinese")}')
        print(f'Math score: {record.get("Math")}')
        print(f'English score: {record.get("English")}')


def process_add(student_data: dict):
    Name = input("Please input name: ")
    Chinese_score = input("Please input Chinese score: ")
    Math_score = input("Please input Math score: ")
    English_score = input("Please input English score: ")

    record = {"Name": Name, 
              "Chinese": int(Chinese_score),
              "Math": int(Math_score),
              "English": int(English_score)
    }

    student_data[Name] = record
    print("Add student scores successfully")


def process_edit(student_data: dict):
    pass

def process_delete(student_data: dict):
    name = input("Please input name: ")
    if name in student_data.keys():
        student_data.pop(name)
        print(f'delete "{name}" successfully')
    else:
        print(f'Student "{name} does not exit"')
        



def process_command(cmd: str, student_data: dict):
    if cmd == "list":
        process_list(student_data)
    elif cmd == "add":
        process_add(student_data)
    elif cmd == "edit":
        process_edit(student_data)
    elif cmd == "delete":
        process_delete(student_data)
