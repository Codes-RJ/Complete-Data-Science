# Dataset Links 🔗

A curated collection of public datasets for data science practice.

---

## 📚 General Dataset Repositories

| Source | Description | Link |
|--------|-------------|------|
| Kaggle | Largest dataset community | [kaggle.com/datasets](https://www.kaggle.com/datasets) |
| UCI ML Repository | Classic datasets | [archive.ics.uci.edu](https://archive.ics.uci.edu) |
| Data.gov | US government data | [data.gov](https://www.data.gov) |
| AWS Open Data | Large-scale datasets | [registry.opendata.aws](https://registry.opendata.aws) |
| Google Dataset Search | Dataset search engine | [datasetsearch.research.google.com](https://datasetsearch.research.google.com) |
| Hugging Face | ML/NLP datasets | [huggingface.co/datasets](https://huggingface.co/datasets) |
| Papers with Code | Research datasets | [paperswithcode.com/datasets](https://paperswithcode.com/datasets) |

---

## 📊 Excel & BI Practice

| Dataset | Description | Link |
|---------|-------------|------|
| Superstore Sales | Retail sales data | [Sample Superstore](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting) |
| HR Analytics | Employee data | [HR Dataset](https://www.kaggle.com/datasets/rhuebner/human-resources-data-set) |
| Financial Sample | Finance data | [Financial Sample](https://www.kaggle.com/datasets/arnavsaha19/financial-sample) |
| Global Sales | International sales | [Global Superstore](https://www.kaggle.com/datasets/anshtanwar/global-superstore-dataset) |

---

## 🐍 Python & Pandas Practice

| Dataset | Description | Link |
|---------|-------------|------|
| Titanic | Passenger survival | [Titanic](https://www.kaggle.com/c/titanic/data) |
| Iris | Flower classification | [Iris](https://archive.ics.uci.edu/dataset/53/iris) |
| Boston Housing | Housing prices | [Boston](https://www.kaggle.com/datasets/vikrishnan/boston-house-prices) |
| Wine Quality | Wine ratings | [Wine](https://archive.ics.uci.edu/dataset/186/wine+quality) |
| Customer Churn | Telecom churn | [Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) |

---

## 🗄️ SQL Practice

| Dataset | Description | Link |
|---------|-------------|------|
| Northwind | Classic DB | [Northwind](https://github.com/microsoft/sql-server-samples/tree/master/samples/databases/northwind-pubs) |
| Sakila | Movie rental DB | [Sakila](https://dev.mysql.com/doc/sakila/en/) |
| IMDb | Movie data | [IMDb](https://www.imdb.com/interfaces/) |
| Stack Overflow | Developer survey | [Stack Overflow Survey](https://insights.stackoverflow.com/survey) |

---

## 🤖 Machine Learning

| Dataset | Description | Use Case | Link |
|---------|-------------|----------|------|
| MNIST | Handwritten digits | Image classification | [MNIST](http://yann.lecun.com/exdb/mnist/) |
| Credit Card Fraud | Fraud detection | Classification | [Fraud](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) |
| California Housing | Housing prices | Regression | [Housing](https://www.kaggle.com/datasets/camnugent/california-housing-prices) |
| Mall Customers | Customer segments | Clustering | [Mall](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python) |
| Heart Disease | Medical diagnosis | Classification | [Heart](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset) |

---

## 📝 NLP Datasets

| Dataset | Description | Link |
|---------|-------------|------|
| IMDB Reviews | Sentiment analysis | [IMDB](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews) |
| Twitter Sentiment | Tweets | [Twitter](https://www.kaggle.com/datasets/kazanova/sentiment140) |
| Spam SMS | Message classification | [Spam](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset) |
| News Groups | Topic classification | [20 Newsgroups](https://scikit-learn.org/0.19/datasets/twenty_newsgroups.html) |
| Amazon Reviews | Product reviews | [Amazon](https://www.kaggle.com/datasets/bittlingmayer/amazonreviews) |

---

## 🖼️ Computer Vision

| Dataset | Description | Size | Link |
|---------|-------------|------|------|
| CIFAR-10 | 10 classes | 60k images | [CIFAR](https://www.cs.toronto.edu/~kriz/cifar.html) |
| CIFAR-100 | 100 classes | 60k images | [CIFAR-100](https://www.cs.toronto.edu/~kriz/cifar.html) |
| Fashion MNIST | Clothing items | 70k images | [Fashion MNIST](https://github.com/zalandoresearch/fashion-mnist) |
| Cats vs Dogs | Binary classification | 25k images | [Cats/Dogs](https://www.kaggle.com/datasets/shaunthesheep/microsoft-catsvsdogs-dataset) |
| Flowers | Flower species | 3.6k images | [Flowers](https://www.kaggle.com/datasets/alxmamaev/flowers-recognition) |

---

## 📈 Time Series

| Dataset | Description | Link |
|---------|-------------|------|
| Air Passengers | Monthly airline data | [Air Passengers](https://www.kaggle.com/datasets/rakannimer/air-passengers) |
| Stock Prices | Historical stock data | [Yahoo Finance](https://finance.yahoo.com/) |
| Weather | Temperature records | [NOAA](https://www.ncdc.noaa.gov/cdo-web/) |
| Electricity Demand | Power consumption | [UCI](https://archive.ics.uci.edu/dataset/321/electricityloaddiagrams20112014) |

---

## 🏥 Healthcare

| Dataset | Description | Link |
|---------|-------------|------|
| Diabetes | Patient health data | [Diabetes](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database) |
| COVID-19 | Global pandemic data | [COVID-19](https://github.com/CSSEGISandData/COVID-19) |
| Medical Cost | Insurance costs | [Medical Cost](https://www.kaggle.com/datasets/mirichoi0218/insurance) |

---

## 🛍️ E-commerce & Marketing

| Dataset | Description | Link |
|---------|-------------|------|
| Online Retail | UK retail transactions | [Online Retail](https://archive.ics.uci.edu/dataset/352/online+retail) |
| E-commerce | Brazilian e-commerce | [Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) |
| Marketing Campaign | Customer response | [Marketing](https://www.kaggle.com/datasets/rodsaldanha/arketing-campaign) |

---

## 📦 Sample Datasets (Available in pandas/seaborn)

These come built-in with libraries:

```python
# Built-in datasets
import pandas as pd
import seaborn as sns
from sklearn import datasets

# Pandas
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

# Seaborn
tips = sns.load_dataset('tips')
iris = sns.load_dataset('iris')
titanic = sns.load_dataset('titanic')

# Scikit-learn
iris = datasets.load_iris()
digits = datasets.load_digits()
wine = datasets.load_wine()
```

---

## 💾 Quick Download Script

```python
# download_datasets.py
import os
import pandas as pd

datasets = {
    "titanic": "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv",
    "iris": "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv",
    "tips": "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
}

os.makedirs("datasets/sample", exist_ok=True)

for name, url in datasets.items():
    df = pd.read_csv(url)
    df.to_csv(f"datasets/sample/{name}.csv", index=False)
    print(f"Downloaded: {name}")
```

---

*Use these datasets for learning, practicing, and building your portfolio!*