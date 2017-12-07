PUZZLE_INPUT = '''2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14'''


def make_key(a):
    return '_'.join([str(x) for x in a])


def rebalance(banks):
    num_banks = len(banks)
    results = banks
    largest = max(banks)
    for i in range(num_banks):
        if results[i] == largest:
            disburse = results[i]
            results[i] = 0
            current = (i + 1) % num_banks
            while disburse > 0:
                results[current] += 1
                disburse -= 1
                current = (current + 1) % num_banks
            return results
    print('fall through {}, {}'.format(banks, results))
    return results


def day6_halt(s):
    banks = [int(x) for x in s.split()]
    iters = set()
    iters.add(make_key(banks))
    step = 1
    n = rebalance(banks)
    while make_key(n) not in iters:
        # print(iters)
        iters.add(make_key(n))
        step += 1
        n = rebalance(n)
    return step


def day6_halt_loop(s):
    banks = [int(x) for x in s.split()]
    iters = {}
    iters[make_key(banks)] = 1
    step = 1
    n = rebalance(banks)
    while make_key(n) not in iters.keys():
        # print(iters)
        step += 1
        iters[make_key(n)] = step
        n = rebalance(n)
    return step - iters[make_key(n)] + 1


def main():
    print('halting after {} steps'.format(day6_halt(PUZZLE_INPUT)))
    print('halting with {} step loop'.format(day6_halt_loop(PUZZLE_INPUT)))

if __name__ == '__main__':
    main()