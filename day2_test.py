from day2 import convert_to_arrays, day2_chksum, day2_div


TEST_ARRAY = '''5 1 9 5
7 5 3
2 4 6 8'''


def test_convert_to_arrays():
    a = convert_to_arrays(TEST_ARRAY)
    assert len(a) == 3
    assert len(a[0]) == 4
    assert len(a[1]) == 3
    assert len(a[2]) == 4


def test_day2_chk():
    assert day2_chksum(TEST_ARRAY) == 18


TEST_2 = '''5 9 2 8
9 4 7 3
3 8 6 5'''


def test_day2_div():
    assert day2_div(TEST_2) == 9