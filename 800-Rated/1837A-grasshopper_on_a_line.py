if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())

        if (n%k) != 0:
            print(1)
            print(n)
        else:
            print(2)
            nums = [n-1, 1]
            print(*nums)
                
                