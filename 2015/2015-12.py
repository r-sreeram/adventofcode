# Day 12: JSAbacusFramework.io
# https://adventofcode.com/2015/day/12


def dfs(obj):
    if isinstance(obj, int):
        return obj, obj
    if isinstance(obj, list) and obj:
        return (sum(s) for s in zip(*[dfs(x) for x in obj]))
    if isinstance(obj, dict) and obj:
        v = [sum(s) for s in zip(*[dfs(x) for x in obj.values()])]
        return v[0], 0 if "red" in obj.values() else v[1]
    return 0, 0


print(*(dfs(eval(input()))), sep="\n")
