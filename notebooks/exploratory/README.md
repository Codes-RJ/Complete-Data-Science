
# Exploratory Data Analysis Notebooks 📊

This folder contains Jupyter notebooks focused on exploratory data analysis (EDA).

## 📁 Folder Purpose

EDA notebooks are used to:
- Understand dataset structure and quality
- Identify patterns and relationships
- Detect outliers and missing values
- Generate hypotheses for modeling
- Create visual summaries

## 📝 Notebooks

| Notebook | Dataset | Key Concepts |
|----------|---------|--------------|
| titanic_eda.ipynb | Titanic | Missing values, survival patterns, feature correlations |
| iris_analysis.ipynb | Iris | Distribution analysis, pair plots, species separation |
| customer_analysis.ipynb | Customer data | Demographics, purchasing behavior, segmentation insights |

## 🔍 EDA Checklist

Each EDA notebook should cover:

### 1. Data Overview
- [ ] Shape of dataset (rows, columns)
- [ ] Data types
- [ ] Basic statistics
- [ ] First and last rows

### 2. Missing Values
- [ ] Identify missing values
- [ ] Visualize missing patterns
- [ ] Decide handling strategy

### 3. Univariate Analysis
- [ ] Numerical: histograms, box plots, summary stats
- [ ] Categorical: bar charts, frequency tables

### 4. Bivariate Analysis
- [ ] Numerical vs Numerical: scatter plots, correlation
- [ ] Categorical vs Numerical: box plots, violin plots
- [ ] Categorical vs Categorical: stacked bar charts

### 5. Multivariate Analysis
- [ ] Pair plots
- [ ] Correlation heatmap
- [ ] Feature interactions

### 6. Outlier Detection
- [ ] Box plots
- [ ] Z-score method
- [ ] IQR method

### 7. Key Insights
- [ ] Summary of findings
- [ ] Recommendations for next steps

## 📊 Common Visualizations

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Distribution
sns.histplot(data=df, x='column', kde=True)
sns.boxplot(data=df, x='column')

# Relationships
sns.scatterplot(data=df, x='col1', y='col2', hue='category')
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')

# Categorical
sns.countplot(data=df, x='category')
sns.barplot(data=df, x='category', y='value')
```

## 🎯 Learning Objectives

After completing these notebooks, you should be able to:

1. Load and inspect any dataset
2. Identify data quality issues
3. Create meaningful visualizations
4. Document findings clearly
5. Prepare data for modeling

## 🚀 Getting Started

```bash
# Navigate to this folder
cd notebooks/exploratory/

# Launch Jupyter
jupyter notebook titanic_eda.ipynb
```

---

*Start with titanic_eda.ipynb to learn the fundamentals of EDA.*