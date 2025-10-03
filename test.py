import torch

# 替换为你的模型路径
checkpoint_path = "/srv/storage/hdd/zqc/wlb/code/SepMetaSyncfolders/MiniImageNet-Res12-Pre/0.1_0.1_[350, 400, 440, 460, 480]/model_best.pth.tar"
checkpoint = torch.load(checkpoint_path)

# 打印所有键名
print("模型文件中的键名：", checkpoint.keys())