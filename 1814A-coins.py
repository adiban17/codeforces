if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())

        if n%2 == 0:
            print("YES")
        else:
            if n%k == 0:
                print("YES")
            else:
                rem = n-k
                if rem%2 == 0:
                    print("YES")
                else:
                    print("NO")