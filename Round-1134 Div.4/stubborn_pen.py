if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        
        n = int(input())
        s = input()

        switches_needed = 0
        current_color = 'R'

        for idx in range(0, n):
            if s[idx] == current_color:
                if s[idx] == 'R':
                    current_color = 'B'
                else:
                    current_color = 'R'
            else:
                switches_needed += 1
                if current_color == 'R':
                    current_color = 'R'
                else:
                    current_color = 'B'

        print(switches_needed)

