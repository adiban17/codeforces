if __name__ == "__main__":
    t = int(input())

    for _ in range(t):

        n, k, x = map(int, input().split())

        if n == 1 and x == 1:
            print('NO')
        elif n == 2:
            if k == 2:
                if x == 2:
                    print('YES')
                    print(2)
                    nums = [1, 1]
                    print(*nums)
                elif x == 1:
                    print('YES')
                    print(1)
                    print(2)
            elif k == 1:
                if x == 1:
                    print('NO')
        else:
            if n % 2 == 0:
                print('YES')
                if x==1:
                    print(n//2)
                    nums = []
                    for i in range(n//2):
                        nums.append(2)
                    print(*nums)
                else:
                    print(n)
                    nums = []
                    for i in range(n):
                        nums.append(1)
                    print(*nums)
            else:
                if x!=1:
                    print('YES')
                    print(n)
                    nums = []
                    for i in range(n):
                        nums.append(1)
                    print(*nums)
                else:
                    factors = 0
                    gd = 0
                    for i in range(2, k+1):
                        if n % i == 0:
                            gd = i
                            factors += 1
                    #print(f"Factors={factors}\nGD={gd}")
                    if factors != 0:
                        print('YES')
                        print(int(n//gd))
                        nums = []
                        for i in range(n//gd):
                            nums.append(gd)
                        print(*nums)
                    else:
                        print('NO')


