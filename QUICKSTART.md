# Quick Start Guide

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行完整分析（三种方式）

#### 方式 1: 使用 Jupyter Notebook（推荐）
```bash
jupyter notebook airbnb_analysis.ipynb
```
在浏览器中打开，运行所有单元格。

#### 方式 2: 使用 Python 脚本
```bash
python run_analysis.py
```

#### 方式 3: 使用独立模块
```python
# 运行 ETL 管道
from etl_pipeline import AirbnbETLPipeline
pipeline = AirbnbETLPipeline('.', CITIES, PERIODS)
df = pipeline.run_pipeline()

# 运行分析
from analysis_queries import AirbnbAnalytics
analytics = AirbnbAnalytics(df)
results = analytics.top_n_cities_by_price(5)

# 生成可视化
from visualizations import AirbnbVisualizations
viz = AirbnbVisualizations(df)
viz.plot_price_distribution_by_city()
plt.show()
```

## 项目结构说明

- **airbnb_analysis.ipynb** - 主分析笔记本（完整端到端分析）
- **etl_pipeline.py** - 数据提取、转换、加载模块
- **analysis_queries.py** - SQL风格的分析查询
- **visualizations.py** - 数据可视化模块
- **run_analysis.py** - 一键运行所有分析的脚本
- **requirements.txt** - Python依赖包

## 输出文件

运行后会生成：
- `processed_airbnb_data.csv` - 处理后的数据
- `city_summary_statistics.csv` - 城市汇总统计
- `*.png` - 可视化图表

## 关键功能

✅ **ETL 管道** - 数据加载、清洗、特征工程  
✅ **SQL 风格分析** - 类似SQL的Pandas查询  
✅ **统计分析** - 假设检验、相关性分析  
✅ **数据可视化** - 综合仪表板  
✅ **业务洞察** - 可执行的商业建议  

## 符合 Amazon BIE 面试标准

本项目展示了 Amazon Business Intelligence Engineer 职位所需的核心技能。

