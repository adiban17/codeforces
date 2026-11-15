if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        s = input()

        one_counts = s.count('1')
        zero_counts = s.count('0')

        if one_counts >= zero_counts:
            if zero_counts <= k:
                zero_counts = zero_counts - k
                one_counts = one_counts + k
            else:
                one_counts = n
                zero_counts = 0
        else:
            if one_counts <= k:
                one_counts = one_counts - k
                zero_counts = zero_counts + k
            else:
                zero_counts = n
                one_counts = 0

        maxim = max(one_counts, zero_counts)

        final_count = (maxim * (maxim + 1)) // 2

        print(final_count)