if __name__ == "__main__":
     t= int(input())

     for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        total = 0

        for gd in a:
            total = total + gd

        print(-1*total)