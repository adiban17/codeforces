if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        s = input()

        while True:
            if (s[0]=='0' and s[-1]=='1' ) or (s[0]=='1' and s[-1]=='0'):
                len_s = len(s)
                s = s[1:len_s-1]
                #print(f"len_s={len_s}")
                #print(f"s={s}")
                if s == "":
                    break
            else:
                break
        
        print(len(s))
