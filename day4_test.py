from day4 import day4_is_valid, day4_has_anagrams


def test_valid():
    assert day4_is_valid('aa bb cc dd ee') == True
    assert day4_is_valid('aa bb cc dd aa') == False
    assert day4_is_valid('aa bb cc dd aaa') == True
    

def test_anagrams():
    assert day4_has_anagrams('abcde fghij') == True
    assert day4_has_anagrams('abcde xyz ecdab') == False
    assert day4_has_anagrams('a ab abc abd abf abj') == True
    assert day4_has_anagrams('iiii oiii ooii oooi oooo') == True
    assert day4_has_anagrams('oiii ioii iioi iiio') == False
