if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        
        n, q = map(int, input().split())
        a = list(map(int, input().split()))

        pref = [0] * (n+1)
        idx = 1

        for i in range(n):
            pref[idx] = pref[idx-1] + a[i]
            idx += 1

        total = pref[-1]
            

        for __ in range(q):
            l, r, k = map(int, input().split())
            
            k_sum = ((r-l)+1)*k
            sub_sum = pref[r] - pref[l-1]

            new_sum = total - sub_sum + k_sum

            if new_sum % 2 == 1:
                print("YES")
            else:
                print("NO")