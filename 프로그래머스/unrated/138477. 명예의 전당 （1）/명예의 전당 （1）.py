# pseudo code
"""
업데이트 되는 순서대로 stacking, sorting -> 상위 k개의 리스트 반환 -> 그중 가장 작은 값
"""


def solution(k, score):
    answer = []

    top_k_list = []

    for i in score:
        top_k_list.append(i)
        top_k_list = sorted(top_k_list, reverse=True)[:k]

        answer.append(min(top_k_list))

    return answer


if __name__ == "__main__":
    print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
    # expected output: [10, 10, 10, 20, 20, 100, 100]