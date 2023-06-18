from collections import Counter


def solution(participant: list, completion: list) -> str:
    comp = Counter(completion)

    for person in participant:
        if person not in comp:
            return person
        else:
            comp[person] -= 1

    for person, num in comp.items():
        if num == -1:
            return person


if "__main__" == __name__:
    print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
    # expected output: "leo"

## Counter 객체
import collections


def solution_1(participant: list, completion: list) -> str:
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


if "__main__" == __name__:
    print(solution_1(["leo", "kiki", "eden"], ["eden", "kiki"]))
    # expected output: "leo"
