if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        operations_needed = 0

        positive_ones = 0
        negative_ones = 0

        for i in arr:
            if i == -1:
                negative_ones += 1
            else:
                positive_ones += 1

        while True:
            
            
            if positive_ones >= negative_ones and negative_ones % 2 ==0:
                print(operations_needed)
                break
            else:
                if negative_ones > positive_ones:
                    negative_ones = negative_ones - 1
                    positive_ones = positive_ones + 1
                    operations_needed += 1
                elif negative_ones % 2 == 1:
                    negative_ones = negative_ones - 1
                    positive_ones = positive_ones + 1
                    operations_needed += 1

