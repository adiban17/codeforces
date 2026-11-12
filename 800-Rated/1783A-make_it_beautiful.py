if __name__ == "__main__":
    t = int(input())

    for _ in range(t):

        n = int(input())

        a = list(map(int, input().split()))

        all_same_flag = True
        num_1 = a[0]

        for num in a:
            if num==a[0]:
                continue
            else:
                all_same_flag = False
        
        if all_same_flag:
            print("NO")
        else:
            a.sort(reverse=True)
            for i in range(1, n):
                running_sum = 0
                for j in range(0,i):
                    running_sum += a[j]

                if a[i] == running_sum:
                    temp = a[i]
                    a[i] = a[-1]
                    a[-1] = temp

            
            print("YES")
            print(*a)
