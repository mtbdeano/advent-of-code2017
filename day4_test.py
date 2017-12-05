from day4 import day4_is_valid


def test_valid():
    assert day4_is_valid('aa bb cc dd ee') == True
    assert day4_is_valid('aa bb cc dd aa') == False
    assert day4_is_valid('aa bb cc dd aaa') == True
    