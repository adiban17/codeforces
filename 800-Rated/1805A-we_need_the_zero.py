if __name__ == "__main__":

    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        
        total_xor = 0

        for num in a:
            total_xor = total_xor ^ num

        if n%2 == 1:
            print(total_xor)
        else:
            if total_xor == 0:
                print(0)
            else:
                print(-1)




