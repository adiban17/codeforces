from collections import Counter
import sys

input = sys.stdin.readline


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        
        n = int(input())
        a = list(map(int, input().split()))

        # finding the highest freq element
        mf = 1
        curr = 1

        a.sort()

        for i in range(1, n):
            if a[i] == a[i-1]:
                curr += 1
                if curr > mf:
                    mf = curr
            else:
                curr = 1

        ops = 0

        while mf < n:
            # copy 
            ops += 1
            mf = mf*2

            # swap
            if mf < n:
                ops += mf//2
            else:
                ops += (n-(mf//2))
            

        print(ops)
                
