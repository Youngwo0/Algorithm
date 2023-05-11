def solution(n: int, lost: list, reverse: list) -> int:
    reverse_student = set(reverse) - set(lost)
    lost_student = set(lost) - set(reverse)

    for student in reverse_student:
        if (student - 1) in lost_student:
            lost_student.remove((student - 1))
        elif (student + 1) in lost_student:
            lost_student.remove((student + 1))

    return n - len(lost_student)


if __name__ == "__main__":
    print(solution(5, [2, 4], [1, 3, 5]))
    # expected output: 5
    print(solution(5, [2, 4], [3]))
    # expected output: 4xa
    print(solution(3, [3], [1]))
    # expected output: 2
