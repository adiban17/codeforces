def solve():
    
    
    arr = list(map(int, input().split()))
    if sum(arr) > 1:
        return 1

    return(0)


if __name__=="__main__":
    t = int(input())
    ans = 0
    for _ in range(t):
        ans += solve()

    print(ans)

    