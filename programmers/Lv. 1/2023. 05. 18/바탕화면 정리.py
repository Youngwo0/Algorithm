def solution(wallpaper: list) -> list:
    a, b = [], []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                a.append(i)
                b.append(j)
    return [min(a), min(b), max(a) + 1, max(b) + 1]


if __name__ == "__main__":
    print(solution([".#...", "..#..", "...#."]))
    # expected output: [0,1,3,4]
    print(
        solution(["..........", ".....#....", "......##..", "...##.....", "....#....."])
    )
    # expected output: [1,3,5,8]
    print(
        solution(
            [
                ".##...##.",
                "#..#.#..#",
                "#...#...#",
                ".#.....#.",
                "..#...#..",
                "...#.#...",
                "....#....",
            ]
        )
    )
    # expected output: [0,0,7,9]
