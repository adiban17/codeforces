import math
from functools import reduce


# function to find if the array is good or not
def is_good(arr):
    length = len(arr)

    if length >= calc_gcd(arr):
        return True
    else:
        return False

# function to calculate the gcd
def calc_gcd(arr):
    return reduce(math.gcd, arr)


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):

    # take inputs
        n = int(input())
        a = list(map(int, input().split()))

        # case for n = 2
        if n == 2:
            if is_good(a):
                print("Yes")
            else:
                print("No")
        else:
            # case for n > 2

            flag = False

            # check if any pair have gcd <= 2
            for i in range(0, n-1):
                for j in range(i+1, n):
                    if calc_gcd([a[i], a[j]]) <= 2:
                        flag = True
                        break
                    else:
                        continue

            # final condition
            if flag == True:
                print("Yes")
            else:
                print("No")

        