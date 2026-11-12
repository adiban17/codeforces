if __name__ == "__main__":


    n = int(input())
    a = list(map(int, input().split()))

    abs_a = [abs(x) for x in a]

    print(min(abs_a))
