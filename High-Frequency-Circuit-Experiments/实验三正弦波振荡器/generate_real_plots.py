import matplotlib.pyplot as plt
import numpy as np
import os

# 配置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei'] # Windows 默认黑体
plt.rcParams['axes.unicode_minus'] = False 

save_dir = r"F:\A学习资料\高频电路\实验课\实验三正弦波振荡器"

# --- 真实数据：西勒振荡器 ---
V1 = np.array([4, 5, 6, 7, 8, 9, 10, 10.93])
f1 = np.array([6.325, 7.035, 7.710, 8.338, 8.826, 9.153, 9.383, 9.548])
Vout1 = np.array([1.319, 1.591, 1.767, 1.930, 1.952, 2.052, 2.110, 2.100])

plt.figure(figsize=(7, 5))
plt.plot(f1, Vout1, marker='o', markersize=8, color='#d62728', linewidth=2.5, linestyle='-', label="实验实测数据")
plt.title('图2-1 西勒振荡电路：幅频特性曲线', fontsize=14)
plt.xlabel('振荡频率 f (MHz)', fontsize=12)
plt.ylabel('输出幅度 Vp-p (V)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='lower right', fontsize=11)
plt.tight_layout()
plt.savefig(os.path.join(save_dir, "西勒幅频特性.png"), dpi=300)
plt.close()


# --- 真实数据：克拉泼振荡器 ---
V2 = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
f2 = np.array([7.863, 8.063, 8.286, 8.512, 8.730, 8.999, 9.311, 9.692, 10.100, 10.640, 11.270])
Vout2 = np.array([2.120, 2.070, 2.032, 2.002, 1.984, 1.956, 1.876, 1.827, 1.775, 1.723, 1.601])

plt.figure(figsize=(7, 5))
plt.plot(f2, Vout2, marker='^', markersize=8, color='#1f77b4', linewidth=2.5, linestyle='-', label="实验实测数据")
plt.title('图2-2 克拉泼振荡电路：幅频特性曲线', fontsize=14)
plt.xlabel('振荡频率 f (MHz)', fontsize=12)
plt.ylabel('输出幅度 Vp-p (V)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper right', fontsize=11)
plt.tight_layout()
plt.savefig(os.path.join(save_dir, "克拉泼幅频特性.png"), dpi=300)
plt.close()

print("Real data images generated successfully!")