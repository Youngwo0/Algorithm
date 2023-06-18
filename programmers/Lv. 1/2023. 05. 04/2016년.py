import datetime


def solution(a, b):
    t = "MON TUE WED THU FRI SAT SUN".split()
    return t[datetime.datetime(2016, a, b).weekday()]


if __name__ == "__main__":
    print(solution(5, 24))
