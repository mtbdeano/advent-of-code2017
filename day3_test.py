from day3 import day3_coord, day3_dist, next_x, walk_around, day3_find_biggest


def test_gen():
    gen = next_x()
    assert next(gen) == (3, 2)
    assert next(gen) == (5, 11)
    assert next(gen) == (7, 28)
    assert next(gen) == (9, 53)


def test_walkabout():
    assert walk_around(5, 11, 22) == (-1, -2)
    assert walk_around(5, 11, 11) == (2, 0)
    assert walk_around(3, 2, 10) == (2, -1)
    assert walk_around(3, 2, 3) == (1, 1)
    assert walk_around(7, 28, 28) == (3, 0)
    assert walk_around(7, 28, 51) == (4, -2)
    assert walk_around(7, 28, 40) == (-3, 0)


def test_coord():
    assert day3_coord(2) == (1, 0)
    assert day3_coord(4) == (0, 1)
    assert day3_coord(15) == (0, 2)
    assert day3_coord(13) == (2, 2)
    assert day3_coord(20) == (-2, -1)
    assert day3_coord(6) == (-1, 0)


def test_dist():
    assert day3_dist(2) == 1
    assert day3_dist(4) == 1
    assert day3_dist(15) == 2
    assert day3_dist(13) == 4
    assert day3_dist(20) == 3
    assert day3_dist(6) == 1
    assert day3_dist(12) == 3
    assert day3_dist(23) == 2
    assert day3_dist(1024) == 31


def test_biggest():
    assert day3_find_biggest(4) == 5
    assert day3_find_biggest(23) == 25
    assert day3_find_biggest(122) == 133
    assert day3_find_biggest(140) == 142
    assert day3_find_biggest(747) == 806
    assert day3_find_biggest(400) == 747

