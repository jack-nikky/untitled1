from __future__ import print_function
import torch

x = torch.ones(3, 3, requires_grad=True)
print(x)
y = x + 2
print(y)
# 每个张量都有一个 .grad_fn 属性保存着创建了张量的 Function 的引用，
# （如果用户自己创建张量，则g rad_fn 是 None ）
print(y.grad_fn)
z = y * y * 3
out = z.mean()
print(z, out)
# a = torch.randn(2, 2)
# a = ((a * 3) / (a - 1))
# # 输入的标记默认为 False
# print(a.requires_grad)
# # .requires_grad_(True)使它为True,
# a.requires_grad_(True)
# print(a.requires_grad)
# b = (a * a).sum()
# print(b.grad_fn)

'''
O = 1/4*(3(xi + 1)^2)
O' = 3/2*(xi + 1)   xi = 1
x.grad = 4.5

'''
out.backward()
print(x.grad)



