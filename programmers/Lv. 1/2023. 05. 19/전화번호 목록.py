def solution(phone_book: list) -> bool:
    answer = True
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if len(phone_book[i]) < len(phone_book[i + 1]):
            if phone_book[i + 1][: len(phone_book[i])] == phone_book[i]:
                answer = False
                break
    return answer


if __name__ == "__main__":
    print(solution(["119", "97674223", "1195524421"]))
    # expected result = False
    print(solution(["123", "456", "789"]))
    # expected result = True
