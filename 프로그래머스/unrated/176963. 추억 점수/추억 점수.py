def solution(name, yearning, photo):
    answer = [0] * len(photo)

    for i, j in zip(name, yearning):
        for k, l in enumerate(photo):
            if i in l:
                answer[k] += j
    return answer