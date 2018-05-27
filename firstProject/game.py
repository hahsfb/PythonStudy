# 0:黑  1：白  9:空白
# 开始坐标(x1,y1), (x2,y2)

"""
    1  1  1
 1  0  0  0  1
 0  0  0  0  1
 0  0  1  1  1
 0  1  1  0  1
    0  0  1
"""

# 定义一个二维数组
x_len = 6
y_len = 5
game_test = [
    [9, 1, 1, 1, 9],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 1, 1, 1],
    [0, 1, 1, 0, 1],
    [9, 0, 0, 1, 9]
]

start_poit1 = (1, 0)
start_poit2 = (5, 3)

for x in range(x_len):
    for y in range(y_len):
        print(game_test[x][y], end=' ')
    print()

print(game_test[start_poit1[0]][start_poit1[1]])
