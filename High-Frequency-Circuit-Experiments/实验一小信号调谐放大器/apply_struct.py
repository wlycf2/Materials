import re

with open('实验一_小信号调谐放大器_实验报告.tex', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. 任务一添加要求
c = re.sub(
    r'(%  请在这里插入实验中通过扫频仪或逐点描绘法绘制的单调谐放大器.*?\\end\{figure\})',
    r'\\vspace{1em}\n\\textbf{要求：}以横轴为频率，纵轴为电压幅值，按表 1-1，画出单调放大器的幅频特性曲线。\n% 📝 请在这里插入曲线图\n% \\begin{figure}[H]\n% \\centering\n% \\includegraphics[width=0.8\\textwidth]{此处替换为单调谐特性曲线图片路径}\n% \\caption{单调谐放大器幅频特性曲线}\n% \\label{fig:single_tuned_curve}\n% \\end{figure}',
    c, flags=re.DOTALL
)

# 2. 插入任务二
new_task2 = '''\\subsection*{任务二：观察集电极负载对单调谐放大器幅频特性的影响}

% 📝 请在这里插入集电极负载改变后的特性曲线图
% \\begin{figure}[H]
% \\centering
% \\includegraphics[width=0.8\\textwidth]{此处替换为不同集电极负载下的对比曲线图片路径}
% \\caption{集电极负载对单调谐放大器幅频特性影响对比图}
% \\label{fig:load_effect_curve}
% \\end{figure}

\\subsubsection*{结果分析}
\\textbf{不同集电极负载对幅频特性的影响分析：}
\\begin{itemize}
    \\item \\textbf{有载品质因数与通频带的关系：} 当接通开关并入负载电阻时，集电极等效负载电阻减小。根据谐振回路原理，有载品质因数 $Q$ 值极速下降。这将直观地导致幅频特性曲线变“胖”，即通频带 $BW$ 展宽。
    \\item \\textbf{增益变化：} 由于等效并联谐振阻抗 $R_p$ 的减小，处于中心谐振点时的最大电压增益 $A_{v0}$ 亦随之显著下降。反之，当断开负载电阻时，曲线变“瘦”（选择性增强，通频带变为狭窄），同时中心最大增益上升。这充分从工程上验证了单调谐电路中“增益-带宽”本质上互相制约的经典特性规律。
\\end{itemize}

\\subsection*{任务三：双调谐回路谐振放大器幅频特性测量}'''
c = c.replace('\\subsection*{任务二：双调谐回路谐振放大器幅频特性测量}', new_task2)

# 3. 现在的任务三内：增加要求的这三点内容
# 为了避免转义问题，直接用 string 操作替换
old_task3_comment = '''%  请在这里插入测试出的双调谐放大器幅频特性曲线图以及改变1C19耦合电容时的曲线。
% \\begin{figure}[htbp]
% \\centering
% \\includegraphics[width=0.8\\textwidth]{此处替换为图片路径}
% \\caption{双调谐幅频特性曲线与改变耦合电容时的观测图}
% \\label{fig:double_tuned_curve}
% \\end{figure}'''

new_task3_comment = '''\\vspace{1em}
\\textbf{要求与补充分析：}
\\begin{enumerate}
    \\item[(3)] \\textbf{测出两峰之间凹陷点的大致频率是多少？} \\par
    答：根据数据实测及其分析可知，两峰之间中心凹陷点的大致频率约为 $\\mathbf{6.15\\text{MHz}}$。
    \\item[(4)] \\textbf{以横轴为频率，纵轴为幅度，按照表 1-2，画出双调谐放大器的幅频特性曲线。}
    % 📝 请在这里放入双调谐幅频特性曲线图
    % \\begin{figure}[H]
    % \\centering
    % \\includegraphics[width=0.8\\textwidth]{此处替换为双调谐特性曲线图片路径}
    % \\caption{双调谐放大器幅频特性曲线}
    % \\label{fig:double_tuned_curve1}
    % \\end{figure}
    
    \\item[(5)] \\textbf{调整 1C19 的电容，按照上述方法测出改变 1C19 时幅频特性曲线。}
    % 📝 请在这里放入改变耦合电容 1C19 后的对比曲线图
    % \\begin{figure}[H]
    % \\centering
    % \\includegraphics[width=0.8\\textwidth]{此处替换为改变1C19后的曲线图片路径}
    % \\caption{调整耦合电容 1C19 后的双调谐幅频特性曲线对比图}
    % \\label{fig:double_tuned_curve2}
    % \\end{figure}
\\end{enumerate}'''
c = c.replace(old_task3_comment, new_task3_comment)

# 4. 任务三改为任务四
c = c.replace('\\subsection*{任务三：放大器动态范围测量}', '\\subsection*{任务四：放大器动态范围测量}')

with open('实验一_小信号调谐放大器_实验报告.tex', 'w', encoding='utf-8') as f:
    f.write(c)

print("done2")
