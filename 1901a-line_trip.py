if __name__=="__main__":

    t = int(input())

    for _ in range(t):
        n, x = map(int, input().split())
        gas_stations = list(map(int, input().split()))
        gas_stations.append(0)
        gas_stations.sort()
        #print(gas_stations)
        n += 1
        distances = []
        for a in range(0, n):
            if a==n-1:
                distances.append(2*(x-gas_stations[a]))
                break
            else:
                distances.append(gas_stations[a+1]-gas_stations[a])
        
        print(max(distances))