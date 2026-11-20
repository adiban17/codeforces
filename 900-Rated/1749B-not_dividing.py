if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        
        n = int(input())
        a = list(map(int, input().split()))


        for i in range(n):
            if a[i] == 1:
                a[i] = 2

        

        for i in range(0, n-1):
            if a[i+1] % a[i] == 0:
                a[i+1] += 1
        
        print(*a)
