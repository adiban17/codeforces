if __name__ == "__main__":
    t = int(input())

    for _ in range(t):

        n, k = map(int, input().split())
        a = list(map(int, input().split()))

        counter = 0
        max_balanced = 0


        a.sort()

        for i in range(0, n-1):
            #print(f"diff={a[i+1]-a[i]}")
            
            if (a[i+1]-a[i]) <= k:
                counter += 1
            else:
                if counter > max_balanced:
                    max_balanced = counter
                
                counter = 0

        if counter > max_balanced:
            max_balanced = counter
            
        #print(f"counter={counter}")
        #print(f"max balanced = {max_balanced}")

        max_balanced += 1

        print(n - max_balanced)