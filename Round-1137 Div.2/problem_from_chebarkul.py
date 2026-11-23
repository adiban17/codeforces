if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        
        n, k= map(int, input().split())
        a = list(map(int, input().split()))

        
        

        if n == k:
            print(n)
        elif k == 1:
            un = set(a)
            if len(un) == 1:
                print(1)
            else:
                print(0)
        else:
            counter = 0
            for i in range(0, (n-k+1)):
                temp_count = 0
                for j in range(i, i+k):
                    #print(i,j)
                    if a[i] == a[j]:
                        temp_count += 1
                
                if temp_count == k:
                    counter += 1
                    
            print(counter)
