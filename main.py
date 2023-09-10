
from utills import load_file, filter_file, sort_file, get_last_operation, finish_file

number = int(input("Введите желаемое количество операций для выввода: "))
def main(number):

    old_file = load_file()
    filt_file = filter_file(old_file)
    sor_file = sort_file(filt_file)
    fin_file = get_last_operation(sor_file, number)
    redact_file = finish_file(fin_file)
    for row in redact_file:
        print(row, end='\n\n')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(number)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
