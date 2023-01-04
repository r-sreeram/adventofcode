import itertools


def cyclic_permutations(iterable):
    if (n := len(pool := tuple(iterable))) < 3:
        yield pool
        return
    for a, b in itertools.combinations(range(1, n), 2):
        for perm in itertools.permutations(pool[1:a] + pool[a + 1 : b] + pool[b + 1 :]):
            yield (pool[0], pool[a], *perm, pool[b])
