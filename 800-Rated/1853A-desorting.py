if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        if arr != sorted(arr):
            print(0)
        else:
            diffs = []
            for i in range(0, n-1):
                diffs.append(arr[i+1]-arr[i])
            
            min_diff = min(diffs)

            print(min_diff//2 + 1)