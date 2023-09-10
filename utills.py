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
