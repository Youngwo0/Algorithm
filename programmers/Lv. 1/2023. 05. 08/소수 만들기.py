from itertools import combinations


def is_prime_number(n):  # 소수 판별 함수
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True


def solution(nums):
    answer = 0

    cmb = list(combinations(nums, 3))
    sum_cmb = list(map(sum, cmb))

    for a in sum_cmb:
        if is_prime_number(a):
            answer += 1

    return answer


if __name__ == "__main__":
    print(solution([1, 2, 7, 6, 4]))
