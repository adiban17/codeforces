if __name__=="__main__":
    t = int(input())

    for _ in range(t):

        # inputs
        n = int(input())
        numbers = list(map(int, input().split()))

        # logic
        sortable = False
        if numbers[0] != 1:
            sortable = False
        else:
            for x in range(n-1):
                #print(f"Numbers:{numbers}")
                if numbers == sorted(numbers):
                    sortable = True
                    break
                for idx in range(1, n-1):
                    if numbers[idx] > numbers[idx-1] and numbers[idx] > numbers[idx+1]:
                        temp = numbers[idx]
                        #print(f'temp={temp}')
                        numbers[idx] = numbers[idx+1]
                        #print(f"numbers[idx]={numbers[idx]}")
                        numbers[idx+1] = temp
                        #print(f'numbers[idx+1]={numbers[idx+1]}')
                 
        if sortable:
            print('YES')
        else:
            print('NO')
