from utills import load_file, filter_file


def test_load_file():
    assert type(load_file()) == list


def test_filter_file():
    assert filter_file()[1]["state"] == "EXECUTED"
