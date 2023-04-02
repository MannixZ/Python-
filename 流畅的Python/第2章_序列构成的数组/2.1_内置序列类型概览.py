'''
容器序列
list、tuple 和 collections.deque 这些序列能存放不同类型的数据。
扁平序列
str、bytes、bytearray、memoryview 和 array.array，这类序列只能容纳一种类型。

可变序列
list、bytearray、array.array、collections.deque 和 memoryview。
不可变序列
tuple、str 和 bytes
'''

# 使用列表推到计算笛卡尔积
colors = ['block', 'white']
sizes = ['S', 'M', 'L']
# 优先把颜色输出完，再输出大小
tshirts_color = [(color, size) for color in colors for size in sizes]
# 优先把大小输出完，再输出颜色
tshirts_size = [(color, size) for color in colors for size in sizes]
# 总结：列表推导式如果想按照哪个变量优先输出，则 for x in x 从句放在前面

# 生成器表达式 =》 遵循迭代器协议
# 生成器表达式 比 列表推导 更加节约内存
# 使用生成器表达式生成以上的 tshirts
for tshirts in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirts)

