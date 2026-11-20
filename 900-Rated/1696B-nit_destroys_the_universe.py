if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        snaps = []
        count = 0
        first_flag = -1
        last_flag = -1
        
        for i in range(0, n):
            if a[i] != 0 and first_flag==-1:
                first_flag = i+1
            if a[(n-1)-i] !=0 and last_flag==-1:
                last_flag = (n-1)-i
            if first_flag != -1 and last_flag != -1:
                break

        if first_flag==-1 and last_flag==-1:
            print(0)
        else:
            if first_flag == last_flag:
                print(1)
            else:
                zero_flag = False
                for i in range(first_flag, last_flag):
                    if a[i] == 0:
                        zero_flag = True
                        break
                
                if zero_flag:
                    print(2)
                else:
                    print(1)

            
        