# 内置的树叶结构请见https://minecraft.fandom.com/wiki/Tree/Structure
LEAF_SHAPE = {}

# 普通橡木
LEAF_SHAPE["oak_tree"] = [
    # 第6层
    (0, 1, 0), (1, 1, 0), (-1, 1, 0), (0, 1, 1), (0, 1, -1),
    # 第5层
    (-1, 0, 1), (0, 0, 1), (1, 0, 1), (-1, 0, 0), (1, 0, 0), (-1, 0, -1), (0, 0, -1), (1, 0, -1),
    # 第4层
    (-1, -1, 1), (0, -1, 1), (1, -1, 1), (-1, -1, 0), (1, -1, 0), (-1, -1, -1), (0, -1, -1), (1, -1, -1),
    (-2, -1, 2), (-1, -1, 2), (0, -1, 2), (1, -1, 2), (2, -1, 2), (-2, -1, 1), (2, -1, 1), (-2, -1, 0), (2, -1, 0),
    (-2, -1, -1), (2, -1, -1), (-2, -1, -2), (-1, -1, -2), (0, -1, -2), (1, -1, -2), (2, -1, -2),
    # 第3层
    (-1, -2, 1), (0, -2, 1), (1, -2, 1), (-1, -2, 0), (1, -2, 0), (-1, -2, -1), (0, -2, -1), (1, -2, -1),
    (-2, -2, 2), (-1, -2, 2), (0, -2, 2), (1, -2, 2), (2, -2, 2), (-2, -2, 1), (2, -2, 1), (-2, -2, 0), (2, -2, 0),
    (-2, -2, -1), (2, -2, -1), (-2, -2, -2), (-1, -2, -2), (0, -2, -2), (1, -2, -2), (2, -2, -2)
]
