def pyramid_sort(arr):

    # sorting the array
    sorted_arr = sorted(arr)

    # pyramid sort
    n = len(sorted_arr)
    arranged_arr = [0] * n

    left = 0
    right = n-1

    for i, val in enumerate(sorted_arr):
        if i%2 == 0:
            arranged_arr[left] = val
            left += 1
        else:
            arranged_arr[right] = val
            right -= 1
    
    return arranged_arr




if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        
        n = int(input())
        h = list(map(int, input().split()))

        arranged_h = pyramid_sort(h)
        compute_max = False

        k = 0
        largest_shelf = max(arranged_h)

        for i in range(n):
            if i == 0 and arranged_h[i] != largest_shelf:
                k += 1
            else:
                if arranged_h[i] != largest_shelf:
                    if arranged_h[i] == arranged_h[i-1]:
                        continue
                    else:
                        k += 1
                else:
                    # if we are on the largest shelves
                    if compute_max == False:
                        # count the number of times max is present in the shelf
                        max_count = arranged_h.count(largest_shelf)
                        if max_count == 1:
                            k += 1
                        else:
                            k += 2
                        compute_max = True
                    else:
                        continue
            #print(f"i={i}")
            #print(f"k={k}")

        print(k)
        print(*arranged_h)
        









            

        
