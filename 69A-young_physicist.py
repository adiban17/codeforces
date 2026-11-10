if __name__=="__main__":
    
    # take input
    n = int(input())

    # initialize running sum values
    x = 0
    y = 0
    z = 0

    # logic
    for i in range(n):

        # take forces input
        forces = list(map(int, input().split()))

        # update running sum
        x += forces[0]
        y += forces[1]
        z += forces[2]

    # final conditional
    if x==0 and y==0 and z==0:
        print("YES")
    else:
        print("NO")    
