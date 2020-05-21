from __future__ import print_function
import torch

# x = torch.empty(5, 3)  #构造一个5x3矩阵，不初始化。
# x = torch.rand(5, 3)  # 构造一个随机初始化的矩阵
x = torch.zeros(5, 3, dtype=torch.long)  # 构造一个矩阵全为 0，而且数据类型是 long.
# x = torch.tensor([5.5, 3])  # 构造一个张量，直接使用数据
# print(x)
x = x.new_ones(5, 3, dtype=torch.double)      # new_* methods take in sizes
# print(x)
x = torch.randn_like(x, dtype=torch.float)    # override dtype!
print(x)                                      # result has the same size
# print(x.size())   # 获取它的维度信息

y = torch.rand(5, 3)
# 加法方式一
# print(x+y)
# 加法方式二
# print(torch.add(x, y))
# 加法方式三：提供一个输出tenor作为参数
# result = torch.empty(5, 3)
# torch.add(x, y, out=result)
# print(result)
# 加法方式四   任何使张量发生变化的操作函数名都有'_'
y.add_(x)
# print(y)
print(x[:, 1])
x = torch.randn(4, 4)
y = x.view(16)
z = x.view(-1, 8)  # the size -1 is inferred from other dimensions
print(x.size(), y.size(), z.size())
x = torch.randn(1)
print(x)
print(x.item())




