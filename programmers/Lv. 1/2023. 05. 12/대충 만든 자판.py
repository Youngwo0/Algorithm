def solution(keymap: list, targets: list) -> list:
    answer = []

    for word in targets:
        times = 0

        for chr in word:
            flag = False
            time = 101

            for key in keymap:
                if chr in key:
                    time = min(key.index(chr) + 1, time)
                    flag = True

            if not flag:
                times = -1
                break

            times += time

        answer.append(times)

    return answer


if __name__ == "__main__":
    print(solution(["ABACD", "BCEFD"], ["ABCD", "AABB"]))
    # expected output: [9,4]
