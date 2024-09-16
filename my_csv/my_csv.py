import csv

def read_csv(filename):
    file_instance = open(filename, encoding='utf8')
    csv_reader = csv.reader(file_instance)

    for line in csv_reader:
        print(line)

    file_instance.close()

def read_csv2(filename):
    file_instance = open(filename, encoding='utf8')
    csv_reader = csv.DictReader(file_instance)

    for row in csv_reader:
        print(row)

def write_csv(filename):
    file_instance = open(filename, 'w',  encoding='utf8')
    csv_writer = csv.writer(file_instance)

    header = ['Name', 'Chinese', 'English', 'Math']
    rows = [
        ['Zhangsan', '80', '87', '100'],
        ['Lisi', '78', '79', '98'],
        ['Wangwu', '67', '90', '88']
    ]

    csv_writer.writerow(header)
    csv_writer.writerows(rows)

    file_instance.close()

def write_csv2(filename):
    file_instance = open(filename, 'w', encoding='utf8')

    header = ['Name', 'Chinese', 'English', 'Math']
    rows = [
        {'Name': 'zhangsan',
         'Chinese': 89,
         'English': 76,
         'Math': 90},
        {'Name': 'lisi',
         'Chinese': 84,
         'English': 97,
         'Math': 34},
        {'Name': 'wangwu',
         'Chinese': 83,
         'English': 66,
         'Math': 92}
    ]

    csv_writer = csv.DictWriter(file_instance, fieldnames=header)

    csv_writer.writeheader()
    csv_writer.writerows(rows)

    file_instance.close()


if __name__ == '__main__':
    # read_csv('./students.csv')
    # write_csv('./students2.csv')
    # write_csv2('./students3.csv')
    read_csv2('my_csv\students.csv')