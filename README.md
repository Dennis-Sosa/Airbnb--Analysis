# 🏠 Airbnb Supply Analysis - Business Intelligence Engineer Portfolio Project

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.3+-green.svg)](https://pandas.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **End-to-end Business Intelligence project demonstrating production-ready skills in ETL pipelines, SQL analytics, statistical analysis, and data visualization. Perfect portfolio piece for Amazon Business Intelligence Engineer (BIE), Data Scientist (DS), and Data Analyst (DA) roles.**

---

## 🎯 Project Overview

This comprehensive Business Intelligence project analyzes Airbnb listing supply patterns across **10 major European cities** using advanced data analytics techniques. The project showcases **production-ready skills** that align with **Amazon Business Intelligence Engineer (BIE)**, **Data Scientist (DS)**, and **Data Analyst (DA)** role requirements.

### What This Project Demonstrates

Based on the [Amazon Business Intelligence Engineer Interview Guide](https://datalemur.com/blog/amazon-business-intelligence-engineer-interview), this project addresses core competencies required for BIE, DS, and DA positions:

- ✅ **ETL Pipeline Development** - Production-ready data extraction, transformation, and loading
- ✅ **SQL Proficiency** - Complex analytical queries and data aggregations  
- ✅ **Statistical Analysis** - Hypothesis testing, correlation analysis, and statistical inference
- ✅ **Data Visualization** - Comprehensive dashboards and business intelligence reports
- ✅ **Feature Engineering** - Derived features, market segmentation, and data enrichment
- ✅ **Business Acumen** - Actionable insights and strategic recommendations
- ✅ **Python Programming** - Clean, modular, production-ready code architecture

---

## 🚀 Core Competencies by Role

### 🔧 Business Intelligence Engineer (BIE) Skills

**As defined in the [Amazon BIE Interview Guide](https://datalemur.com/blog/amazon-business-intelligence-engineer-interview)**, Business Intelligence Engineers build analytics, define KPIs, automate data pipelines, and create reports/dashboards. This project demonstrates:

| BIE Skill Area | Implementation | Evidence |
|----------------|----------------|----------|
| **ETL/Data Pipeline** | Complete ETL pipeline with extraction, transformation, and loading | `etl_pipeline.py` - Production-ready ETL class |
| **SQL Proficiency** | 10+ SQL-like queries implemented in Pandas | `analysis_queries.py` - Complex aggregations and joins |
| **Data Warehousing** | Multi-source data integration (20 CSV files) | Automated data loading and consolidation |
| **Data Quality** | Missing value handling, data validation, quality reports | ETL pipeline with quality assessment |
| **BI Tools & Visualization** | Comprehensive dashboards and visualizations | `visualizations.py` - Interactive dashboards |
| **Business Acumen** | Actionable insights and strategic recommendations | Business intelligence insights section |
| **KPI Development** | City-level metrics and performance indicators | Summary statistics and key metrics |
| **Report Development** | Automated report generation | Export functionality for further analysis |

**Key BIE Deliverables:**
- ✅ End-to-end ETL pipeline with error handling
- ✅ Data quality assessment reports
- ✅ SQL-like analytical queries (Top N, aggregations, joins)
- ✅ Business intelligence dashboards
- ✅ Strategic recommendations and KPIs

### 🧪 Data Scientist (DS) Skills

**Data Scientists focus on statistical analysis, machine learning, and advanced analytics.** This project demonstrates:

| DS Skill Area | Implementation | Evidence |
|---------------|----------------|----------|
| **Statistical Analysis** | T-tests, correlation analysis, hypothesis testing | Statistical analysis section with scipy |
| **Feature Engineering** | Price segmentation, location scoring, derived features | Feature engineering module |
| **Exploratory Data Analysis** | Comprehensive EDA with insights | Jupyter notebook with full EDA |
| **Data Visualization** | Correlation heatmaps, distribution plots, dashboards | Advanced visualization module |
| **Python Programming** | Object-oriented design, modular code structure | Clean, production-ready code |
| **Predictive Analytics Readiness** | Feature preparation for ML models | Derived features and segmentation |
| **Statistical Methods** | Hypothesis testing, correlation coefficients | Statistical tests implementation |

**Key DS Deliverables:**
- ✅ Statistical hypothesis testing (t-tests, correlations)
- ✅ Feature engineering and derived variables
- ✅ Correlation analysis and relationship discovery
- ✅ Data preparation for machine learning models
- ✅ Advanced analytical techniques

### 📊 Data Analyst (DA) Skills

**Data Analysts translate business needs into data solutions and create actionable insights.** This project demonstrates:

| DA Skill Area | Implementation | Evidence |
|---------------|----------------|----------|
| **Data Analysis** | Large dataset analysis, trend identification | Complete analysis across 10 cities |
| **Data Interpretation** | Insights extraction and business context | Business intelligence insights |
| **Report Development** | Comprehensive reports with visualizations | Dashboard and summary reports |
| **Business Process Optimization** | Data-driven recommendations | Strategic recommendations section |
| **Data Visualization** | Effective communication of findings | Multiple visualization types |
| **SQL-like Queries** | Complex data manipulation | Pandas operations equivalent to SQL |
| **Cross-functional Collaboration** | Business-focused insights | Stakeholder-ready recommendations |

**Key DA Deliverables:**
- ✅ Comprehensive data analysis and interpretation
- ✅ Business-focused reports and dashboards
- ✅ Data-driven recommendations
- ✅ Clear visualization of insights
- ✅ Actionable business intelligence

### 📈 Data Visualization Expertise

**Advanced visualization skills are critical for BIE, DS, and DA roles.** This project demonstrates:

| Visualization Type | Implementation | Use Case |
|-------------------|----------------|----------|
| **Distribution Plots** | Box plots, histograms | Price distribution by city |
| **Comparative Visualizations** | Bar charts, grouped comparisons | Weekend vs weekday analysis |
| **Correlation Analysis** | Heatmaps | Feature correlation matrix |
| **Dashboard Design** | Multi-panel dashboards | Comprehensive city supply dashboard |
| **Market Segmentation** | Categorical visualizations | Price segment analysis |
| **Geographic Analysis** | Location-based insights | City-level comparisons |
| **Time Series Visualization** | Period comparisons | Weekday/weekend patterns |

**Visualization Tools Used:**
- Matplotlib for custom visualizations
- Seaborn for statistical plots
- Correlation heatmaps for feature relationships
- Multi-panel dashboards for comprehensive analysis

---

## 📊 Dataset

### Cities Analyzed
🇳🇱 **Amsterdam** | 🇬🇷 **Athens** | 🇪🇸 **Barcelona** | 🇩🇪 **Berlin** | 🇭🇺 **Budapest**  
🇵🇹 **Lisbon** | 🇬🇧 **London** | 🇫🇷 **Paris** | 🇮🇹 **Rome** | 🇦🇹 **Vienna**

### Data Attributes
- **Pricing**: `realSum` (total price), `price_per_person` (derived)
- **Accommodation**: `room_type`, `bedrooms`, `person_capacity`
- **Host Quality**: `host_is_superhost`, `cleanliness_rating`
- **Guest Satisfaction**: `guest_satisfaction_overall`
- **Location**: `dist`, `metro_dist`, `attr_index`, `rest_index`, coordinates

### Data Scope
- **20 CSV files** (10 cities × 2 time periods: weekdays/weekends)
- **Supply-side analysis** (listings data)
- **Note**: Time-series and demand data not included (focus on supply patterns)

---

## 🏗️ Project Structure

```
Airbnb--Analysis/
├── 📓 airbnb_analysis.ipynb      # Main analysis notebook (full EDA)
├── 🔧 etl_pipeline.py             # ETL pipeline module (BIE core skill)
├── 📊 analysis_queries.py         # SQL-like analytical queries (BIE/DA skill)
├── 📈 visualizations.py           # Data visualization module (BIE/DS/DA skill)
├── 🚀 run_analysis.py            # One-command execution script
├── 📋 requirements.txt            # Python dependencies
├── 📖 README.md                   # Project documentation
├── ⚡ QUICKSTART.md               # Quick start guide
├── 📁 data/                       # Raw data files (20 CSV files)
│   ├── amsterdam_weekdays.csv
│   ├── amsterdam_weekends.csv
│   ├── ... (18 more files)
└── 📁 docs/                       # Documentation and outputs
```

---

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
# Option A: Jupyter Notebook (Recommended for exploration)
jupyter notebook airbnb_analysis.ipynb

# Option B: Python script (Production execution)
python run_analysis.py

# Option C: Run ETL pipeline separately
python etl_pipeline.py
```

---

## 📈 Analysis Components

### 1. ETL Pipeline (`etl_pipeline.py`) - **BIE Core Skill**

**Business Intelligence Engineer Skills:**
- Multi-file data extraction
- Data quality assessment
- Missing value imputation
- Feature engineering
- Data validation
- Production-ready error handling

```python
from etl_pipeline import AirbnbETLPipeline

pipeline = AirbnbETLPipeline('.', CITIES, PERIODS)
processed_data = pipeline.run_pipeline()

# Generate data quality report
quality_report = pipeline.get_data_quality_report(processed_data)
```

**Key Features:**
- Handles 20 CSV files automatically
- Data quality reports with missing value analysis
- Derived features: `price_per_person`, `location_score`, `price_segment`
- Boolean normalization
- Missing value handling with median imputation
- Logging and error handling

### 2. SQL-like Analysis (`analysis_queries.py`) - **BIE/DA Core Skill**

**Business Intelligence Engineer & Data Analyst Skills:**
- Complex aggregations
- Multi-table joins (conceptual)
- Window functions
- Group-by operations
- Top N queries

**10+ Key Analytical Queries:**
1. Top N cities by average price
2. Room type distribution by city
3. Superhost performance analysis
4. Weekend vs weekday pricing comparison
5. Top cities by listing count
6. Customer lifetime value (city-level)
7. Value proposition analysis
8. Market segmentation analysis
9. Inventory/supply analysis
10. Revenue breakdown by period

```python
from analysis_queries import AirbnbAnalytics

analytics = AirbnbAnalytics(df)
top_cities = analytics.top_n_cities_by_price(5)
pricing_analysis = analytics.weekend_vs_weekday_pricing()
superhost_analysis = analytics.superhost_performance_analysis()
```

### 3. Statistical Analysis - **DS Core Skill**

**Data Scientist Skills:**
- **Hypothesis Testing**: T-tests for price differences
- **Correlation Analysis**: Pearson correlation coefficients
- **Descriptive Statistics**: Central tendencies and distributions
- **Statistical Inference**: Significance testing

**Key Statistical Tests:**
- Weekend vs Weekday price significance test (t-test)
- Superhost vs Regular host price comparison (t-test)
- Price vs Satisfaction correlation (Pearson correlation)
- Distribution analysis

```python
from scipy import stats

# Weekend vs Weekday price comparison
weekend_prices = df[df['period'] == 'weekends']['realSum']
weekday_prices = df[df['period'] == 'weekdays']['realSum']
t_stat, p_value = stats.ttest_ind(weekend_prices, weekday_prices)
```

### 4. Data Visualization (`visualizations.py`) - **BIE/DS/DA Core Skill**

**Business Intelligence, Data Science & Data Analyst Skills:**
- Comprehensive dashboards
- Correlation heatmaps
- Distribution analysis
- Comparative visualizations
- Market segmentation charts

**Visualization Types:**
- Price distributions by city (box plots)
- Room type analysis (pie charts, box plots)
- City supply dashboard (multi-panel)
- Correlation matrices (heatmaps)
- Weekend vs weekday comparisons
- Market segmentation charts
- Location quality analysis

```python
from visualizations import AirbnbVisualizations

viz = AirbnbVisualizations(df)
viz.generate_full_dashboard(save_path='dashboard.png')
viz.plot_price_distribution_by_city()
viz.plot_correlation_heatmap()
```

### 5. Business Intelligence Insights - **BIE/DA Core Skill**

**Key Findings:**
- 📊 **Pricing Variations**: Significant price differences across cities
- 📍 **Supply Concentration**: Uneven distribution of listings across cities
- ⭐ **Quality Impact**: Superhosts command premium pricing with higher satisfaction
- 📅 **Weekend Premium**: Consistent price increase on weekends
- 💎 **Best Value Cities**: High satisfaction, competitive pricing

**Strategic Recommendations:**
1. **Market Expansion Opportunities**: Identify underserved cities
2. **Dynamic Pricing Strategy**: Implement weekend premium pricing
3. **Quality Improvement**: Focus on superhost program development
4. **Room Type Optimization**: Balance supply by property type
5. **Data Collection Enhancements**: Recommendations for additional metrics

---

## 📊 Key Metrics & KPIs

| Metric | Description | Business Value | Role Relevance |
|--------|-------------|----------------|----------------|
| **Average Price by City** | Market positioning metrics | Pricing strategy decisions | BIE/DA |
| **Listing Concentration** | Supply distribution analysis | Market entry decisions | BIE/DA |
| **Superhost Percentage** | Quality indicator | Host development programs | BIE/DA |
| **Weekend Premium** | Dynamic pricing insight | Revenue optimization | BIE/DS |
| **Value Score** | Satisfaction/Price ratio | Competitive positioning | DS/DA |
| **Location Quality Score** | Composite location metric | Property evaluation | BIE/DS |
| **Statistical Significance** | Hypothesis test results | Data-driven decisions | DS |

---

## 🎓 Skills Alignment with Amazon Interview Requirements

### Amazon Business Intelligence Engineer (BIE) Requirements

Based on the [Amazon BIE Interview Guide](https://datalemur.com/blog/amazon-business-intelligence-engineer-interview), this project demonstrates:

✅ **SQL Proficiency** - Complex queries implemented in Pandas (equivalent to SQL)  
✅ **ETL Development** - Production-ready pipeline with error handling  
✅ **Data Warehousing** - Multi-source data integration (20 CSV files)  
✅ **BI Tools** - Dashboard creation and visualization  
✅ **Statistical Analysis** - Hypothesis testing and correlations  
✅ **Business Acumen** - Actionable insights and strategic recommendations  
✅ **Python Programming** - Clean, modular, production code  
✅ **Data Quality** - Assessment and handling of missing values  
✅ **Report Development** - Comprehensive business intelligence reports  
✅ **KPI Definition** - City-level metrics and performance indicators  

### Data Scientist (DS) Requirements

✅ **Statistical Methods** - T-tests, correlations, hypothesis testing  
✅ **Feature Engineering** - Derived features and segmentation  
✅ **Data Visualization** - Comprehensive dashboards and visualizations  
✅ **Exploratory Data Analysis** - Deep-dive insights with EDA  
✅ **Python/Pandas** - Advanced data manipulation and analysis  
✅ **Machine Learning Readiness** - Feature preparation for ML models  
✅ **Statistical Inference** - Significance testing and interpretation  

### Data Analyst (DA) Requirements

✅ **Data Analysis** - Large dataset analysis and trend identification  
✅ **Data Interpretation** - Business context and insights extraction  
✅ **Report Development** - Comprehensive reports with visualizations  
✅ **Business Process Optimization** - Data-driven recommendations  
✅ **Data Visualization** - Effective communication of findings  
✅ **SQL-like Queries** - Complex data manipulation  
✅ **Cross-functional Collaboration** - Business-focused insights  

---

## 📁 Output Files

After running the analysis, the following files are generated:

- `processed_airbnb_data.csv` - Cleaned and processed dataset
- `city_summary_statistics.csv` - Aggregated city-level metrics
- `full_dashboard.png` - Comprehensive visualization dashboard
- `price_distribution.png` - Price analysis visualization
- `city_supply_dashboard.png` - Supply analysis dashboard
- `correlation_heatmap.png` - Feature correlation matrix

---

## 🔬 Advanced Features

### Feature Engineering (DS Skill)
- **Price Segmentation**: Budget/Mid-range/Premium classification
- **Location Scoring**: Composite location quality index (`attr_index + rest_index`)
- **Price per Person**: Value metric calculation
- **Market Positioning**: City-tier classification
- **Location Quality**: Low/Medium/High categorization

### Statistical Tests (DS Skill)
- Independent samples t-tests (weekend vs weekday, superhost vs regular)
- Pearson correlation analysis (price vs satisfaction)
- Descriptive statistics (mean, median, std, quartiles)
- Distribution analysis

### ETL Pipeline Features (BIE Skill)
- Multi-file extraction
- Data quality assessment
- Missing value imputation
- Feature derivation
- Data validation
- Error handling and logging

---

## 🚀 Next Steps & Extensions

### Potential Enhancements for Portfolio:

1. **Machine Learning Models** (DS Enhancement)
   - Price prediction models (regression)
   - Market segmentation (clustering)
   - Demand forecasting (time series)

2. **Time Series Analysis** (BIE/DS Enhancement)
   - Seasonal trend analysis
   - Holiday and event impact
   - Long-term pricing trends

3. **Geographic Analysis** (BIE/DS Enhancement)
   - Spatial clustering and heatmaps
   - Location-based recommendations
   - Geographic market analysis

4. **Demand Integration** (BIE Enhancement)
   - Booking data analysis
   - Occupancy rate calculations
   - Demand-supply balance

5. **A/B Testing Framework** (DS Enhancement)
   - Pricing strategy experiments
   - Hypothesis testing framework
   - Statistical significance validation

6. **Real-time Dashboards** (BIE Enhancement)
   - Streamlit/Plotly Dash implementation
   - Interactive visualizations
   - Real-time data updates

---

## 📚 References & Learning Resources

- [Amazon Business Intelligence Engineer Interview Guide](https://datalemur.com/blog/amazon-business-intelligence-engineer-interview) - Comprehensive interview preparation guide
- [DataLemur SQL Interview Questions](https://datalemur.com/questions) - Practice SQL and data analytics questions
- [Airbnb Data Analysis Best Practices](https://github.com/Dennis-Sosa/Airbnb--Analysis) - This repository

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Dennis-Sosa/Airbnb--Analysis/issues).

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Dennis Sosa**

- GitHub: [@Dennis-Sosa](https://github.com/Dennis-Sosa)
- Project: [Airbnb Analysis](https://github.com/Dennis-Sosa/Airbnb--Analysis)

---

## ⭐ Acknowledgments

- Data source: European Airbnb listings dataset
- Analysis framework: Amazon BIE, DS, and DA best practices
- Interview preparation: [DataLemur Amazon BIE Interview Guide](https://datalemur.com/blog/amazon-business-intelligence-engineer-interview)
- Visualization inspiration: DataLemur interview guides and best practices

---

**⭐ If you find this project helpful for your interview preparation, please consider giving it a star!**

---

## 📊 Project Statistics

![GitHub stars](https://img.shields.io/github/stars/Dennis-Sosa/Airbnb--Analysis?style=social)
![GitHub forks](https://img.shields.io/github/forks/Dennis-Sosa/Airbnb--Analysis?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/Dennis-Sosa/Airbnb--Analysis?style=social)

---

## 🎯 Interview Preparation Tips

This project addresses common interview questions from the [Amazon BIE Interview Guide](https://datalemur.com/blog/amazon-business-intelligence-engineer-interview):

### SQL Interview Questions Covered:
- ✅ Top N products/cities by sales/price
- ✅ Revenue breakdown by country/city and period
- ✅ Customer lifetime value analysis
- ✅ Inventory/supply analysis
- ✅ Cross-table aggregations

### Python Interview Questions Covered:
- ✅ Pandas data cleaning and preprocessing
- ✅ Missing data handling
- ✅ Performance optimization
- ✅ Data manipulation (JOIN-like operations)
- ✅ Statistical calculations

### Statistical Analysis Questions Covered:
- ✅ Hypothesis testing (t-tests)
- ✅ Correlation analysis
- ✅ Statistical significance interpretation
- ✅ Business application of statistics

---

**Ready to showcase your BIE, DS, and DA skills? Start by cloning this repository and exploring the analysis!**
