def solution(board: list, moves: list) -> int:
    answer = 0
    doll_list = []

    for move in moves:
        for j in range(len(board)):
            if board[j][move - 1] == 0:
                continue
            else:
                doll_list.append(board[j][move - 1])
                board[j][move - 1] = 0

                if len(doll_list) > 1:
                    if doll_list[-1] == doll_list[-2]:
                        doll_list.pop(-1)
                        doll_list.pop(-1)
                        answer += 2
                break
    return answer


if __name__ == "__main__":
    print(
        solution(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 3],
                [0, 2, 5, 0, 1],
                [4, 2, 4, 4, 2],
                [3, 5, 1, 3, 1],
            ],
            [1, 5, 3, 5, 1, 2, 1, 4],
        )
    )

# expected result = 4
