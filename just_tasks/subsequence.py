def subsequence(substring, whole):
    position = -1
    for i in substring:
        position = whole.find(i, position + 1)
        if position == - 1:
            return False
    return True


if __name__ == '__main__':
    substring, whole = input(), input()
    print(subsequence(substring, whole))
