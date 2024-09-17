from common import course_def


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
              "Chinese": Chinese_score,
              "Math": Math_score,
              "English": English_score
    }

    student_data[Name] = record
    print("Add student scores successfully")

def process_edit(student_data: dict):
    name = input("Please input name: ")
    if name in student_data:
        course = input("Please input course name: ")
        if course in course_def.CPURSE_NAME_LIST:
            score = input("Please input score: ")
            student_data[name][course] = score
            print("Update score successfully")
        else:
            print(f'Course "{course}" is not supported')
    else:
        print(f'Student "{name} does not exit"')

def process_delete(student_data: dict):
    name = input("Please input name: ")
    if name in student_data.keys():
        student_data.pop(name)
        print(f'Delete "{name}" successfully')
    else:
        print(f'Student "{name} does not exit"')

def process_average(student_data: dict):
    student_count = len(student_data)
    if student_count == 0:
        print("No student scores")
        return 
    
    Total_result = {}
    for course in course_def.CPURSE_NAME_LIST:
        Total_result[course] = 0
    
    for record in student_data.values():
        for course in course_def.CPURSE_NAME_LIST:
            Total_result[course] = Total_result[course] + int(record.get(course))

    for course in course_def.CPURSE_NAME_LIST:
        average = Total_result[course] / student_count
        print(f'Average of {course} is: {average}')
    

def process_command(cmd: str, student_data: dict):
    if cmd == "list":
        process_list(student_data)
    elif cmd == "add":
        process_add(student_data)
    elif cmd == "edit":
        process_edit(student_data)
    elif cmd == "delete":
        process_delete(student_data)
    elif cmd == "average":
        process_average(student_data)
