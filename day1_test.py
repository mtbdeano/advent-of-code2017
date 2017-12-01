from day1 import adder


def test_adder():
    assert adder('1122') == 3


def test_adder2():
    assert adder('1111') == 4


def test_adder3():
    assert adder('1234') == 0


def test_adder4():
    assert adder('91212129') == 9
