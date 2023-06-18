def solution(X, Y):
    answer = ""

    num_x = {str(n): 0 for n in range(10)}
    num_y = {str(n): 0 for n in range(10)}

    for x in X:
        num_x[x] += 1

    for y in Y:
        num_y[y] += 1

    for k in range(9, -1, -1):
        k = str(k)
        iter_num = min(num_x[k], num_y[k])

        if answer == "" and k == "0" and iter_num != 0:
            return "0"

        answer = "".join([answer, k * iter_num])

    if answer == "":
        return "-1"
    else:
        return answer


if __name__ == "__main__":
    print(solution("100", "2345"))
    # expected output: "-1"
    print(solution("100", "203045"))
    # expected output: "0"
