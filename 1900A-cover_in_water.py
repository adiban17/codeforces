if __name__ == "__main__":

    t = int(input())

    for _ in range(t):

        # taking the inputs
        n = int(input())
        seq = input()

        three_continuous_cells = False
        number_of_actions = 0

        for idx in range(n):
            if idx <= n-3 and seq[idx] == '.' and seq[idx+1] == '.' and seq[idx+2] == '.':
                three_continuous_cells = True
                #print("YES")
                break
            else:
                if seq[idx] == '.':
                    number_of_actions += 1


        # print the output
        if three_continuous_cells:
            print(2)
        else:
            print(number_of_actions)
        