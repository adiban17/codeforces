if __name__=="__main__":
    t = int(input())

    for _ in range(t):

        n, k = map(int, input().split())
        a = list(map(int, input().split()))

        found = 0

        for idx in range(n):
            if a[idx] == k:
                print('YES')
                found = 1
                break

        if found == 0:
            print('NO')