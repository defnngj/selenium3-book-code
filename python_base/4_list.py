"""
列表(list)基本用法
"""

# 定义列表
lists = [1, 2, 3, 'a', 5]

# 打印列表
print(lists)

# 打印列表中的第1个元素
print(lists[0])

# 打印列表中的第5个元素
print(lists[4])

# 打印列表中的最后一个元素
print(lists[-1])

# 修改列表中的第5个元素为“b”
lists[4] = 'b'
print(lists)

# 向列表末尾添加元素
lists.append('c')
print(lists)
# 删除列表中的第一个元素
lists.pop(0)
print(lists)