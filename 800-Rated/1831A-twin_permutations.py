if __name__ == "__main__":

    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        b = []

        for i in a:
            b.append((n-i)+1)

        print(*b)