if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        target = [input().strip() for _ in range(10)]
        
        total_points = 0
        score_matrix = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
            [1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
            [1, 2, 3, 4, 5, 5, 4, 3, 2, 1],
            [1, 2, 3, 4, 5, 5, 4, 3, 2, 1],
            [1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
            [1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

        for i in range(0, 10):
            for j in range(0, 10):
                #print(f"i={i}, j={j}")
                if target[i][j] == 'X':
                    total_points += score_matrix[i][j]

        
        print(total_points)