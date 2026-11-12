if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        
        n = int(input())
        h = list(map(int, input().split()))

        arranged_h = []

        h.sort()
        h_idx = 0
        
        
        # arrange h

        # for even sized h
        if n%2 == 0:
            
            for idx in range(n):
                if h_idx > n-1:
                    new_h_idx = h_idx - 2
                arranged_h[idx] = h[h_idx]
                h_idx = h_idx+2






            

        
