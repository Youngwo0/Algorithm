def solution(number, limit, power):
    div = [1]
    for i in range(2, number + 1):
        cnt = 0
        for j in range(1, int(i ** (0.5) + 1)):
            if i % j == 0:
                cnt += 1
                if j**2 != i:
                    cnt += 1

        if cnt > limit:
            cnt = power
            div.append(cnt)

        else:
            div.append(cnt)
    return sum(div)


if __name__ == "__main__":
    print(solution(5, 3, 2))
    # expected output: 10
    print(solution(10, 3, 2))
    # expected output: 21
