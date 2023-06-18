def solution(numbers: list, hand: str) -> str:
    answer = ""

    pad = {
        "1": (0, 0),
        "2": (0, 1),
        "3": (0, 2),
        "4": (1, 0),
        "5": (1, 1),
        "6": (1, 2),
        "7": (2, 0),
        "8": (2, 1),
        "9": (2, 2),
        "*": (3, 0),
        "0": (3, 1),
        "#": (3, 2),
    }

    left = pad["*"]
    right = pad["#"]

    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += "L"
            left = pad[str(num)]

        elif num == 3 or num == 6 or num == 9:
            answer += "R"
            right = pad[str(num)]

        else:
            # 번호와 왼손의 거리 계산
            left_dis = abs(left[0] - pad[str(num)][0]) + abs(left[1] - pad[str(num)][1])
            # 번호와 오른손의 거리 계산
            right_dis = abs(right[0] - pad[str(num)][0]) + abs(
                right[1] - pad[str(num)][1]
            )

            # 왼손이 더 가까울 때
            if left_dis < right_dis:
                answer += "L"
                left = pad[str(num)]

            # 오른손이 더 가까울 때
            elif left_dis > right_dis:
                answer += "R"
                right = pad[str(num)]

            # 왼손과 오른손 거리가 같을 때
            else:
                if hand == "right":
                    answer += "R"
                    right = pad[str(num)]
                else:
                    answer += "L"
                    left = pad[str(num)]

    return answer


if "__main__" == __name__:
    print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
    # expected output: "LRLLLRLLRRL"
    print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
    # expected output: "LRLLRRLLLRR"
