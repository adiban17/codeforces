if __name__ == "__main__":
     t = int(input())

     for _ in range(t):

        a, b, c = map(int, input().split())

        total_anna = 0
        total_katie = 0

        if c%2==0:
            total_anna = a + c//2
            total_katie = b + c//2
        else:
            total_anna = a + (c+1)//2
            total_katie = b + (c-1)//2

        if total_anna > total_katie:
            print("First")
        else:
            print("Second")

