def is_palindrome(self, s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # palindrome 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

def is_palindrome_d(self, s: str) -> bool: #Deque
    import collections
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True




if __name__ == "__main__":
    print(is_palindrome(self,'raceacar'))