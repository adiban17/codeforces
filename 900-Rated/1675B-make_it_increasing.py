if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        
        n = int(input())
        a = list(map(int, input().split()))

        counter = 0
        zero_counter = 0

        if n == 1:
            print(0)
        elif a[-1] == 0:
            print(-1)
        else:
            for i in reversed(range(n-1)):
                if a[i] == 0 and i != 0:
                        zero_counter = 2
                else:
                    if a[i] >= a[i+1]:
                        #print(f"a[i]={a[i]}\na[i+1]={a[i+1]}")
                            
                            while True:
                                a[i] = a[i]//2
                                counter += 1
                                if a[i] == 0:
                                    zero_counter += 1
                                    break
                                if a[i] < a[i+1]:
                                    break
                            #print("new a =", *a)
            
            if zero_counter > 1:
                print(-1)
            else:
                print(counter)
                    
            