# 이익 = (최저 사과 점수) * (한 상자에 담긴 사과 개수) * (상자의 개수)
# k = 최고점, m = 한 상자에 들어가는 사과의 수, score = 사과들의 점수
"""
pseudo code
sort -> m개 씩 자르고 -> 가격 구해서 -> 합
"""


def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)

    for i in range(0, len(score), m):
        tmp = score[i : i + m]

        if len(tmp) == m:
            answer += min(tmp) * m

    return answer


if __name__ == "__main__":
    print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
    # expected_output = 8
    print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))
    # expected_output = 33


# 1-line Code
def solution(k, m, score):
    return sum(sorted(score)[len(score) % m :: m]) * m
