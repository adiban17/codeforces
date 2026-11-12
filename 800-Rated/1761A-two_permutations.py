if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n, a, b = map(int, input().split())

        if n == a == b:
            print('Yes')
        else:
            diff = n-(a+b)
            #print(f"diff={diff}")
            if diff>=2:
                print("Yes")
            else:
                print('No')


#if __name__ == "__main__":
#    t = int(input())
#
#    for _ in range(t):
#        n, a, b = map(int, input().split())
#
#        if n == a == b:
#            print('Yes')
#        else:
            #diff = n-(a+b)
            #print(f"diff={diff}")
#            if a+b+2<=n:
#                print("Yes")
#            else:
#                print('No')
