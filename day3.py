

def next_x():
    x = 0
    i = 0
    while True:
        x = pow(2 * i + 1, 2) + i + 1
        i += 1
        yield (i * 2 + 1, x)


def walk_around(size, start, n):
    # print('wa {}, {}, {}'.format(size, start, n))
    if n == 1:
        return (0, 0)
    elif n == 2:
        return (1, 0)
    move = (0, 1)
    current = start
    limit = int(size / 2)
    (x, y) = (limit, 0)
    while current != n:
        (x, y) = (x + move[0], y + move[1])
        current += 1
        if move == (0, 1) and y == limit:
            move = (-1, 0)
        elif move == (-1, 0) and x == -limit:
            move = (0, -1)
        elif move == (0, -1) and y == -limit:
            move = (1, 0)
        elif move == (1, 0) and x == limit + 1:  # now go up
            move = (0, 1)
        print("x, y = {}, {}, move = {}, {}, current = {} looking for {}".
              format(x, y, move[0], move[1], current, n))
    print('found {}, {}'.format(x, y))
    return (x, y)


def day3_coord(n):
    gen = next_x()
    (size, start) = next(gen)
    (psize, pstart) = (1, 1)
    while n > start:
        # print('size {} start {} n {}'.format(size, start, n))
        (psize, pstart) = (size, start)
        (size, start) = next(gen)
    # `psize` is the length of a side, `pstart` is the `(y = 0, x = psize/2)`
    print('final size {} start {} n {}'.format(size, start, n))
    return walk_around(psize, pstart, n)


def day3_dist(n):
    (x, y) = day3_coord(n)
    return abs(x) + abs(y)


def day3_find_biggest(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    current = 2
    board = {(0, 0): 1, (1, 0): 1}
    subtot = 1
    while subtot <= n:
        current += 1
        (x, y) = day3_coord(current)
        subtot = \
            board.get((x - 1, y - 1), 0) + \
            board.get((x, y - 1), 0) + \
            board.get((x + 1, y - 1), 0) + \
            board.get((x + 1, y), 0) + \
            board.get((x + 1, y + 1), 0) + \
            board.get((x, y + 1), 0) + \
            board.get((x - 1, y + 1), 0) + \
            board.get((x - 1, y), 0)
        board[(x, y)] = subtot
        print(board)
        print('im at {}, {}, value {} sum {}'.format(x, y, current, subtot))

    return subtot


def main():
    print('distance is {}'.format(day3_dist(361527)))
    print('biggest is {}'.format(day3_find_biggest(361527)))


if __name__ == '__main__':
    main()
