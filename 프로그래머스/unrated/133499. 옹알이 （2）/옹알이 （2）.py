import itertools


def solution(babbling: list) -> int:
    count = 0
    bab_list = ["aya", "ye", "woo", "ma"]

    for bab in babbling:
        for text in bab_list:
            if text * 2 not in bab:
                bab = bab.replace(text, " ")
        if bab.strip() == "":
            count += 1
    return count


if "__main__" == __name__:
    print(solution(["aya", "yee", "u", "maa"]))
    # expected output: 1
    print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
    # expected output: 2
