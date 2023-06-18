def solution(s: str) -> int:
    answer = 0
    cnt1, cnt2 = 0, 0
    for chr in s:
        if cnt1 == cnt2:
            answer += 1
            k = chr

        if chr == k:
            cnt1 += 1
        else:
            cnt2 += 1
    return answer


if __name__ == "__main__":
    print(solution("banana"))
    # expected output: 3
    print(solution("abracadabra"))
    # expected output: 6
    print(solution("aaabbaccccabba"))
    # expected output: 3
