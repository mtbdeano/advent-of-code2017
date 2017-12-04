from day1 import adder, halfadder


def test_adder():
    assert adder('1122') == 3


def test_adder2():
    assert adder('1111') == 4


def test_adder3():
    assert adder('1234') == 0


def test_adder4():
    assert adder('91212129') == 9


def test_hadder2():
    assert halfadder('1221') == 0

def test_hadder3():
    assert halfadder('123425') == 4


def test_hadder():
    assert halfadder('1212') == 6


def test_hadder4():
    assert halfadder('123123') == 12
    


def test_hadder5():
    assert halfadder('12131415') == 4
    
