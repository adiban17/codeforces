def check_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n  = int(input())
        s = input()

        operations_needed = 0

        if check_palindrome(s):
            print(operations_needed)
        else:
            if n%2 == 0:
                ascii_list = []
                diffs = []
                for char in s:
                    ascii_list.append(ord(char))
                for idx in range(0, n-1):
                    diffs.append(abs(ascii_list[idx]-ascii_list[idx+1]))

                print(ascii_list)
                print(diffs)




