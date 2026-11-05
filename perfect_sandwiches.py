def solve(a, b):
    # a is the number of cheese slices
    # b is the number of sausages

    if b >= a:
        return -1

    if a >= (2*b):
        return b
    
    return b-1

if __name__ == '__main__':
    # Read the number of test cases
    t = int(input())
    
    for _ in range(t):
        # Read a and b for each testcase
        a, b = map(int, input().split())
        
        # Call your function and print the result
        result = solve(a, b)
        print(result)