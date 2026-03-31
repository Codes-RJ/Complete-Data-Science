# Datasets 📊

This folder contains information about datasets used throughout this repository.

## 📁 Folder Structure

```
datasets/
├── README.md              # This file
├── dataset_links.md       # Curated links to public datasets
├── raw/                   # Raw dataset files (gitignored - too large)
├── processed/             # Cleaned datasets (gitignored)
└── sample/                # Small sample datasets for testing
```

## ⚠️ Important Note

Most datasets are **not stored directly** in this repository due to size limitations. Instead:
- Links to datasets are provided in [dataset_links.md](./dataset_links.md)
- Download instructions are included where needed
- Sample datasets under 10MB may be included for quick testing

## 📥 How to Download Datasets

### Option 1: Manual Download
1. Visit the dataset link in [dataset_links.md](./dataset_links.md)
2. Download the dataset
3. Place it in `datasets/raw/` or `datasets/processed/` as needed

### Option 2: Using Python
```python
import pandas as pd
import kagglehub

# Download from Kaggle
dataset = kagglehub.dataset_download("username/dataset-name")

# Or load directly from URL
df = pd.read_csv("https://raw.githubusercontent.com/path/to/data.csv")
```

### Option 3: Using Command Line
```bash
# Using wget
wget https://example.com/dataset.csv -O datasets/raw/dataset.csv

# Using curl
curl -o datasets/raw/dataset.csv https://example.com/dataset.csv
```

## 📂 Recommended Dataset Locations

| Dataset Type | Location | Git Status |
|-------------|----------|------------|
| Sample files (<10MB) | `datasets/sample/` | ✅ Tracked |
| Large raw files | `datasets/raw/` | ❌ Gitignored |
| Processed files | `datasets/processed/` | ❌ Gitignored |

## 🗂️ Common Datasets by Section

### Excel/Power BI/Tableau
- Sales data
- Financial reports
- HR employee data

### Python/Pandas
- Titanic dataset
- Iris dataset
- Boston housing

### Machine Learning
- California housing
- MNIST (images)
- Customer churn data

### NLP
- IMDB reviews
- Twitter sentiment data
- Spam/ham messages

### Deep Learning
- CIFAR-10/100
- Fashion MNIST
- Cats vs Dogs

---

*See [dataset_links.md](./dataset_links.md) for the complete list of dataset sources.*