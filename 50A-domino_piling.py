import math


if __name__=="__main__":
    m,n = map(int, input().split())
    area = m*n
    print(math.floor(area/2))