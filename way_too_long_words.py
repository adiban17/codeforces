#import sys


def solve():
    # take input
    word = input()

    # check length
    word_length = len(word)

    # logic
    if word_length > 10:
        print(word[0]+str(word_length-2)+word[-1])
    else:
        print(word)


if __name__ == "__main__":
    #input = sys.stdin.read().splitlines

    #if input:
    #    input_iter = iter(input)
    #    def next_line():
    #        return next(input_iter)


    t = int(input())

    for _ in range(t):
        solve()



