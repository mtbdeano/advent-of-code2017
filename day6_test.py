from day6 import day6_halt, rebalance, make_key, day6_halt_loop


def test_make_key():
    assert make_key(['1', '2', '3']) == '1_2_3'


def test_balance():
    assert rebalance([0, 2, 7, 0]) == [2, 4, 1, 2]
    assert rebalance([2, 4, 1, 2]) == [3, 1, 2, 3]
    assert rebalance([3, 1, 2, 3]) == [0, 2, 3, 4]
    assert rebalance([0, 2, 3, 4]) == [1, 3, 4, 1]
    assert rebalance([1, 3, 4, 1]) == [2, 4, 1, 2]
    

def test_halting():
    assert day6_halt("0 2 7 0") == 5


def test_halting_length():
    assert day6_halt_loop("0 2 7 0") == 4
