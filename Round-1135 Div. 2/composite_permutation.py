if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        
        # take input
        n = int(input())

        p = [x for x in range(1, n+1)]

        final_p = [0] * n
        even_idx = 0
        odd_idx = 1

        if n <= 3:
            print(-1)
        else:

            final_p[1] = 2
            final_p[2] = 3
            final_p[3] = 1
            final_p[0] = 4
            for i in range(5, n+1):
                final_p[i-1] = i

            print(*final_p)


