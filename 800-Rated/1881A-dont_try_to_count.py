if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n, m = map(int, input().split())
        x = input()
        s = input()

        operations_needed = 0
        found = False

        if n <= m:
            while True:
                if s in x:
                    #print(operations_needed)
                    found = True
                    break
                else:
                    while len(x) <= 2*m:
                        x = x+x
                        operations_needed += 1
                        if s in x:
                            found = True
                            break

                        #print(f"x={x}\ns={s}\noperations needed={operations_needed}")
                    break

                    
        else:
            if s in x:
                found = True
            else:
                x = x+x
                if s in x:
                    found = True
                    operations_needed += 1


        if found:
            print(operations_needed)
        else:
            print(-1)
