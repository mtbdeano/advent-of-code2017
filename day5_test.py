from day5 import day5_exit, day5_exit2


def test_exit():
    assert day5_exit('''0
3
0
1
-3''') == 5


def test_exit2():
    assert day5_exit2('''0
3
0
1
-3''') == 10
    