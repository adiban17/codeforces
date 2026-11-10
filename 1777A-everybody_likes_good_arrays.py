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
            while idx < n-1:
                #print(f"idx+1={idx+1}")
                if (a[idx]%2==0 and a[idx+1]%2==0) or (a[idx]%2==1 and a[idx+1]%2==1):
                    print(f"a[idx]={a[idx]}\na[idx+1]={a[idx+1]}")
                    a[idx] = a[idx]*a[idx+1]
                    print(f"a[idx]={a[idx]}")
                    a.pop(idx+1)
                    print(f"a={a}")
                    idx = 0
                    n = n-1
                    print(f"idx={idx}\nn={n}")
                    operation_needed += 1
                else:
                    idx += 1

            print(operation_needed)