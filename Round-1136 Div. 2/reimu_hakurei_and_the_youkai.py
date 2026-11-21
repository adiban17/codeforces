if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        
        n, x = map(int, input().split())
        a = list(map(int, input().split()))

        # sort
        a.sort()

        spells = 0

        for i in range(n):
            low = a[0]
            flag = False

            if not flag:
                if a[i] == low:
                    a[i] -= 1
                    if  a[i] == 0:
                        pass

