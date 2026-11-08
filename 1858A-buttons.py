if __name__ == "__main__":
     t = int(input())

     for _ in range(t):

        a, b, c = map(int, input().split())

        if c % 2 == 0:
            total_a = a + (c//2)
            total_b = b + (c//2)
        else:
            total_a = a + (c//2)

        
        if a == b:
            if c % 2 == 1:
                print('First')
            else:
                print('Second')
        elif a > b:
            print('First')
        elif b > a:
            print('Second')

            2 1 3
