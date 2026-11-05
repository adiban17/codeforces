def check(s):
    if s.upper() == "YES":
        return "YES"
    return "NO"


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        sol = check(s)
        print(sol)
