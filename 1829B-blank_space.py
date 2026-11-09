if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        counter = 0
        max = 0

        a.append(1)

        for i in a:
            if i == 0:
                counter += 1
            else:
                if counter > max:
                    max = counter
                counter = 0

        print(max)