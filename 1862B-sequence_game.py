if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))

        if b == sorted(b):
            print(n)
            print(*b)
        else:
            a = []
            a.append(b[0])

            for idx in range(1, n):
                if b[idx-1] <= b[idx]:
                    a.append(b[idx])
                else:
                    a.append(1)
                    a.append(b[idx])

            print(len(a))
            print(*a)
            #print(f"m={len(a)}")
            #print(f"a={a}")
