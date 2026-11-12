if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        
        stones = list(map(int, input().split()))

        stones.sort()
        #print(stones)
        #print(stones[0])
        #print(stones[1]-1)
        #print(stones[2]-1)

        if stones[0]==(stones[1]-1) and stones[1]==(stones[2]-1):
            print("YES")
        else:
            print("NO")

        

