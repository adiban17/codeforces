if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        s, t= map(input().split())
        flag = True

        if s == t:
            print("YES")
        else:
            not_needed_chars = []
            for char in s:
                if char in t:
                    s.replace(char, "")
                    
            

            
            