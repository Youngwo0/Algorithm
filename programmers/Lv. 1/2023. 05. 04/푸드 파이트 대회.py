"""x = "abcdefghijklmnopqrst"
y = "".join(reversed(x))  # 문자열 뒤집기
"""


def solution(food):
    a = ""
    for i, j in enumerate(food):
        a += str(i) * (int(j) // 2)
    return a + "0" + "".join(reversed(a))


if __name__ == "__main__":
    print(solution([1, 3, 4, 6]))
