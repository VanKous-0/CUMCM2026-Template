# 全国大学生数学建模竞赛 LaTeX 社区模板（2026）

> 本项目是依据全国大学生数学建模竞赛官方 2026 年规范制作的**社区模板**，不是全国组委会发布的官方 LaTeX 模板。竞赛规则如有更新，以全国组委会官网和所在赛区通知为准。

原模板由 Jiayi（[@langonginc](https://github.com/langonginc)）制作；本仓库 fork 自 [`langonginc/CUMCM2026-Template`](https://github.com/langonginc/CUMCM2026-Template)。保留原作者署名与来源。原作者说明：模板制作过程使用 OpenAI GPT 5.6 辅助，使用本品所产生的一切影响由使用者自行承担。

## 项目定位

模板面向电子版论文，提供一套稳定、克制、适合打印的 XeLaTeX 排版骨架：

- A4 纸张，四边页边距 2.5 cm；
- 摘要为电子版第 1 页，从该页起在页脚中央连续编号；
- 正文不生成目录，附录包含支撑材料清单与完整程序；
- 2026 年 AI 工具使用声明位于参考文献之前；
- 三人协作友好的模块化章节；
- 正文一级标题采用“一、二、三”，二级标题采用“1.1、1.2”；
- 面向 C 题的数据预处理、预测评价、机器学习与优化写作骨架；
- 可跨页三线符号表和 Python/Matlab 代码附录；
- 隐藏超链接样式、匿名 PDF 元数据、黑白代码清单。

字体、字号、行距、颜色等未被官方规范统一规定。本模板采用四号/小四标题和 1.25 倍行距作为默认排版选择，**不是官方强制要求**。

## 快速开始

### Overleaf

下载仓库 ZIP → Overleaf 选择 **Upload Project** → Compiler 选择 **XeLaTeX** → Main document 选择 `main.tex`。

### 本地

必须安装含中文支持的 TeX Live 或 MiKTeX，并使用 XeLaTeX：

```bash
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
```

如已安装 `latexmk` 和 `make`：

```bash
make pdf
make check
make clean
```

## 文件结构

```text
.
├── main.tex                         # 清晰的总控文件
├── cumcm2026.sty                    # 版式与常用命令
├── ai_statement.tex                 # 2026 AI 声明，提交前必须核实
├── references.tex                   # 简单参考文献方案
├── example.pdf                      # 已编译的示例预览
├── Makefile
├── sections/
│   ├── 01_problem.tex
│   ├── 02_analysis.tex
│   ├── 03_assumptions_symbols.tex
│   ├── 04_data.tex
│   ├── 05_problem1.tex
│   ├── 06_problem2.tex
│   ├── 07_problem3.tex
│   ├── 08_validation.tex
│   └── 09_evaluation_conclusion.tex
├── figures/                         # 图片资源
├── code/                            # 完整可运行程序
├── data/                            # 自主查询的数据（如有）
└── results/                         # 必要中间结果（如有）
```

## 常用操作

### C 题章节骨架

正文默认按照“问题重述—问题分析—模型假设—符号说明—数据预处理—问题一/二/三—模型评价”组织。问题一文件进一步提供“问题分析、数据处理、模型建立、模型求解、结果分析”五段占位结构；比赛时直接替换注释和占位文字即可。

插图（图题位于图下）：

```latex
\begin{figure}[H]
  \centering
  \includegraphics[width=0.72\textwidth]{figures/example.pdf}
  \caption{示例图题}
  \label{fig:example}
\end{figure}
```

表格（表题位于表上）：

```latex
\begin{table}[H]
  \centering
  \caption{示例表题}
  \begin{tabular}{cc}
    \toprule 指标 & 数值 \\
    \midrule A & 1.00 \\
    \bottomrule
  \end{tabular}
\end{table}
```

可跨页符号表（三线表、自动重复表头）：

```latex
\begin{symboltable}[主要符号说明]
  \label{tab:symbols}
  $x_i$ & 第 $i$ 个样本的观测值 & -- \\
  $t$ & 时间索引 & d \\
\end{symboltable}
```

算法流程图占位框（后续可替换为实际图片）：

```latex
\figureplaceholder{问题一建模流程图}{fig:problem1-flow}
```

连续公式编号与引用：

```latex
\begin{equation}
  S_i=\sum_{j=1}^{m}w_jz_{ij}.
  \label{eq:score}
\end{equation}
由式~\ref{eq:score} 可得综合得分。
```

对齐的问题列表：

```latex
\begin{problemlist}
  \item 完成数据清洗与描述性统计；
  \item 建立评价模型，并说明参数来源；
  \item 检验模型并给出可解释结论。
\end{problemlist}
```

从文件插入完整程序，参数依次为 listings 选项、显示标题、实际路径：

```latex
\sourcefile[language=Python]{问题一完整源程序}{code/problem1.py}
\sourcefile[language=Matlab]{问题一 Matlab 程序}{code/problem1.m}
```

## 2026 AI 工具使用声明

正式提交前必须根据队伍真实 AI 使用情况，在 `ai_statement.tex` 中二选一填写，严禁隐瞒或虚假声明。若使用 AI，还须在支撑材料中提交 `AI工具使用详情.pdf`，如实说明工具名称及版本/型号、用途与环节、主要提示方式及过程、采纳与人工修改和核验情况。

模板中的“未使用 AI”仅为可编译占位，并不代表参赛队的真实情况。

## 2026 提交检查表

- [ ] 电子版第一页是摘要，标题、摘要和关键词原则上不超过一页；
- [ ] 摘要页从 1 编号，页码位于页脚中部；
- [ ] 正文无目录且不超过 30 页，附录置于正文之后；
- [ ] 摘要、正文、附录、文件名和文档属性均不含队员、学校或赛区信息；
- [ ] 论文引用均在正文标注并列入参考文献；
- [ ] 附录包含支撑材料文件列表和全部完整、可运行源程序；
- [ ] 自主查询数据和必要中间结果进入支撑材料；赛题提供的原始数据不重复提交；
- [ ] 论文电子版建议使用 PDF，单文件不超过 20MB；支撑材料 ZIP/RAR 不超过 20MB；
- [ ] AI 工具使用声明位于参考文献之前，内容与真实情况一致；
- [ ] 如使用 AI，支撑材料包含 `AI工具使用详情.pdf`；
- [ ] 最终 PDF 已用 XeLaTeX 至少编译两遍，引用、页码和版面均已人工检查。

## Git 与比赛安全提醒

> **不要在正式竞赛期间把当年赛题、真实论文、附件数据、AI 交互记录、未公开代码或支撑材料提交到这个公开模板仓库。**

2026 参赛规则明确禁止竞赛期间在 GitHub 等交流平台浏览、发布或讨论与赛题相关的内容。本仓库仅用于赛前维护通用模板；实际比赛项目应使用私有工作目录、私有仓库或受控的 Overleaf 项目，并遵守全国组委会和所在赛区规定。

## 官方依据

- [全国大学生数学建模竞赛论文格式规范（2026 年修订稿）](https://www.mcm.edu.cn/html_cn/node/4cd596519c9eb9fbd866398f6df0caa3.html)
- [全国大学生数学建模竞赛参赛规则（2026 年修订稿）](https://www.mcm.edu.cn/html_cn/node/9d8e511fe7a1447b35f53a82c908e2e0.html)
- [全国大学生数学建模竞赛人工智能工具使用规定（2026 年试行）](https://www.mcm.edu.cn/html_cn/node/fef94648f2836ab6cc81586f4c38512b.html)
