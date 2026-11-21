if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        
        health = int(input())
        stack = 1
        moves = 0
        charges = 0
        attacks = 0

        if health == 1:
            print(1)
        else:
            for i in range(health):
                
                damage = (stack*(stack+1))//2
                if damage >= health:
                    break

                stack += 1
                charges += 1

            while health > 0:
                health = health - stack
                stack = stack - 1
                attacks += 1

            print(attacks + charges)


            

        
        #print(f"health={health}")
        #print(f"stack={stack}")
        #print("moves needed=",stack+(stack-1))
        
        #print(attacks)
        #print(moves)
