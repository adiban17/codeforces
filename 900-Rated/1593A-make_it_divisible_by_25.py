def calc_operations(n, possible_value):
    operations = 0
    l = len(n)

    checker_index = len(possible_value) - 1

    for i in reversed(range(l)):
        if n[i] == possible_value[checker_index]:
            checker_index -= 1
        else:
            operations += 1

        if checker_index < 0:
            break

    if checker_index > 0:
        return float('inf')
    else:
        return operations



if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = input().strip()

        possible_values = ["00", "25", "50", "75"]
        ans = float('inf')

        for possible_value in possible_values:
            ans = min(ans, calc_operations(n, possible_value))

        print(ans)
