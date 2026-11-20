if __name__ == "__main__":

    t = int(input())

    for _ in range(t):
        s = input()

        unique = 0
        lst = []

        for char in s:
            if char not in lst:
                lst.append(char)
                unique += 1

        if unique == 1:
            print(-1)
        elif unique == 2:
            if s.count(s[0])==1 or s.count(s[0])==3:
                print(6)
            else:
                print(4)
        elif unique == 3:
            print(4)
        elif unique == 4:
            print(4)