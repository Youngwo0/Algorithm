"""
def solution(players: list, callings: list) -> list:
    for call in callings:  # for each call
        idx = players.index(call)  # index=call of players'
        players[idx], players[idx - 1] = players[idx - 1], players[idx]  # swap
    return players
->wrong code(run time error)
why? list의 특성 때문인듯. dict/tuple 자료형으로 변환할 필요
"""


def solution(players: list, callings: list) -> list:
    idx_dict = {i: p for i, p in enumerate(players)}
    player_dict = {p: i for i, p in enumerate(players)}

    for call in callings:
        cur_idx = player_dict[call]
        front_idx = cur_idx - 1

        cur_player = call
        front_player = idx_dict[front_idx]

        player_dict[cur_player], player_dict[front_player] = front_idx, cur_idx
        idx_dict[cur_idx], idx_dict[front_idx] = front_player, cur_player

    return list(idx_dict.values())


if __name__ == "__main__":
    print(
        solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])
    )
