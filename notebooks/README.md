# Notebooks 📓

This folder contains Jupyter notebooks for exploratory data analysis, machine learning experiments, and deep learning models.

## 📁 Folder Structure

```
notebooks/
├── README.md                    # This file
├── exploratory/                 # EDA notebooks
│   ├── README.md
│   ├── titanic_eda.ipynb
│   ├── iris_analysis.ipynb
│   └── customer_analysis.ipynb
├── machine_learning/            # ML experiments
│   ├── README.md
│   ├── regression_models.ipynb
│   ├── classification_models.ipynb
│   ├── clustering.ipynb
│   └── hyperparameter_tuning.ipynb
└── deep_learning/               # DL models
    ├── README.md
    ├── cnn_mnist.ipynb
    ├── rnn_sentiment.ipynb
    └── transfer_learning.ipynb
```

## 📝 Naming Convention

- Use `snake_case` for file names
- Include purpose in name: `topic_description.ipynb`
- Examples:
  - `titanic_eda.ipynb`
  - `house_price_regression.ipynb`
  - `customer_segmentation_kmeans.ipynb`

## 🚀 How to Run Notebooks

### Local Setup
```bash
# Navigate to repository root
cd Data-Science-Repository

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Launch Jupyter Lab
jupyter lab

# Or launch classic notebook
jupyter notebook
```

### VS Code
1. Install Python extension
2. Open `.ipynb` file
3. Select kernel (Python environment)
4. Run cells

### Google Colab
1. Upload notebook to Google Drive
2. Open with Colab
3. Mount drive if accessing data:
```python
from google.colab import drive
drive.mount('/content/drive')
```

## 📋 Notebook Template

Each notebook should follow this structure:

```markdown
# Title

## 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

## 2. Load Data
```python
df = pd.read_csv('../../datasets/sample/titanic.csv')
```

## 3. Data Exploration
- Shape, info, describe
- Missing values
- Basic statistics

## 4. Data Cleaning
- Handle missing values
- Remove duplicates
- Fix data types

## 5. Data Visualization
- Distribution plots
- Correlation analysis
- Key insights

## 6. Analysis/Modeling
- Feature engineering
- Model building
- Evaluation

## 7. Conclusion
- Key findings
- Next steps

## 🔗 Accessing Datasets

From notebooks, reference datasets using relative paths:

```python
# Sample datasets
df = pd.read_csv('../../datasets/sample/titanic.csv')

# Raw datasets (if downloaded)
df = pd.read_csv('../../datasets/raw/dataset.csv')

# Processed datasets
df = pd.read_csv('../../datasets/processed/cleaned_data.csv')
```

## 📦 Exporting Notebooks

### To HTML
```bash
jupyter nbconvert --to html notebook.ipynb
```

### To PDF
```bash
jupyter nbconvert --to pdf notebook.ipynb
```

### To Python Script
```bash
jupyter nbconvert --to script notebook.ipynb
```

## 💾 Best Practices

1. **Add markdown cells** explaining each step
2. **Keep cells focused** - one purpose per cell
3. **Clear outputs before committing** to avoid large files
4. **Add comments** in code
5. **Include visualizations** to support analysis
6. **Save processed data** when needed

## 🧹 Cleaning Notebooks Before Commit

```bash
# Clear all outputs
jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace notebook.ipynb

# Or use nbstripout
pip install nbstripout
nbstripout notebook.ipynb
```

---

*Start with the notebooks in `exploratory/` to build your analysis skills!*