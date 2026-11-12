if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))
        b = []

        # initializing b
        for i in range(n):
            b.append(0)

        pairs = []

        # finding pairs of x and y
        for x in range(0, n-1):
            for y in range(x+1,n):
                if p[x] <= p[y]:
                    pairs.append([p[x], p[y]])

        #print(pairs)

        
