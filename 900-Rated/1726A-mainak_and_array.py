if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))

        max_element = max(a)
        min_element = min(a)

        if a[0] == min_element or a[-1] == max_element:
            print(max_element-min_element)
        else:
            diffs = []
            #  rotate the whole array
            for i in range(0, n-1):
                diffs.append(a[i]-a[i+1])
            # locked in place
            diffs.append(a[-1]-a[0])
            # 1st element doesnt move
            diffs.append(max(a[1:])-a[0])
            # last element doesnt move
            diffs.append(a[-1]-(min(a[:-1])))

            print(max(diffs))
            