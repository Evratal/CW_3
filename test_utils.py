from utills import load_file


def test_load_file():
    assert type(load_file()) == list
