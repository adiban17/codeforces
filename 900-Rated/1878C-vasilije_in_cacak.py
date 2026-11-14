if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n, k, x = map(int, input().split())

        min_sum = (k*(k+1))//2
        max_sum = ((n*(n+1))//2) - (((n-k)*(n-k+1))//2)

        #print(min_sum)
        #print(max_sum)

        if x>=min_sum and x<=max_sum:
            print("YES")
        else:
            print("NO")
