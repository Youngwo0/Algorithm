def solution(food):
    a = ""
    for i, j in enumerate(food):
        a += str(i) * (int(j) // 2)
    return a + "0" + "".join(reversed(a))