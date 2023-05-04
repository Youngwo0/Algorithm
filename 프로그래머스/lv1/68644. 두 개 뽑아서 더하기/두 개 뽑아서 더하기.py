from itertools import combinations


def solution(numbers):
    return list(sorted(list(set(map(sum, combinations(numbers, 2))))))