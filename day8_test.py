from day8 import day8_run

PROGRAM = '''b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10'''


def test_day8():
    results = day8_run(PROGRAM)
    assert results['c'] == -10
    assert results['a'] == 1
    assert results['b'] == 0
    assert max(results.values()) == 1
