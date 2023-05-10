def solution(cards1, cards2, goal):
    answer = "Yes"
    # index for each word in cards1 and cards2
    card1_idx, card2_idx = 0, 0

    for word in goal:
        if len(cards1) > card1_idx and word == cards1[card1_idx]:
            card1_idx += 1
        elif len(cards2) > card2_idx and word == cards2[card2_idx]:
            card2_idx += 1
        else:
            answer = "No"
            break

    return answer


if __name__ == "__main__":
    print(
        solution(
            ["i", "drink", "water"],
            ["want", "to"],
            ["i", "want", "to", "drink", "water"],
        )
    )
    # expected output: 'Yes'
    print(
        solution(
            ["i", "water", "drink"],
            ["want", "to"],
            ["i", "want", "to", "drink", "water"],
        )
    )
    # expected output: 'No'
