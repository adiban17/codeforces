if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        
        n = int(input())

        max_buses = 0
        min_buses = 0

        found_flag = True

        max_found = False
        min_found = False


        if n%2 == 1 or n < 4:
            # odd and min edge cases
            found_flag = False
            print(-1)
            
        else:
            # finding out the max number of buses
            if n%4 == 0:
                max_buses = n//4
            else:
                max_buses = 1 + ((n-6)//4)
            
            # finding out he min number of buses
            if n%6 == 0:
                min_buses = n//6
            else:
                if (n-4)%6 == 0:
                    min_buses = 1 + ((n-4)//6)
                elif (n-8)%6 == 0:
                    min_buses = 2 + ((n-8)//6)

        
        buses = [min_buses, max_buses]
        if found_flag:
            print(*buses)