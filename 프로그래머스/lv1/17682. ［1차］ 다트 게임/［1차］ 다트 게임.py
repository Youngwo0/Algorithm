def solution(dartResult):
    answer = []
    n = ""

    for chr in dartResult:
        if chr.isdigit():
            n += chr
        elif chr == "S":
            n = int(n)
            answer.append(n)
            n = ""
        elif chr == "D":
            n = int(n) ** 2
            answer.append(n)
            n = ""
        elif chr == "T":
            n = int(n) ** 3
            answer.append(n)
            n = ""
        elif chr == "*":
            if len(answer) > 1:
                answer[-2] *= 2
                answer[-1] *= 2
            else:
                answer[-1] *= 2
        elif chr == "#":
            answer[-1] *= -1
    return sum(answer)


if __name__ == "__main__":
    print(solution("1S2D*3T"))
    # expected output: 37
    print(solution("1D2S#10S"))
    # expected output: 9
