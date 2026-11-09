if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        a, b, c, d = map(int, input().split())

        if d < b:
            print(-1)
        elif c > (d-b)+a:
            print(-1)
        else:
            total_y = d-b
            new_x = (d-b) + a
            total_x = new_x - c
            total = total_x + total_y
            #print("YES")
            print(total)