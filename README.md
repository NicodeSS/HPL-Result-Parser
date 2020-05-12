# HPL Result Parser

本程序用于将 **HPL**(High Performance Linpack) 的输出结果格式化为 CSV 文件，并输出 HPL 测试中的最佳结果（GFlops 结果最高者）

## 准备

在开始使用前，请确保你的的电脑上已经安装 **python3** ，且安装了以下包：

1. numpy
2. pandas

## 使用

```shell
python3 parser.py <hpl_result_file>
```

HPL 结果会存放到 result.csv 中