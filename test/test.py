import torch

x = torch.randn(3, 1, requires_grad=True)
y = x * 2
v = torch.tensor([[1.], [1.], [1.]], dtype=torch.float)
y.backward(v)
print(x.grad)