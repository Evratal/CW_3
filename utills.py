import json


def load_file():
    with open('operations.json', 'r', encoding='utf-8') as file:
        old_file = json.load(file)
        return old_file


def filter_file():
    filter_list = []
    old_list = load_file()
    for row in old_list:
        if "state" in row and row['state'] == 'EXECUTED':
            filter_list.append(row)
    return filter_list


def sort_file():
    work_list = filter_file()
    work_list.sort(key=lambda d: d['date'], reverse=True)
    return work_list


def get_last_operation(number_last_values):
    operation_list = sort_file()
    operation_list = operation_list[:number_last_values]
    return operation_list


print(load_file())
print('*************************')
print(filter_file())
for row in filter_file():
    print (row['date'])
print('----------------------')
print(sort_file())
for row in sort_file():
    print (row['date'])
print('...................')
print(get_last_operation(1)[0])