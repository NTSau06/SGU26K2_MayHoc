import torch

a = torch.zeros(2, 3, 4)

print("Tensor: ")
print(a)
print("shape: ", a.shape)
print("size:", a.size())
print("Number of dimensions: ", a.ndim)
print("Data type: ", a.dtype)