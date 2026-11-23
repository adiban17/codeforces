if __name__ ==  "__main__":
    t = int(input())

    for _ in range(t):

        a, b = map(int, input().split())
        gcd = abs(a-b)
        movs = 0

        if gcd == 0:
            movs = 0
        else:
            d = a//gcd

            if d == 0:
                movs = min(a, (gcd-a))
            else:
                movs = min(abs((d*gcd)-a), abs(((d+1)*gcd)-a))

        out = [gcd, movs]
        print(*out)

