if __name__ == "__main__":

    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        a.sort()
        #print(f"sorted a: {a}")

        b = []
        c = []

        max = a[-1]
        #print(f"max={max}")
        unique_max = 0

        for num in a:
            if num == max:
                unique_max += 1
        #print(f"unique max = {unique_max}")

        if unique_max == n:
            print(-1)
        else:
            b = a[:(n-unique_max)]
            c = a[(n-unique_max):]
            lens = [len(b), len(c)]
            print(*lens)
            print(*b)
            print(*c)