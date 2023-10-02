'''
2D list
'''

ROWS = 3
COLS = 4
empty2DList = [[0] * COLS for i in range(ROWS)]
print(empty2DList)

for r in range(ROWS):
    print("\nRow ", r, end=":")
    for c in range(COLS):
        print(empty2DList[r][c], end="")