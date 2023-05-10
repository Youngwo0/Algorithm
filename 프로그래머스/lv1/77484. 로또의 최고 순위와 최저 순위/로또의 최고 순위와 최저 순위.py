def solution(lottos, win_nums):
    dict = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    low = len(set(lottos) & set(win_nums))
    answer = [dict[low + lottos.count(0)], dict[low]]
    return answer


if __name__ == "__main__":
    print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
    # expected output: [3,5]
    print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
    # expected output: [1,6]
    print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))
    # expected output: [1,1]
