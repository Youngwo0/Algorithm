def solution(id_list: list, report: list, k: int) -> list:
    # count reports
    report_dict = {id: 0 for id in id_list}
    for rep in list(set(report)):
        report_dict[rep.split()[1]] += 1

    # reported id
    reported_id = []
    for id in id_list:
        if report_dict[id] >= k:
            reported_id.append(id)

    # count mails
    mail_dict = {id: 0 for id in id_list}
    for rep in list(set(report)):
        if rep.split()[1] in reported_id:
            mail_dict[rep.split()[0]] += 1

    return list(mail_dict.values())


if __name__ == "__main__":
    print(
        solution(
            ["muzi", "frodo", "apeach", "neo"],
            ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
            2,
        )
    )
    # expected result [2,1,1,0]
    print(
        solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)
    )
