from utills import load_file, filter_file, sort_file, get_last_operation


def test_load_file():
    assert type(load_file()) == list


def test_filter_file():
    assert filter_file()[1]["state"] == "EXECUTED"


def test_sort_file():
    assert sort_file()[1]["date"][:10] == "2019-12-07"


def test_get_last_operation():
    assert get_last_operation(1)[0]["id"] == 863064926
