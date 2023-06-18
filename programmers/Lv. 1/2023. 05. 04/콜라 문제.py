def solution(a, b, n):
    answer = 0

    while n >= a:
        r = n % a
        n = (n // a) * b
        answer += n
        n += r

    return answer


if __name__ == "__main__":
    print(solution(2, 1, 20))
    # expected result = 19
