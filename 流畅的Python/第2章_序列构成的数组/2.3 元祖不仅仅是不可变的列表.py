'''
元祖（tuple）除了是不可变的列表外，还是一个记录数据的重要手段，因为元祖的每个元素都存放一个字段的数据，外加这个字段的位置。
'''

# 把元祖用作记录
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

# 元祖拆包
# * 运算符把一个可迭代对象拆开作为函数的参数
t = (20, 8)
quotient, remainder = divmod(*t)

# * 处理多余的元素
a, b, *rest = range(5)  # (0, 1, [2, 3, 4])
a, b, *rest = range(3)  # (0, 1, [2])
a, b, *rest = range(2)  # (0, 1, [])
a, *body, c, d = range(5)  # (0, [1, 2], 3, 4)

# 具名元祖
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
# 查看具名元祖的类属性
print(City._fields)
# 将已创建的元祖对象，存在放具名元祖中
LatLong = namedtuple('LatLong', 'lat long')  # 具名元祖1
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)  # 具名元祖2
City(*delhi_data)  # 使用拆包的方式将元祖拆包，作用同上面
# 具名元祖 items 化，类似 dict 的 items方法
print(delhi._asdict())
for k, v in delhi._asdict().items():
    print(f"{k} : {v}")

