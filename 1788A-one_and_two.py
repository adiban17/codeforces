if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        two_count = 0

        for num in a:
            if num == 2:
                two_count += 1

        
        if two_count % 2 == 1:
            print(-1)
        elif two_count == 0:
            print(1)
        else:
            mid_two = two_count // 2
            idx_two = 0
            for num in a:
                idx_two += 1
                if num == 2:
                        mid_two = mid_two - 1
                        if mid_two == 0:
                            print(idx_two)
                            break
                        