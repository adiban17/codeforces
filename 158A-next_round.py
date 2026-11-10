if __name__ == "__main__":
    
    # take input
    n, k = map(int, input().split())
    marks = list(map(int, input().split()))
    marks.sort(reverse=True)

    qualification_marks = marks[k-1]
    flag = 0

    if qualification_marks > 0:
        qualified = k
        for idx in range(k, len(marks)):
            if marks[idx] == qualification_marks:
                qualified += 1
            
        flag = 1
        print(qualified)
        
    else:
        qualified = 0
        for idx in range(0, k):
            if marks[idx] > 0:
                qualified += 1
            else:
                flag = 1
                print(qualified)
                break

    if flag == 0:
        print(0)
    