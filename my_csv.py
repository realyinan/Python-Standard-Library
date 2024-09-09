import csv

def read_csv(filename):
    file_instance = open(filename, encoding='utf8')
    csv_reader = csv.reader(file_instance)

    for line in csv_reader:
        print(line)

    file_instance.close()

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


if __name__ == '__main__':
    # read_csv('./students.csv')
    write_csv('./students2.csv')