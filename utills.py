from datetime import datetime
import json


def load_file():
    with open('operations.json', 'r', encoding='utf-8') as file:
        old_file = json.load(file)
        return old_file


def filter_file(not_filt_file):
    filter_list = []
    for row in not_filt_file:
        if "state" in row and row['state'] == 'EXECUTED':
            filter_list.append(row)
    return filter_list


def sort_file(not_sort_list):
    work_list = not_sort_list
    work_list.sort(key=lambda d: d['date'], reverse=True)
    return work_list


def get_last_operation(file, number_last_values):
    operation_list = file
    operation_list = operation_list[:number_last_values]
    return operation_list


def finish_file(list_operation):
    finish_list = []
    for row in list_operation:
        date = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = row["description"]

        if "from" in row:
            string_from_letter = "".join(letter for letter in row["from"] if letter.isalpha() and not letter.isdigit())
            string_from_digit = "".join(letter for letter in row["from"] if letter.isdigit() and not letter.isalpha())
            new_string_from_digit = " " + string_from_digit[:4] + " " + string_from_digit[
                                                                        4:6] + "** **** " + string_from_digit[-4:]
            finish_string_from = string_from_letter + new_string_from_digit
        else:
            finish_string_from = ''
        string_to = "Счет **" + row["to"][-4:]
        string_bill = row["operationAmount"]["amount"] + " " + row["operationAmount"]["currency"]["name"]

        finish_list.append(f"""\
 {date} {description}
 {finish_string_from}->{string_to}
 {string_bill}""")

    return finish_list


