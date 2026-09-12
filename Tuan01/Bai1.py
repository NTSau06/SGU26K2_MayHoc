import torch

a = torch.tensor (
    [[1, 2, 3],
     [4, 5, 6]],

    dtype = torch.int32
)

print(a)
print("Shape: " , a.shape)          # Kích thước
print("Dimensions: ", a.dim())      # Số Chiều
print("Data type: ", a.dtype)       # Kiểu dữ liệu