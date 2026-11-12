if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = map(int, input().split())

        odds = 0
        evens = 0

        for num in arr:
            if num % 2 == 0:
                evens += 1
            else:
                odds += 1

        if odds % 2 == 0:
            print('YES')
        else:
            print('NO')