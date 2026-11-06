if __name__=="__main__":
    
    # take input
    matrix = [list(map(int, input().split())) for _ in range(5)]
    flag = 0

    # finding the non 0 integer
    for x in range(5):

        if flag == 1:
            break
        
        for y in range(5):
            if matrix[x][y] == 1:
                x_abs = abs((x+1)-3)
                y_abs = abs((y+1)-3)
                print(x_abs+y_abs)
                flag = 1
                break



    