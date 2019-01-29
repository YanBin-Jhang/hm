from matplotlib import pyplot as plt

x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]

# 設置圖片大小
plt.figure(figsize=(20, 8), dpi=80)

# 繪圖
plt.plot(x, y)

# 設置x軸的刻度
_xtick_labels = [i/2 for i in range(4, 49)]
plt.xticks(_xtick_labels[::3])

# 設置y軸的刻度
plt.yticks(range(min(y), max(y) + 1))

# 保存
# plt.savefig("./t1.png")

# 展示圖形
plt.show()