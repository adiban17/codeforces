import math
from functools import reduce

def find_gcd(arr):
    return reduce(math.gcd, arr)


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        if n == 2:
            gcd = find_gcd(a)
            if gcd <= n:
                print('YES')
            else:
                print("NO")
        else:
            gcd = find_gcd(a)
            new_a = []
            gcd_count = 0
            for num in a:
                if num == gcd:
                    gcd_count += 1
            
            for i in range(gcd_count):
                new_a.append(gcd)
            
            no_gcd_a = [item for item in a if item != gcd]
            no_gcd_a.sort()
            for num in no_gcd_a:
                new_a.append(num)

            flag = True
            x = 2
            for i in range(n-1):
                gcd = find_gcd(new_a[:x])
                len_new_a = len(new_a[:x])
                x += 1
                if gcd > len_new_a:
                    flag = False
                else:
                    continue

            if flag == True:
                print("YES")
            else:
                print("NO")
