if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        
        # take inputs
        a, b = map(int, input().split())
        xk, yk = map(int, input().split())
        xq, yq = map(int, input().split())

        # position from where the king can get killed
        king_kill_pos = [
            [xk+a, yk+b],
            [xk-a, yk-b],
            [xk+a, yk-b],
            [xk-a, yk+b],
            [xk+b, yk+a],
            [xk-b, yk-a],
            [xk+b, yk-a],
            [xk-b, yk+a]
        ]

        queen_kill_pos = [
            [xq+a, yq+b],
            [xq-a, yq-b],
            [xq+a, yq-b],
            [xq-a, yq+b],
            [xq+b, yq+a],
            [xq-b, yq-a],
            [xq+b, yq-a],
            [xq-b, yq+a]
        ]

        killable_positions = []

        for i in range(8):
            for j in range(0, 8):
                #print(f"king killable position = {king_kill_pos[i]}")
                #print(f"queen killable position: {queen_kill_pos[j]}")
                #print(f"i={i} j={j}")
                if king_kill_pos[i] == queen_kill_pos[j]:
                    if king_kill_pos[i] not in killable_positions:
                        killable_positions.append(king_kill_pos[i])
                    #print(f"killable position: {king_kill_pos[i]}")
                #else:print("not killable")

        print(len(killable_positions))

