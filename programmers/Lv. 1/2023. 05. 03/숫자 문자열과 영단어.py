def solution(s):
    arr = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    for i, j in enumerate(arr):
        s = s.replace(j, str(i))

    return int(s)


if __name__ == "__main__":
    print(solution("one4seveneight"))
