if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))


        idx = 0
        operation_needed = 0

        if n == 1:
            print(0)
        else:
            operation_needed = 0
            for idx in range(0, n-1):
                if a[idx]%2 == a[idx+1]%2:
                    operation_needed+=1

            print(operation_needed)