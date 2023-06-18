def solution(name, yearning, photo):
    answer = [0] * len(photo)

    for i, j in zip(name, yearning):
        for k, l in enumerate(photo):
            if i in l:
                answer[k] += j
    return answer


if __name__ == "__main__":
    print(
        solution(
            ["may", "kein", "kain", "radi"],
            [5, 10, 1, 3],
            [
                ["may", "kein", "kain", "radi"],
                ["may", "kein", "brin", "deny"],
                ["kon", "kain", "may", "coni"],
            ],
        )
    )
# expected output: [19,15,6]
