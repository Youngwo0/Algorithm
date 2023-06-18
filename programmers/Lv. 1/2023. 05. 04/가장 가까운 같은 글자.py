def solution(s):
    char_set = {}
    answer = [-1] * len(s)

    for i, char in enumerate(s):
        if char in char_set:
            answer[i] = i - char_set[char]
        char_set[char] = i

    return answer


if __name__ == "__main__":
    print(solution("banana"))
