def solution(n, m, section):
    answer = 0
    tmp = 0
    for i in range(len(section)):
        # print(section[i])
        if section[i] <= tmp:
            # print(tmp)
            continue

        else:
            answer += 1
            tmp = section[i] + m - 1

    return answer


if __name__ == "__main__":
    print(solution(8, 4, [2, 3, 6]))
    # expected output: 2
    print(solution(5, 4, [1, 3]))
    # expected output: 1
    print(solution(4, 1, [1, 2, 3, 4]))
    # expected output: 4
