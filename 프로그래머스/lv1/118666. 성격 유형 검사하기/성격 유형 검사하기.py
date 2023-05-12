def solution(survey: list, choices: list) -> str:
    answer = ""
    dict = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    for q, a in zip(survey, choices):
        if a > 4:
            dict[q[1]] += a - 4
        elif a < 4:
            dict[q[0]] += 4 - a
        else:
            continue

    if dict["T"] > dict["R"]:
        answer += "T"
    else:
        answer += "R"

    if dict["F"] > dict["C"]:
        answer += "F"
    else:
        answer += "C"

    if dict["M"] > dict["J"]:
        answer += "M"
    else:
        answer += "J"

    if dict["N"] > dict["A"]:
        answer += "N"
    else:
        answer += "A"

    return answer


if __name__ == "__main__":
    print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
    # expected output: "TCMA"
    print(solution(["TR", "RT", "TR"], [7, 1, 3]))
    # expected output: "RCJA"
