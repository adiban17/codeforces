if __name__ == "__main__":

    t = int(input())

    for _ in range(t):

        a, b, c = map(int, input().split())
        x = list(map(int, input().split()))

        total_time = b

        for i in x:
            total_time += min(a-1, i)

        print(total_time)
        