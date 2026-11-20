if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())

        if abs((a+c)-b) > abs(a-b):
            print(abs(a+c)-b)
        elif abs(a-(b+c)) < abs(a-b):
            print(abs(a-(b+c)))
        else:
            print(abs(a-b)) 