def date_today(date):
    year, month, day = map(int, date.split("."))
    return (year * 12 * 28) + (month * 28) + day


def solution(today: str, terms: list, privacies: list) -> list:
    answer = []

    # today
    today = date_today(today)

    # terms
    terms_info = dict()
    for term in terms:
        term = term.split()
        terms_info[term[0]] = int(term[1]) * 28

    # privacies
    for i in range(len(privacies)):
        date, term = privacies[i].split()
        if date_today(date) + terms_info[term] <= today:
            answer.append(i + 1)

    return answer


if __name__ == "__main__":
    print(
        solution(
            "2022.05.19",
            ["A 6", "B 12", "C 3"],
            ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"],
        )
    )
    # expected output = [1,3]
    print(
        solution(
            "2020.01.01",
            ["Z 3", "D 5"],
            [
                "2019.01.01 D",
                "2019.11.15 Z",
                "2019.08.02 D",
                "2019.07.01 D",
                "2018.12.28 Z",
            ],
        )
    )
    # expected output = [1,4,5]
