if __name__ == "__main__":
    t = int(input())

    for _ in range(t):

        n, k, x = map(int, input().split())

        flag = False

        # universal false case
        if n == 1 and x == 1:
            flag = False
            #print("NO")
        elif x!=1:
            # if x is not one
            print("YES")
            flag = True
            nums = []
            for i in range(n):
                nums.append(1)
            print(len(nums))
            print(*nums)
        else:

            # if x is one

            # if x is not k and k is n
            if k==n and x!=k:
                flag = True
                print("YES")
                print(1)
                print(k)
            else:
                # if n
                # k is greater than 2
                if k >=2:
                    # if n is even
                    if n%2==0:
                        flag = True
                        print("YES")
                        nums = []
                        for i in range(n//2):
                            nums.append(2)
                        print(len(nums))
                        print(*nums)
                    else:
                        if k>=3:
                            # if n is odd
                            flag = True
                            diff = n-3
                            nums = []
                            nums.append(3)
                            for i in range(diff//2):
                                nums.append(2)
                            print("YES")
                            print(len(nums))
                            print(*nums)
                        else:
                            flag = False
        if flag == False:
            print("NO")
