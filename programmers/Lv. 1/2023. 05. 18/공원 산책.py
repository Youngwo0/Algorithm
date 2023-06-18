def solution(park: list, routes: list) -> list:
    x, y = 0, 0
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "S":
                x, y = j, i
                break
    for route in routes:
        xx, yy = x, y
        for step in range(int(route[2])):
            if route[0] == "E" and xx != len(park[0]) - 1 and park[yy][xx + 1] != "X":
                xx += 1
                if step == int(route[2]) - 1:
                    x = xx  # step만큼 움직였으면 위치 초기화
            # 서쪽 : 현재 위치가 map 가장 왼쪽이면 안됨, 이동할 곳이 장애물이면 안됨
            elif route[0] == "W" and xx != 0 and park[yy][xx - 1] != "X":
                xx -= 1
                if step == int(route[2]) - 1:
                    x = xx
            # 남쪽 : 현재 위치가 map 가장 아래쪽이면 안됨, 이동할 곳이 장애물이면 안됨
            elif route[0] == "S" and yy != len(park) - 1 and park[yy + 1][xx] != "X":
                yy += 1
                if step == int(route[2]) - 1:
                    y = yy
            # 북쪽 : 현재 위치가 map 가장 위쪽이면 안됨, 이동할 곳이 장애물이면 안됨
            elif route[0] == "N" and yy != 0 and park[yy - 1][xx] != "X":
                yy -= 1
                if step == int(route[2]) - 1:
                    y = yy

    return [y, x]


if __name__ == "__main__":
    print(solution(["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"]))
    # expected result = [2,1]
    print(solution(["SOO", "OXX", "OOO"], ["E 2", "S 2", "W 1"]))
    # expected result = [0,1]
    print(solution(["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"]))
    # expected result = [0,0]
