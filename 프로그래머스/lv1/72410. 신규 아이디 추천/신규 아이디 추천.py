def solution(new_id):
    answer = ""
    # step 1 모든 대문자를 소문자로 변환
    new_id = new_id.lower()
    # step 2 특수기호 제거
    for chr in new_id:
        if chr.isalnum() or chr in "-_.":
            answer += chr
    # step 3 연속되는 .. 제거
    while ".." in answer:
        answer = answer.replace("..", ".")
    # step 4 처음이나 끝의 . 제거
    answer = answer[1:] if answer[0] == "." and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == "." else answer
    # step 5 빈 문자열이라면 'a' 대입
    answer = "a" if answer == "" else answer
    # step 6 길이가 16자 이상이라면 첫 15개 문자열
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]
    # step 7
    if len(answer) <= 3:
        answer = answer + answer[-1] * (3 - len(answer))
    return answer


if "__main__" == __name__:
    print(solution("...!@BaT#*..y.abcdefghijklm"))
    # expected output: "bat.y.abcdefghi"
    print(solution("z-+.^."))
    # expected output: "z--"
