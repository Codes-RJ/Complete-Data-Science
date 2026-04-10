# Data Science Repository 📊

> A comprehensive, structured learning path for Data Science - from fundamentals to advanced concepts including Machine Learning, Deep Learning, MLOps, and Generative AI.

## 📚 Table of Contents

- [About This Repository](#about-this-repository)
- [Prerequisites](#prerequisites)
- [Learning Roadmap](#learning-roadmap)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [How to Use This Repository](#how-to-use-this-repository)
- [Tools & Technologies Covered](#tools--technologies-covered)
- [Projects](#projects)
- [Resources](#resources)
- [Contributing](#contributing)
- [License](#license)

## About This Repository

This repository is designed to be your complete companion in mastering Data Science. Whether you're a beginner taking your first steps or an experienced professional looking to deepen your expertise, you'll find structured content, practical examples, and real-world projects here.

### 🎯 Goals

- Provide a structured, industry-relevant curriculum
- Cover both theoretical concepts and practical implementation
- Include hands-on projects with real datasets
- Offer interview preparation materials
- Stay updated with latest technologies (MLOps, GenAI, LLMs)

### 📖 What You'll Learn

- **Fundamentals**: Python, R, SQL, Statistics
- **Data Analysis**: Excel, Power BI, Tableau, Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn, Tableau
- **Machine Learning**: Supervised & Unsupervised Learning, Model Evaluation
- **Deep Learning**: Neural Networks, CNNs, RNNs, Transformers
- **Data Engineering**: ETL, Spark, Airflow, Cloud Platforms
- **MLOps**: Model Deployment, Monitoring, CI/CD for ML
- **GenAI & LLMs**: Prompt Engineering, RAG, Fine-tuning, Vector Databases

## Prerequisites

- Basic programming knowledge (any language)
- Foundational mathematics (algebra, basic statistics)
- A computer with minimum 8GB RAM (16GB recommended for deep learning)
- Willingness to learn and experiment!

## Learning Roadmap

Follow this structured path for optimal learning:

```
┌───────────────────────────────────────────────────────────────┐
│                     PHASE 1: FOUNDATIONS                      │
├───────────────────────────────────────────────────────────────┤
│  • Introduction to Data Science                               │
│  • Excel & Data Analysis                                      │
│  • Python/R Programming Basics                                │
│  • Statistics & Probability                                   │
└───────────────────────────────────────────────────────────────┘
                               ↓
┌───────────────────────────────────────────────────────────────┐
│                  PHASE 2: DATA ANALYSIS                       │
├───────────────────────────────────────────────────────────────┤
│  • SQL for Data Science                                       │
│  • Pandas & NumPy                                             │
│  • Data Visualization (Matplotlib, Seaborn, Tableau, Power BI)│
└───────────────────────────────────────────────────────────────┘
                               ↓
┌───────────────────────────────────────────────────────────────┐
│                PHASE 3: MACHINE LEARNING                      │
├───────────────────────────────────────────────────────────────┤
│  • Supervised Learning (Regression, Classification)           │
│  • Unsupervised Learning (Clustering, PCA)                    │
│  • Model Evaluation & Hyperparameter Tuning                   │
│  • Ensemble Methods                                           │
└───────────────────────────────────────────────────────────────┘
                               ↓
┌───────────────────────────────────────────────────────────────┐
│                  PHASE 4: ADVANCED TOPICS                     │
├───────────────────────────────────────────────────────────────┤
│  • Deep Learning (CNNs, RNNs, Transformers)                   │
│  • Data Engineering & MLOps                                   │
│  • Generative AI & LLMs                                       │
│  • System Design for Data Science                             │
└───────────────────────────────────────────────────────────────┘
                               ↓
┌───────────────────────────────────────────────────────────────┐
│                     PHASE 5: PROJECTS                         │
├───────────────────────────────────────────────────────────────┤
│  • Beginner Projects                                          │
│  • Intermediate Projects                                      │
│  • Advanced Projects                                          │
│  • Domain-specific Case Studies                               │
└───────────────────────────────────────────────────────────────┘
```

## Repository Structure

### 📁 Tree Structure
```
Data-Science-Repository/
│
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── .gitignore
├── requirements.md
├── .env.example
│
├── 00_roadmap/
│   ├── README.md
│   ├── 01_learning_path.md
│   └── 02_timeline.md
│
├── assets/
│   ├── images/
│   ├── diagrams/
│   └── gifs/
│
├── datasets/
│   ├── README.md
│   └── dataset_links.md
│
├── notebooks/
│   ├── exploratory/
│   ├── machine_learning/
│   └── deep_learning/
│
├── 01_introduction_to_data_science/
│   ├── README.md
│   ├── 01_what_is_data_science.md
│   ├── 02_data_science_lifecycle.md
│   ├── 03_applications.md
│   ├── 04_tools_and_technologies.md
│   ├── 05_ethics_in_data_science.md
│   ├── 06_key_concepts_terminology.md
│   └── interview_questions.md
│
├── 02_excel/
│   ├── README.md
│   ├── 01_basics.md
│   ├── 02_formulas_functions.md
│   ├── 03_data_cleaning.md
│   ├── 04_pivot_tables.md
│   ├── 05_dashboards.md
│   ├── 06_advanced_formulas.md
│   ├── 07_macros_vba.md
│   └── interview_questions.md
│
├── 03_power_bi/
│   ├── README.md
│   ├── 01_introduction.md
│   ├── 02_data_import.md
│   ├── 03_data_transformation.md
│   ├── 04_dax_basics.md
│   ├── 05_dashboards.md
│   ├── 06_advanced_dax.md
│   ├── 07_service_collaboration.md
│   ├── 08_row_level_security.md
│   └── interview_questions.md
│
├── 04_tableau/
│   ├── README.md
│   ├── 01_introduction.md
│   ├── 02_data_connection.md
│   ├── 03_visualizations.md
│   ├── 04_dashboards.md
│   ├── 05_calculations.md
│   ├── 06_tableau_prep.md
│   ├── 07_server_online.md
│   ├── 08_storytelling.md
│   └── interview_questions.md
│
├── 05_python/
│   ├── README.md
│   ├── 01_tokens_and_comment/
│   ├── 02_data_types/
│   ├── 03_control_statements.md
│   ├── 04_functions.md
│   ├── 05_modules_packages.md
│   ├── 06_file_handling.md
│   ├── 07_error_exceptions.md
│   ├── 08_object_oriented_programming.md
│   ├── 09_list_comprehensions.md
│   ├── 10_lambda_functions.md
│   ├── 11_iterators_generators.md
│   ├── 12_decorators.md
│   └── interview_questions.md
│
├── 06_r_programming/
│   ├── README.md
│   ├── 01_introduction.md
│   ├── 02_data_types.md
│   ├── 03_vectors.md
│   ├── 04_data_frames.md
│   ├── 05_functions.md
│   ├── 06_control_structures.md
│   ├── 07_apply_functions.md
│   ├── 08_data_manipulation_dplyr.md
│   ├── 09_visualization_ggplot2.md
│   ├── 10_r_markdown.md
│   └── interview_questions.md
│
├── 07_numpy/
│   ├── README.md
│   ├── 01_introduction.md
│   ├── 02_arrays.md
│   ├── 03_indexing.md
│   ├── 04_operations.md
│   ├── 05_broadcasting.md
│   ├── 06_linear_algebra.md
│   ├── 07_random_sampling.md
│   ├── 08_universal_functions.md
│   └── interview_questions.md
│
├── 08_pandas/
│   ├── README.md
│   ├── 01_introduction.md
│   ├── 02_series.md
│   ├── 03_dataframes.md
│   ├── 04_data_cleaning.md
│   ├── 05_groupby.md
│   ├── 06_merge_join_concatenate.md
│   ├── 07_pivot_tables.md
│   ├── 08_time_series.md
│   ├── 09_reshaping.md
│   ├── 10_visualization.md
│   └── interview_questions.md
│
├── 09_matplotlib/
│   ├── README.md
│   ├── 01_introduction.md
│   ├── 02_line_plots.md
│   ├── 03_bar_charts.md
│   ├── 04_customization.md
│   ├── 05_subplots.md
│   ├── 06_histograms.md
│   ├── 07_scatter_plots.md
│   ├── 08_3d_plots.md
│   ├── 09_animations.md
│   └── interview_questions.md
│
├── 10_seaborn/
│   ├── README.md
│   ├── 01_introduction.md
│   ├── 02_distribution_plots.md
│   ├── 03_categorical_plots.md
│   ├── 04_heatmaps.md
│   ├── 05_regression_plots.md
│   ├── 06_matrix_plots.md
│   ├── 07_grids.md
│   ├── 08_styling.md
│   └── interview_questions.md
│
├── 11_sql/
│   ├── README.md
│   ├── 01_introduction.md
│   ├── 02_basic_queries.md
│   ├── 03_filtering_sorting.md
│   ├── 04_joins.md
│   ├── 05_aggregations_groupby.md
│   ├── 06_subqueries.md
│   ├── 07_window_functions.md
│   ├── 08_indexes_performance.md
│   ├── 09_stored_procedures.md
│   ├── 10_database_design.md
│   └── interview_questions.md
│
├── 12_machine_learning/
│   ├── README.md
│   ├── 01_introduction.md
│   ├── 02_data_preprocessing.md
│   ├── 03_train_test_split.md
│   ├── 04_linear_regression.md
│   ├── 05_logistic_regression.md
│   ├── 06_decision_trees.md
│   ├── 07_random_forest.md
│   ├── 08_svm.md
│   ├── 09_knn.md
│   ├── 10_clustering_kmeans.md
│   ├── 11_pca.md
│   ├── 12_model_evaluation.md
│   ├── 13_hyperparameter_tuning.md
│   ├── 14_ensemble_methods.md
│   ├── 15_xgboost_lightgbm.md
│   └── interview_questions.md
│
├── 13_deep_learning/
│   ├── README.md
│   ├── 01_introduction.md
│   ├── 02_neural_networks.md
│   ├── 03_activation_functions.md
│   ├── 04_backpropagation.md
│   ├── 05_tensorflow_basics.md
│   ├── 06_keras_basics.md
│   ├── 07_cnn.md
│   ├── 08_rnn_lstm.md
│   ├── 09_transfer_learning.md
│   ├── 10_transformers.md
│   ├── 11_generative_models.md
│   └── interview_questions.md
│
├── 14_statistics_probability/
│   ├── README.md
│   ├── 01_descriptive_stats.md
│   ├── 02_probability_basics.md
│   ├── 03_probability_distributions.md
│   ├── 04_sampling.md
│   ├── 05_hypothesis_testing.md
│   ├── 06_confidence_intervals.md
│   ├── 07_correlation.md
│   ├── 08_bayesian_statistics.md
│   ├── 09_anova.md
│   ├── 10_time_series_analysis.md
│   └── interview_questions.md
│
├── 15_data_engineering/
│   ├── README.md
│   ├── 01_etl_pipelines.md
│   ├── 02_data_warehousing.md
│   ├── 03_apache_spark.md
│   ├── 04_hadoop.md
│   ├── 05_airflow.md
│   ├── 06_data_lakes.md
│   ├── 07_cloud_platforms.md
│   ├── 08_docker.md
│   ├── 09_kubernetes.md
│   └── interview_questions.md
│
├── 16_projects/
│   ├── README.md
│   ├── 01_beginner/
│   ├── 02_intermediate/
│   └── 03_advanced/
│
├── 17_resources/
│   ├── README.md
│   ├── books.md
│   ├── courses.md
│   ├── datasets.md
│   ├── blogs_podcasts.md
│   ├── cheatsheets.md
│   ├── interview_preparation.md
│   └── certifications.md
│
├── 18_case_studies/
│   ├── README.md
│   ├── 01_finance.md
│   ├── 02_healthcare.md
│   ├── 03_ecommerce.md
│   ├── 04_manufacturing.md
│   ├── 05_marketing_analytics.md
│   └── 06_supply_chain.md
│
├── 19_mlops/
│   ├── README.md
│   ├── 01_introduction.md
│   ├── 02_model_deployment.md
│   ├── 03_model_monitoring.md
│   ├── 04_ci_cd_ml.md
│   ├── 05_mlflow.md
│   ├── 06_model_versioning.md
│   └── interview_questions.md
│
├── 20_system_design_for_ds/
│   ├── README.md
│   ├── 01_data_pipeline_design.md
│   ├── 02_real_time_vs_batch.md
│   ├── 03_scalability.md
│   ├── 04_data_modeling.md
│   └── interview_questions.md
│
└── 21_genai_llm/
    ├── README.md
    ├── 01_introduction.md
    ├── 02_prompt_engineering.md
    ├── 03_embeddings.md
    ├── 04_vector_databases.md
    ├── 05_rag.md
    ├── 06_fine_tuning.md
    ├── 07_llm_applications.md
    └── interview_questions.md
```

### 📁 Core Sections

| Section | Description |
|---------|-------------|
| [**00_roadmap**](./00_roadmap/README.md) | Learning path, timeline, and progress tracking |
| [**01_introduction_to_data_science**](./01_introduction_to_data_science/README.md) | DS fundamentals, lifecycle, tools, ethics |
| [**02_excel**](./02_excel/README.md) | Excel for data analysis, formulas, dashboards |
| [**03_power_bi**](./03_power_bi/README.md) | Power BI fundamentals, DAX, dashboards |
| [**04_tableau**](./04_tableau/README.md) | Tableau visualizations, calculations, storytelling |
| [**05_python**](./05_python/README.md) | Python programming fundamentals |
| [**06_r_programming**](./06_r_programming/README.md) | R programming, dplyr, ggplot2 |
| [**07_numpy**](./07_numpy/README.md) | Numerical computing with NumPy |
| [**08_pandas**](./08_pandas/README.md) | Data manipulation with Pandas |
| [**09_matplotlib**](./09_matplotlib/README.md) | Basic visualizations with Matplotlib |
| [**10_seaborn**](./10_seaborn/README.md) | Statistical visualizations with Seaborn |
| [**11_sql**](./11_sql/README.md) | SQL for data extraction and analysis |
| [**12_machine_learning**](./12_machine_learning/README.md) | ML algorithms, model evaluation, tuning |
| [**13_deep_learning**](./13_deep_learning/README.md) | Neural networks, CNNs, RNNs, Transformers |
| [**14_statistics_probability**](./14_statistics_probability/README.md) | Statistical concepts for data science |
| [**15_data_engineering**](./15_data_engineering/README.md) | ETL, Spark, Airflow, cloud platforms |
| [**16_projects**](./16_projects/README.md) | Hands-on projects by difficulty level |
| [**17_resources**](./17_resources/README.md) | Books, courses, datasets, cheatsheets |
| [**18_case_studies**](./18_case_studies/README.md) | Real-world applications across domains |
| [**19_mlops**](./19_mlops/README.md) | Model deployment, monitoring, CI/CD for ML |
| [**20_system_design_for_ds**](./20_system_design_for_ds/README.md) | Data pipeline design, scalability |
| [**21_genai_llm**](./21_genai_llm/README.md) | Generative AI, LLMs, RAG, vector databases |

### 📂 Additional Folders

| Folder | Purpose |
|--------|---------|
| [**assets**](./assets/) | Images, diagrams, and GIFs for documentation |
| [**datasets**](./datasets/) | Dataset links and instructions |
| [**notebooks**](./notebooks/) | Jupyter notebooks for exploratory analysis |

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Data-Science-Repository.git
cd Data-Science-Repository
```

### 2. Set Up Python Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Copy `.env.example` to `.env` and add your API keys if needed:

```bash
cp .env.example .env
```

### 4. Start Learning

Begin with [00_roadmap](./00_roadmap/README.md) to understand the learning path, then dive into any section you're interested in!

## How to Use This Repository

### For Beginners
1. Follow the [roadmap](./00_roadmap/README.md) sequentially
2. Start with [01_introduction_to_data_science](./01_introduction_to_data_science/README.md)
3. Complete all beginner projects before moving to advanced topics
4. Use the interview questions at the end of each section for self-assessment

### For Intermediate Learners
1. Skip foundational sections you're comfortable with
2. Focus on [12_machine_learning](./12_machine_learning/README.md) and [13_deep_learning](./13_deep_learning/README.md)
3. Work on intermediate and advanced projects
4. Explore domain-specific [case studies](./18_case_studies/README.md)

### For Advanced Learners
1. Dive into [15_data_engineering](./15_data_engineering/README.md), [19_mlops](./19_mlops/README.md), and [21_genai_llm](./21_genai_llm/README.md)
2. Build end-to-end projects with deployment
3. Practice system design for data science interviews

### For Interview Preparation
- Each section includes interview questions
- Check [17_resources/interview_preparation.md](./17_resources/interview_preparation.md)
- Review [case studies](./18_case_studies/) for domain-specific knowledge

## Tools & Technologies Covered

### Languages
- Python 3.8+
- R
- SQL

### Data Analysis & Visualization
- Excel / Google Sheets
- Power BI
- Tableau
- Pandas, NumPy
- Matplotlib, Seaborn, Plotly

### Machine Learning
- Scikit-learn
- XGBoost, LightGBM
- CatBoost

### Deep Learning
- TensorFlow
- Keras
- PyTorch

### Big Data & Data Engineering
- Apache Spark (PySpark)
- Hadoop
- Apache Airflow
- dbt

### Cloud Platforms
- AWS (S3, SageMaker, Redshift)
- Google Cloud Platform
- Microsoft Azure

### MLOps & Deployment
- Docker
- Kubernetes
- MLflow
- FastAPI, Flask
- GitHub Actions / Jenkins

### Databases
- PostgreSQL
- MySQL
- MongoDB
- Vector Databases (Pinecone, Weaviate)

### Generative AI & LLMs
- OpenAI API
- LangChain
- LlamaIndex
- Hugging Face Transformers

## Projects

### Beginner Level
- Exploratory Data Analysis
- Interactive Dashboard
- Regression Project (House Price Prediction)
- Classification Project (Titanic Survival)

### Intermediate Level
- Web Scraping & Analysis
- Time Series Forecasting
- Recommendation System
- NLP Sentiment Analysis

### Advanced Level
- End-to-End ML Pipeline with Deployment
- Computer Vision (Image Classification/Detection)
- LLM Application (RAG Chatbot)
- Big Data Project with Spark

*See [16_projects](./16_projects/README.md) for detailed project guides*

## Resources

- [Books](./17_resources/books.md) - Curated reading list
- [Courses](./17_resources/courses.md) - Recommended online courses
- [Datasets](./17_resources/datasets.md) - Public dataset sources
- [Cheatsheets](./17_resources/cheatsheets.md) - Quick reference guides
- [Blogs & Podcasts](./17_resources/blogs_podcasts.md) - Stay updated
- [Certifications](./17_resources/certifications.md) - Certification paths

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on how to:
- Report bugs
- Suggest enhancements
- Add content
- Submit pull requests

## License

This project is licensed under the terms in [LICENSE](./LICENSE) file.

## ⭐ Star the Repository

If you find this repository helpful, please consider giving it a star! It helps others discover this resource.

## 📧 Contact

For questions, suggestions, or collaboration opportunities:
- Open an issue on GitHub

---

## **Happy Learning! 🚀**