N = 8

def printSol(b):
    for r in b:
        print(" ".join(str(x) for x in r))
    print()  # For a new line after the board

def isSafe(r, c, b, rL, sL, bL):
    # Check if placing a queen at (r, c) is safe
    if rL[r] or sL[r + c] or bL[r - c + N - 1]:
        return False
    return True

def solveNQUtil(b, c, rL, sL, bL):
    if c >= N:  # All queens are placed
        return True
    for i in range(N):
        if isSafe(i, c, b, rL, sL, bL):
            b[i][c] = 1
            rL[i] = sL[i + c] = bL[i - c + N - 1] = True
            if solveNQUtil(b, c + 1, rL, sL, bL):
                return True
            # Backtracking
            b[i][c] = 0
            rL[i] = sL[i + c] = bL[i - c + N - 1] = False
    return False

def solveNQ():
    b = [[0] * N for _ in range(N)]
    rL = [False] * N
    sL = [False] * (2 * N - 1)
    bL = [False] * (2 * N - 1)
    if not solveNQUtil(b, 0, rL, sL, bL):
        print("Solution does not exist")
        return False
    printSol(b)
    return True

solveNQ()
