from utills import load_file, filter_file, sort_file, get_last_operation, finish_file

old_file = load_file()
filt_file = filter_file(old_file)
sor_file = sort_file(filt_file)
fin_file = get_last_operation(sor_file, 5)
redact_file = finish_file(fin_file)





def test_load_file():
    assert type(load_file()) == list


def test_filter_file():
    assert filter_file(old_file)[1]["state"] == "EXECUTED"


def test_sort_file():
    assert sort_file(filt_file)[1]["date"][:10] == "2019-12-07"


def test_get_last_operation():
    assert get_last_operation(sor_file,1)[0]["id"] == 863064926

def test_finish_file():
    assert type(finish_file(fin_file)) == list
