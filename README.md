# 🏠 Airbnb Supply Analysis - Business Intelligence & Data Science Project

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.3+-green.svg)](https://pandas.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **End-to-end Business Intelligence project demonstrating advanced analytics, ETL pipelines, and data-driven insights for Airbnb supply patterns across European markets.**

## 🎯 Project Overview

This comprehensive Business Intelligence project analyzes Airbnb listing supply patterns across **10 major European cities** using advanced data analytics techniques. The project showcases **production-ready skills** in data engineering, statistical analysis, and business intelligence that align with **Amazon Business Intelligence Engineer (BIE)** and **Data Scientist (DS)** roles.

### Key Highlights

- ✅ **End-to-End ETL Pipeline** - Production-ready data processing
- ✅ **SQL-like Analytical Queries** - Complex data aggregation and analysis
- ✅ **Statistical Analysis** - Hypothesis testing and correlation analysis
- ✅ **Advanced Visualization** - Interactive dashboards and insights
- ✅ **Business Intelligence** - Actionable recommendations and KPIs
- ✅ **Feature Engineering** - Derived features and market segmentation

## 🚀 Core Competencies Demonstrated

### Business Intelligence Engineer (BIE) Skills

| Skill Area | Implementation | Evidence |
|-----------|----------------|----------|
| **ETL/Data Pipeline** | Complete ETL pipeline with extraction, transformation, and loading | `etl_pipeline.py` |
| **SQL Proficiency** | 7+ SQL-like queries implemented in Pandas | `analysis_queries.py` |
| **Data Quality** | Missing value handling, data validation, quality reports | ETL pipeline |
| **BI Tools** | Comprehensive dashboards and visualizations | `visualizations.py` |
| **Business Acumen** | Actionable insights and strategic recommendations | Analysis notebook |
| **KPI Development** | City-level metrics and performance indicators | Summary statistics |

### Data Scientist (DS) Skills

| Skill Area | Implementation | Evidence |
|-----------|----------------|----------|
| **Statistical Analysis** | T-tests, correlation analysis, hypothesis testing | Statistical analysis section |
| **Feature Engineering** | Price segmentation, location scoring, derived features | Feature engineering module |
| **Data Visualization** | Correlation heatmaps, distribution plots, dashboards | Visualization module |
| **Exploratory Data Analysis** | Comprehensive EDA with insights | Jupyter notebook |
| **Predictive Analytics** | Value scoring, market segmentation | Advanced analysis |
| **Python Programming** | Object-oriented design, modular code structure | All modules |

## 📊 Dataset

### Cities Analyzed
- 🇳🇱 Amsterdam | 🇬🇷 Athens | 🇪🇸 Barcelona | 🇩🇪 Berlin | 🇭🇺 Budapest
- 🇵🇹 Lisbon | 🇬🇧 London | 🇫🇷 Paris | 🇮🇹 Rome | 🇦🇹 Vienna

### Data Attributes
- **Pricing**: `realSum` (total price), `price_per_person`
- **Accommodation**: `room_type`, `bedrooms`, `person_capacity`
- **Host Quality**: `host_is_superhost`, `cleanliness_rating`
- **Guest Satisfaction**: `guest_satisfaction_overall`
- **Location**: `dist`, `metro_dist`, `attr_index`, `rest_index`, coordinates

### Data Scope
- **20 CSV files** (10 cities × 2 time periods)
- **Supply-side analysis** (listings data)
- **Note**: Time-series and demand data not included

## 🏗️ Project Structure

```
Airbnb--Analysis/
├── 📓 airbnb_analysis.ipynb      # Main analysis notebook (full EDA)
├── 🔧 etl_pipeline.py             # ETL pipeline module
├── 📊 analysis_queries.py         # SQL-like analytical queries
├── 📈 visualizations.py           # Data visualization module
├── 🚀 run_analysis.py            # One-command execution script
├── 📋 requirements.txt            # Python dependencies
├── 📖 README.md                   # Project documentation
├── ⚡ QUICKSTART.md               # Quick start guide
├── 🗂️ data/                       # Raw data files (20 CSV files)
└── 📁 docs/                       # Documentation and outputs
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager

### Quick Start

```bash
# 1. Clone repository
git clone https://github.com/Dennis-Sosa/Airbnb--Analysis.git
cd Airbnb--Analysis

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run analysis (choose one method)
# Option A: Jupyter Notebook (Recommended)
jupyter notebook airbnb_analysis.ipynb

# Option B: Python script
python run_analysis.py
```

## 📈 Analysis Components

### 1. ETL Pipeline (`etl_pipeline.py`)

**Business Intelligence Engineer Skills:**
- Multi-file data extraction
- Data quality assessment
- Missing value imputation
- Feature engineering
- Data validation

```python
from etl_pipeline import AirbnbETLPipeline

pipeline = AirbnbETLPipeline('.', CITIES, PERIODS)
processed_data = pipeline.run_pipeline()
```

**Key Features:**
- Handles 20 CSV files automatically
- Data quality reports
- Derived features: `price_per_person`, `location_score`, `price_segment`
- Boolean normalization
- Missing value handling

### 2. SQL-like Analysis (`analysis_queries.py`)

**Business Intelligence Engineer Skills:**
- Complex aggregations
- Multi-table joins (conceptual)
- Window functions
- Group-by operations

**7 Key Analytical Queries:**
1. Top N cities by average price
2. Room type distribution by city
3. Superhost performance analysis
4. Weekend vs weekday pricing
5. Top cities by listing count
6. Value proposition analysis
7. Market segmentation analysis

```python
from analysis_queries import AirbnbAnalytics

analytics = AirbnbAnalytics(df)
top_cities = analytics.top_n_cities_by_price(5)
pricing_analysis = analytics.weekend_vs_weekday_pricing()
```

### 3. Statistical Analysis

**Data Scientist Skills:**
- **Hypothesis Testing**: T-tests for price differences
- **Correlation Analysis**: Pearson correlation coefficients
- **Descriptive Statistics**: Central tendencies and distributions

**Key Tests:**
- Weekend vs Weekday price significance test
- Superhost vs Regular host price comparison
- Price vs Satisfaction correlation

### 4. Data Visualization (`visualizations.py`)

**Business Intelligence & Data Science Skills:**
- Comprehensive dashboards
- Correlation heatmaps
- Distribution analysis
- Comparative visualizations

**Visualization Types:**
- Price distributions by city
- Room type analysis
- City supply dashboard
- Correlation matrices
- Weekend vs weekday comparisons
- Market segmentation charts

```python
from visualizations import AirbnbVisualizations

viz = AirbnbVisualizations(df)
viz.generate_full_dashboard(save_path='dashboard.png')
```

### 5. Business Intelligence Insights

**Key Findings:**
- 📊 **Pricing Variations**: Significant differences across cities (€X to €Y range)
- 📍 **Supply Concentration**: Top 3 cities account for X% of listings
- ⭐ **Quality Impact**: Superhosts command X% premium with Y% higher satisfaction
- 📅 **Weekend Premium**: X% price increase on weekends
- 💎 **Best Value Cities**: High satisfaction, competitive pricing

**Strategic Recommendations:**
1. Market expansion opportunities in underserved cities
2. Dynamic pricing strategy (weekend premium)
3. Quality improvement initiatives (superhost program)
4. Room type optimization
5. Data collection enhancements

## 📊 Key Metrics & KPIs

| Metric | Description | Business Value |
|--------|-------------|----------------|
| **Average Price by City** | Market positioning | Pricing strategy |
| **Listing Concentration** | Supply distribution | Market entry decisions |
| **Superhost Percentage** | Quality indicator | Host development |
| **Weekend Premium** | Dynamic pricing insight | Revenue optimization |
| **Value Score** | Satisfaction/Price ratio | Competitive positioning |
| **Location Quality Score** | Composite location metric | Property evaluation |

## 🎓 Skills Alignment

### Amazon Business Intelligence Engineer Requirements

✅ **SQL Proficiency** - Complex queries in Pandas  
✅ **ETL Development** - Production-ready pipeline  
✅ **Data Warehousing** - Multi-source data integration  
✅ **BI Tools** - Dashboard creation and visualization  
✅ **Statistical Analysis** - Hypothesis testing and correlations  
✅ **Business Acumen** - Actionable insights and recommendations  
✅ **Python Programming** - Clean, modular, production code  

### Data Scientist Requirements

✅ **Statistical Methods** - T-tests, correlations, hypothesis testing  
✅ **Feature Engineering** - Derived features and segmentation  
✅ **Data Visualization** - Comprehensive dashboards  
✅ **Exploratory Data Analysis** - Deep-dive insights  
✅ **Python/Pandas** - Advanced data manipulation  
✅ **Machine Learning Readiness** - Feature preparation for ML models  

## 📁 Output Files

After running the analysis:

- `processed_airbnb_data.csv` - Cleaned and processed dataset
- `city_summary_statistics.csv` - Aggregated city-level metrics
- `full_dashboard.png` - Comprehensive visualization dashboard
- `price_distribution.png` - Price analysis visualization
- `city_supply_dashboard.png` - Supply analysis dashboard
- `correlation_heatmap.png` - Feature correlation matrix

## 🔬 Advanced Features

### Feature Engineering
- **Price Segmentation**: Budget/Mid-range/Premium classification
- **Location Scoring**: Composite location quality index
- **Price per Person**: Value metric calculation
- **Market Positioning**: City-tier classification

### Statistical Tests
- Independent samples t-tests
- Pearson correlation analysis
- Descriptive statistics
- Distribution analysis

## 🚀 Next Steps & Extensions

### Potential Enhancements:
1. **Machine Learning**: Price prediction models
2. **Time Series Analysis**: Seasonal trend analysis
3. **Geographic Analysis**: Spatial clustering and heatmaps
4. **Demand Integration**: Booking data analysis
5. **A/B Testing**: Pricing strategy experiments
6. **Real-time Dashboards**: Streamlit/Plotly Dash implementation

## 📚 References

- [Amazon Business Intelligence Engineer Interview Guide](https://datalemur.com/blog/amazon-business-intelligence-engineer-interview)
- [Airbnb Data Analysis Best Practices](https://github.com/Dennis-Sosa/Airbnb--Analysis)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Dennis-Sosa/Airbnb--Analysis/issues).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Dennis Sosa**

- GitHub: [@Dennis-Sosa](https://github.com/Dennis-Sosa)
- Project: [Airbnb Analysis](https://github.com/Dennis-Sosa/Airbnb--Analysis)

## ⭐ Acknowledgments

- Data source: European Airbnb listings dataset
- Analysis framework: Amazon BIE & DS best practices
- Visualization inspiration: DataLemur interview guides

---

**⭐ If you find this project helpful, please consider giving it a star!**

---

## 📊 Project Statistics

![GitHub stars](https://img.shields.io/github/stars/Dennis-Sosa/Airbnb--Analysis?style=social)
![GitHub forks](https://img.shields.io/github/forks/Dennis-Sosa/Airbnb--Analysis?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/Dennis-Sosa/Airbnb--Analysis?style=social)
