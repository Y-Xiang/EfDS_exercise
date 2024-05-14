def printSquare(size):
    for r in range(size):
        for c in range(size):
            if r == 0 or r == size - 1 or c == 0 or c == size - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

printSquare(5)

def printX(n):
    for r in range(n):
        for c in range(n):
            if r == c or r == n - 1 - c:
                print('*', end='')
            else:
                print(' ', end='')
        print()

printX(7)
