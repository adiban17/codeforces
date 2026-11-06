if __name__=="__main__":

    t = int(input())

    for _ in range(t):
        
        n, k = map(int, input().split())
        boxes = list(map(int, input().split()))

        if k == 1:
            if boxes == sorted(boxes):
                print("YES")
            else:
                print("NO")
        else:
            print("YES")
        

    