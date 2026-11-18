if __name__ == "__main__":
    
    t = int(input())

    for _ in range(t):

        n = int(input())
        s = input()

        current = s[0]
        count = 0
        max_count = 0

        for idx in range(n):
            if current == s[idx]:
                count += 1
                #print(count)
            else:
                if count > max_count:
                    max_count = count
                count = 1
                current = s[idx]

        if max_count < count:
            max_count = count
        
        #print(max_count)

        print(max_count+1)
