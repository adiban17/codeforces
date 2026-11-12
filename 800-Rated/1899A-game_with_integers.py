if __name__=="__main__":
    t = int(input())

    for _ in range(t):

        # take input
        n = int(input())

        # logic
        if n % 3 == 0:
            print("Second")
        else:
            print("First")