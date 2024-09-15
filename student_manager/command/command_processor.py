def process_list(student_data: dict):
    records = list(student_data.values())
    records.sort(key=lambda a: a.get("name"))

    for record in records:
        print(record.get("Name"))
        print(f'Chinese score: {record.get("Chinese")}')
        print(f'Math score: {record.get("Math")}')
        print(f'English score: {record.get("English")}')


def process_add():
    pass

def process_edit():
    pass

def process_delete():
    pass


def process_command(cmd: str, student_data: dict):
    if cmd == "list":
        process_list(student_data)
    elif cmd == "add":
        process_add(student_data)
    elif cmd == "edit":
        process_edit(student_data)
    elif cmd == "delete":
        process_delete(student_data)
