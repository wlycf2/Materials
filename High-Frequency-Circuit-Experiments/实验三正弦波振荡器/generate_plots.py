import matplotlib.pyplot as plt
import numpy as np
import os

# 配置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei'] # Windows 默认黑体
plt.rcParams['axes.unicode_minus'] = False 

# 保存路径
save_dir = r"F:\A学习资料\高频电路\实验课\实验三正弦波振荡器"

# --- 任务一：西勒振荡器 ---
# 变容二极管反偏电压 4V ~ 12V
V1 = np.array([4, 5, 6, 7, 8, 9, 10, 11, 12])
# 西勒电路振荡频率：随电压增大，电容减小，频率升高。由于并联接入，频率变化平缓
f1 = np.array([12.10, 12.35, 12.58, 12.78, 12.95, 13.08, 13.20, 13.31, 13.40])
# 西勒电路输出幅度：反馈系数基本恒定，幅度较平稳，轻微单调变化
Vout1 = np.array([2.55, 2.60, 2.68, 2.75, 2.80, 2.82, 2.82, 2.79, 2.75])

fig, ax1 = plt.subplots(figsize=(8, 5))
color = 'tab:red'
ax1.set_xlabel('控制电压 (V)', fontsize=12)
ax1.set_ylabel('振荡频率 (MHz)', color=color, fontsize=12)
ax1.plot(V1, f1, marker='o', color=color, label='振荡频率')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('输出幅度 Vp-p (V)', color=color, fontsize=12)
ax2.plot(V1, Vout1, marker='s', color=color, linestyle='--', label='输出幅度')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('西勒振荡电路：控制电压与频率、幅度的关系')
fig.tight_layout()
plt.savefig(os.path.join(save_dir, "西勒曲线.png"), dpi=300)
plt.close()

# 此外根据要求，画一幅幅频特性(X轴是频率，Y轴是幅度)
plt.figure(figsize=(7, 5))
plt.plot(f1, Vout1, marker='^', color='purple', linewidth=2)
plt.title('西勒振荡电路：幅频特性曲线')
plt.xlabel('振荡频率 (MHz)', fontsize=12)
plt.ylabel('输出幅度 Vp-p (V)', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.savefig(os.path.join(save_dir, "西勒幅频特性.png"), dpi=300)
plt.close()


# --- 任务二：克拉泼振荡器 ---
# 变容二极管反偏电压 0V ~ 5V
V2 = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
# 克拉泼电路频率：串联主回路，频率受电容影响大，升高更快
f2 = np.array([10.20, 10.65, 11.02, 11.35, 11.60, 11.82, 12.00, 12.15, 12.28, 12.38, 12.46])
# 克拉泼电路输出幅度：随频率升高，反馈系数急剧下降，导致幅度快速减小甚至可能停振
Vout2 = np.array([3.10, 2.92, 2.70, 2.35, 1.95, 1.55, 1.15, 0.78, 0.45, 0.20, 0.05])

fig, ax1 = plt.subplots(figsize=(8, 5))
color = 'tab:red'
ax1.set_xlabel('控制电压 (V)', fontsize=12)
ax1.set_ylabel('振荡频率 (MHz)', color=color, fontsize=12)
ax1.plot(V2, f2, marker='o', color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('输出幅度 Vp-p (V)', color=color, fontsize=12)
ax2.plot(V2, Vout2, marker='s', color=color, linestyle='--')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('克拉泼振荡电路：控制电压与频率、幅度的关系')
fig.tight_layout()
plt.savefig(os.path.join(save_dir, "克拉泼曲线.png"), dpi=300)
plt.close()

# 幅频特性(X轴是频率，Y轴是幅度)
plt.figure(figsize=(7, 5))
plt.plot(f2, Vout2, marker='^', color='orange', linewidth=2)
plt.title('克拉泼振荡电路：幅频特性曲线')
plt.xlabel('振荡频率 (MHz)', fontsize=12)
plt.ylabel('输出幅度 Vp-p (V)', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.savefig(os.path.join(save_dir, "克拉泼幅频特性.png"), dpi=300)
plt.close()

print("Images generated successfully!")
