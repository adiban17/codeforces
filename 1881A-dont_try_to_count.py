if __name__=="__main__":
    t = int(input())

    for _ in range(t):
        n, m = map(int, input().split())
        x = input()
        s = input()

        counter = 0
        found = 0

        if m < n:
            if s in x:
                found = 1
            else:
                x = x+x
                if s in x:
                    counter +=1
                    print(1)
        else:
            while len(x) <= 2*(len(s)):
                if s in x:
                    found = 1
                    print(counter)
                    break
                else:
                    x = x+x
                    counter += 1
                    #print(x)
                    #print(counter)

        if found == 0 and s in x:
            print(counter)
        if found == 0 and s not in x:
            print(-1)