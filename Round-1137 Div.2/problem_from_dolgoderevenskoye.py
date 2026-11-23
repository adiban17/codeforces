if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        
        x = int(input())

        if x%2 == 1:
            print("YES")
        else:
            if x==1:
                print("YES")
            elif x==2:
                print("NO")
            else:
                ctr = 0
                d = x//2
                if d%2 == 1:
                    print("NO")
                else:
                    print("YES")
                