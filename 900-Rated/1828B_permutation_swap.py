import math

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        
        n = int(input())
        p = list(map(int, input().split()))

        diffs = []

        sorted_p = sorted(p)

        for idx in range(0, n):
            diff = abs(p[idx] - sorted_p[idx])
            diffs.append(diff)

        result = math.gcd(*diffs)
            

        print(result)
