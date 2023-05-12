def solution(s: str, skip: str, index: int) -> str:
    answer = ""

    alpha = "abcdefghijklmnopqrstuvwxyz"

    for chr in skip:
        if chr in alpha:
            alpha = alpha.replace(chr, "")

    for i in s:
        change = alpha[
            (alpha.index(i) + index) % len(alpha)
        ]  # s의 문자 인덱스 + index를 alpha의 길이로 나눈 나머지를 알파벳으로 변환
        answer += change

    return answer


if __name__ == "__main__":
    print(solution("aukks", "wbqd", 5))
    # expected output: 'happy'
