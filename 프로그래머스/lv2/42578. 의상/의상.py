def solution(clothes: list) -> int:
    answer = 1

    hash_map = {}
    for clothe, type in clothes:
        hash_map[type] = hash_map.get(type, 0) + 1

    for type in hash_map:
        answer *= hash_map[type] + 1

    return answer - 1


if __name__ == "__main__":
    print(
        solution(
            [
                ["yellow_hat", "headgear"],
                ["blue_sunglasses", "eyewear"],
                ["green_turban", "headgear"],
            ]
        )
    )
