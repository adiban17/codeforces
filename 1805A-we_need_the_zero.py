if __name__ == "__main__":

    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        bin_a = []
        for num in a:
            bin_a.append(str(format(num, 'b')))

        # normalize
        max_len = len(bin_a[0])
        for bin_num in bin_a:
            if len(bin_num) > max_len:
                max_len = len(bin_num)
        
        for idx in range(len(bin_a)):
            if len(bin_a[idx]) < max_len:
                diff = max_len - len(bin_a[idx])
                for x in range(diff):
                    bin_a[idx] = "0" + bin_a[idx]

        
        # check
        ones_count = []
        for x in range(0, max_len):
            counter = 0
            for y in range(n):
                if bin_a[y][x] == '1':
                    counter += 1
            ones_count.append(counter)

        
        # condition
        final_num = ""
        for num in ones_count:
            if num % 2 == 0:
                final_num = final_num + "0"
            else:
                final_num = final_num + "1"

        total_xor = 0
        a.append(int(final_num, 2))
        for num in a:
            total_xor = total_xor ^ num
        if total_xor == 0:
            print(int(final_num, 2))
        else:
            print(-1)

                




