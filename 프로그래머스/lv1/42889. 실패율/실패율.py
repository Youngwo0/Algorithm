def solution(N, stage):
    answer = []
    length = len(stage)
    # from 1 to N, look for the stage
    for i in range(1, N + 1):
        # count for do not clear the stage
        count = stage.count(i)
        # calculate the fail rate
        if length == 0:
            fail = 0
        else:
            fail = count / length
        # count for the player reaches the next stage
        length -= count
        # append the answer list to the (stage number, fail rate) tuple
        answer.append((i, fail))
    answer = sorted(answer, key=lambda x: x[1], reverse=True)
    # sort by the fail rate by lambda expression
    answer = [i[0] for i in answer]
    return answer


if __name__ == "__main__":
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
    # expected output: [3,4,2,1,5]
    print(solution(4, [4, 4, 4, 4, 4]))
    # expected output: [4,1,2,3]