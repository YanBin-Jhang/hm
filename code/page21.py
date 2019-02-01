from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager


# Windows 和 Linux 設置字體的方式
# font = {'family': 'MicroSoft YaHei',
#         'weight': 'bold',
#         'size': 'larger'}
#
# matplotlib.rc("font", **font)
# matplotlib.rc("font", family='MicroSoft YaHei', weight='bold')

# 另外一種設置字體的方式 (一定可行)
my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

plt.figure(figsize=(20, 8), dpi=80)

plt.plot(x, y)

# 調整x軸的刻度
_xtick_labels = ["10點{}分".format(i) for i in range(60)]
_xtick_labels += ["11點{}分".format(i) for i in range(60)]
# 取步長，數字和字符串一一對應，數據的長度一樣
plt.xticks(list(x)[::3], _xtick_labels[::3], rotation=45, fontproperties=my_font)  # rotation旋轉的度數

plt.show()