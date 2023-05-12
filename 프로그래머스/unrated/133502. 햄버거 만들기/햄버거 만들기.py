def solution(ingredient: list) -> int:
    answer = 0

    stack = []
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1, 2, 3, 1]:
            answer += 1
            for i in range(4):
                stack.pop()

    return answer


if "__main__" == __name__:
    print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
    # expected: 2
    print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))
    # expected: 0
