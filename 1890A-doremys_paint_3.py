if __name__=="__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))

        flag = False

        if n == 2 or n == 1:
            flag = True
        else:
            unique_nums = []
            for num in nums:
                if num not in unique_nums:
                    unique_nums.append(num)
            
            if len(unique_nums) > 2:
                flag = False
            elif len(unique_nums) == 1:
                flag = True
            else:
                count_a = 0
                count_b = 0

                for num in nums:
                    if num == unique_nums[0]:
                        count_a += 1
                    else:
                        count_b += 1
                
                if n%2 == 0:
                    if count_a == count_b:
                        flag = True
                    else:
                        flag = False
                else:
                    if count_a==count_b+1 or count_b==count_a+1:
                        flag = True
                    else:
                        flag = False
        
        if flag:
            print('Yes')
        else:
            print('No')

